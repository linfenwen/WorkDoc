CSCuq12455
==========

.. role:: strike
.. role:: strtt
.. role:: underline

MMP Servers
-----------

* Scope
 + MC
 + EC
 + TC

* MMP Session
 + VIOP only
 + Hybrid VOIP
 + AB(Audio Broadcast) 
 + Video
 + SVS
 + NBRPlayer 
 

* AtConfMgr pre-condition
 + SVN ready
 + VSCM Test Env ready
 + ARM, TP interface ready
 + Team or Resource
 + MMP SDK relevant interface ready
 + Time currently less than 40 Days

* Windows Client
 + Need cache mutile Certs


* User Cases

  - Presenter
  
    + Cert Error, Mutile Session (Audio, Video etc..), same Cert, Just show one time Cert Error Window
    + Cert Error, Mutile Session (Audio, Video etc..), different Cert, Show mutile times Cert Error Window
    + Cert Error, Single Session (Audio or Video), Show Cert Error Window
    + Cert Error, Cert Error Window showed, and User click **Don't Connect**
    + Cert Error, Cert Error Window showed, and User click **Connect Anyway**

  - Attendee
  
    + Cert Error, Mutile Session (Audio, Video etc..), same Cert, Just show one time Cert Error Window
    + Cert Error, Mutile Session (Audio, Video etc..), different Cert, Show mutile times Cert Error Window
    + Cert Error, Single Session (Audio or Video), Show Cert Error Window
    + Cert Error, Cert Error Window showed, and User click **Don't Connect**
    + Cert Error, Cert Error Window showed, and User click **Connect Anyway**
  
* :strike:`Need UT?`
* :strike:`Need merge to other branch?`

Interface between **CC** and **Service**
-----------------------------------------

* **Video Windows** 

::

 typedef enum
 {
         MMT_VIDEO_SESSION_JOIN_SUCCESS,
         MMT_VIDEO_SESSION_JOIN_FAIL,
         MMT_VIDEO_SESSION_LEAVE,
         MMT_VIDEO_SESSION_PENDING_SSL_CERTIFICATE
 }MMT_VIDEO_SESSION_STATUS, *PMMT_VIDEO_SESSION_STATUS;
 
 typedef enum
 {
         MMT_VIDEO_CERTIFICATION_TYPE_SSL = 0x00
 
 }MMT_VIDEO_CERTIFICATION_TYPE, *PMMT_VIDEO_CERTIFICATION_TYPE;
 
 typedef enum
 {
         MMT_VIDEO_CERTIFICATION_ACTION_IGNORE = 0x00,
         MMT_VIDEO_CERTIFICATION_ACTION_CANCEL = 0x01
 
 }MMT_VIDEO_CERTIFICATION_ACTION, *PMMT_VIDEO_CERTIFICATION_ACTION;
 
 //get/set SSL certification INFO/action
 virtual void GetCertificationInfo(unsigned char type, char* pCertificationInfo, unsigned long& ulCertificationInfoLen) = 0;
 virtual void SetCertificationAction(unsigned char type, unsigned char action) = 0;


* **SVS Windows**

::

 typedef enum
 {
         MM_MEDIASTREAMING_SESSION_STATUS_JOIN_SUCCESS = 0,
         MM_MEDIASTREAMING_SESSION_STATUS_JOIN_FAIL,
         MM_MEDIASTREAMING_SESSION_STATUS_JOIN_RETRY,
         MM_MEDIASTREAMING_SESSION_STATUS_LEAVE_OK,
         MM_MEDIASTREAMING_SESSION_STATUS_RECONNECTING,
         MM_MEDIASTREAMING_SESSION_STATUS_RECONNECT_SUCCESS,
         MM_MEDIASTREAMING_SESSION_STATUS_RECONNECT_FAIL,
         MM_MEDIASTREAMING_SESSION_STATUS_RECONNECT_NETWORK_ERROR,
         MM_MEDIASTREAMING_SESSION_STATUS_PENDING_SSL_CERTIFICATE,
 
         // if Attendee's number has reached to max count(1000 defined), pop up message for new attendee!
         MM_MEDIASTREAMING_SESSION_STATUS_ATTENDEE_REACH_MAX_COUNT = 100,
         // if SVC exists and presenter don't want stop SVC, so it need stop SVS.
         MM_MEDIASTREAMING_SESSION_STATUS_STOP_SVS_FOR_SVC,
         MM_MEDIASTREAMING_SESSION_STATUS_ALLOW_PLAY
 
 }MM_MEDIASTREAMING_SESSION_STATUS;
 
 typedef enum
 {
         MM_MEDIASTREAMING_CERTIFICATION_TYPE_SSL = 0x00
 }MM_MEDIASTREAMING_CERTIFICATION_TYPE, *PMM_MEDIASTREAMING_CERTIFICATION_TYPE;
 
 typedef enum
 {
         MM_MEDIASTREAMING_CERTIFICATION_ACTION_IGNORE = 0x00,
         MM_MEDIASTREAMING_CERTIFICATION_ACTION_CANCEL = 0x01
 
 }MM_MEDIASTREAMING_CERTIFICATION_ACTION, *PMM_MEDIASTREAMING_CERTIFICATION_ACTION;
 
 //get/set SSL certification INFO/action
 virtual void GetCertificationInfo(unsigned char type, char* pCertificationInfo, unsigned long& ulCertificationInfoLen) = 0;
 virtual void SetCertificationAction(unsigned char type, unsigned char action) = 0;

