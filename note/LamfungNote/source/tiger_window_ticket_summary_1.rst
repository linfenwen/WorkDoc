Tiger Windows Meeting Client Tickets Summary
============================================

CSCvc64610, T31.8 Unable to record meeting with other teleconference, the drop down to select the country hang
--------------------------------------------------------------------------------------------------------------



CSCvc40283, T31.8 Incorrect host name appears for all host using PMR or MC
--------------------------------------------------------------------------

#. 


CSCvc14491, Intercall TSP VoIP Client cannot be verified
---------------------------------------------------------

	#. CEDT Link
		+ https://cdetsng.cisco.com/webui/#view=CSCvc14491
	#. Keynotes
		+ Docshow
			- TSPHybridFlag
			- THClientHashList
			- CDTAppPDU_Evt_CreateTSPConference
			- TSPHybridSecureAccess
		+ Super Admin => New Site => Security Options
			- TSP partner is sending only SHA256 values in TSP API clienthashlist.(enabling this will stop checking for SHA1 hash values)
	#. DEV 3W Analysis
		+ What's the problem?
			- Intercall TSP VoIP Client cannot be verified
		+ What's the root cause?
			- It's caused by security option (docshow TSPHybridSecureAccess)
			- Then windows client use SHA256 for security verify
		+ What's the solution?
			- UnCheck **TSPHybridSecureAccess** from page
	#. Lessons learned
		+ Developer / QA need know more case (TSP, Non-TSP)
		+ Document, page is too complicate
		+ Team building with Paul's team (Tiger team)
		+ Work at the same page (Spark room)
	



2016-11-22
----------


CSCvb19442, MC crash after End Meeting
--------------------------------------

#. CDET Link
	https://cdetsng.cisco.com/webui/;jsessionid=E5D6B080A24B65796EBBFBE1A9EE24CC.webui-springtail#view=CSCvb19442
#. Keynotes
	+ Docshow
		- TeleMetryInfo
		- MetricsEnable
	+ GetMetricsEnable
	+ WbxMetricsInitialize() : In windows, create one thread to post metrics message
	+ WbxMetricsUnInitialize()
#. DEV 3W Analysis
	+ What's the problem?
		- MC crash after End Meeting
	+ What's the root cause?
		- It's caused by featured tracking function.
		- When meeting end, not call kill work thread, so the work thread still work.
		- But the main thread has exited, so meet crash.
	+ What's the solution?
		- If not support feature tracking, do not need create work thread.
#. Lessons learned
	+ Make sure **WbxMetricsInitialize** and **WbxMetricsUnInitialize** pairs correctly.
	+ Developer self test
	+ Make sure QA understood the feature
	+ Enable / Disable feature to test
	+ Code review

CSCvb45367, T31R2 fail to join meeting
--------------------------------------

#. CDET Link
	https://cdetsng.cisco.com/webui/#view=CSCvb45367
#. Keynotes
	+ After host crash, CB end meeting. But MZM will keep the meeting 4 minutes.
	+ In 4 minutes, attendee should send create conference request to MZM.
	+ It does not exist on 31.0.0.1304 client build.	
