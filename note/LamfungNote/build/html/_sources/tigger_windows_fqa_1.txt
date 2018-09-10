Tiger Windows FQA 
============================

#. [D] WO0000000443473, (CFD::CSCvf64128)
	+  Start a meeting , as soon as Audio and Video connection pops up. Click on call me immediately. We see call me trying to connect , however keeps spinning for a minute or so and disconnects with “ No answer”
	+ Key Points
		- CSmTelephonyMgr::Connect
		- CSmTelephonyMgr::InitializeConfirm

#. [P] WO0000000432420, MC client crashes for all users when screen is shared
	+ CPfwMainPanelsView::Layout_MovePanels
	+ CPfwMainPanelsView::LayoutPanels
	+ https://wiki.cisco.com/display/ORIOLE/Walmart+RT+-+20170727 

#. [P] WO0000000436669, (CFD::CSCvf60288)
	+ why Panelists are not able to sort the Attendee List by the "Company" column for an Event Center.
	+ Key Points
		- CDlgAttendeeList
		- CDlgAttendeeList::LoadList

2017-08-14
----------

#. [P] WO0000000426487, (CFD::CSCvf56875)
	+ customer said that there is a delay when the user end the meeting
	+ Key Points
		- CMCServiceMgr::Initialize
		- WbxFeatureTrackingInitialize
		- SetTelemetryXML		
	+ Docshow Parameters
		- TeleMetryInfo

2017-08-08
----------

2017-08-01
----------

#. [P] HD0009411511
	+ Audio & Video Statistics issue
	+ Key Points
		- MMT_SPECIAL_EVENT_RECORD_VIDEO_QUALITY
		- PMMD_VIDEO_QUALITY_RECORD
		- SaveVideoStatisticsInfoSend
		- CSmHybridAudioMgr::OnAudioNotify
		- WEBEX_AUDIO_SESSION_REPORT_INFO
		- SaveAudioStatisticsInfo

#. [P] WO0000000387183
	+ TSP audio - NBR does not work  for one user
	+ The user can start the recording successfully, but after 30 seconds the recording is disconnected
	+ Key Points
		- CNBRControlMgrWrapper::StartNbr
		- CSmNBRSessionMgr2::OnRecorderPanelNotify
		- CSmNBRSessionMgr2::LaunchWizard
		- CSmNBRSessionMgr2::SetTeleRecType
		- CSmHybridAudioMgr::OnSSREvent
		- CSmNBRSessionMgr2::OnHybridNotify
		- CSmNBRSessionMgr2::OnTelephonyNotify
		- CSmNBRSessionMgr2::OnTelephonyNBREvent
		- CSmNBRSessionMgr2::Start
	+ Docshow Parameters
		- SessionTypeOptions 
		- CMCDocshowMgr::HandleSessionTypeOptions
		- SetSiteEnableOption
		- SessionTypeOptionsExt
		- HandleSessionTypeOptionsExt
		- SetPicassoOptions
		- CMCServiceMgr::Initialize
		- CMCSiteConfigMgr::InitSiteConfig
		- PICASSO_OPTION_TSPWITHOUTADAPTER, 0x40000
	+ Session Type
		- APPSVR_SESSIONTYPE_TELEPHONY
		- APPSVR_SESSIONTYPE_TELEPHONY_THIRD

#. [P] WO0000000392645
	+ Host is not able to upload file and share the file inside the WebEx meeting
	+ Key Points
		- CMCUIMgr::OnSharePresentation
		- CMCUIMgr::LaunchPresentationShare
		- CSmDefUIMgr::OnMenuShareDocument
		- CSmDocViewSessionMgr::NewDocument
		- CPcmDocViewMgr::NewDocument
		- CWBXFileDlg::DoModal

#. [P] WO0000000407644
	+ Meeting center hangs for about 10+ minutes
	+ Issue occurs when Hava Video device is installed
	+ Key Points
		- CSmSvcVideoSessionMgr::OpenVideoOptionDialog
		- CSVCVideoOptionDlg

#. [P] WO0000000407279, (CFD::CSCvf37008)
	+ Meeting client crash when opening Call In teleconference d
	+ Key Points
		- CCallInSubWindow::Initialize
		- strLink.Format(strFmt, IDW_STATIC_8049, strTemp2.c_str())

#. [P] WO0000000394309
	+ While joining the meeting headphone show unhook status
	+ Issue Device
		- Jabra, LogiTech, Sennheiser, Plantronics
		- The above device support mute/unmute sync feature
	+ Solution
		- Check if there are skype process running
		- If yes, disable mute/unmute sync feature

#. [P] CSCvf34460
	+ video, EC, practice session

2017-07-24
----------

#. [P] WO0000000396195
	+ If a user configured their WebEx audio device to be the same USB headset that Microsoft Skype for Business was configured with, Skype would become the active window, and a dial tone would play in the user’s headset after the user connected to audio in Meeting Center.

#. [P] WO0000000393960
	+ The host should be able to join the meeting after the alternate host and use the VoIP functionality
	+ CSmTelephonyMgr::C2W_OnConnectIndication, TSPSDK_CONNECT_VOIP_CONNECT_FAIL

#. [P] WO0000000394536
	+ 

#. [P] WO0000000384873
	+ When customer is on WiFi, PMR and scheduled meetings as host or attendee are unable to join by video
	+ Key Points
		- APPSVR_SESSIONTYPE_MM_VIDEO
		- CPfwServiceMgr::CheckDefaultSession
	
#. [P] WO0000000396708
	+ User is unable to initiate Call using computer having the Skype for Business opened

#. [P] WO0000000394730
	+ 
	+ Key points
		- CWseMFSourceReaderSink::CloseDevice

2017-07-17
----------

#. [P] WO0000000371763
	+ Key points
		- SESSION_TYPE_ENABLE_VOIP
		- SESSION_TYPE_ENABLE_WBX_VIDEO
		- CSmSvcVideoSessionMgr::OnVideoSessionStatus
	+ Docshow
		- SessionTypeOptions
		- HandleSessionTypeOptions

#. [P] WO0000000372715
	+ WebEx Meeting Center - Server Failure or Security Setting Error
	+ tp.dll dependency issue
	+ https://blogs.msdn.microsoft.com/cesardelatorre/2011/03/27/the-application-has-failed-to-start-because-its-side-by-side-configuration-is-incorrect-error-related-to-mmc-exe-programs-and-weird-cause-simple-solution/
	+ https://www.microsoft.com/en-us/download/details.aspx?id=5582


2017-07-11
----------

#. [P] WO0000000357861
	+ When change back to practice mode, attendee can see video
	+ Root Cause
		- CVUIThumbnailView::OnTimer
		- CVUIThumbnailView::AttachVisiblePorts
		- CVUIThumbnailView::SlideInOneUserItem
		- CVUIThumbnailView::AttachUser
		- CVUIThumbnailVideoPort::RequestSource
		- CVUIVideoPort::RequestVideoSource
		- CVUIVideoPort::RequestVideoSourceCMR3
		- IRenderingController::RequestSourceVideo
	+ Key points
		- IDS_EC_PS_TITLE_P
		- CECDocViewSessionMgr::InitMeetingInfoPracticeSession
		- m_bPracticeSessionStarted
		- StartPracticeSession
		- HandlePracticeSessionPDU
		- EC_PDU_TYPE_PRACTICE_SESSION
		- StopPracticeSession
		- StartMainViewVideo
		- SendPracticeSessionPDU
		- SetPanelist
		- GetPanelistsArray
		- CheckPanelistStatusFromEnFlag
		- OnPracticeSessionStarted
		- PFW_MODEL_WPARAM_UI_EC_PS_UPDATE
		- CWndPracticipantlistContainer::VideoStatusChanged
		- CMCPListThumbNailView::StartVideoView
	+ PFWPANEL_MODE
		- PFWPANEL_MODE_COLLAPSE
		- PFWPANEL_MODE_EXPAND
	+ PFWPANEL_STATUS
		- PFWPANEL_STATUS_FLOAT
		- PFWPANEL_STATUS_IN_MM_MGR
		- PFWPANEL_STATUS_IN_FIT_MGR
		- PFWPANEL_STATUS_IN_MM_BAR
		- PFWPANEL_STATUS_IN_FIT_BAR
	+ panel style 
		- PFWPANEL_STYLE_CAN_RESIZE
		- PFWPANEL_STYLE_FLASH_ALERT
		- PFWPANEL_STYLE_DISABLE

#. [P] WO0000000367321
	+ crash at wseclient.dll
	+ https://sqbu-github.cisco.com/WebExSquared/wme/pull/6398/commits/87c12f128d5c8668344f7e23681d470a4af1afa3

2017-07-04
----------

#. [P] SR 682379022 
	+ AOZORA BANKLTD, CWMS Call-in number Japanese characters not displaying, BEMS652230, Clients
	+ Key Points
		- CSmHybridAudioMgr::OnTELEDownloadFinishedEx
		- m_szCallinNumFileEx

#. [D] CSCvf06317
	+ Meeting client closes when started from Firefox
	

#. [P] WO0000000364461, (CFD::CSCve85325)
	+ upgrade to T32.3.1.3 voip issue
	+ Key Points
		- CAccessoryMgrWrapper::ConnectToDevice

#. [P] Alpha site does not show user's cookied photo avatar
	+ https://sqbu-github.cisco.com/CMR/ATS/issues/147
	+ Key Points
		- CCComUIMgr::DrawAvatar
		- OnUserAvatarURLRetrieved
		- OnUserAvatarImageDownloaded
		- GetPhotoURL
		- OnGetPhotoURL
		- CSmHttpCallMgr::ParseResult, e_reqtGetPhotoURL
		- DownloadImageByURL
		- AvatarSavePath, %appdata%\webex
		- CSmAvatarMgr::OnConfJoinConfirm, GetPhotoURL
	+ Docshow Parameters
		- GetPhotoURL

