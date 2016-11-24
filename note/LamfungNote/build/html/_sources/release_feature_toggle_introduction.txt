Release Toggle Introduction
===========================


Overall work flow
-----------------

	.. image:: _static/releaseToggle.png

urllink: 
	https://www.draw.io/?state=%7B%22ids%22:%5B%220B2Ykfab9ktB2Mkk3QkFkWUxMSnc%22%5D,%22action%22:%22open%22,%22userId%22:%22102822533125939981740%22%7D#G0B2Ykfab9ktB2Mkk3QkFkWUxMSnc

PO or SA or SM edit configure file
----------------------------------

* Feature Toggle Git Repo
  
  https://bitbucket-eng-chn-sjc1.cisco.com/bitbucket/projects/CCTG/repos/webex-release-toggles/browse

* features-config.json
  ::
    
    {
        "features": 
            [
                {
                    "key": "release-toggle-sample",
                    "name": "Release toggle sample",
                    "description": "this is a sample release toggle config for demo",
                    "owner": "Admin Test",
                    "enable": false,
                    "target-release": "T32",
                    "sub-flags": 
                               {
                                   "flag": 
                                         [
                                             {
                                                 "name": "j2ee_flag",
                                                 "enabled": true
                                             },
                                             {
                                                 "name": "cb_flag",
                                                 "enabled": false
                                             }
                                         ]
                               }
                },
                {
                    "key": "release-toggle-1",
                    "name": "Release toggle 1",
                    "description": "this is a 1 feature toggle config for demo",
                    "owner": "Admin Test",
                    "enable": false,
                    "target-release": "T32"
                }
            ]
    }

* staticToggle.json (utf-8 format)
  ::
    
   {
      "features": 
                [
                    {"enable": false, "key": "release-toggle-sample"}, 
                    {"enable": false, "key": "release-toggle-1"}
                ]
    }

Component Impact
----------------

* webex-cloudsapp-config
	+ gpcini.webex (MC)
		- VistaBasic section
* MSI


webex-windows-feature-toggle
----------------------------
#. API
   ::
      
      bool releaseToggleIsEnable(char* pszFeatureName);

#. Repo
	https://bitbucket-eng-chn-sjc1.cisco.com/bitbucket/projects/CCTG/repos/webex-windows-feature-toggle/browse

#. Where to download lib and header file ?
	http://ccatg-build2.cisco.com/cirepo/artifacts/32.0.0/webex-windows-feature-toggle/
	
#. T32.0
	+ http://ccatg-build2.cisco.com/cirepo/webex_artifacts/client/webex-windows-release-toggle/32.0.0/

Two mode
--------

#. Release mode
	+ Undefine *RT_DEBUG_MODE*
	+ Load *staticToggle.json* from *featuretoggle.dll*
	+ For security consider, in binary level disalbe debug relevant code
#. Debug mode
	+ Define *RT_DEBUG_MODE*
	+ Load *staticToggle.json* from file which locate at the same directory of *featuretoggle.dll* first,
	  else load *staticToggle.json* from *featuretoggle.dll*
	+ Convenient for developer debug

How other project use feature toggle
------------------------------------

#. Add **webex-windows-feature-toggle** to your *dependencies.xml* file
#. Add **featureToggleAgent.h** header file to your *project*
#. Call **releaseToggleIsEnable** where you want to use *release toggle*

Code Example
------------

#. Example1

  ::
    
    #include "releaseToggleAgent.h"
    
    int CMCServiceMgr::OnConfJoinConfirm(short result, ARMConferenceHandle conf_handle, CAtUser* pUser)
    {
        ...
        
        if( releaseToggleIsEnable("F1447") ) 
        {
            m_pCSIMgr = new CSmCSIMgr();
            if(NULL != m_pCSIMgr)
            {
                m_pCSIMgr->SetServiceMgr(this);
                m_pCSIMgr->OnConfJoinConfirm(result, conf_handle, pUser);
            }
        }
        
        ...
    }


Effect on **UT**
----------------

* UT for **Example1**

  ::
    
    class CMCServiceMgrTest : public testing::Test
    {
        public:
            
            CMCServiceMgrTest()
            {
                m_pServiceMgr = NULL;
            }
            
            virtual void SetUP()
            {
                if(NULL == m_pServiceMgr)
                {
                    m_pServiceMgr = new CMCServiceMgr;
                }
            }
            
            virtual void TearDown()
            {
                if(NULL != m_pServiceMgr)
                {
                    delete m_pServiceMgr;
                    m_pServiceMgr = NULL;
                }
            }
        
        protected:
            CMCServiceMgr*    m_pServiceMgr;
    };
    
    TEST_F(CMCServiceMgrTest, Test1) 
    {
        EXPECT_TRUE(NULL != m_pServiceMgr);
        
        short result;
        ARMConferenceHandle conf_handle;
        CAtUser atUser;
        m_pServiceMgr->OnConfJoinConfirm(result, conf_handle, &atUser);
        
        EXPECT_TRUE(NULL != m_pServiceMgr->GetCSIMgr());
    }

* The above UT will run failure for **Release Feature Toggle**
* Solution

	+ Place *staticToggle.json* in the *UT execute file folder*

webex-windows-feature-toggle
------------------------------

#. build
#. dependencies
#. doc
#. include
	+ featureToggleAgent.h
#. output
#. src
	+ featuretoggle.rc
	+ resource.h
	+ featuretoggle.vcxproj
	+ featureToggleAPI.h
	+ featureToggleAPI.cpp
	+ featureToggleImpl.h
	+ featureToggleImpl.cpp
	+ staticToggle.json
#. test


Wiki
----

* Feature over view design
	https://wiki.cisco.com/display/HFWEB/Release+Feature+Toggle#ReleaseFeatureToggle-4.1theflowdiagram
* View build status
	https://cctg-ec2.cisco.com/commander/link/workspaceFile/workspaces/default?jobStepId=e217ec53-5fa5-11e6-9cbe-005056af0148&fileName=build.e217ec53-5fa5-11e6-9cbe-005056af0148.log&jobName=official_Train_Client_31.6.0_webex-windows-feature-toggle_1057900_201608110226&jobId=bcbb6915-5fa5-11e6-8406-005056af0148&diagCharEncoding=&resourceName=cctg-ci-win33&completed=0
* Download feature toggle **zip package**
	https://ccatg-build2.cisco.com/cirepo/artifacts/32.0.0/webex-windows-feature-toggle
* https://wiki.cisco.com/display/wxclient/makefile.ec+detail
* https://wiki.cisco.com/display/WEBEXCI/Build+Client+Component+Locally


Reference
---------

* http://martinfowler.com/articles/feature-toggles.html
* http://martinfowler.com/bliki/FeatureToggle.html

