SC AS DS Introduce
==================

Where is the *SC*
-----------------

* Source code directory : 029/src/windows/SC
* Project name : sc.sln

SC Owner
--------

#. Dev: Xiaolong Cao
#. QA: Nick Zhang

How to build unifiedAppShare
----------------------------

#. Enter *020p\\src\\windows\\unifiedAppShare*
#. Run *OneClickBuild.bat*
#. Enter *bld* folder

Change List
-----------

#. add relevant dll to SC filelist
#. update msi package
#. update resource file


File Change List
----------------

#. include folder for FRAMEWORK

	#. 029\\include\\FRAMEWORK\\AppSharingProxy.h
	#. 029\\include\\FRAMEWORK\\pcmappsharemgr.h
	#. 029\\include\\FRAMEWORK\\SmAppShareSessionMgr.h
	#. 029\\include\\FRAMEWORK\\SmDialogs.h

#. include folder for FRAMEWORK_Artemis

	#. 029\\include\\FRAMEWORK_Artemis\\AppSharingProxy.h
	#. 029\\include\\FRAMEWORK_Artemis\\pcmappsharemgr.h
	#. 029\\include\\FRAMEWORK_Artemis\\SmAppShareSessionMgr.h

#. framework folder

	#. 029\\src\\windows\\FRAMEWORK\\ServiceMgr\\ServiceMgr.vcxproj
	#. 029\\src\\windows\\FRAMEWORK\\ServiceMgr\\SmAppShareSessionMgr.cpp
	#. 029\\src\\windows\\FRAMEWORK\\componentmgr\\AppSharingProxy.cpp
	#. 029\\src\\windows\\FRAMEWORK\\componentmgr\\Pcm.h
	#. 029\\src\\windows\\FRAMEWORK\\componentmgr\\PcmAppShareMgr.cpp
	#. 029\\src\\windows\\FRAMEWORK\\componentmgr\\cm.vcxproj

#. framework_artemis folder

	#. 029\\src\\windows\\FRAMEWORK_Artemis\\ServiceMgr\\ServiceMgr.vcxproj
	#. 029\\src\\windows\\FRAMEWORK_Artemis\\ServiceMgr\\SmAppShareSessionMgr.cpp
	#. 029\\src\\windows\\FRAMEWORK_Artemis\\ServiceMgr\\SmDefUIMgr.cpp
	#. 029\\src\\windows\\FRAMEWORK_Artemis\\componentmgr\\AppSharingProxy.cpp
	#. 029\\src\\windows\\FRAMEWORK_Artemis\\componentmgr\\PcmAppShareMgr.cpp
	#. 029\\src\\windows\\FRAMEWORK_Artemis\\componentmgr\\cm.vcxproj

#. tc folder

	#. 029\\src\\windows\\TC\\WebExMgr\\TCBOSessionMgr.cpp
	#. 029\\src\\windows\\TC\\WebExMgr\\TCBOSessionMgr.h
	#. 029\\src\\windows\\TC\\WebExMgr\\TCBOUIMgr.cpp
	#. 029\\src\\windows\\TC\\WebExMgr\\TCUIMgr.cpp
	#. 029\\src\\windows\\TC\\WebExMgr\\webexmgr.vcxproj
	#. 029\\src\\windows\\TC\\tcholmgr\\tcholmgr.vcxproj
	#. 029\\src\\windows\\TC\\WebExMgr\\WebExMgr.rc
	#. 029\\src\\windows\\TC\\tcholmgr\\tcholmgr.rc

#. sc folder

	#. 029\\src\\windows\\SC\\atsccli\\SCAppASMgr.cpp
	#. 029\\src\\windows\\SC\\atsccli\\SCAppASMgr.h
	#. 029\\src\\windows\\SC\\atsccli\\SCAppMgr.cpp
	#. 029\\src\\windows\\SC\\atsccli\\SCAppMgr.h
	#. 029\\src\\windows\\SC\\atsccli\\atsccli.vcxproj
	#. 029\\src\\windows\\SC\\atsccli\\scclicust.vcxproj
	#. 029\\src\\windows\\SC\\atsccli\\atsccli.rc

#. ST folder

	#. 029\\src\\windows\\ST\\RAMTMGR\\ramtmgr.vcxproj
	#. 029\\src\\windows\\ST\\RAMTMGR\\ramtmgr.rc
	

File Change List for T31 TC
---------------------------

#. webex-framework-artemis\\src\\cfw\\componentmgr

	#. AppSharingProxy.cpp
	#. PcmAppShareMgr.cpp (merge code and remove ActiveApp)
	#. cm.vcxproj

#. webex-framework-artemis\\src\\cfw\\include

	#. AppSharingProxy.h
	#. pcmappsharemgr.h
	#. SmAppShareSessionMgr.h
	
#. webex-framework-artmis\\src\\cfw\\ServiceMgr

	#. SmAppShareSessionMgr.cpp
	#. SmDefUIMgr.cpp
	