#. [P] New enhancement hasn't been functioning in F2F cluster
	+ what if my country is not listed?
	+ Confirmed that this feature was implement in T31.13 and T32.1
	+ Key Points
		- https://wiki.cisco.com/display/WXTRAINSP/T32.1
		- https://wiki.cisco.com/display/WXTRAINSP/T31.13

2017-06-26
----------

#. [P] CSCve88570
	+ Video call back "Could not connect to the video system. Check the video address and try again"
	+ Key Points
		- HandleTPProfileInfo
		- AddTPProfileNum
		- m_arUserTPProfile
		- GetTPProfileNumByIndex
		- GetProfileTPNumberList
		- GetRecentlyTPCallNumber
		- GetRecentlyTPCallFromReg
		- CallTP, m_strLastTPCallNumber = strVideoAddr
	+ Docshow parameters
		- VideoCallbackInfo

#. [P] MC Client package for CWMS 2.7MR3 and 2.8MR1
	+ MC Client package for CWMS 2.7MR3 and 2.8MR1

#. [D] CSCve94573
	+ T31 client freeze wseclienttr.dll

#. [D] HD0009592572
	+ Key Points
		- SessionTypeOptions=972779519
		- SessionType[39fb6fff], PicassoOptions[3b347b]
		- CMCSiteConfigMgr::InitSiteConfig | dwEverestOption: 972779519, dwPicassoOption: 3880059
		- CSmSvcVideoSessionMgr call UIDataMgr>>CPfwVideoMgr::SetHDVideoEnable(1)
		- CMCSvcVideoSessionMgr::Initialize bIsTPMeeting[0] bCanTPVideo[0] bCanWbxVideo[0] bHQ[1] bHD[1]
		- CSmSvcVideoSessionMgr::ChangeSVCExpOption(1, 1) begin
		- CMmSVideoClient::SetSVCExpMode, ulSVCExpMode = 2

#. [D] TP Callback Issue
	+ Key Points
		- CAudioMainDlg::TPCallBack
		- CSmAudioStatusWrapper::CallTP
		- CPfwServiceMgr::CallTP
		- CAtConfManagerImpl::CallTPDeviceByCB
		- CAtConfAgent::CallTPDeviceByCB
		- send_parameter_request
		- TPCallbackUser_Enter
		- CAtConfAgent::on_conference_parameter_change_indication
		- ENDPOINT_STATUS_RSC_ID, SetTPCallbackDeviceStatus

#. [D] ATS no video session
	+ The video panel on top of the participant list is missing
	+ https://sqbu-github.cisco.com/CMR/ATS/issues/118
	+ CSCve83045
	+ CPfwServiceMgr::CheckPendingSession

#. [P] WO0000000261159
	+ When the customer tries to joint in at his WebEx 11 meeting on the ITalian numer not display on client.
	+ T30.19
	+ Key Points
		- CCallInSubWindow
		- MPMeeting, $MP_FLAG
		- TeleConfParam
		- InitAudioController
		- OnCallInNumberChanged
		- SaveNumber
		- SetCallInConfig
		- SetTeleCallInInfo
		- CSmHybridAudioMgr::GetSessionParam

#. [P] WO0000000345405
	+ WebEx crashes seconds after share-screen application is started
	

2017-06-20
----------

#. [P] WO0000000345890
	+ Crestron Device compatibility issue
	+ Key Point
		- CWclPlistSelfBar::FormatVoipToolTip
		- _string_helper
		- at_str_vprintf
		- need WCL to fix
	
#. [P] WO0000000319087

#. [P] WO0000000337706, (::MMP Server)
	+ WebEx - Audio quality issue reported by all Audio broadcast users
	+ Key Points
		- CMSJitterDetect
		- CAudioStreamingConference::OnDataIndication, AnalysePacket
		- CHybridSIPConnection::on_data_indication, AnalysePacket
	+ Server log
		- 10.100.13.170
		- guest/P!ss!3!7
	
#. [P] WO0000000342853
	+ Unable to click on the start Webcam button / Webcam video shows chopped up

#. [P] WO0000000336095
	+ walmart Crash after upgrade from T30 to T31

2017-06-12
----------

#. [P] WO0000000272041
	+ When the panelists started to drop and I was about to end the session, I saw 6 questions appear suddenly.
	+ Key Points
		- CPcmChatMgr
		- atlchat.dll
		- CSmQASessionMgr
		- CPcmQAMgr
		- qactrl30.dll
		- CQaItemWindow
		- CQaListViewWindow
		- CWndQAContainer
	
#. [P] WO0000000321328
	+ 

2017-06-05
----------

#. [P] HD0009596358, (CFD::CSCve67635)
	+ Meeting Client Can't display Canada Flag
	+ Docshow Parameters
		- MajorCountryCode
	+ Key points
		- Audio and Video Connection
		- CAudioMainDlg
		- CCallMeSubWindow
		- CWndPhonenumber
		- CWndCountryCode::InitData
		- CSmAudioPhoneWrapper::GetAvailableCountryList
		- PrepareCountryArray, g_CountryArray
		- GetDefaultCallbackCountry
		- GetCountryByID
		- pfwres.dll
		- IDB_BITMAP_COUNTRY_FLAGS, 575
	

#. [P] WO0000000297080, (CFD::CSCve64901)
	+ How to reproduce
		- hasuper.qa.webex.com/superadmin/SuperAdmin.jsp
		- /My WebEx/Preferences/Audio
	+ Key Points
		- CAudioMainDlg
		- CAudioMainDlg::CallIn
		- CCallInSubWindow
		- IDW_WINDOWS_AUDIO_CHILD_CALL_IN
		- IDW_STATIC_8049
		- SetCallInPhoneNo1
		- SetCallInCaption1
		- CheckDownloadGTCEx
		- ParseGTCNumberItem

2017-05-31
----------

#. [P] WO0000000296643
	+  WebEx 11 Services - Flag issue for Ireland Toll number

#. [P] WO0000000314760
	+ Customer is unable to convert the recording file

#. [P] WO0000000311149
	+ all the users have lost video

#. [D] CSCve53108, (CFD::CSCve53108)
	+ customer's sound preferences are not saving in meeting

#. [D] CSCve53113, (CFD::CSCve53113)
	+ customer's sound preferences are not saving in meeting

#. [D] WO0000000310774
	+ symc.w.c - customer's sound preferences are not saving in meeting
	+ Root Cause
		- CMCPreferenceWrapper Initialize issue
	+ Key points
		- CMCPreferenceDlg
		- conIOptionsDlgBase
		- CMCUIMgr::OnEditPreference
		- CMCPreferenceWrapper
		- conIMCPreference
		- CMCServiceMgr::OnUserChangeIndicationByService
	+ DlgMeetingPreference.cpp
		- CDlgMeetingPreference::OnOK
		- CDlgMeetingPreference::OnApply
	+ conIOptionsDlgBase
		- conIOptionsMgr
		- conITabPageBase
		- DLG_MEETING_PREFERENCE
		- CDlgMeetingPreference
		- TAB_PAGE_MCPREFERENCE_CHAT
		- CWndMeetingPreferenceChat
		- TAB_PAGE_MCPREFERENCE_PARTICIPANTS
		- CWndMeetingPreferenceParticipants

2017-05-22
----------

#. [P] WO0000000305350
	+ 'The WebEx application has encountered a problem and needs to close' during the meeting
	+ mutiltpd!CRlbConnTCPClient::OnTimer

#. [D] CSCve20228, (CFD::CSCve20228)
	+ wrong user type for attenee in attandance report.
	+ After checked with team, we think it is Not A bug.
		- Attendee detail report only treat the user as ?Panelist? when the user being invited as panelist in EC scheduler page, all other attendees will treat as ?Attendee?.
		- Applicate don't save the user type change status in meeting;
		- Even if we can change code to save it, but If one user are changing from ?Attendee? to ?Panelist?, then to ?Attendee?, it is not easy to know what is the right user type for the user.


#. [D] P3-SR 682283032, (CFD::CSCvd97856)
	+ CWMS 2.7MR2 patch 4 client can't input Japanese character directly on chat window, BEMS616773, Clients
	+ after upgrading to CWMS 2.7MR2 Patch 4, the transformation window is displayed on the left-upper side (not in the chat window, as it was on previous versions).

#. [D] CSCve36558
	+ wrong flag Ireland
	+ Country Code ID
		- http://countryid.com/
		- http://www.nationsonline.org/oneworld/international-calling-codes.htm
	+ GTC number format
		- % split TCALLINNUMBER item
		- @ split, number, country name, country id, bTollFree
	+ Key Points
		- CSmHybridAudioMgr::ParseGTCNumberItem
		- Global Call-In Numbers for This Meeting
		- IDD_MANAGE_GLOBAL_CALLIN
		- CWCLReskin::ShowGlobalCallInDlg
	+ CGlobalCallInNumbersDlg
		- ITelephoneFunc::GetCallinTeleInfo
		- CSmAudioStatusWrapper::GetCallinTeleInfo
		- CWndCustomlistview
		- CWndListview
		- CBitmapCountryFlag, pfwres.dll, IDB_BITMAP_COUNTRY_FLAGS, conutry_flags.bmp


#. [W] WO0000000279539
	+ T30.4.4 capgroup.w.c  atmgr memory error when disconnecting from meetings
	+ Key Points
		- RestartAtMgrForUpdateIEPlugin
		- GetServiceType
		- CAtmgrUpdateIEPluginHelper::RunInUpdateIEPluginMode
		- CMDLINE_UPDATE_IEPLUGIN, /UpdateIEPlugin
		- CAtmgrUpdateIEPluginHelper::RunInStartUpdateIEPluginMode
		- CMDLINE_START_UPDATE_IEPLUGIN, /StartUpdateIEPlugin

#. [D] WO0000000288837
	+ the client crash when the user join the meeting
	+ Deployment issue

2017-05-08
----------

