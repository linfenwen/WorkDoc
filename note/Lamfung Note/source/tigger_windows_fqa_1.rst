Tiger Windows FQA 
============================


#. [P] WO0000000218922
	+ Host is not able to see avatar picture in the Personal Meeting Room
	+ CSCuz30267
	+ Key points
		- CSmAvatarMgr::CSmCacheMgr::SaveIntoLocalCache
		- CSmConnectionPointContainer::Fire_OnUserAvatarURLRetrieved
		- CWCLReskin::IsAvatarFromFile

#. [P] WO0000000223509
	+ T31.5.20 win10  Crash when sharging application or when changing presenter role between participants.
	+ Ask to schedule a trouble shooting.


#. [W] CSCvc15881
	+ T31R2 Flash client E Attendees and panelists are unable to hear the host
	+ Assign to Winter Yu

#. [W] WO0000000221501
	+ WebEx application crashes when starting or join a meeting
	+ Seems the same as WO0000000216828
	+ Request dump file
	+ CSCuz52797
	::
	 
	 From Jun Ma:
	 I have checked dump file that dump indicate the crash location is SensorsApi.dll. 
	 I think this crash same with surface pro case. you can add HP  Elite X2 to filter White-list. Thanks

#. [D] CSCvc17039
	+ T31.7 Share Multimedia YouTube Adobe Flash Player error
	+ Assgin to Morgan
#. [D] CSCvc17031
	+ cannot recover memory location
	+ Mail to Caroline Ye
	+ F1573 
#. [P] CSCvc14491
	+ https://cdetsng.cisco.com/webui/#view=CSCvc14491
	+ Intercall
	+ From Alexander Fleck (afleck), send out mail request client log
	+ TSP server connect the third party server
	+ Dongong Peng From TSP server
	+ PO (ren bo), TL (Ty)
	+ Super Admin => New Site => Security Options
		- TSP partner is sending only SHA256 values in TSP API clienthashlist.(enabling this will stop checking for SHA1 hash values)
	+ Docshow parameters
		- TSPHybridFlag
		- THClientHashList
		- CDTAppPDU_Evt_CreateTSPConference
		- TSPHybridSecureAccess
	::
	 

#. [W] WO0000000227555
	+ VoIP audio connection issue
	+ Mail out, need trouble shooting

#. [D] Issue 317
	+ same as WO0000000226507,WO0000000226423
	+ https://sqbu-github.cisco.com/CMR/support/issues/317
	+ This issue is in CMR 3.5 repo, CMR 3.5 plan to LA on 12/14, so need to fix it in this month, please take this as high priority.
	+ Waiting for client log
	
	::
	 
	 Turns out to be a RJ Cable faulty connecting Nexus GW to the UCS server with a lot of input errors
	 
	 The Cable was replaced, no errors
	 
	 Set up a basic WebEx bridge and registered a test phone on AM1 with dial back to the test extn
	 
	 We have tested the one test meeting of 45min+ (Jason/Pranith/Ravi) and none of the call got dropped after 30+ or so no drops
	 
2016-11-21
----------

#. [D] WO0000000221097
	+ crash
	+ Seems crashed at SensorApi module
	+ Jun Ma is checking
	+ Mail out, ask Jun for update, need more time to research
	+ SSE asked us to close this case
	::
	 
	 19  Id: 2700.12f4 Suspend: 0 Teb: 01042000 Unfrozen
	     ChildEBP RetAddr  Args to Child              
	     1352ef5c 76ece221 00001210 00000000 00000000 ntdll_77d70000!ZwWaitForSingleObject+0xc (FPO: [3,0,0])
	     1352efd0 76ece182 00001210 ffffffff 00000000 KERNELBASE!WaitForSingleObjectEx+0x91 (FPO: [SEH])
	     1352efe4 5e265f05 00001210 ffffffff 00000000 KERNELBASE!WaitForSingleObject+0x12 (FPO: [Non-Fpo])
	     1352f014 76f5f4a2 1352f0d4 6e8d620d 00000000 webexmgr!Exception_Report+0x27c
	     1352f0a4 77e135ee 1352f0d4 77deb020 1352f908 KERNELBASE!UnhandledExceptionFilter+0x172 (FPO: [Non-Fpo])
	     1352f908 77dd5dae ffffffff 77dfb7d8 00000000 ntdll_77d70000!__RtlUserThreadStart+0x3d83a
	     1352f918 00000000 5b49d260 00000dfc 00000000 ntdll_77d70000!_RtlUserThreadStart+0x1b (FPO: [Non-Fpo])
	 
	 Exception content
	     1352f804 5b4ccb98 0c5ea948 5b494ccc 00000001 SensorsApi!CSensorV2::DataCallback+0x1cb
	     1352f818 5b49d5e9 014f6878 0c5ea948 57beb1f7 SensorsApi!CSensorV2::s_DataCallback+0x18
	     1352f8ac 769038f4 00000dfc 769038d0 858b2299 SensorsNativeApi_V2!NativeSensorCollectionNotifThread+0x389
	     1352f8c0 77dd5de3 00000dfc 8f9a3de4 00000000 kernel32!BaseThreadInitThunk+0x24
	     1352f908 77dd5dae ffffffff 77dfb7d8 00000000 ntdll_77d70000!__RtlUserThreadStart+0x2f
	     1352f918 00000000 5b49d260 00000dfc 00000000 ntdll_77d70000!_RtlUserThreadStart+0x1b


	