#. Key log
	::
	 
	 1	atmgr.exe	[320:3620]	ServCom	02:07:56.418 09/23/16	atmgr CommandLine["C:\ProgramData\WebEx\WebEx\T31_UMC\atmgr.exe"  /mcstd C:\Users\user.rabbit-sjc-ta3\AppData\LocalLow\WebEx]
	 2	atmgr.exe	[320:3620]	ServCom	02:07:56.454 09/23/16	ConfID: 40721322134735873
	 3	atmgr.exe	[320:3620]	ServCom	02:07:56.454 09/23/16	SiteURL: https://pj1jut31.eng.webex.com/pj1jut31
	 4	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.631 09/23/16	ctx>>ClientBuildVersion=31.6.2.2
	 5	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.648 09/23/16	pingAgent>>doPing-enter
	 6	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.648 09/23/16	pingAgent>>doPing,create=0
	 7	atarm.dll	[320:3620]	EUREKA	02:07:56.649 09/23/16	GCC_Ping_Mgr::ping_request_0,ION=0,create=0,secure=3,
	 8	atarm.dll	[320:3620]	EUREKA	02:07:56.649 09/23/16	GCC_Ping_Mgr::ping_request,ION=0,conf_name="Client 3's Personal Room.40721322134735873",conf_key="640038044",conf_id="40721322134735873",site_id=3437,user_id=0xfff02147,est_num=10,num_of_ping_svrs=1,
	 9	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.649 09/23/16	pingAgent>>doPing, return=0
	 10	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.758 09/23/16	ctx>>VMRFlagID=2
	 11	atarm.dll	[320:3620]	EUREKA	02:07:56.769 09/23/16	GCC_Ping_Mgr::notify_ping_confirm,ION=0,cb_address="tcp://epj1cb1101.eng.webex.com:1270",gateway_address="https://epj1cb1101.eng.webex.com:80",top_cb_address="",result=10,zone_flag=1,last_top_cb_address="",last_result=10,
	 12	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.769 09/23/16	mph>>gccSink>>on_ping_confirm,result=10,create=0
	 13	confmgr.dll	[320:3620]	UNKNOWN	02:07:56.769 09/23/16	mph>>conf>>pnigAgent>>on_ping_confirm, create=0, result=10, confid=40721322134735873
	 14	CONFMGR		[320:3620]	ConfMgr	02:07:56.770 09/23/16	on_ping_confirm,to_create= 0,result=10, conf_ID=0x8D9A1C0
	 15	CONFMGR		[320:3620]	ConfMgr	02:07:56.770 09/23/16	CAtConfManagerImpl::SetPingErrorTen,bErrorTen=1
	 16	webexmgr.dll	[320:3620]	ServCom	02:07:56.770 09/23/16	mph>>CAtConfAgent::on_ping_confirm, __INTERNAL_PING_FAILED
	 17	confmgr.dll	[320:3620]	UNKNOWN	02:08:15.474 09/23/16	pingAgent>>doPing-enter
	 18	confmgr.dll	[320:3620]	UNKNOWN	02:08:15.474 09/23/16	pingAgent>>doPing,create=1
	 19	atarm.dll	[320:3620]	EUREKA	02:08:15.474 09/23/16	GCC_Ping_Mgr::ping_request_0,ION=0,create=1,secure=3,
	 20	atarm.dll	[320:3620]	EUREKA	02:08:15.474 09/23/16	GCC_Ping_Mgr::ping_request,ION=0,conf_name="Client 3's Personal Room.40721322134735873",conf_key="640038044",conf_id="40721322134735873",site_id=3437,user_id=0xfff02147,est_num=0,num_of_ping_svrs=1,
	 21	confmgr.dll	[320:3620]	UNKNOWN	02:08:15.475 09/23/16	pingAgent>>doPing, return=0
	 22	atarm.dll	[320:3620]	EUREKA	02:08:15.536 09/23/16	GCC_Ping_Mgr::notify_ping_confirm,ION=0,cb_address="tcp://epj1cb1101.eng.webex.com:1270",gateway_address="https://epj1cb1101.eng.webex.com:80",top_cb_address="tcp://epj1cb1101.eng.webex.com:1270",result=2,zone_flag=1,last_top_cb_address="tcp://epj1cb1101.eng.webex.com:1270",last_result=2,
	 23	confmgr.dll	[320:3620]	UNKNOWN	02:08:15.536 09/23/16	mph>>gccSink>>on_ping_confirm,result=2,create=1
	 24	confmgr.dll	[320:3620]	UNKNOWN	02:08:15.536 09/23/16	mph>>conf>>pnigAgent>>on_ping_confirm, create=1, result=2, confid=40721322134735873
	 25	confmgr.dll	[320:3620]	UNKNOWN	02:08:15.536 09/23/16	mph>>conf>>pnigAgent>>on_ping_confirm,PING_RESULT_CONFERENCE_ALREADY_EXIST
	 26	webexmgr.dll	[320:3620]	ServCom	02:08:15.662 09/23/16	mph>>CAtConfAgent::TryAvailableCBSvr,bGrabHostToken=0,bGrabPresenterToken=0
	 27	CONFMGR	[	320:3620]	ConfMgr	02:08:15.662 09/23/16	IsJoinAsHost=1,m_pConfManager->GetHostType()=0,m_pConfManager->IsPingErrorTen()1
	 28	CONFMGR		[320:3620]	ConfMgr	02:08:15.662 09/23/16	CAtConfManagerImpl::SetPingErrorTen,bErrorTen=0
	 29	atmgr.exe	[320:3620]	ServCom	02:08:26.159 09/23/16	atmgr quit ok

#. DEV 3W Analysis
	+ What's the problem?
		- Can't join meeting
	+ What's the root cause?
		- CAtConfManagerImpl::SetPingErrorTen hadn't reset when start next ping
	+ What's the solution?
		- CAtConfAgent::on_ping_confirm reset CAtConfManagerImpl::SetPingErrorTen
#. Lessons learned
	+ Code logic too complex to hard test
	+ Developer need more carefully when coding
	+ Make sure QA understood the feature
	+ Sync with Paul Liu Team how to test 
	+ Code review