#. [D] WO0000000261105
	+ ARM
		- CAtConfAgent::TryAvailablePingSvr
		- GCC_Provider::ping_request
		- GCC_Ping_Mgr::notify_ping_confirm
		- GCC_Provider_Impl::notify_ping_confirm
		- GCC_Node_Controller_SAP_Sink::on_ping_confirm
		- CAtConfAgent, public GCC_Node_Controller_SAP_Sink
		- CAtConfAgent::on_ping_confirm
		- CAtConfAgent::m_wAgentEngine = AGENT_TRYCB_TIMER
		- CAtConfAgent::Heartbeat
		- CAtConfManager::StartCBAgent
		- CAtConfAgent::RetryCBConnection
		- CAtConfAgent::TryAvailableCBSvr
		- GCC_Provider::conference_join_request
		- CAtConfAgent::on_conference_join_confirm
		- GCC_RESULT_CONNECTION_UNSUCCESSFUL, 5
		- ::OnConfJoinConfirm(CONF_ERROR_DISCONNECT
		- CAtConfManager::CleanUpConnection
		- CAtConfAgent::m_wAgentEngine = AGENT_PING_TIMER

#. [P] WO0000000259210
	+ Keypoints
		- CMCMMPSessionMgr::OnCacheDataUpdated
		- CMCMMPSessionMgr::SetURL
	+ web browser control
		- https://blogs.msdn.microsoft.com/patricka/2015/01/12/controlling-webbrowser-control-compatibility/
	+ Root cause
		- HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Internet Settings
		- Security_HKLM_only=dword:00000001		
		- after this REG is set, the web browser control read the REG config only from HKEY_LOCAL_MACHINE
		- Download IEDigest from: https://www.microsoft.com/en-us/download/details.aspx?id=51694
		- Download(Need to install) Fiddler from http://www.fiddler2.com/fiddler2/
		- Download Process Monitor from https://technet.microsoft.com/en-us/sysinternals/processmonitor.aspx   	
	+ CDlgShareMultimedia
		- IDC_STATIC_SHARE_MULTIMEDIA_NOTE
		- IDD_MANAGE_SHARE_MULTIMEDIA
		- pServiceMgr->ShareMultimedia
		- CMCServiceMgr::ShareMultimedia
		- CMCMMPSessionMgr::SetURL
		- MEDIA_VIEW_CACHE_NAME
		- PFW_SESSION_TYPE_MMP
		- CIECntrWnd::SetURL

#. [D] WO0000000281442
	+ Unable to click on the start Webcam button

#. [D] WO0000000282685
	+ the video button is not enabled when video session is joined successfully and camera detected

#. [D] WO0000000272041, (CFD::CSCve20228)
	+ Panelist can't answer the question from attendee in EC session
	+ https://cdetsng.cisco.com/webui/#view=CSCve20228
	+ How to reproduce
		- Join the meeting as Attendee
		- Host promote some attendee to Panelist.
		- Start QA session in meeting and sent to panlelist and host
		- Check the meeting in activity report

2017-05-02
----------

#. [D] CSCvd77855
	+ CSCvd84327
	+ T31.11.2 Unable to maximize meeting win when secondary monitor resolution is higher than primary
	+ https://bitbucket-eng-chn-sjc1.cisco.com/bitbucket/projects/CCTG/repos/webex-framework-reskin/pull-requests/406/commits/6ad5cb33b50af564d8ddfbdaf67701d6336265bc
	+ Key Points
		- CPfwMainFrame::OnGetMinMaxInfo
		- //lpMMI->ptMaxSize.x = GetSystemMetrics(SM_CXFULLSCREEN) + GetSystemMetrics(SM_CXDLGFRAME);
		- //lpMMI->ptMaxSize.y = GetSystemMetrics(SM_CYFULLSCREEN) + GetSystemMetrics(SM_CXDLGFRAME) + GetSystemMetrics(SM_CYCAPTION);

#. [D] WO0000000272682, (CFD::CSCve12714)
	+ You cannot join the event because another attendee has already joined using this registration ID.
	+ Key ponts
		- CONF_CONTEXT_USER_RID_MEETING
		- CAtConfManagerImpl::SetRegIDStatus
		- CAtConfManagerImpl::GetRegIDStatus
		- commit id: d46edfa380 @2017-01-20, refactored interface according to jason's feedback
	+ Test account
		- ariel/P@ss123, Ariel Wu ariel8@qa.webex.com	
		- lyn/P@ss123, Lyn Chen	lyn@qa.webex.com
		- nick/P@ss123, Nick Zhang	nick@qa.webex.com
		
2017-04-24
----------

#. [P] INC000000017298
	+ Meeting Centers, High, Service Restored, CB servers alerts on Cls-AB and ED1VACB342
	+  “12000005”: It’s GCC_RESULT_CONNECTION_UNSUCCESSFUL.

#. [D] WO0000000269796, (CFD::CSCve08717)
	+ Joining a meeting and WEBEX crashes.
	+ Commit by Baifer Yu @2017-03-15, fix cscvd56899 and cscvd52828
		- commit id: b4338535
	+ What’s the problem?
		- JBH meeting and docshow parameters “WBXHybridFlag” was 0, attendee join meeting will encounter this issue.
        - This issue introduced at release/32.1.0.     
    + What’s the solution?
        - Correct the session type: APPSVR_SESSIONTYPE_TELEPHONY_HYBRID => APPSVR_SESSIONTYPE_TELEPHONY     
    + What’s the root cause?
        - Engineer copied following code, he modified the class type (CSmHybridAudioMgr => CSmTelephonyMgr) but forgot to modify the session type

#. [W] WO0000000260111
	+ GM BSOD when joining a WebEx meeting

#. [D] Phone drop from meeting
	+ Phone drop from meeting

#. [P] CSCvd97856
	+ T31.11 2 byte characters such as Japanese cannot be inputted directly in chat space
	+ Introduce by Reskin
	+ IME WM_IME_CONTROL
		- https://msdn.microsoft.com/en-us/library/cc195101.aspx
		- https://msdn.microsoft.com/en-us/library/aa768126(v=vs.85).aspx
	+ candidate windows are always on top-left corner of Mozilla window.
		- https://bugzilla.mozilla.org/show_bug.cgi?id=283136
	+ http://m.blog.csdn.net/article/details?id=17322131
	+ Code commit
		- https://bitbucket-eng-chn-sjc1.cisco.com/bitbucket/projects/CCTGFORK/repos/webex-wcl/commits/ac112fc2dafe2f1d7cfe1b2d714739415a9b8864
		- https://bitbucket-eng-chn-sjc1.cisco.com/bitbucket/projects/CCTGFORK/repos/webex-wcl/commits/72b124468cc58a1b085801aa4c71b1504615433a

#. [D] CSCvd97741

#. [D] join meeting by approve with PT the client keep 2 windows.
	+ https://cdetsng.cisco.com/webui/#view=CSCve01138 
	+ Introduced by CSCvd84297 fix

2017-04-17
----------

#. [W] WO0000000257688
	+ Unable to click on connect to audio in meeting
	+ docshow parameters: TeleConfParam

#. [D] WO0000000260834, (CFD::CSCvd97856)
	+ T31.11 2 byte characters such as Japanese cannot be inputted directly in chat space
	+ WCL.dll

#. [W] WO0000000260424
	+ SYMC CAP:  3 minute media time out

#. [W] WO0000000256871
	+ Webcam icon isn't seen intermittently in the meeting
	+ This issue had been fixed
		- release\32.1.0
		- CSmDefUserMgr2::UpdateAllUsers
	+ GetVideoCameraStatus
	+ CVUIActiveMainSelfVideoPort
		- CVUIVideoPortView
		- VUI_HIDE_MYSELFVIDEO_BTN_ID
		- WM_HIDEMYSELFVIDEO
	+ CVUIShowSelfBtnObjectT::ShowMySelfVideoBtn
		- CPfwDirectUI_Button
		- CPfwDirectUI
		- WBXUI_RENDER_STYLE_HIDDEN
	+ IDC_PLIST_SELF_BAR_VIDEO_BTN
	+ CParticipantItemButton
	+ CWndParticipantlistContainer::VideoStatusChanged
		- CWndParticipantlistContainer::OnVideoStatusChanged
		- CWndParticipantItem::SetVideoIconStatus
		- CWndParticipantItem::ChangeVideoIconStaus
	+ CSmDefUserMgr2::UpdateAllUsers
		- CSmDefUserMgr2::OnIdle
		- CSmDefUserMgr2::RealUpdateAllUser
		- CSmConnectionPointContainer::Fire_OnAllUsersUpdated, dwReasons=1024
		- CPListUserMgr::OnAllUsersUpdated
		- CWndParticipantItem::SetVideoIconStatus
		- CWndParticipantItem::ChangeVideoIconStaus
		- REASON_ENABLE_VIDEO, 1024

#. [W] WO0000000254813
	+ Unable to connect VoIP intermittently.
	+ JoinWithVOIP
		- TONE_TYPE_BEEP
	+ OnVoIPUserEnrollConfirm
		- SESSION_CALLIN_FAIL
	+ CMMHybridClientSink
		- OnSessionStatus

2017-04-10
----------

#. [P] WO0000000253382
	+ Audio Broadcast stopped working
	+ wbxtra_03082017_084814.wbt, matches with the Conf ID: 1759174696 . 
	+ Logs are located under https://cisco.box.com/s/8ruksvrfcbb9y7xio2ahr7zsdlbno0nl 
	+ Key points
		- PFW_SESSION_TYPE_AUDIOSTREAM
		- CSmAudioStreamMgr
		- CECAudioStreamMgr


#. [P] WO0000000259319
	+ Customer is unable to join the Audio using Call using computer option which spins at 


#. [D] WO0000000259799
	+ T30L10NSP6EP6
	+ CTCServiceMgr::OnUserChangeIndicationByService
	+ TS performance issue

#. [P] WO0000000258264
	+ cannot start the another SC session even when host ended the session
	+ mutiltpd.dll block the main thread more than 2s when leave conference

#. [P] WO0000000242517
	+ 

#. [W] WO0000000251891
	+ US41938
	+ Call Flow
		- CSmNBRSessionMgr2::OnIdle
		- CSmNBRSessionMgr2::GetConnectState
		- CSmNBRSessionMgr2::GetVideoStatus
		- CSmSvcVideoSessionMgr::IsMMPReconnecting
	+ IDS_NBR2_CONNECT_ERROR_LOST_VIDEO_CONNECTION
		- Your video is not being recorded	
	+ CSmSvcVideoSessionMgr::OnVideoSessionStatus
		- MM_VIDEO_SESSION_DISCRIPTION_NETWORK_ERROR
		- MMT_VIDEO_SESSION_LEAVE
	+ CSmSvcVideoSessionMgr::OnVideoSessionStatus
		- MMT_VIDEO_SESSION_JOIN_FAIL
		- 
	+ CSmSvcVideoSessionMgr::OnVideoReconnectStart
		- m_bMMPReconnecting
	+ CSmSvcVideoSessionMgr::OnVideoReconnectFailed
		- m_pMPPDisconnected
	+ CSmSvcVideoSessionMgr::OnNBRStatus
		- MM_NBR_VIDEO_EVENT_RECORING_ERROR
		- m_bMMPDisconnected

2017-04-05
----------


#. [P] WO0000000254388
	+ Meeting Center steals the focus while users attempt to use other applications on their computer

#. [D] WO0000000255787, (CFD::CSCvd84297)
	+ T31.11 crash webexmgr.dll
	+ Keypoints
		- CMCDocViewSessionMgr::InitMeetingInfoNotHybridSubscriberAccessCode
		- m_pServiceMgr == Null

#. [W] WO0000000254665
	+ After WebEx loads 100% seems like it is frozen for up to a minute before everything works as normal
	+ GCC_Ping_Mgr::ping_request
	+ on_ping_confirm
	+ CAtConfManager::StartCBAgent
	+ CAtConfAgent::RetryCBConnection 
	+ CAtConfAgent::TryAvailableCBSvr
	+ GCC_Conference::on_conference_create_confirm

#. [W] WO0000000256357
	+ Unable to share PDF file in a WebEx Meeting
	+ Key Points
		- IDS_PD_SHARE_WARNING_P
		- CPcmDocViewMgr::GlobalCallBack
		- PD_CB_EVENT_NO_PRINTER
		- CPcmDocViewMgr::OnGCBEventNoPrinter
		- CSmDocViewSessionMgr::OnEventNoPrinter
		- CPDAppShareDlg::SetInfo
		- CPcmDocViewContainer		

2017-03-27
----------

#. [D] CSCvd60475 
	+ Webex usage to invoice mismatch Jan 2017
	+ CMCServiceMgr::Initialize
		- IDS_MULTI_CLIENT_JOIN_TITLE
		- IDS_MC_MULTI_CLIENT_JOIN_WARNING
	+ CWndMessageBoxBase
	+ CECServiceMgr::Initialize
		- IDS_EVENT_MULTI_CLIENT_JOIN_WARNING
	+ Windows,  MC, EC and TC   
		- Set the Cancel as the default button in duplicate join warning dialog.
	+ release/31.13.0 and master 
		
#. [W] WO0000000254741
	+ the customer can't use his audio divice to join VOIP and can't load mac.dll from the wbxtracer.
	+ Cause by MEDIASSION.dll and TP.dll
	+ https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package 
	+ https://cisco.box.com/s/u86vrdsvenk7oq3hkkm496m94p3489eu
	+ http://www.removeonline.com/fix-api-ms-win-core-winrt-string-l1-1-0-dll-is-missing-and-not-found-errors/
		- System File Checker or Sfc.exe is a Mircrosoft Windows utility. 
		- This Windows utility will scan and restore your API-MS-WIN-CORE-WINRT-STRING-L1-1-0.DLL corrupt, missing or deleted Windows system files.

#. [W] WO0000000254542
	+ Customer is unable to join using VoIP
	+ PFW_SESSION_MASK_APPLICATION_AUDIO
	+ CPfwServiceMgr::SetSessionMask
	+ CSmAudioSessionMgr::CheckAudioStartVoip
	+ _EXT_JMFERR_StdDownloadExt_FALSE, StdDownloadExt return False

#. [W] WO0000000243420
	+ Webex meeting was disconnected
	+ atmgr.exe!MC_RunMessageLoop() Line 359 C++

2017-03-20
----------

#. [W] WO0000000254104 
	+ VoIP fails to load and the user receives error 65008
	+ You set debug option in registry, maybe cause unexpect
	+ CMmSVideoClient::UpdateVideoCCMetrics
	+ GetIniFileUrl

#. [W] WO0000000253691
	+ Several users lost ability to use MMP video in session
	+ CMCOptionMgr::NotifyOptionChange dwOption
	+ CAtConfAgent::on_session_close_indication,conference
	+ Meeting Options

#. [W] WO0000000253440
	+ Audio Services / Audio Broadcasting Outage - Rbc.webex.com
	+ GCC_RESULT_INVOKE_APPSVR_TIMEOUT, 107
	+ Keypoints
		- CECUIMgr::OnCommunicateMenuPopupForHybrid
	+ CECUIMgr::UpdateTeleConfMenuStatus4Hybrid

#. [D] WO0000000254135, (CFD::CSCvd52936)
	+ confID 55915843714857052 - shows TP participant
	+ IsSupportVideoCall
		- _SUPPORT_NEW_VIDEOCALLBACK
	+ GetCallTPJsonStr
	+ BTS site
	+ Media Fashion
	+ Video Callback
	+ endpointDisplayName
	+ https://wiki.cisco.com/display/EUREKA/Media+Fusion+Video+Callback+Interface
	+ CPfwServiceMgr::CallTP
	+ CallTPDeviceByCB
	
#. [D] MMP performance test, can't join meeting
	+ From Hong Liu

2017-03-13
----------

#. [D] CSCvd39982
	+ CSCvc83497
	+ global call-in link only not display in customer's info tab in the meeting
	+ Key point

#. [D] WO0000000250962
	+ global call-in link only not display in customer's info tab in the meeting
	+ Key docshow parameters
		- QSTemplateURL
		- TSPGlobalNumURL
		- TSPGlobalNumLabel
		- TSPGLOBALCALLINFLAG
		- MP_FLAG
	+ Key point
		- GetTSPGlobalCallinNumURL
		- GetTSPGlobalCallinNumFlag
		- CMCDocViewSessionMgr::GetTeleInstructions
		- CMCDocViewSessionMgr::InitMeetingInfo
		- CMCDocViewSessionMgr::InitMeetingInfoMPShowTele
		- CMCDocViewSessionMgr::SetPDLinkButtonStyle

2017-03-06
----------

#. [P] WO0000000245864
	+ Host unable to view the video shared by attendees
	+ Key points
		- CWndParticipantlistContainer::AdjustMainVideoPanel
		- CWndParticipantlistContainer::LayoutUI
		- CWndParticipantlistContainer::AdjustParticipantList
		- CWndParticipantlistContainer::ShowMainVideoView
		- CMainFrameWrapper::ShowRealVideoPanelView
		- CWindowVideoUIMgr::ShowMainVideoPanelView
		- CMCPListVideoPanel::StartVideoView
		- WM_AFTER_SHOW_HIDE
		- CMCPListVideoPanel::OnAfterShowHide
		- CVUIActiveMainVideoPort::UpdateActiveVideo

#. [W] WO0000000246366
	+ Webex application crash 

#. [W] WO0000000248456
	+ Improper use of telephony international callbacks
	+ ibm2.webex.com
	+ 2637 audio callback, 2637 SMS 

2017-02-28
----------

#. [P] CSCvd05951, (CFD::CSCvd05951)
	+ https://hbt31-ns.qa.webex.com/ lyn/P@ss123
	+ https://wdc.webex.com/wdc/globalcallin.php?serviceType=MC&ED=485011217&tollFree=1
	+ http://mail.qa.webex.com
	+ CCA: Cloud Connected Audio
	+ Key Points
		- ShowInviteRemindDlg
		- CSmQuickStartSessionMgr::ShowInviteRemindDlg
		- CDlgInviteRemind::
		- CDlgInviteRemind::OnSendMail
		- CInviteRemindWrapper::SendEmail
		- CSmDocViewSessionMgr::SendMailUseWebEx
		- CInviteRemindWrapper::SendMailComplete
		- CSmDocViewSessionMgr::UpdateInviteList
		- CSmDocViewSessionMgr::OnQSXMLFileDownloaded
		- AppData\Roaming\webex\QSXMLFile.dat
		- SendInviteMailURL
		- Global call-in numbers
		- CSmDocViewSessionMgr::GetQuickStartInfoXMLFromFile

#. [P] CSCvc90991, (CFD::CSCvc90991)
	+ How to enable and disable MQD feature
	+ MQD basic metric
		- low volume
		- echo
		- noisy
		- microphone
	+ MQD component
		- MQD decision layer
		- MQD data collect layer
		- MQD UI layer
	+ MQD relevant module
		- mac.dll
		- WbxMQDUIManager.cpp
		- audio qulity detect
		- WME
		- Windows client UI
	+ Key Points
		- HCC_INFO_VOIP_MQD_NORMAL
		- IDS_MQD_QUALITY_
		- HCC_INFO_VOIP_MQD_SCORE
		- CSmFITUIMgr::ShowMQDTip
		- CSmFITUIMgr::OnPfwNotifyGetAudioIconBubbleInfo
		- CSmHybridAudioMgr::OnInfoChangeIndication MQD Status

#. [P] WO0000000240975


#. [D] WO0000000236572
	+ Pure call in show as Spanish language: such as:  not call_in_11 but Usuario de llamada entrante_11
	+ Super Admin => Docshow => TA
	+ TSSecParams
	+ From Avinash Vinu <avinu@cisco.com>
		- Customer has agreed on this.
		- Customer has updated to close the case.
		- Thanks everyone for the support on this case.

#. [P] WO0000000237796
	+ The host of the following meeting insist that one of her participants (Bernd Justen) was not muted upon entry after joining the teleconference (everyone else was muted).
	+ Code to test
	+ Check "Mute upon entry for all participants" when schedule meeting
	+ IDC_MANAGE_ATTENDEE_LIST, 11249, CDlgAttendeeList
	+ CECAttendeeListDlg
	+ CECAttendeeListForHostDlg
	+ CECUserMgr::GetAttendeesArray

#. [P] WO0000000235001, (M::VOIP), (F::MQD)
	+ People with a Jabra or Plantronics speakerphone would face error every time they unmute
	+ Key Points
		- CHCCVoIPService::OnMQDInfo, MQD_INFO_SPEECHLVL
		- CMMHybridClientSink::OnMQDInfo
		- CSmHybridAudioMgr::OnInfoChangeIndication

#. [W] (CFD::CSCvd05951)
	+ CCA globalcallin link redirect to meeting has been cancelled from Join WebEx meeting in progress
	+ Mail to Aier Huang request more info

#. [W] HD0009415846
	+ unable to see the chat in the recording
	+ It is about the p-list not able to display the participant properly
	+ http://kb.webex.com/WBX54331
	+ Recording info
		- https://nokiameetings.webex.com/nokiameetings/lsr.php?RCID=05d0ac54666246b984f1de2ea53a4d82 

#. [W] WO0000000242201, (M::WME)
	+ WebEx client crashes right after a user joins the WebEx meeting, Error- &quot;WebEx application ha


#. [W] WO-086237, BCG
	+ Video session hadn't created when host and presenter changed
	+ APPSVR_SESSIONTYPE_MM_VIDEO
	
#. [W] WO0000000243469
	+ T31.9.8 Unable to start/join the meeting and getting crashed at 10% 
	+ CPfwServiceMgr::LoadResource, pfwres.dll hadn't loaded
	+ webex-wcl\src\WCL\wtwclapp.cpp@69
	+ CSmDefUserMgr2::CreateContainer
	+ pPanelMgr->m_hWCLRightPanelView hadn't been checked if NULL or not
	

#. [D] WO0000000229584, CSCvc31346, (CFD::CSCvc34464), (F::VOIP),(M::JMT), (RCA::GPC)
	+ Unable to join VoIP audio conference
	::
	 
	 This issue was caused by GPC download GTC and QS XML failed.
	 We had a similar issue WO# WO0000000227555 and fired a bug CSCvc34464.
	 This bug was fixed and verified on T31.8.5 at 12/07/2016.

2017-02-07
----------

#. [D] (CFD::CSCvc85292)
	+ https://cdetsng.cisco.com/webui/#view=CSCvc85292

#. [P] This problem is because Paul's meeting client freeze.
	+ WbxUI_IsAeroSupport
	+ CVUIVideoPort::ConfigurePresenterRenderWhenEnterFIT

#. [P] WO0000000238496, (Tom is checking)
	+ EC - Low Bandwidth Error from Presenter's Camera View after an attendee starts speaking
	+ pVideoClient->SelectChiefSender
	+ CSmSvcVideoSessionMgr::NeedApplytoCC

#. [W] WO0000000233708
	+ When doing a screen share the laptop BSODs

#. [W] WO0000000239289
	+ This customer is reporting an intermittent issue that when in a Webex meeting and trying to share from a secondary monitor that the system crashes to the BSOD and reboots the computer. This happens right after he joins into a meeting somewhere between 5 and 25 minutes. The issue always happens when the user tries to share the secondary monitor. It happens even if he has shared successfully and then switched back to sharing from the primary display. The system will still crash.
	+ Could you please help on this BSOD issue on Dell E7470 with Windows 7 64 bit

#. [W] WO0000000240362
	+ PFW_JMF_ERRORCODE_NOERROR_INITED = 2000
	+ PFW_JMF_ERRORCODE_NOERROR_UI_INITED = 3000

#. [D] (CFD::CSCvc70793)
	+ WO0000000238249
	+ Host joined before alternate host but the Host role was autonmatically switched to the alternate
	+ https://www.draw.io/#G0B2Ykfab9ktB2U3NzbUdTMWVuN2s
	
2017-01-22
----------
	

#. [W] WO0000000236342
	+ since they are facing the issue while joining the voip on this T31 site https://catechnologies.webex.com.
	+ WBXHybridFlag
	+ TSP VOIP

#. [D] CSCvc82198, (M::NBR), (RCA::HDPI)
	+ cannot restrict specific country code rather than US on NBR wizard dialog if TSP+other tel
	+ https://cdetsng.cisco.com/webui/#view=CSCvc82198
	+ TSPOtherCountryCodeRestriction

#. [D] CSCvc82097, (M::NBR), (RCA::HDPI)
	+ It doesn't work when enable specific option to prevent host to select other country flags

#. [D] WO0000000239840, (CFD::CSCvc80152)
	+ unable to end the meeting. Application crashes.
	+ https://cdetsng.cisco.com/webui/#view=CSCvc50691
	+ https://bitbucket-eng-chn-sjc1.cisco.com/bitbucket/projects/CCTG/repos/webex-framework-reskin/commits/af1dddbc48cada2735d3abe05fb7f60a0595653e

#. [W] WO0000000240038
	+ 31.9.5 B one Win10 user can not join meeting
	+ PT

#. [W] WO0000000238505
	+ High WebEx CPU Usage when connecting to video using Microsoft Lifecam Cinema USB WebCam
	+ CSmDefUIMgr::OpenAVStatisticsDlg
	+ PopupDlgMgr.cpp
	+ CWndAudioVideoStatistics
	+ CAudioVideoStatisUtil::GetAVStaticsInfo
	+ CWndAudioVideoStatistics::UpdateData
	+ CheckAVStatisticsInfo
	+ CAudioVideoStatisticsUtil::SaveLog
	+ CMmSVideoClient::OnTimer, Update Quality Report, local: cpuUsage
	+ Work Flow
		- CMmSVideoClient::OnTimer
		- m_Timer_Update_Quality_Report
		- ISVideoClientSink::OnSpecailEventReport
		- MMT_SPECIAL_EVENT_RECORD_VIDEO_QUALITY
		- CMmSVideoClient::UpdateQualityRecord
		- m_pSVideoClientSink->OnSpecialEventReport
		- CSmSvcVideoSessionMgr::OnSpecailEventReport

#. [D] WO0000000238111, (CFD::CSCvc41813), (M::WME_Audio)
	+ MSO team has confirmed that the user has joined the session but couldn’t join MMP VoIP
	+ Key points
		- WBXHybridFlag
		- TSPHybridFlag
		- HybridType

2017-01-16
----------

#. [W] WO0000000238772, (M::GPC)
	+ T31.9.5 Meeting stops loading at 10-40%, customer receives error message
	+ Proxy Env
	+ https://msdn.microsoft.com/en-us/library/ms775145(v=vs.85).aspx
	+ fuzPercentMgr.cpp
		- CPerentManager::GetCurrentPerent()
		- CPerentManager::SetPercent()
		- CPerentManager::NotifyPoint
	+ IFuzzyWindowMgr.h
		- FUZZY_PROGRESS_JOIN_STEP
		

#. [W] WO0000000238671, (JBH)
	+ No VOIP and Video options in the session are missing


#. [W] WO0000000237850
	+ T31.9.5 Melissa said webex crashes when sharing any presentation
	+ 

#. [D] HD0009324438, (CFD::CSCvc67068), （RCA::QA）
	+ T31 MC client grays out Call Me in video callback window when plus is in URI
	+ Verified that per RFC 3986, a + character is perfectly valid to have in the user-identifying portion of a SIP URI
	+ Conflict with CSCuy54722, discuss with Jeremy Zhang, drop CSCuy54722
	+ Root Cause
		- CTPAddressChecker::IsUserName
	+ Key points
		- *Enter your video address* , L1665
		- CCallTPSubWindow::OnCallTPNum
		- CAudioMainDlg::CreateTPWindow
		- CCallTPSubWindow::Initialize(), m_tpEdit
		- CCallTPSubWindow::OnEditTPNumber
		- CSmAudioStatusWrapper::IsValidTPAddress
		- CTPAddressChecker::Test
		- CEMailAddressChecker::IsUserName
		- CTPAddressChecker::IsUserName
		- CSmAudioStatusWrapper::IsTPAddressBlockByBlackWhiteList

#. [D] CSCvc66196, (CFD::CSCvc66196), (F::HDPI), (M::ComUI), (RCA::code issue)
	+ record button is not enabled after close nbr wizard dailog via X
	+ Introduced by HDPI
	
#. [D] CSCvc64610, (CFD::CSCvc64610),(F::HDPI), (M::ComUI), (RCA::code issue)
	+ What's the problem
		- Unable to record meeting with other teleconference, the drop down to select the country for
	+ What's the solution
		- Correct **input parameter (AUDIO_COUNTRY_TYPE_PHONE => AUDIO_COUNTRY_TYPE_NBR)**
		- Enhance **CwndCountryCode**  
	+ What's the root cause
		- Wrong parameter
		- Wrong code reuse

2017-01-09
----------

#. [D] WO0000000235859, CSCvc31346, (CFD::CSCvc34464), (M::GPC)
	+ Due to a connection issue, you cannot invite or remind others unless you exit and restart the meeting.
	+ CSmDocViewSessionMgr::CheckQSXMLFileDownload

#. [D] WO0000000229664, (M::PD), (RCA::by design)
	+ Due to an event capacity limit
	+ Key log
		- SVS sesseion reachs the maximum attendee count
		- UserJoinType=3
		- Schedule EC meeting and upload UCF file, then attendee join first
	+ Root Cause
		- UpdateMyVideoReceivePrivilegeStatus
		- CPfwVideo::EnableReceiveVideoPrivilege
		- CECStreamingVideoMgr::ReceivePDCommand
		- CSmStreamingVideoMgr::ReceivePDCommand
		- IMediaStreamingClient::ReceiveCommand		
	+ Key points
		- CPcmDocViewMgr::GlobalCallBack
		- PD_CB_VS_MEDIA_STREAMING_COMMAND
		- CPcmDocViewMgr::OnGCBStreamingVideoCommand
		- WM_PD_STREAMINGVIDEO_COMMAND
		- CSmDocViewSessionMgr::OnStreamingVideoCommand


#. [D] WO0000000236287, (CFD::CSCvc64610), (F::HDPI), (M::ComUI), (RCA::code issue)
	+ Unable to record meeting with other teleconference, the drop down to select the country for 
	+ Page Config
		- Site Admin : Edit User => UnCheck ‘Call-back teleconferencing’
		- Super Admin : UnCheck 'Country Code Restriction'
	+ Root cause
		- CDlgNbrWiz3rdAccount::InitPage
		- m_wndPhoneNumber::Initialize
		- CwndCountryCode::OnClickedCountry => IsGlobalCallbackSupport
		- error parameters : AUDIO_COUNTRY_TYPE_PHONE => AUDIO_COUNTRY_TYPE_NBR
		- CDlgNbrWizard::OnCancel
	+ Key points, T31.10
		- TSPOtherCountryCodeRestrictionFlag
		- SetTSPOtherDialoutCountryCodeFlag
		- IDW_WINDOW_NBR_WIZARD_REC_TYPE
		- CDlgNbrWizard
		- CWndNbrWizardTeleType
		- CDlgNbrWiz3rdAccount
		- CWndCountryImage
		- CWndCountryCode
		- CSmAudioPhoneWrapper::GetAvailableCountryList
		- GetCountryCode: CountryCode
	+ Key points, T30
		- CNbrWiz3rdAccount::CreatePfwAudioCmb
		- AddCmbBtnDroplistEx
		- CNbrWiz3rdAccount::m_pfwAudioCmb
		- CNbrWiz3rdAccount::m_imgListFlags
	

2017-01-03
----------

#. [D] WO0000000234162, (CFD::CSCvc61782), (F::HDPI), (M::ComUI), (RCA::code issue)
	+ Unable to disable- 'Allow participants to change the sequence of panels' option from Event window
	+ It can only duplicate on T31.8.5 for windows
	+ There is no known bug for this issue from QAs, on T31.8/T31.9 release.
	+ Key Point
		- CDlgHostPanelManager
		- CDlgHostPanelManager::GetIsAllowToManagePanels()

		
#. [W] CSCvc15286, (CFD::CSCvc15286), (F::NBR), (M::NBR), (RCA::wrong configuration)
	+ https://cdetsng.cisco.com/webui/#view=CSCvc15286
	+ CWMS automatic recording feature is not work
	+ Page side checked **Record this meeting** box, but page pass docshow parameter to client is 0
	+ Key Ponits
		- CSmNBRSessionMgr2::OnHostChanged
		- CSmNBRSessionMgr2::OnHostChanged NBR autostart
	+ Docshow Parameter
		- NBRAutoRecording
		- NBRForceRecording
		- TeleFlag
	+ Test site and account
		- https://orionf3vip.qa.webex.com
		- oradm@qa.webex.com  P@ss123

2016-12-26
----------

#. [W] WO0000000233852, (M::VOIP)
	+ No response after selecting 'call using computer'

#. [W] WO0000000228324, (M::Video), (RCA::Docshow)
	+ HD Video is not working during sessions
	+ Key Points
		- CMCDocshowMgr::ProcessParameters
		- CMCDocshowMgr::ProcessMeetingTypeParam
		- CMCDocshowMgr::HandleSessionTypeOptions
		- m_pContextMgr->GetSiteEnableOption : SessionTypeOptions
		- m_pContextMgr->GetPicassoOptions : MtgPanelStatus
		- CMCSiteConfigMgr::InitSiteConfig
		- CMCSvcVideoSessionMgr::Initialize
		- CSmSvcVideoSessionMgr::ChangeSVCExpOption
		- CMmSVideoClient::SetSVCExpMode
	::
	 
	 Docshow Parameters: SessionTypeOptions
	 #define SESSION_TYPE_ENABLE_VIDEO					0x02
	 #define SESSION_TYPE_ENABLE_VIDEO_HQ				0x8000000 //for SVC task, High video quality
	 #define SESSION_TYPE_ENABLE_VIDEO_HD				0x20000000	//Roni<<FR29 HD Video<<2011.04.11

#. [D] CSCvc57112, (CFD::CSCvc57112), (F::HDPI), (M::Whiteboard), (RCA::HDPI)
	+ Whiteboard option shows up in  meeting client
	+ Docshow Parameter: WhiteboardSupport
	+ Key points
		- CWndPdTabPanel::NewWhiteBoardTbn_ShowWindow
		- CMCUIMgr::CheckSharingTBStatus
		- CWndPdTabPanel::ShowNewWhiteBoardBtn
		- CWndPdTabPanel::OnTabNewWhiteboard
		- CMCUIMgr::CheckSharingTBStatus
	::
	 
	 Whiteboard does not show up in T30 sites. Issue only occurs with T31 clients.
	 
	 Steps to duplicate:
	 1. Open Site Administration page
	 2. Browse to Configuration > Common Site Settings > Session Types
	 3. Create new PRO Session > Disable Whiteboard > Add
	 4. Assign the new session type to the desired host's
	 5. Start meeting from the new session type host
	 
	 Expected results:
		- Meeting client opens up, and option for Whiteboard does not show up
	 
	 Actual results:
		- Meeting client opens up, and option for new whiteboard appears
		- When users click on +New Whiteboard option, nothing happens
	 
#. [D] CSCvc56545 , (CFD::CSCvc56545), (F::HDPI), (M::PList), (RCA::)
	+ Space between Participant's Names and Hand/Camera
	+ CSCvc38505
	::
	 
	 This new design feature is generating tons of frustration and complains from Nokia. 
	 They consider this as a Defect since the most important in the Participant Panel is the name of the participants.
	  
	 As mentioned in you last email, we see that the Function buttons are talking most of the space which create this issue.
	 What Nokia is requesting is that we go back to the original Participant Panel where the Function button was taking much less space, allowing users to see the Participant names without stretching it.

#. [W] WO0000000228802
	+ wanted to know how to disable how was webex pop up after meeting ends
	+ CMCServiceMgr::ShouldPopSurveyUI
		- _wtof
		- Use std::strtod to replace
		::
		 
		 char* e = NULL;
		 int errno = 0;
		 double x = std::strtod(mystring, &e);
		 if((NULL != e) || (0 != errno))
		 	//fail

#. [D] WO0000000234320, (CFD::CSCvc56072), (F::JBH), (M::Page),(RCA::Docshow)
	+ T30.9 client WebEx Ball Will not pass during meeting center
	+ https://cdetsng.cisco.com/webui/#view=CSCvc04028
	+ https://cdetsng.cisco.com/webui/#view=CSCvc56072
	+ Super Admin: Participant can grab presenter role
	+ Site Admin: Allow Participants to Share in meetings (MC only)
	+ Session Type: Participant can grab presenter role
	+ Key Points
		- JBH
		- Repeat meeting

#. [D] WO0000000230313, 
	+ Error on meeting center exit

#. [W] WO0000000232524, (F::VOIP), (RCA::Docshow)
	+ Unable to Join through VOIP
	+ WBXHybridFlag=0
	+ This recording introduce how to set these docshow paramerters
		- WBXHybridFlag=0
		- TSPHybridFlag=0
		- HybridType=0
		- https://go.webex.com/go/lsr.php?RCID=cc3a84739c7f41c5a4e400e89ee9668b
	+ Key Points
		- CAudioMainDlg::OnInitDialog
		- CAudioMainDlg::GetInitStatus
		- CAudioMainDlg::InitControls
		- CSmAudioStatusWrapper::IsShowCallVoIP
		- IsVoIPPortionEnabled, m_bVoIPPortionEnabled
		- GetHybridTelephoneOnlyFlag, $HybridTelephoneOnlyFlag
		- AT::CWclWindow(Item(IDW_PUSHBUTTON_USING_COMPUTER)).ShowWindow(bJoinedMeeting && m_bIsVoip ? SW_HIDE: SW_SHOW) 

#. [D] CSCvc44326, (CFD::CSCvc44326), (F:Video), (M::WME)
	+ Site was upgraded to page version 31.7.6 in the last couple of weeks  
	+ since then his Blackmagic Intensity Shuttle for USB 3.0" capture card connected with usb to the computer no longer shows video to participants during his meetings.
	+ pass to Keith Yan

#. [D] CSCvc37774, (CFD::CSCvc37774), (F::NBR),(M::NBR), (RCA::DefautValue)
	+ Telephony NBR fail to start when privilege change for the meeting host
	+ Key points
		- CSmNBRSessionMgr2::CloseConnectingDlg(IDCLOSE)
		- CSmNBRSessionMgr2::CloseConnectingDlg default value is IDOK
	+ Call Flow
	::
	 
	 1. CSmNBRSessionMgr2::LaunchWizard
	 2. CSmNBRSessionMgr2::OnWizardNotify
	 3. NBR_WM_CLOSE_CONNECTING
	 4. CSmNBRSessionMgr2::ShowConnectingDlg (2S)
	 5. CSmNBRSessionMgr2::OnTelephonyNotify
	 6. NBR_TN_READY
	 7. CSmNBRSessionMgr2::OnTelephonyReady
	 8. CSmNBRSessionMgr2::ConnectTelephony
	 9. CHCCTelephoneService::NBRRequest
	 10. CSmNBRSessionMgr2::OnTelephonyConnect
	 11. CSmNBRSessionMgr2::Start (check timer)
	 12. CSmNBRSessionMgr2::OnIdle (m_dwConnectingTick)

#. [D] CSCvc39475, (CFD::CSCvc39475)
	+ Block network between two meeting zones: zone1 and zone2 and restart mzm in zone1 and zone2 (which is for the meeting not sync in zone1 and zone2)
	+ Kill wwp process
	+ TP plus and WebEx host create meeting on a meeting zone respectively(TP plus in zone1,webex host in zone2)
	+ Jucked
	::
	 
	 Sorry to jump in. I was assigned for this CFD bug to help what exactly happen for customer. 
	 Would you please help response Lamfung’s question?  
	 We will base on your confirmation to determine next action.  
	 
	 Here are more information we researched those days:  Jun and myself have reviewed the TA/CB/TPGW server logs for confid:  3243470856, 
	 we found this conference issue is caused by the TPGW call got disconnected, and CB conference close is due to bug: CSCvc33320, 
	 which have been fix in Nov release Tahoe3.10.4.  


2016-12-19
----------
	 
#. [D] WO0000000229581, (F::PMR), (), (RCA::ByDesign)
	+ Computer do not gets locked or goes to Sleep if a PMR meeting is running regardless of the co	
	+ http://stackoverflow.com/questions/629240/prevent-windows-from-going-into-sleep-when-my-program-is-running
	+ powercfg /requests
	+ CSCuo46601
	+ For PMR meeting is a personal room, it is persistent meeting.
	+ Key points
		- CPfwServiceMgr::DisablePCSleep, SetThreadExecutionState(ES_CONTINUOUS|ES_SYSTEM_REQUIRED|ES_DISPLAY_REQUIRED)
	::
	 
	 Customer’s computer policy is set to go off to Sleep in 5 Minutes if there is no activity. 
	 If we start a Scheduled meeting and leave the computer idle for 5 Min, the computer goes off to sleep. 
	 However, if we start a PMR Meeting the computer do not go off to sleep regardless of the system stays Idle for hours. 
	 This behavior is consistent across multiple versions and sites.

#. [P] WebEx Error Message, (M::IPv6)
	+ From Allison


#. [D] WO0000000223509, (M::Crash), (RCA::None)
	+ T31.5.20 win10  Crash when sharging application or when changing presenter role between participants.
	+ Had trouble shooting at 2016-12-12, 10PM-12PM
	+ Customer had updated to T31.8.5 and hadn't reproduce, waiting for response

#. [D] WO0000000229615, (M:JBH)
	+ From BCG
	+ Sharing option removed during meeting - for all but Presenter
	+ For the presenter change request failed at 2016.11.23 07:31:18. It was caused by Presenter Key verification failed on CB. The option (=8) client sent to CB was not match with the option (=3) queried from Page.
	+ Key Points
		- SiteConfigExt
		- HandleSiteConfigExt
		- CPfwServiceMgr::SetUserAsPresenter
		- CAtConfManager::SetUserAsPresenter
		- CAtConfManagerImpl::SetUserAsPresenter
		- CAtConfAgent::SetUserAsHostPresenter

#. [D] WO0000000231914, (RCA::Design Issue)
	+ From BCG
	+ You are no longer connected to the meeting, Automatically Reconnecting²
	+ Key points
		- CMCServiceMgr::ShowAutoReconnectDlg
		- CMCServiceMgr::ModalAutoReconnectDlg
		- CMCServiceMgr::ShowUnableToConnectDlg
		- $SupportPageWaiting
	::
	 
	 What's the problem: 
	 When users try to join meeting, received error message: "You are no longer connected to the meeting, Automatically Reconnecting" 
 	 
	 RCA: 
	 It is design issue for the sites which have more than one meeting zone. 
	 When two users try to create a meeting at the same time(send create ping MZM server for JBH meeting), 
	 since any meeting client will 'ping' MZM servers one by one,  if user1's ping request first reached to zone 1,
	 but reached to zone2 secondly. And user2's ping request first reached to zone 2, but reached to zone1 secondly. 
	 These two users will both ping successful, and per MZM 's split meeting protection mechanism, 
	 it will return conference_not_ready for the next create meeting ping on the same meeting, 
	 then user1 and user2 will also both get conference_not_ready message, 
	 this message has high priority to accept than others. So, both users will be waiting until meeting is created or timeout(60s), 
	 when waiting, client will pop up the reconnecting dialog, and any other users try to join meeting before the meeting been created, 
	 will also pop up the reconnecting dialog.
  	 
	 Next Action: 
	 Merge two meeting zones into one meeting zone to avoid customer getting into such race condition.

2016-12-12
----------

#. [P] CSCvc36124, (CFD::CSCvc36124)
	+ https://cdetsng.cisco.com/webui/#view=CSCvc36124
	+ "Call Using Computer" clickable before CSP client sent C2W_OnConnectIndication TSPSDK_CONNECT_VOIP_ENROLL_OK (1001)
		- https://orionf3vip.qa.webex.com
		- oradm@qa.webex.com  P@ss123

#. [D] CSCvc40283, (CFD::CSCvc40283), (F::), (M::MCRes),(RCA::HDPI)
	+ Incorrect host name appears for all host using PMR or MC
	+ I had found 73 issued ID, for time limit, I had fixed 8, and asked train team help to check other potential issue
	+ Root Cause
		- MCRes.rc & pfwres.rc
		- WebExMgr get resource Key ID from PfwResID.h
		- WebExMgr get resource Key Value from MCRes.rc
		- There are some Resource Key ID exist in PfwResID.h and MCResId.h
		- Like: IDS_USERNAME_INTER

#. [D] WO0000000231983, (CFD::CSCvc40283)
	+ Incorrect host name appears for all host using PMR or MC
	::
	 
	 It’s a code issue: there are 2 same resource ID, one is correct, 
	 another is for menu item “&File (Including Video)”. 
	 At this place, resource get by error as “&File (Including Video)”


#. [W] Start meeting fails sometime during automation test
	+ From 6:48 – 6:52, the client fail to join VoIP session, client traces shows above some error.

#. [D] CSCvc09856, (CFD::CSCvc09856)
	+ go.webex.com, on windows 10 PC, when doing video call back, the local video window did not minimize.
	+ https://cdetsng.cisco.com/webui/#view=CSCvc09856

#. [D] WO0000000228352， CSCvc37774, (M::NBR)
	+ No audio present in the recording
	+ Ask to fire a bug, caused the the incorrect PDU sequence.

#. [W] WO0000000229462, (M::WME)
	+ When a user joins VoIP, EC crashes  it is happening for multiple users in customer environment 
	+ Crashed at wseclient.dll moduel, loop WME team
	+ Build private dll to customer to verify

#. [W] WO0000000221501, (M::WME)
	+ WebEx application crashes when starting or join a meeting
	+ Seems the same as WO0000000216828
	+ Request dump file
	+ CSCuz52797， Gang asked customer try to replace wseclient.dll and collect log
	::
	 
	 From Jun Ma:
	 I have checked dump file that dump indicate the crash location is SensorsApi.dll. 
	 I think this crash same with surface pro case. you can add HP  Elite X2 to filter White-list. Thanks

#. [D] WO0000000227797, CSCvc31346, (CFD::CSCvc34464), (M::GPC)
	+ error message "Due to a connection issue, you cannot invite or remind others until you exit and restart the meeting." and is unable to start VoIP on one computer
	+ Key points
		- QSTemplateURL, DOWNLOAD_TYPE_TEMPLATE
		- QSInviteURL  , DOWNLOAD_TYPE_QS_XMLFILE
	+ https://cisco.box.com/s/e0nixhe10w103u7supsahey6i2jgd3qn 
	+ [go site] https://cisco.box.com/s/55ciyndr6a5ltpe38eg3pvsg5i3gg9eg
	+ Ask to fire a bug
	
#. [D] WO0000000227555, CSCvc31346, (CFD::CSCvc34464), (M::GPC)
	+ VoIP audio connection issue
	+ Mail out, need trouble shooting
	+ IDS_QSXML_DOWNLOAD_FAILED_TIP
	+ Due to a connection issue, you cannot invite or remind others unless you exit and restart the meeting

#. [D] WO0000000230170, CSCvc31346, (CFD::CSCvc34464), (M::GPC)
	+ Due to a connection issue, you cannot invite or remind others unless you exit and restart the meeting
	+ GPC download failed.

2016-12-05
----------

#. [D] CSCvc17031, WO0000000223017
	+ cannot recover memory location
	+ Mail to Caroline Ye
	+ F1573
	+ Reopen, need check tomorrow 
	+ Refer to Certify XenApp 7.6 in T31.9 - Test result
	+ CSCva47546/CSCuz01715
	+ Mail out, waiting for customer
	::
	 
	 This issue looks like the same root cause as bug CSCva47546/CSCuz01715 (Lamfung , please double check).
	 It is Citrix issue which we escalated to Citrix Support. They resolved it and the fixes is included in XenApp/Desktop 7.6.2000 (LTSR).
	

#. [D] CSCvb95846, (CFD::CSCvb95846), (M::PList), (RCA::)
	+ Need Allison help to check from DB side
	+ Client shows the same as the DB
	+ Check the Mats, is the same like the plist , so seems not a bug, J
	+ Assign to Chen tao
	::
	 
	 I tried on go site, the reversed string works well “pɐpɹɥǝɯ ʎʞɹoʇ”, as well as the normal one“torky mehrdad”. 
	 I think this user is just for fun…
 	 
	 You can use this site for fun too… 
	http://www.fileformat.info/convert/text/upside-down.htm
	  
	 I don’t think page have problem, because customer input it indeed.
	 

#. [D] Webex crash
	+ WebEx client crash when presenter stop app sharing
	+ https://cdetsng.cisco.com/webui/#view=CSCvc24688
	+ https://cdetsng.cisco.com/webui/#view=CSCvc25551
	+ Key points
		- Share App from **Indicate Button**
	::
	 
	 1)Host MeggersJHomeDX start a meeting, and start video
	 2)Windows user Javed Khan joined
	 3)Mac attendee Donna Fontaine joined
	 4)Host pass presenter to Donna Fontaine, Donna Fontaine shared app
	 5)Presenter was passed to Javed Khan, Javed Khan shared app
	 6)After some time, Javed Khan stop sharing, Javed Khan's client crashed.