#. [D] CSCut59183, CFD S6
	+ https://cdetsng.cisco.com/webui/#view=CSCut59183
	+ Confirmed with PM Selim Baygin (sbaygin)

#. [O] WO0000000226784
	+ Morgan , Wallis Tong (Mobile)
	+ Attendees are able to hear the panelists during breakout.
	+ Mobile client  don’t support practice session, mobile client users are always out of practice session, so if mobile user is the panelist, the attendee still  can hear mobile panelist.	

#. [W] WO0000000225244
	+ No speaker was detected! Make sure your device is connected correctly and test it again.
	+ TSP
	+ CSmAgentWnd::W2C_IsAudioDeviceNormal, end, lResult = 4
	+ Need SSE engineer to check further with TSP provider side
	
#. [W] WO0000000226507
	+ Waiting for client log for further investigation
	+ Wu Xi is checking (Mac OS)

#. [W] WO0000000226765
	+ Connection taking too long to get connected to VoIP
	+ Gpc hadn't callback caused the client hadn't join VoIP
	+ File a bug

#. [D] CSCvc02236
	+ https://cdetsng.cisco.com/webui/#view=CSCvc02236
	+ OnSessionCreateConfirm, sRet[1]
	+ Analyze From Xu Bin
		- Client failed to start hybrid session 
		- because Tahoe get invalid account info from TahoeDB (see below error log), 
		- so Tahoe respond the error to CB.

#. [D] 681199594
	+ SR 681199594, DB SYSTEL GMBH, Whiteboard CWMS, BEMS517272
	+ whiteboard enable logic
	+ Document and presentation sharing
	+ To enable whiteboard feature, bit 10 of SessionTypeOptions should be 1
	::
	 
	 I’ve checked customer’s system and ITEMVALUE from WBXMEETINGTYPECONFIG table, 
	 where meetingtype=3 (default meeting session) and ITEMNAME='SupportPresentation'value was “0” on both DCs (in both DBs). 
	 Changing it to “1” for both DCs, fixed the issue.

#. [D] WO0000000211161
	+ Unable to join VOIP conference or use Webcam to share video in meetings.
	+ Loadlibrary failure, msvc.dll, mac.dll, tp.dll, gpsvc.dll
	+ Customer will re-install systom
	+ Test on customer site
	+ Ask for update [mail out]
	+ Got confirm from Chris Chen, Closed


2016-11-14
----------

#. [P] WO0000000226423
	+ SVP Call Drop
	+ telephony audio was dropped every 30 minutes for two users
	+ Conference ID: 2886604324

#. [D] WO0000000224978
	+ MC T30.6, Save File can't work
	+ From SuZhou Eric Tang
	+ Root Cause
		- Docshow: AllowSaveAndPrintInDocShring disable
		- Site Admin >> Common Site Settings >> Allow Print / Save in Document 

#. [P] CSCut59183, Action(confirm with PM - Selim Baygin)
	+ Issue description
		- Host buy two account
		- Expectation : Just can start two meeting at the same time
		- Actual : It can start the 3rd meeting in TP
	+ CMR Hybrid solution, maintain
	+ Current use CMR4, without this issue
#. [D] CSCvb69543
	+ Had closed
	+ Confirmed with PM: Connie Tang and Engineer: Wilson Chen & Wallice Wang, the conclusion is: the engineering team feels that opening the firewall for only the WebEx MMP servers is still a secure solution

#. [D] CSCvb71340, T31.8 (CC 2016.10.15)
	+ Update status to Bill Wu
	+ Need HF team help to reproduce, mail
	+ Confirmed with Paul, changed to U
	

2016-11-07
----------

#. [W] CMR issue 43
	+ https://sqbu-github.cisco.com/CMR/support/issues/43#issuecomment-213229
	+ Need Send a mail to paul liu
	+ Request webex log

#. [P] WO0000000211492
	+ URGENT WO0000000211492: VoIP Issue HD0009165473
	+ Sunny Liao sugget rollback to T30

#. [D] CSCvb95846
	+ https://cdetsng.cisco.com/webui/#view=CSCvb95846&vt=2
	+ Check the Mats, is the same like the plist , so seems not a bug, J

#. [P] WO0000000224259, add to pits
	+ Webex client crashed on HP Elite x2 1012 G1
	+ ntdll encounter 0x80000003 error
	::
	 
	 This happens when you hit a breakpoint (int 3) instructionand there is no
	 debugger connected.  Most often, this is a breakpoint in the storage
	 allocator, usually hit when the rather simplistic tests done in the
	 Release CRT discover heap damage, although that is not the only source of
	 the error.

#. [D] ATS ISSUE: can't record
	+ From Rudy Sheng
	+ Seems caused by the build
	+ EC crashed, WCLDll.dll

