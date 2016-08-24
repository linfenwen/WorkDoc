Tigger Windows FQA 2016-08-23
=============================

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