#. [O] WO0000000223894
	+ Video feed issue

#. [D] WO0000000229219, (M::WME)
	+ When starting webex audio(VOIP), webex crashes
	+ Loop WME team, occurs at util.dll
	+ Seems caused by dead lock, FreeLibraryAndExitThread and FreeLibrary.

#. [D] CSCvc27759, (F::whiteboard)
	+ whiteboard will be opened automatically when switch presenter
	+ Can we ask QA team to test it on go.w.c?
	+ Forward to Chaonan

	
#. [W] WO0000000228870, (F::VoIP), (M::WME)
	+ VoIP Freezes the WebEx client
	+ SensorsAPI module
	+ https://sqbu-github.cisco.com/WebExSquared/wme/issues/4278
	
#. [D] CSCvc14491, (CFD::CSCvc14491), (F::TSP), (RSA::Security)
	+ https://cdetsng.cisco.com/webui/#view=CSCvc14491
	+ Intercall
	+ From Alexander Fleck (afleck), send out mail request client log
	+ TSP server connect the third party server
	+ Dongong Peng From TSP server
	+ PO (ren bo), TL (Ty), assigned to Evan Xie
	+ Super Admin => New Site => Security Options
		- TSP partner is sending only SHA256 values in TSP API clienthashlist.(enabling this will stop checking for SHA1 hash values)
	+ Docshow parameters
		- TSPHybridFlag
		- THClientHashList
		- CDTAppPDU_Evt_CreateTSPConference
		- TSPHybridSecureAccess