#. [P] Audio session is grayed out for some user
	+ From Daisy Zhang
	+ Need check hybird audio control flag
	+ https://sqbu-github.cisco.com/CMR/support/issues/150
	+ https://sqbu-github.cisco.com/CMR/support/files/2141/wbxtra_10272016_184649.zip
 

#. [W] WO0000000223395, CSCvb92423
	+ Meeting Center client Help option is loading the generic page instead of redirecting to the PG customized page
	+ Docshow => URLs => QSHelpURL
	
#. [D] WO0000000221752
	+ Client crash, wseclient.dll
	+ Assigned to WME (Karina Li)
	::
	 
	 The previous fix is about ticket HD0009185218/WO0000000210084 and cdets  https://cdetsng.cisco.com/webui/#view=CSCvb18905
	 The code fix has submitted in T30.13, and already in T30.14.

2016-10-31
----------

#. [W] WO0000000216828
	+ Webex client crashes
	+ https://cisco.box.com/s/n1odfzep4l0msktbdjxms1e20015kwke
	+ WME qiwei hao is checking

#. [D] WO0000000213144, No response from customer
	+ Video dropped for all PC endpoints
	+ Pingru Cheng mailed to close for the customer hadn't response
	::
	 
	 1	mac.dll	[8412:11944]	MMP	23:22:52.606 10/12/16	[UTIL] INFO: [MAC] CMMAudioClientCtrl::OnQoEReport [WbxMQD] [MQD -> MMP] SiteID=867872, ConfID=3906915798, NodeID=16818177, Mic Quality=(0.5591, 0.9093, 0.9405), Mic MOS=(3.3268, 3.5150, 3.5083), 0d=0.41050, 1d=0.57891, 2d=0.28477, 3d=-0.14279, 4d=-0.68760, 5d=-0.54891, 6d=0.53802, 7d=-0.35928, 8d=-0.11508, 9d=0.24854, 10d=0.67064, 11d=0.72355, 12d=0.47830, 13d=0.19600
	 2	CFW	[8412:11944]	CFW	23:24:28.296 10/12/16	CSmDefUserMgr2::OnAddUser, NodeId[16826369], ClientOSType[0], Name[Trey Contello], TPUserType[0], AttendeeID[135973] LockStatus[0] TPVAID[0]
	 3	atarm.dll [8412:11944]	EUREKA	23:58:20.908 10/12/16	GCC_Conference::on_session_close_indication,ION=0,conf_id="3906915798",prot_type=21,session_id=113,reason=128,
	 4	CONFMGR	[8412:11944]	ConfMgr	23:58:20.908 10/12/16	CAtConfAgent::on_session_close_indication,conference: 0xA1135AC Reason: 128session_key0x65ABBC0
	 5	CONFMGR	[8412:11944]	ConfMgr	23:58:20.908 10/12/16	RemoveSession:m_pSink->OnSessionCloseIndication(reason,pSession);
	 6	webexmgr.dll	[8412:11944]	ServCom	23:58:20.908 10/12/16	CMCServiceMgr::OnSessionCloseIndication, pSession[a005e08], sessionType: 21, sessionName: APPSVR_SESSIONTYPE_MM_VIDEO
	 7	CFW	[8412:11944]	CFW	23:58:20.908 10/12/16	CPfwServiceMgr::OnSessionCloseIndication, reason=128,Session type = 21
	 8	CFW	[8412:11944]	CFW	23:58:20.908 10/12/16	CSmSvcVideoSessionMgr::OnSessionCloseIndication, start
	 9	atarm.dll	[8412:11944]	EUREKA	00:10:17.865 10/13/16	GCC_Conference::on_session_close_indication,ION=0,conf_id="3906915798",prot_type=4,session_id=115,reason=128,
	 10	CONFMGR	[8412:11944]	ConfMgr	00:10:17.865 10/13/16	CAtConfAgent::on_session_close_indication,conference: 0xA1135AC Reason: 128session_key0x65ABBC0
	 11	CONFMGR	[8412:11944]	ConfMgr	00:10:17.865 10/13/16	RemoveSession:m_pSink->OnSessionCloseIndication(reason,pSession);
	 12	webexmgr.dll	[8412:11944]	ServCom	00:10:17.865 10/13/16	CMCServiceMgr::OnSessionCloseIndication, pSession[162c5a80], sessionType: 8, sessionName: APPSVR_SESSIONTYPE_DESKTOP_SHARING


#. [D] WO0000000212478
	+ 3 users were disconnected almost at the same time
	+ Bhaskar Bhaumik had closed. Need check the ticket
	+ They find it odd that nothing would have changed yet all of a sudden it's working again
	
	::
	 
	 https://cisco.box.com/s/ecdck4abgkqqojg0aghuswuqqot1bc90
	 ConfID: 1870316351
	 Impacted user: Guadalupe Larrieu
	 Impacted User's Phone Number: +54 11 5777 2071

#. [D] WO0000000219862, CSCvb78192
	+ SC crash
	+ AppSharing load failure
	+ Fix in T31.8 & T30.14
	+ https://cdetsng.cisco.com/webui/#view=CSCvb78192

#. [D] WO0000000223080, INC000000015580
	+ WebEx 11 , urgent
	+ VOIP can't use
	+ root cause: SHA264 crypto method change, need page to fix