* **AB**

::

 /****************************************************************************/
 /*Interface name: AudioSS_GetCertificationInfo                                                                     */
 /*                                 AudioSS_SetCertificationAction                                                                        */
 //Description: Set current AB Certification                                                                         */
 /*Parameters:                                                                                                                                                      */
 /*               type: value of AUDIOSS_CERTIFICATION_TYPE                          */
 /*      action: value of AUDIOSS_CERTIFICATION_ACTION                                                     */
 /****************************************************************************/
 void __stdcall AudioSS_GetCertificationInfo(unsigned char type, char* pCertificationInfo, unsigned long& ulCertificationInfoLen) ;
 void __stdcall AudioSS_SetCertificationAction(unsigned char type, unsigned char action)  ;
 
 
 #define AUDIOSS_STATUS_CERTIFICATION 1009
 
 typedef enum
 {
         AUDIOSS_CERTIFICATION_TYPE_SSL = 0x00
 
 }AUDIOSS_CERTIFICATION_TYPE, *PAUDIOSS_CERTIFICATION_TYPE;
 
 typedef enum
 {
         AUDIOSS_CERTIFICATION_ACTIION_IGNORE = 0x00,
         AUDIOSS_CERTIFICATION_ACTIION_CANCEL = 0x01
 
 }AUDIOSS_CERTIFICATION_ACTION, *PAUDIOSS_CERTIFICATION_ACTION;

* **Audio**

::

 typedef void (__stdcall* MmGetCertificationInfo)(unsigned char type, char* pCertificationInfo, unsigned long& ulCertificationInfoLen) ;
 typedef void (__stdcall* MmSetCertificationAction)(unsigned char type, unsigned char action) ;
 
 typedef enum
 {
         AUDIO_CERTIFICATION_TYPE_SSL = 0x00
 
 }AUDIO_CERTIFICATION_TYPE, *PAUDIO_CERTIFICATION_TYPE;
 
 typedef enum
 {
         AUDIO_CERTIFICATION_ACTIION_IGNORE = 0x00,
         AUDIO_CERTIFICATION_ACTIION_CANCEL = 0x01
 }AUDIO_CERTIFICATION_ACTION, *PAUDIO_CERTIFICATION_ACTION;
 
 const DWORD WEBEX_AUDIO_SESSION_CONFIRM                = 31016;//0：join success; 1：join or rejoin fail
         const DWORD SESSION_JOIN_OK                               = 0;
         const DWORD SESSION_JOIN_FAIL                            = 1;
         const DWORD SESSION_JOIN_RETRY                        = 2;
         const DWORD SESSION_CALLIN_FAIL                       = 3;
         const DWORD SESSION_LEAVE_OK                            = 4;
         const DWORD SESSION_CAPACITY_LIMIT               = 5;
         const DWORD SESSION_CERTIFICATION                  = 6;
 
 When Get WEBEX_AUDIO_SESSION_CONFIRM with code SESSION_CERTIFICATION,
 Then call MmGetCertificationInfo
 Then MmSetCertificationAction



Common Resource
---------------

* Wiki

  - http://wikicentral.cisco.com/display/CSGQAWIKI/Security+Bug+CSCuq12455+fixing
* SVN

  - Client
    
    + https://wwwin-svn-sjc-2.cisco.com/csg/XXXX/branches/T29L10NSP13
  
  - `MMP Servers`_
    