#. [D] WO0000000229413, (CFD::CSCvc29069), (F::JBH), (M::AnyoneCanShare), (RSA::Security)
	+ Share screen / application grayed out on meeting
	::
	 
	 We could reproduce it in local by following steps:
	 1. Schedule repeat MC meeting with support JBH, first attendee to be presenter and participant can grab presenter.
	 2. Attendee A join meeting before host. User A can share in meeting.
	 3. Use TP device join meeting.
	 4. Attendee B join meeting after TP device in meeting. User B’s “Share” button will gray out.
	 5. Host didn't join meeting.
	  
	 Workaround:
	  Host join meeting.
	  
	 Analysis:
	  After TP device joined meeting, it insert unexpected “startTimeOfInstance” into wbxmmconfparam. 
	  This will result doc-show return “FirstParticipantIsPresenter=0” to client.
	  As host not joined meeting, client(Windows/Mac) will let “Share” button gray out when “FirstParticipantIsPresenter=0”.

2016-11-28
----------	
	

#. [D] WO0000000228604, (CFD::CSCvb98202), (F::NBR)
	+ Attendees have the privilege to record the meetings by the HOST but they are still unable to record the meetings.
	+ Docshow parameters
		- NBRForceRecording
		- NBRForceRecordingWithControl
	+ Keynotes
		- CMCUIMgr::IsShowRecordBtn
		- CMCQuickStartSessionMgr::CheckQSStatus
		- ID_MEETING_START_RECORD
		- OnQsRecordBtn