#. [D] CSCvb85985
	+ The page of Meeting info became blank screen on MC client with PPT info  template
	+ https://cdetsng.cisco.com/webui/#view=CSCvb85985
	+ From QA, Cellion Ye is checking

2016-10-24
----------

#. [D] CSCvb78958
	+ multi cameras support
	+ https://cdetsng.cisco.com/webui/#view=CSCvb78958&vt=3
	+ assign to Ju Ma, wseshell.exe
	

#. [W] CSCvb69936, T30.14 (CC 2016.10.15)
	+ DNS, DHCP can config proxy url
	+ WPAD
	+ HD0009249582,HD0009243179
	+ It takes 1-3 minutes to connect to VoIP/Video for certain networks on WBS30.9 MC client.
	+ Downgrade sites to WBS30.6 or lower or Upgrade sites to WBS 31.
	+ CCmHttpProxyManager::InitGetterArray
	+ Configuring WPAD Entries
		- https://technet.microsoft.com/en-us/library/cc713344.aspx 

#. [W] WO0000000214739
	+ Meeting window crashes few seconds after joining the meeting.From logs, it crashed in tp.dll
	+ WME issue, Karina Li is checking

#. [W] WO0000000216265, Video option is not getting enabled while in session also hangs at connecting to audio
	+ CSmSvcVideoSessionMgr::OnVideoSessionStatus
	

2016-10-15
----------

#. [D] CSCvb45367
	+ T32 R2 client, received ping result 2, meeting exist but client still try to create meeting and it failed.
	+ Root cause: SetPingErrorTen hadn't reset when start next ping
	+ Which introduced by CSCux45779
	+ CSCux45779
		- After host crash, CB end meeting. But MZM will keep the meeting 4 minutes. 
		- In 4 minutes, attendee should send create conference request to MZM.
		- It does not exist on 31.0.0.1304 client build.


#. [W] WO0000000217451, INC800004982208
	+ docshow parameters:
		- AutoDisconnectFlag
		- SingleDuration
	+ CMCDocshowMgr::ProcessMeetingParam
	+ some automatically end meeting scenarios
		- Meeting reached to max meeting duration, which is configured in session type in Superadmin, controlled in CB
		- Meeting reached to scheduled end time+1 hour when host hasn’t joined yet into meeting. Controlled in CB,  this is the case for pic in Lisa’s reply.
		- When there is only one WebEx attendee in a meeting(all others left meeting), attendee side will leave meeting automatically, then CB will close meeting.


#. [W] WO0000000209473 
	+ Audio option not populating properly
	+ Our SSE is working with the customer to get the latest data [2016-09-21]
	+ Checklist
		- CDlgQuickstart::EnableItem
		- CSmAudioStatusWrapper
		- CQuickStartDlgPresenter::OnAudioMore
		- CSmHybridAudioMgr::StartHybrid
		- CSmHybridAudioMgr::CheckDownloadGTC
		- CSmHybridAudioMgr::OnTELEDownloadFinished
		- CSmHybridAudioMgr::CheckDownloadGTCEx
	::
	 
	 From trace, when create audio session, will try to download global call in number use url: https://kpit.webex.com/url3000/getGlobalTelecon.do?siteurl=kpit&confId=3239013003&isLarge=1&location=0&needFilter=false&tollFree=1  ,
	 But there is no download finished notify, so audio session is not created.
	 
	 From recording, it can show audio dialog at 5:10, I think there is long network delay.

#. [D] WO0000000213231 (The link provided by Fibin unavailable), Audio settings always reset
	+ REGKEY_VOIP_PATH
	+ CAudioTestDialog::CheckAudioDevice
	+ CSmHybridAudioMgr
	+ CAudioTestDialog
		- GetDeviceList
		- CAudioTestWizardWrapper::SetSelDevice
	+ IAudioWizard
	+ CAudioTestWizardWrapper
		- GetSelDevice
	+ CPcmAudioMgr::AW_CreateAudioWizardCtrl
		- MMCreateAudioWizardCtrl
	+ CPcmAudioMgr::CopyDeviceInfo
	::
	 
	 Audio settings always reset
	 Audio settings of WebEx Meeting Client are reset after the client update from T31.4.2 to T31.5.1.
	 This was reported by many NOKIA users, always after a site upgrade.
	 https://app.box.com/s/wn23mszfurw993aim80hnxb6k3pigu66
	 It has been done on two PCS, on Javier.oscuna.ext@nokia.com and Edwin.vega.ext@nokia.com

#. [W] WO0000000216726, WO0000000216198
	+ It takes up to 2 mins to the audio through  connect to call using computer.

#. [W] CSCvb47815
	+ Can not start meeting from Firefox 49.0.1
	+ Root Cause : 
		- Code Issue which depend on parameter sequence
		- Firefox Changed the parameters sequence
	+ CATGpcWindow::SetParameters
	+ CorrectSchemaofUrlRoot

#. [D] WO0000000206787
	+ Meeting screen is getting frozen
	+ Customer closed this case ,Perhaps , he resolved it by himself without more additional info.

2016-10-08
----------

#. [W] WO0000000214995
	+ 7 minutes of audio missing in the NBR
	+ There is no client trace available.