#. webex-framework-tc\\src\\TC\\WebExMgr

	#. TCBOSessionMgr.cpp
	#. TCBOSessionMgr.h
	#. TCBOUIMgr.cpp
	#. TCUIMgr.cpp
	

How to undecorate name from decorated name?
-------------------------------------------

* undnmae.exe 
* https://msdn.microsoft.com/en-us/library/ms937379.aspx
* http://stackoverflow.com/questions/9177591/how-to-undecorate-name-from-decorated-name
* https://code.google.com/p/pdbparse/source/browse/trunk/src/undname.c?r=97
* https://github.com/moyix/pdbparse


Class
-----

* CAtCtl40EM

	+ CSCMainController
	
		- CDlgManager
		- CSCModel
		- CSCAppMgr
		- CSCDownload
		- CWndFITPanel
		- CUIFactory
		- CUIManager
	
	+ CMSCMainFrame
	
		- CMSCNS
		- CMSCMainPanel

Bug list
--------

#. CSCuv84734 

	* https://cdetsng.cisco.com/webui/#view=CSCuv84734

#. CSCuv84659

	* https://cdetsng.cisco.com/webui/#view=CSCuv84659

#. CSCuv84717

	* https://cdetsng.cisco.com/webui/#view=CSCuv84717


Known Issue
-----------

#. 2015-09-23

	#. SC **Application Share** dialog
	
		* Shared App order

#. 2015-09-16

	#. SC **Application Share** dialog
	
		* Stop Share button disable
		* Mark *Checked status* for the shared app 

#. 2015-09-14

	#. ? Click "Close" button will exit share session when the "Application View" dialog 
	#. Shared application place in the front of the *Application View Dialog*
	#. Conflict Type

		+ SHARE_WEBBROWSER
		+ SHARE_NONE
		+ SHARE_APP
		+ SHARE_DESKTOP

	#. UI Issue

		+ Button layout issue
		+ Center Window
		+ Window Title
		+ Window Style
		+ ?Mark Shared Window with Checked Status

	#. Add AS String resource

		+ IDS_SHARE_AS_TITLE "Application Share"

	#. Untitled Window

		Add IDS_DVAS_UNTITLED_WINDOW "Untitled Window %u"
	
	#. Accessibility Issue (ESC key for AS Running App Dialog)

		+ PUSHBUTTON "Exit Sharing" IDC_EXIT_SHARING => IDCANCEL
		+ atresb5.rc
		+ atresgb.rc
		+ atres.rc
		+ atrestsp.rc
		+ atresde.rc
		+ atreses.rc
		+ atresfr.rc
		+ atresit.rc
		+ atresjp.rc
		+ atresko.rc
		+ atresnl.rc
		+ atrespt.rc
		+ atresru.rc
		+ atressp.rc
		+ atressv.rc

	#. SC

		+ AppSharing.dll
		+ AppSharingUI.dll
		+ aswin8helper.dll

	#. SCC

		+ AppSharing.dll
		+ AppSharingUI.dll
		+ atwbxUI15.dll
		+ aswin8helper.dll

	#. Indicator difference


Test Scope
----------

* OS

	+ Server 2008
	
		- Icon Issue
	
	+ Win8.1
		
	+ Win7
	
		- Avoid Regression Issue
	
	+ Win10
	
		- Verify New Feature
	