#. [D] WO0000000218922, CSCvc27274, (CFD)
	+ Host is not able to see avatar picture in the Personal Meeting Room
	+ CSCuz30267
	+ Key points
		- CSmAvatarMgr::CSmCacheMgr::SaveIntoLocalCache
		- CSmConnectionPointContainer::Fire_OnUserAvatarURLRetrieved
		- CWCLReskin::IsAvatarFromFile

#. [D] CSCvc15881
	+ T31R2 Flash client E Attendees and panelists are unable to hear the host
	+ Assign to Winter Yu


#. [D] CSCvc17039
	+ T31.7 Share Multimedia YouTube Adobe Flash Player error
	+ Assgin to Morgan

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

#. [D] WO0000000221097, (M::WME)
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
	+ Issue description
		- Host buy two account
		- Expectation : Just can start two meeting at the same time
		- Actual : It can start the 3rd meeting in TP
	+ CMR Hybrid solution, maintain
	+ Current use CMR4, without this issue

#. [W] WO0000000226784
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

#. [W] WO0000000226765, (M::GPC)
	+ Connection taking too long to get connected to VoIP
	+ Gpc hadn't callback caused the client hadn't join VoIP
	+ File a bug

#. [D] CSCvc02236, (CFD), (M::Tahoe)
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