#. [D] CSCvb53084
	+ Please take a look on this,  it should be a server side change.
	+ Just change in web side.
	::
	 
	 Description: Background:
	 A user from an external company (called Everything Everywhere = EE) is joining a meeting on T-Systems WebEx.
	 When this external user joins the meeting (successfully), excessive traffic towards T-Systems WebEx Nodes is generated.
	 
	 It is by design.
	 Choose internal, only internal user can start/join meeting, it will only ping NODE MZM.
	 Choose external, Both external/internal users can start/join meeting. all of them will ping DC/GDM and NODE MZM.
	 
	 But currently we do not have external only option. So it is one new requirement. I will file enhance bug and submit requirement to trace.



#. [W] WO0000000197315
	+ Randomly during an EC, Active video user's webcam video turns off, when this happens, EC's meeting option also becomes unchecked (Event -> Option -> "Video" has to be checked again to return Video capabilities for all attendees)
	::
	 
	 Typically when this happens, the option disables.
	 This time the option did not disable, but passing presenter back and forth fixed the issue.
	 
	 Because presenter "Valerie Arnold” have network problem around  08:03:23  to connect the MMP server, 
	 for this case presenter will try do reconnect, and tried 3 times the MMP reconnect still failed.  
	 So presenter will directly close meeting "Video Session”. 

2016-09-26
----------

#. [D] CSCvb41280, CSCva66671
	+ https://cdetsng.cisco.com/webui/#view=CSCva66671
	+ Event Center crash
	+ The truth is the fixing is cross modules in atgpcext.dll and WebExMgr.dll
	+ GPC FuzzyWindow
	::
	 
	 1) Uninstall meeting client and restart computer
	 2) Open IE and login cisco.webex.com, and start a EC
	 3) Exit EC.
	 4) Do not close IE, and create a new IE tab, start a EC on t31sp.qa.webex.com (lyn/P@ss123)
	 5) Meeting will crash after meeting started.

#. About Issue
	+ Check CMR4 video call-back

#. [D] WO0000000212996
	+ check “default call in number” display logic in client
	+ Our customer encountered an issue, when set the default phone number format like this “+61 2-8293-5711”, the call in number will not be shown in client.
	+ We found a workaround, change the phone number format from “+61 2-8293-5711” to “+61(2-8293-5711)” , this number will be shown in client. But ,there is another problem for this workaround, the national flag cannot be displayed in client.
	+ Keynotes
		- CSmHybridAudioMgr::ReplaceWithPreferredGTCItem
		- CSmHybridAudioMgr::CheckDownloadGTCEx
		- CSmHybridAudioMgr::ParseGTCNumberItem
		- CSmHybridAudioMgr::SaveNumber
		- CSmHybridAudioMgr::SearchPreferredGTCNumber


2016-09-19
----------

#. 680669022, CSCvb30721, CSCvb19442
	+ After updating the system to CWMS 2.7, ending the meeting generates error "Cisco WebEx Service has stopped working". It happened only for meetings that were started from PT/Outlook, from Web worked fine.
	+ It’s caused by featured tracking function. When meeting end, not call kill work thread, so the work thread still work. But the main thread has exited, so meet crash.
	::
	 
	 I’ve talked with QA and the same issue is reproducible in our lab, too, with Outlook 2013.
	 They can reproduce it both for meetings started from PT and Web and they opened CSCvb19442, that I pointed out yesterday.
	 
	 As the issue is reproducible in the lab, I’ve tried your scenario in the lab at the first, 
	 reproduced the issue and collected dump logs. You can find it on:
	 https://cisco.box.com/s/vg56oyunfq8cvtwarrijbln7zbl7kxu8

#. CSCva66089, CSCva19645
	+ Cannot print OBTP mail body
	+ Printing Meeting invites from Outlook with telepresence devices enabled
	+ https://cdetsng.cisco.com/webui/#view=CSCva19645

#. WO0000000211898 [Had looped Elton tang]
	+ MMP session was started late
	::
	 
	 For TP meeting, the TPGW will not create MMP and CB video session, 
	 So the logic is the first client (MAC/Win/Linux)  will be responsible for that.
	 
	 In current architecture,  it always be MMP make sip call to TAS,
	 And MMP get TAS ip address only when first user join meeting and create video session.

#. WO0000000208302, [Henry Wang for Video, Xu Bin for Audio]
	+ Telepresence can't hear WebEx audio
	+ WebEx can't view Telepresence video and can't hear Telepresence audio
	+ Checklist
		- CPfwServiceMgr::OnASNPduFromCB Call pPfwAudioMgr->SetActiveSpeakerList
		- CSmSvcVideoSessionMgr::OnVideoSourceStatus
		- CPfwServiceMgr::OnASNPduFromCB
	::
	 
	 From trace, TP user video sending status is earlier than TP user data list, 
	 So webex cannot show TP user video for can't find the corresponding TP user.
	 
	 Tahoe disconnect cascading link since it does not get a final response to re-Invite in 10s

#. WO0000000211961, CSCvb26805
	+ Cluster B fail to connect RA/AA now
	
