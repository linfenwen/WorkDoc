Tiger Windows FQA Analyze
=========================

GPC parameter
-------------

#. MeetingID
#. clientbuildversion
#. productname
#. GpcErrorPageUrl : get ConfID
#. atmgr CommandLine
#. WBXHybridFlag


#. How to identify the wbxtrace.wbt
	+ GCC_Provider_Impl::conf_join_request
	+ CAtConfManager::SetNodeId
#. PList info
	+ CSmDefUserMgr2::OnAddUser
	+ CSmDefUserMgr2::OnRemoveUser 

ASN relevant logic
------------------

#. Who is ASN Selector
	+ CPfwServiceMgr::FindHybridASNSelector
#. Attendee receive ASN from CB
	+ CPfwServiceMgr::OnASNPduFromCB
#. Presenter receive ASN from TA
	+ CPfwServiceMgr::OnASNReport

Active Video logic
------------------

#. CSmSvcVideoSessionMgr::SelectChiefSender
#. CSmSvcVideoSessionMgr::VideoUI_AttachActiveUser
#. ISVideoClient::ResetVideoReceivingStatus

Video Session Failure
---------------------

#. CSmSvcVideoSessionMgr::OnSessionCreateIndication
#. CSmSvcVideoSessionMgr::OnSessionCreateConfirm
#. CSmSvcVideoSessionMgr::OnSessionCloseIndication
#. CSmSvcVideoSessionMgr::OnSessionRestartIndication

#. Freeze when initialise video module
	+ CsmSvcVideoSessionMgr::EnrollMMSession, begin
	+ CsmSvcVideoSessionMgr::EnrollMMSession, end

ARM keywords
------------

#. GCC_Ping_Mgr::ping_request

PMR or CMR Lobby Room
---------------------

#. GPC parameters
	+ CMRExpiredLobbyTime
	+ PMRNotifyHostAPI
	+ PMRRefreshCaptchaAPI
	+ EnableNonLoginUserStayInLobby
	+ IsUserBlockedInLobby
	+ CMRMeetingFlag
#. Inner control parameters
	+ CPfwMainFrame::m_bNeedShowOverlayViewPMR
#. Check Point
	+ CMCServiceMgr::OnConfJoinConfirm
	+ CMCServiceMgr::EnterVMRWaitingRoom


Some questions
--------------

#. IsMRICached