#. [D] WO0000000211161, (TS)
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

#. [D] CSCvb69543
	+ Had closed
	+ Confirmed with PM: Connie Tang and Engineer: Wilson Chen & Wallice Wang, the conclusion is: the engineering team feels that opening the firewall for only the WebEx MMP servers is still a secure solution

#. [D] CSCvb71340, (CFD)
	+ Update status to Bill Wu
	+ Need HF team help to reproduce, mail
	+ Confirmed with Paul, changed to U
	

2016-11-07
----------

#. [W] CMR issue 43
	+ https://sqbu-github.cisco.com/CMR/support/issues/43#issuecomment-213229
	+ Need Send a mail to paul liu
	+ Request webex log

#. [D] WO0000000211492
	+ URGENT WO0000000211492: VoIP Issue HD0009165473
	+ Sunny Liao sugget rollback to T30

#. [D] WO0000000224259, (M::WME)
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
 

#. [D] WO0000000223395, CSCvb92423, (CFD)
	+ Meeting Center client Help option is loading the generic page instead of redirecting to the PG customized page
	+ Docshow => URLs => QSHelpURL
	
#. [D] WO0000000221752, (M::WME)
	+ Client crash, wseclient.dll
	+ Assigned to WME (Karina Li)
	::
	 
	 The previous fix is about ticket HD0009185218/WO0000000210084 and cdets  https://cdetsng.cisco.com/webui/#view=CSCvb18905
	 The code fix has submitted in T30.13, and already in T30.14.