2016-09-12
----------
#. CTG Alpha Outage Notification: Outage in go.webex.com
	+ Multiple Webex hosts are intermittently unavailable and services in go.webex.com are impacted
	+ https://remedy.cloudapps.cisco.com/fetchIncidentBasicInfo.do?case=INC800004825436
	+ We will keep you posted on the progress
#. WO0000000208684
	+ Default information tab template not working as intended
	+ No Access Code or Host Password
	+ No global link
	+ Check List
		- Setinfo lpszCallinPhoneNo
		- CMCDocVideoSessionMgr::SetInfo

#. 680795888 [Waiting for customer]
	+ WebEx always send atinst.exe
	+ For IE protected mode enable, we need use atinst.exe to register and elevate privilege, it only pop up the first time as below UAC Dialog

#. CSCvb19442 [Code done and verified]
	+ An Orion bug 
	+ MC crash after End Meeting

 
#. WO0000000211399
	+ You cannot join the meeting because the meeting number you typed is incorrect
	
	::
	 
	 Currently we found the docshow to client is 
	 <SupportSvrSecParams>1</SupportSvrSecParams><SecureSMAC4Node>0</SecureSMAC4Node>
	 
	 So currently it’s not use the new H256 s_mac, this site send CB with MD5 s_mac, and MD5 is no more support in our new Eureka. 
	 
	 Loop in Jerry and please help check if is config issue or page/server is not in same release. 

#. WO0000000187754, WO0000000187754
	+ Citrix 6.5 Windows Server 2008 R2, Windows 7 Crash
	::
	 
	 So this customer maybe not support ActiveX Scripting Engines
	 Please let customer enable it like https://www.manageengine.com/products/desktop-central/remote-control-enable-activex.html to see if issue can be resolved.

#. WO0000000211492
	+ VoIP Issue
	::
	 
	 I checked server log, the data transport disconnect about 2 minute then recover at first and second time, 
	 It’s cause Mark can’t  hear/speak,  in fact he didn’t leave audio session.

#. 680654847
	+ 20+ seconds to fully load meeting room
	::
	 
	 From trace, the long time happen on two places after show meeting window:
	 One is when init video cc, take about 10 seconds;
	 Second is when preview camera;
	 
	 9 CFW06:15:21.263 08/24/16[7000:7720]CSmSvcVideoSessionMgr::EnrollMMSession, begin
	 10 wseclient.dll06:15:21.404 08/24/16[7000:7720]WSE Info: CBaseGraph::ReleaseGraph m_pGraph done.
	 11 wseclient.dll06:15:31.412 08/24/16[7000:7720]WSE Info: CWseVideoCapEngine::CWseVideoCapEngine.this = 0x95df5a0
	 12 CFW06:15:33.716 08/24/16[7000:7720]CSmSvcVideoSessionMgr::OnEnumerateCameras, ulDevHandle=254110920 end devName=World Facing Right
	 13 CFW06:15:33.716 08/24/16[7000:7720]CSmSvcVideoSessionMgr::OnEnumerateCameras, ulDevHandle=254110360 end devName=HP Full HD Camera
	 14 mutiltpd.dll06:15:33.796 08/24/16[7000:7720][MVC]:CMmSVideoClient::StartCameraPreview
	 15 wseclient.dll06:15:33.846 08/24/16[7000:7720]WSE Info: CWseVideoCapEngine::Init format->width = 640,format->height = 360,format->frame_rate = 30.000000,format->video_type = 3
	 16 ComUI06:15:43.866 08/24/16[7000:7720]CDlgQuickstart::PositionChanged -- begin:

2016-08-23
----------

#. WO0000000206822
	+ ou cannot connect to audio or video because we cannot validate the security certificate
	+