* Session

	+ Old Console
	+ New Console
	+ Multi Session Client
	+ *WebACD (can't work in VSCM Env)*

* Test Entry

	+ Main Menu
	+ Quick Start (UCF)
	+ Quick Start (Non-UCF)
	+ FIT Menu
	+ Indicator


Test Case
---------

* Presenter Change
* Show App Running Dialog from FIT "Select Application"
* Show App Running Dialog from Indicator 
* Share multi app at the same time
* Show "Other Application Dialog"
* Accessibility test case
* Multi Language test case
* When the "App Running Dialog" or "Other Application" Dialog showing , Click "Stop Application Sharing"
* When the "App Running Dialog" or "Other Application" Dialog showing , Customer Leave
* When the "App Running Dialog" or "Other Application" Dialog showing , End SC Conference


.. csv-table:: Win8.0
   :header-rows: 1 
   :stub-columns: 1
   :header: , , "Old Console", , "New Console", , "Multi Session Client", , "WebACD", 
   :widths: 10, 10, 10, 10, 10, 10, 10, 10, 10, 10

   , , "CSRs", "Customers", "CSRs", "Customers", "CSRs", "Customers", "CSRs", "Customers"
   "Show Application View Dialog", "Main Menu: Share View","CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Main Menu: Select Application", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Indicator: Select Application", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   "Application View Dialog Action", "Exit Sharing", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Stop Sharing", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Share", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Double Click Running Application Item", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Close Button", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   "Show Other Application Dialog", "Application View : Other Application", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   "Other Application Action", "Share","CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Cancel", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Close Button", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Double Click Item", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   "Stop Sharing", "Main Menu", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Indicator: Stop Application Sharing", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Customer: Stop Application Sharing", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   "Presenter Change", "Application View Dialog", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Other Application Dialog", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Shared:Application View Dialog", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Shared:Other Application Dialog", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   "End Session", "Application View Dialog", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   , "Other Application Dialog", "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"
   


Test Env
--------

* T30.1 site In VSCM
  
  + Nick Zhang
  + http://t2web1.qa.webex.com/got2wdt30  nick/P@ss123
  
* T30 Out of VSCM
  
  + Super Admin
  + https://hasuper.qa.webex.com/  nick/nickpass
  + Normal Site: nick30sp
  + http://nick30sp.qa.webex.com/  nick/pass, admin/P@ss123
  
Wiki
----

#. http://wikicentral.cisco.com/display/PROJECT/SC+Client+Knowledge+Transfer
#. http://wikicentral.cisco.com/display/ASDS/WIN10-SC
#. http://wikicentral.cisco.com/display/GROUP/T30.2
#. From Morgan
 
	* http://wikicentral.cisco.com/display/HZMACTEAM/Mac+Develop+ENV+Set+up+Process
	* http://wikicentral.cisco.com/display/PROJECT/SC+Client+Knowledge+Transfer
	* http://wikicentral.cisco.com/display/HFNATIVE
	* http://wikicentral.cisco.com/display/HFCLIENT/Productivity+Tools

#. tims.cisco.com//frameset.cmd?proj=9=&mode=b_

T30L10NSP2 HeadLib Location
---------------------------

* ccatg-build2.cisco.com/cirepo/Train/T30L10NSP2/client-T30L10NSP2.buildversion/delivery/headlib-T30L10NSP2-buildversion.zip

SVN 
---

* https://wwwin-svn-sjc-2.cisco.com/csg/020p/branches/T30L10NSP2
* https://wwwin-svn-sjc-2.cisco.com/csg/027/branches/T30L10NSP2
* https://wwwin-svn-sjc-2.cisco.com/csg/029/branches/T30L10NSP2

GIT
---

* https://stash-eng-chn-sjc1.cisco.com/stash/projects

How to generate document
------------------------

* python build029.py status -s

Recording
---------

* https://ha3web.qa.webex.com/nick30/ldr.php?RCID=8d2eb11b29f3c4c4704789def23c29fe

Rally
-----

* Prepare Env & Fix Build Issue : 6H
* Study SC Code : 6H
* Coding & Debug : 12H
* New Console "Share View" Case : 4H
* New Console "Request View" Case : 4H
* Old Console "Share View" Case : 4H
* Old Console "Request View" Case : 4H
* Multi Session Client "Share View" Case : 4H
* Multi Session Client "Request View" Case : 4H
* WebACD "Share View" Case : 6H
* WebACD "Request View" Case : 6H


Others
------

# WebACD

	* ACDInbox.exe
	
		+ attp.dll
		+ atWbxUI15.dll
		+ mcplugin.dll
		+ scplugin.dll
		+ ACDRes.dll
		+ WAPluginMgr.dll
		+ UILibRes.dll
		+ atAuth.dll
		+ scplgres.dll
		+ wbxtrace.dll
		+ raurl.dll
	
	* ACDManager.exe
	
		+ attp.dll
		+ atWbxUI15.dll
		+ ACDRes.dll
		+ UILibRes.dll
		+ atAuth.dll
		+ wbxtrace.dll
		+ raurl.dll
		
	* ACDMonitor.exe
	
		+ attp.dll
		+ atWbxUI15.dll
		+ ACDRes.dll
		+ UILibRes.dll
		+ atAuth.dll
		+ wbxtrace.dll
		+ raurl.dll
	
	* atscmgr.exe
	
		+ atasctrl.dll
		+ welsdec.dll
		+ atres.dll
		+ AppSharing.dll
		+ wbxaecodec.dll
		+ atdl2006.dll
		+ wbxaudioengine.dll
		+ mac.dll
		+ atres_lite.dll
		+ atpack.dll
		+ welsvp.dll
		+ MJPGDecoder.dll
		+ wsertp.dll
		+ mticket.dll
		+ mcsnew.dll
		+ wseclient.dll
		+ mutiltpd.dll
		+ msvc.dll
		+ atfilesp.dll
		+ atfilesr.dll
		+ atlchat.dll
		+ acdti.dll
		+ atacd.dll
		+ atocres.dll
		+ uilibres.dll
		+ mmssl32.dll
		+ wbxcrypt.dll
		+ atmemmgr.dll
		+ attp.dll
		+ atarm.dll
		+ atwbxui15.dll
		+ atsc3cli.dll
		+ atkbctrl.dll
		+ atcarmcl.dll
		+ atgpcext.dll
		+ atgpcdec.dll
		+ ieatgpc.dll
		+ wbxtrace.dll
		