2016-10-31
----------

#. [W] WO0000000216828, (M::WME)
	+ Webex client crashes
	+ https://cisco.box.com/s/n1odfzep4l0msktbdjxms1e20015kwke
	+ WME qiwei hao is checking

#. [D] WO0000000213144
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

#. [D] WO0000000219862, CSCvb78192, (CFD)
	+ SC crash
	+ AppSharing load failure
	+ Fix in T31.8 & T30.14
	+ https://cdetsng.cisco.com/webui/#view=CSCvb78192

#. [D] WO0000000223080, INC000000015580, (M::Security)
	+ WebEx 11 , urgent
	+ VOIP can't use
	+ root cause: SHA264 crypto method change, need page to fix

#. [D] CSCvb85985, (CFD)
	+ The page of Meeting info became blank screen on MC client with PPT info  template
	+ https://cdetsng.cisco.com/webui/#view=CSCvb85985
	+ From QA, Cellion Ye is checking

2016-10-24
----------

#. [D] CSCvb78958, (M::WME)
	+ multi cameras support
	+ https://cdetsng.cisco.com/webui/#view=CSCvb78958&vt=3
	+ assign to Ju Ma, wseshell.exe
	

#. [D] CSCvb69936, (CFD), (M::WME)
	+ DNS, DHCP can config proxy url
	+ WPAD
	+ HD0009249582,HD0009243179
	+ It takes 1-3 minutes to connect to VoIP/Video for certain networks on WBS30.9 MC client.
	+ Downgrade sites to WBS30.6 or lower or Upgrade sites to WBS 31.
	+ CCmHttpProxyManager::InitGetterArray
	+ Configuring WPAD Entries
		- https://technet.microsoft.com/en-us/library/cc713344.aspx 

#. [W] WO0000000214739, (M::WME)
	+ Meeting window crashes few seconds after joining the meeting.From logs, it crashed in tp.dll
	+ WME issue, Karina Li is checking

#. [D] WO0000000216265, 
	+ Video option is not getting enabled while in session also hangs at connecting to audio
	+ CSmSvcVideoSessionMgr::OnVideoSessionStatus
	

2016-10-15
----------

#. [D] CSCvb45367, (CFD)
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


#. [D] WO0000000209473, (M::GPC), (CFD::CSCvc63547) 
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

#. [W] WO0000000216726, WO0000000216198, (M::WME)
	+ It takes up to 2 mins to the audio through  connect to call using computer.

#. [D] CSCvb47815, (CFD), (M::GPC)
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

#. [D] WO0000000214995, (M::NBR)
	+ 7 minutes of audio missing in the NBR
	+ There is no client trace available.

#. [D] CSCvb53084, (CFD)
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



#. [D] WO0000000197315
	+ Randomly during an EC, Active video user's webcam video turns off, when this happens, EC's meeting option also becomes unchecked (Event -> Option -> "Video" has to be checked again to return Video capabilities for all attendees)
	::
	 
	 Typically when this happens, the option disables.
	 This time the option did not disable, but passing presenter back and forth fixed the issue.
	 
	 Because presenter "Valerie Arnold” have network problem around  08:03:23  to connect the MMP server, 
	 for this case presenter will try do reconnect, and tried 3 times the MMP reconnect still failed.  
	 So presenter will directly close meeting "Video Session”. 

2016-09-26
----------

#. [D] CSCvb41280, CSCva66671, (CFD), (M::GPC)
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

#. [D] WO0000000208302
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

#. [D] WO0000000211961, CSCvb26805, (CFD)
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

#. [D] CSCvb19442 , (CFD)
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
	+ you cannot connect to audio or video because we cannot validate the security certificate

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
	