#. WO0000000182993, WO0000000207215
	+ User gets to 99% and is unable to join meeting
	+ Which has bug CSCuz83890 fixed on T31.5.
	+ windowscodecs.dll & WCLDll.dll
	::
	 
	 Trace info:
	 1 CFW 02:45:26.227 07/26/16 [6316:8736]  CConfContextMgr::SetParam name=[$AboutDlgClientVersion] value=[31.4.0.44]
	 2 CFW 02:45:26.227 07/26/16 [6316:8736] CConfContextMgr::SetParam name=[$SiteUrl] value=[https://nbcucmr.webex.com/nbcucmr]
	 3 CFW 02:45:47.923 07/26/16 [6316:8736] [Performance]CSmDefUserMgr2::InitializeUI, end
	 4 ComUI 02:45:48.095 07/26/16 [6316:8736] CDlgQuickstart::OnInitDialog Fire_OnDialogInited
	 5 webexmgr.dll 02:45:48.095 07/26/16 [6316:8736] CQuickStartDlgPresenter::InitLockBubble(), begin
	 6 webexmgr.dll 02:45:48.111 07/26/16 [6316:8736] CQuickStartDlgPresenter::InitLockBubble(), Initial
	 7 webexmgr.dll 02:45:48.111 07/26/16 [6316:8736] CQuickStartDlgPresenter::InitLockBubble(), end
	 8 webexmgr.dll 02:45:48.111 07/26/16 [6316:8736] CQuickStartDlgPresenter::InitInviteRemindButton CMCWebACDMgr = 0
	 9 crashdle 02:45:48.126 07/26/16 [6316:8736] ===================================Crash Log Begin
	 10 crashdle 02:45:48.220 07/26/16 [6316:8736] 77A7754B  001FB9D0  0001:0002754B 5708952E b5acac3b4a6c4515af416d60366399652  "C:\Windows\SysWOW64\ntdll.dll"
	 11 crashdle 02:45:48.220 07/26/16 [6316:8736]  6787BF61  001FBCE4  0001:0010AF61 5706A236 e163ad932d9048ea8775ecac137fa63c1  "C:\Windows\system32\windowscodecs.dll"
	 12 crashdle 02:45:48.220 07/26/16 [6316:8736] 0F1F9295  001FBD30  0001:00008295 56C7043F 48076cc64b1044b7b5600dd54af169752  "C:\ProgramData\WebEx\WebEx\T31_UMC\WCLDll.dll"
	
#. WO0000000206942, WO0000000196500
	+ Microphone not getting detected in webex meetings

#. TAS000000024293, WO0000000198221
	+ Host is getting disconnected from the meeting
	+ CSCux47573
	+ CreateWebcamDetectedPopup
	::
	 
	 1) please have the customer test with both registry values set to 0
	    HKEY_CURRENT_USER\Software\WebEx\Config\BUBBLE\allways_start_my_camera_when_join_meeting = 0
	    HKEY_CURRENT_USER\Software\WebEx\Config\BUBBLE\do_not_show_me_again_when_join_meeting_next_time = 0
	    Then check if issue can be resolved.
	 2) If issue still cannot resolved, please let customer save a new webex client trace to us.

#. BEMS Creation - P3, SR 680475454, EMPRESA DE TECNOLOGIA E INFORMACOES DA PREVIDENCIA, WebEx Meetings Application Freezing, BEMS499797, Clients
	+ Customer noticed this issue with few users so far. 
	+ The one user with the Microsoft LifeCam HD-3000 crashes every time
	+ Other users with Logitech cameras crash intermittently
	+ CSCvb09710 is filed to track this issue
	::
	 
	 According to MSDN, this thread is blocked. 
	 https://msdn.microsoft.com/fr-fr/library/ff541979(v=vs.85).aspx
	 
	 0:000:x86> dt RTL_CRITICAL_SECTION 0b91c044
	 atmgr!RTL_CRITICAL_SECTION
	   +0x000 DebugInfo        : 0x1472b7f0 _RTL_CRITICAL_SECTION_DEBUG
	   +0x004 LockCount        : 0n-6
	   +0x008 RecursionCount   : 0n5136
	   +0x00c OwningThread     : 0x00003970 Void
	   +0x010 LockSemaphore    : 0x00000f58 Void
	   +0x014 SpinCount        : 0
	 0:000:x86> ? 0x1 & (-0n6)
	 Evaluate expression: 0 = 00000000   // the first bit is 0 and therefore the critical section is locked. 
	 0:000:x86> ? (0x2 & (-0n6)) >> 1
	 Evaluate expression: 1 = 00000001  // The second bit is 1, and so no thread has been woken for this lock. 
	 0:000:x86> ? ((-1) - (-0n6)) >> 2
	 Evaluate expression: 1 = 00000001 // The complement of the remaining bits is 5, and so there are five threads waiting for this lock.

#. WO0000000203046, TAS000000024547
	+ MC client crashes on Lenovo ThinkPad X1 laptops when attempting to join PC audio (VoIP).
	::
	 
	 We found some strange log:
	 5 time: 22:45:22 696 07/26/2016     DllName: mutiltpd.dll        Message: CWbxAeAudioCapturePlatformCoreAudio::GetDefaultFormat pfmt, wFormatTag:65534, cbSize:22, nAvgBytesPerSec:768000, nSamplesPerSec: 48000, nChannels:4, wBitsPerSample:32, wFormatTag:65534 this=0x75e4f28 
	 Level: info The default format is read from OS API. They give us channel is 4. But they are not more than 2  in our experiences. 
	 4144 time: 22:45:12 374 07/26/2016     DllName: mutiltpd.dll        Message: [AE AQE]  OnCaptureData()  Failed!, m_IsAQEStarted = 1, dwSize = 20, wFormatTag = 65534, nChannels = 4, nSamplesPerSec = 48000, nAvgBytesPerSec = 384000, nBlockAlign = 8, wBitsPerSample = 16,Data Len = 960 this=0x1982c828 
	 Level: warn Audio data length recorded by OS are 960 bytes witch is usually 2 channels data.   This thread ran for a while and crashed. But there was no any processing except print warning logs. We have not repro bug yet. 
	 Can you ask customer to upgrade audio device driver.  Recently, Lenovo  provides some update for audio device.
#. WO0000000206904, TAS000000024745
	+ Uninvited attendee in meeting
	+ Please use command “%userprofile%/appdata\Local\Temp” to open the tmp folder.
	::
	 
	 For client, we will save 5 counts wbxtrace to tmp folder.
	 Maybe can ask customer provide it, we can check it according to confid.
	 
	 We saved last 5 meeting’s client logs in customer’s computer. We can ask customer to provide it. 
	 And according to the description, seems this user is a pure telephony attendee. 
	 Such attendee will not exist in attendee usage report. Maybe we can check how many telephony users in that meeting, 
	 and compare to the attendee usage report to check if there is any pure telephony user joined.
#. WO0000000200783
	+ camera not work well when sharing desktop 
	+ The integration camera not be found when AppSharing has be launched. So video render module drawing always is fail.
	+ CFW       12:19:32.776 07/20/16    [2988:1212]                CSmSvcVideoSessionMgr::OnCameraModify begin, [Pull out]
#. WO0000000208246, TAS000000024771
	+ Error while joining audio via Computer
	+ MMP call Tahoe fail
#. WO0000000202437
	+ Host receiving Garbled Noise for 10-15 sec,whenever he joins/start Audio portion
	::
	 
	 I check client log, and found client MOS is low at two point, could you help check it
	 22:15:41.957 08/02/16   [5020:9584]        [AudioEngine] INFO: QoEM:[R1-106503424] R_net:-97,MOS_net:2.38125,R:-86,MOS:2.23721,bitrate:29kbps,pktRate:43,jitter:8ms,delay:300ms,pktDrop:38%,plcPktRate:0%,silentRate:38%
	 22:45:40.958 08/02/16   [5020:9584]        [AudioEngine] INFO: QoEM:[R1-106503424] R_net:-128,MOS_net:2.38125,R:-114,MOS:2.23721,bitrate:24kbps,pktRate:35,jitter:5ms,delay:300ms,pktDrop:45%,plcPktRate:0%,silentRate:45%
#. TAS000000024717, WO0000000206898
	+ join meeting failure from spark team cmrforsparktest.webex.com
	+ Client according to following docshow param to transfer new smac/ old smac: SupportSvrSecParams or SecureSMAC4Node
#. WO0000000208253, TAS000000024769
	+ Not able to connect VOIP audio
	::
	 
	 28           tp.dll      00:30:35.583 08/17/16   [2508:4880]        [UTIL] ERROR: CCmReactorNotifyPipe::OnInput, nRecv=-1 fd=0x7e0 err=10093 this=0x986229c[CmReactorNotifyPipe.cpp:79]
	 29           tp.dll      00:30:35.583 08/17/16   [2508:4880]        [UTIL] ERROR: CCmReactorSelect::RunEventLoop, select() failed! nMaxFd=2016 err=10093 this=0x9861900[CmReactorSelect.cpp:80]
	 30           tp.dll      00:30:35.583 08/17/16   [2508:5456]        [UTIL] ERROR: CCmReactorNotifyPipe::OnInput, nRecv=-1 fd=0x7cc err=10093 this=0x985f37c[CmReactorNotifyPipe.cpp:79]
	 31           tp.dll      00:30:35.583 08/17/16   [2508:5456]        [UTIL] ERROR: CCmReactorSelect::RunEventLoop, select() failed! nMaxFd=1996 err=10093 this=0x985e9e0[CmReactorSelect.cpp:80]
	 32           tp.dll      00:30:35.583 08/17/16   [2508:5532]        [UTIL] ERROR: CCmReactorNotifyPipe::OnInput, nRecv=-1 fd=0x5f8 err=10093 this=0x985e45c[CmReactorNotifyPipe.cpp:79]
	 33           tp.dll      00:30:35.583 08/17/16   [2508:5532]        [UTIL] ERROR: CCmReactorSelect::RunEventLoop, select() failed! nMaxFd=1528 err=10093 this=0x985dac0[CmReactorSelect.cpp:80]
	 Look like TP initialize fail, please help check it
#. WO0000000207759, HD0009177484
	+  Trouble joining meetings after upgrade
	+ https://cdetsng.cisco.com/webui/#view=CSCux96839
	+ didn’t update the DLL(mutiltpd.dll) client version, the version is same as T30.5
#. WO0000000203748
	+ Unable to hear the Audio in the session hosted from ufred.webex.com
	+ The attendee is not able to join VoIP using training center, but able to join using the meeting center
#. WO0000000203717
	+ it is because the AAGC of microphone is enabled in R1, but in R2, it is disabled.
	+ From Mac
		::
		 
		 I think case2 is caused by WME’s wrong recoredVolume, Mac client always get 200 volume when the Audio Setting dialog is opened. 
		 Mac codes could call kAudioWizardCommandId_GetRecordVolume to get current setting volume,but WME gave back a wrong value.
		 And this bug didn’t exist on R2, is there any related codes was fixed in R2 but was ignored in SP?
	+ From Windows
		::
		 
		 Window is the same issue, when it always get 30 volume even set to 0 volume.
	+ From Audio Engine
		::
		 
		 #. Windows, Open wizard, uncheck “Automatic adjust volume”, this flag will set to the audio engine used in meeting. This logic is ok. But per Ross, audio CC has a logic to set minimal volume(30) when reload(closing wizard), so this is the root cause of why you can get 30 even you set to zero in Wizard. 
		 #. Mac,  Open wizard, uncheck “Automatic adjust volume”, this flag will not set to the audio engine used in meeting.  So the volume always adjust by the audio engine using in meeting. Please help to check the Wizard logic Audio CC in MAC.
	