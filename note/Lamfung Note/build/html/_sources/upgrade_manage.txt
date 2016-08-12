Upgrade Manage
==============

.. role:: strike

CompatibleDesktopClients
------------------------

The Desktop Client will be able to decide if download of a different client version is 
required before joining the meeting. 

Json format data
~~~~~~~~~~~~~~~~

Here is an example that client will receive from 
docshow parameter::

 Version 1:
 {
 	”CompatibleDesktopClients":
 	{
 		"Client":
 		[ 
 			{
 				"BuildNumber":"1",
 				"Version":"T30LSP1",
 				"ReleaseOrder":"30100",
 				"DisplayVersion":"30.1.0.1",
 				"DownloadLink":"https:\\dileepvm.eng.webex.com\\client\\WBXclient- T30LSP1-1\\mac\\intel\\webex\\self\"
 			}, 
 			{
 				"BuildNumber":"2",
 				"Version":"T30LSP2",
 				"ReleaseOrder":"30200",
 				"DisplayVersion":"30.1.0.1",
 				"DownloadLink":"https:\\dileepvm.eng.webex.com\\client\\WBXclient- T30LSP1-1\\mac\\intel\\webex\\self\"
 			}, 
 			{
 				"BuildNumber":"3",
 				"Version":"T30LSP3",
 				"ReleaseOrder":"30300",
 				"DisplayVersion":"30.1.0.1",
 				"DownloadLink":"https:\\dileepvm.eng.webex.com\\client\\WBXclient- T30LSP1-1\\mac\\intel\\webex\\self\"
 			},
 			{
 				"BuildNumber":"4",
 				"Version":"T30LSP4",
 				"ReleaseOrder":"30400",
 				"DisplayVersion":"30.1.0.1",
 				"DownloadLink":"https:\\dileepvm.eng.webex.com\\client\\WBXclient- T30LSP1-1\\mac\\intel\\webex\\self\"
 			}
 		]
 	}
 }

 Version 2:
 GpcCompatibleClients : 
 {
 	"Client":
 		[
        	{
        		"BuildNumber":"10075",
        		"DisplayVersion":"29.12.0.10075",
        		"Version":"T29LSP12",
        		"DownloadLink":"https:\/\/ndileepvm.eng.webex.com\/clientWBXclient-T29L10NSP12-10075\/webex\/self",
        		"ReleaseOrder":"291200"
        	}
		]
 }
 
 Version 2, original data:
 "GpcUpgradeManagement":"true", 
 "GpcCompatibleClients":"{"Client":[{"BuildNumber":"10075","DisplayVersion":"29.12.0.10075","Version":"T29LSP12","DownloadLink":"https:\/\/ndileepvm.eng.webex.com\/clientWBXclient-T29L10NSP12-10075\/webex\/self","ReleaseOrder":"291200"}]}", 
 
 ??? DisplayVersion ==> ClientBuildVersion
 ??? DownloadLink ==> GpcUrlRoot
 


Class Diagram
~~~~~~~~~~~~~

* Check Version

 .. image:: _static\um_gpc_compatible_clients_class.svg

* CiscoWebExUpdate Proxy

 .. image:: _static\um_gpc_update_proxy_class.svg

How to use **CCompatibleClients**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the example code::

 #include "compatibleclients.h"
 
 string strJson;
 CGpcCompatibleClients compatibleClients;
 compatibleClients.SetGpcCompatibleClients(strJson);
 
 string strLocalFirstDisplayVersion;
 string strLocalSecondDisplayVersion;
 compatibleClients.SetLocalDisplayVersion(strLocalFirstDisplayVersion, strLocalSecondDisplayVersion);
 
 bool bSupportUpgrade;
 compatibleClients.SetUpgradeManagement(bSupportUpgrade);
 
 //
 eCompatibleStatus = compatibleClients.GetCompatibleStatus();
 string strNewestDownloadLink = compatibleClients.GetDownloadLink()
 string strCompatibleDownloadLink = compatibleClients.GetCompatibleDownloadLink()
 
 ...Your Code...

New fields for the *NameValue section* of **webex.ini** 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. UpdateLaunch
#. UpdateClientBuildVersion
#. UpdateGpcUrlRoot
#. UpdateGpcIniFileName
#. UpdatePath
#. MeetingPath
#. UpdateGpcActiveIniSection
#. MeetingPathSecondary
#. UpdateFullGpcIniFileURL
#. regtype
#. UpdateCommunicationWND
#. UpdateCommunicationPID

*. SC don't provide **NameValue** ?

How to test **atgpcext.dll** by ie on windows os
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Build **Release -- No Signature check** version
#. Modify *ieatgpc.dll* and *atgpcext.dll* 's version with official's build
#. Use the **Release -- No Signature check** version *ieatgpc.dll* and *atgpcext.dll* to replace the installed one
#. Open regedit with command: regedit
#. Find all the **ieatgpc.dll** in regedit
#. Use the **Release -- No Signature check** version's path to replace the installed path


FAQ
---

#. How to get local **DisplayVersion** ? 

   - c:\\Users\\lawen\\AppData\\Local\\WebEx\\ClientInfo.ini
   - ??? Provide API to get local DisplayVersion, **ClientBuildVersion**

#. How to use **CiscoWebExUpgrade.exe** ?

   - Command
   
     + CiscoWebExUpgrade.exe *CheckAndUpdate* *webex.ini*
     + CiscoWebExUpgrade.exe *UpdateAndCopy* *webex.ini*
     
   - Parameters
   
     + How to generate saveToPath ? **ClientInfo.ini**
     + How to generate srcUrl ? **GpcUrlRoot**
     + How to generate downloadSection? **gpcactiveinisection**

#. gpc.php ?

    *GpcUrlRoot* + *gpcinifilename*

#. GpcComponentName ? like *atmccli.dll* , *ateccli.dll*

    Indicate which module *atgpcext.dll* should load, and the module will execute *GpcInitCall* and *GpcExitCall*

#. ClientInfo.ini ?

::

 C:\Users\lawen\AppData\Local\WebEx\ClientInfo.ini

#. How to compare the client version and determine whether it is compatible?

::

   Client will get a list of compatible sites in the server from the “GpcCompatibleClients” parameter.
   For example, the list includes T30SP1, T30SP2, T30SP3, and T30SP4. Client will get the display version of the local client.
   Upgrade management uses the display version of the local client to compare with the display version in the list of compatible sites in the server.
   If local display version is equal to anyone of display versions in the server list, it is compatible, otherwise it is NOT compatible.

#. How to determine the upgrade site?

   Just select the last one from the list of compatible sites in the server, and then upgrade to it in the background if it is optimal.

#. How to config to use *Active X Standalone* , *JAVA* , *TFS* start mode to start meeting?

   Use https://vmdev.qa.webex.com/ for example
   
   - Login site, click *Site Administration*
   - Click => Configuration => Common Site Settings => Options
   - Select *Active X and Standalone client* or *Java* or *Temporary Folder Solution*
   - Cliec *Update*

#. Replace **npatgpc.dll** to resolve **Cert Verify** issue for *FireFox*?

   Usually **npatgpc.dll** located at *C:\\Users\\lawen\\AppData\\Mozilla\\plugins*
    - Build **npatgpc.dll** with *Release -- No Signature check*
    - Replace **npatgpc.dll** with *Release -- No Signature check*

#. Replace **CiscoWebExStart.exe** to resolve **Cert Verify** issue for *Chrome* ?

   Usually **CiscoWebExStart.exe** located at *C:\\Users\\lawen\\AppData\\Local\\WebEx\\ChromeNativeHost.exe*
    - Build **CiscoWebExStart.exe** with *Release -- No Signature check*
    - Replace **CiscoWebExStart.exe** with *Release -- No Signature check*

#. **atsc3cls.dll**

   Search trace **LoadMainComponent**

#. How to play ARF (NBR online version)?

   Goto **My WebEx** click **My Files** then click **My Recordings**, click **Playback** button

#. How to enable or disable Browser plugins?

   - Chrome: chrome://extensions
   - FireFox: "Ctrl+Shift+A" or "Main Menu => Add-ons"
   - IE: "Manage add-ons" 

#. Windows File and Folder security ?

   - attribe
   - icacls

#. Windows Common Folder

   http://www.microsoft.com/security/portal/mmpc/shared/variables.aspx#programdata

#. Windows Command Line Reference

   https://technet.microsoft.com/en-us/library/cc753525.aspx

#. Use **Icacls** to disable folder *write data, add file* and *append data, add subdir*

   Icacls *fullFilePath* /deny "userName:(OI)(CI)(WD,AD)"

#. Bat get current user name?

   %USERNAME%

#. Command Redirection

   http://ss64.com/nt/syntax-redirection.html

#. How customize **Quick Start** ?

   #. If your site is : t29de02.qa.webex.com
   #. Login t29de02.qa.webex.com\brand.php with site admin account (admin/P@ss1234)
   #. Find **QuickStart Templates**
   #. Update your own *.ucf* file
   #. Schedule meeting with your customized session 


Common Resource
---------------

* Test Env

  - In VSCM
    
  - Out VSCM
    
    + ndileepvm.eng.webex.com/ndileep , ndileep/C!sco123
    
* Wiki

  - Lion
    
    + http://wikicentral.cisco.com/display/GROUP/Lion
    + http://wikicentral.cisco.com/display/GROUP/Test+Matrix+for+upgrade+management
    + http://wikicentral.cisco.com/display/CSGWEBAPP/Client+Version+Checker

* Rally

  - Dashboard
    
    + https://us1.rallydev.com/#/22229675488ud/dashboard
   
  - Team Status
    
    + https://us1.rallydev.com/#/22229675488ud/teamstatus?iterationKey=25725732534

* EC

  - EC
    + https://cctg-ec.cisco.com/commander/pages/EC-Homepage/homepage?s=Home

* RAPID

  - https://csg-hgh-rapid2.cisco.com

Test Case
---------

Test Scope
~~~~~~~~~~

We will change Cisco WebEx meeting folder name from digital number to string in T30 as following:

.. csv-table:: WebEx Service
   :header-rows: 0 
   :stub-columns: 1
   :header: "Service Type", "x-cli.dll","WebExMgr", "ServiceMgr" 
   :widths: 10, 10, 10, 10

   "MC", "atmccli.dll", WebExMgr.dll, FRAMEWORK_Reskin
   "EC", "ateccli.dll", wbxmgrec.dll, FRAMEWORK_Reskin
   "TC", "wbxtccli.dll", wbxmgrtc.dll, FRAMEWORK_Artemis
   "SC", "atsc3cls.dll", atsc3cli.dll, FRAMEWORK
   "SCC", "atsc3cls.dll", atsccust.dll, FRAMEWORK


::

 +--------------+--------------+-------------------+
 | Service Type | WebExMgr     | ServiceMgr        |
 +==============+==============+===================+
 | MC           | WebExMgr.dll | FRAMEWORK_Reskin  |
 +--------------+--------------+-------------------+
 | EC           | wbxmgrec.dll | FRAMEWORK_Reskin  |
 +--------------+--------------+-------------------+
 | TC           | wbxmgrtc.dll | FRAMEWORK_Artemis |
 +--------------+--------------+-------------------+
 | SC           | atsc3cli.dll | FRAMEWORK         |
 +--------------+--------------+-------------------+
 | SCC          | atsccust.dll | FRAMEWORK         |
 +--------------+--------------+-------------------+


Win XP SP3



.. csv-table:: Win XP SP3
   :header-rows: 1 
   :stub-columns: 1
   :header: , "IE", , , "FireFox", "Chrome", 
   :widths: 10, 10, 10, 10, 10, 10, 10

   , "Active X", "JAVA", "TFS", "NPAPI", "NPAPI", "Native Message"
   "MC", "QuickLaunch=disable, atmgrPath=%programfiles%\\webex\\webex\\T30_MC, cmdLine=/mcstd %temp%\\", , , "QuickLaunch=disable, atmgrPath=%appdata%\\Mozilla\\plugins\\webex\\T30_MC, cmdLine=/mcstd %temp%\\", , "QuickLaunch=disable, atmgrPath=%programfiles%\\webex\\webex\\T30_MC, cmdLine=/mcstd %temp%\\"
   "EC", , , , , ,
   "TC", , , , , ,
   "SC", , , , , ,
   "SCC", , , , , ,

.. csv-table:: Win7
   :header-rows: 1 
   :stub-columns: 1
   :header: , "IE", , , "FireFox", "Chrome", 
   :widths: 10, 10, 10, 10, 10, 10, 10

   , "Active X", "JAVA", "TFS", "NPAPI", "NPAPI", "Native Message"
   "MC", , , , , ,
   "EC", , , , , ,
   "TC", , , , , ,
   "SC", , , , , ,
   "SCC", , , , , ,


.. csv-table:: Win8.0
   :header-rows: 1 
   :stub-columns: 1
   :header: , "IE", , , "FireFox", "Chrome", 
   :widths: 10, 10, 10, 10, 10, 10, 10

   , "Active X", "JAVA", "TFS", "NPAPI", "NPAPI", "Native Message"
   "MC", Yes, , , Yes, , Yes
   "EC", , , , , ,
   "TC", , , , , ,
   "SC", , , , , ,
   "SCC", , , , , ,


.. list-table:: Win8.1
   :widths: 10 10 10 10 10 10 10
   :header-rows: 2
   :stub-columns: 1

   * - 
     - IE
     -
     -
     - FireFox
     - Chrome
     -
   * - 
     - Active X
     - JAVA
     - TFS
     - NPAPI
     - NPAPI
     - Native Message
   * - MC
     - Yes
     - 
     - 
     - Yes
     - 
     - Yes
   * - EC
     - 
     - 
     - 
     -
     -
     -
   * - TC
     - 
     - 
     - 
     -
     -
     -
   * - SC
     - 
     - 
     - 
     -
     -
     -
   * - SCC
     - 
     - 
     - 
     -
     -
     -



+---------------+----------+-----------+----------------+---------------------------------------------------------------------+
|              **UpgradeManagement**                                                                                          |
+---------------+----------+-----------+----------------+---------------------------------------------------------------------+
| Service Type  | OS       | Browser   | Start Mode     | Case                                                                |
+===============+==========+===========+================+=====================================================================+
| MC            | Win XP3  | IE        | Active X       | * atmgr.exe                                                         |
|               | (32)     |           |                |                                                                     |
|               |          |           |                |   - %ProgramFiles%\\WebEx\\WebEx\\T30_MC                            |
|               |          |           |                |   - /mcstd %TEMP%                                                   |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock  (%APPDATA%\\Mozilla\\plugins\\WebEx)                        |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_MC                                   |
|               |          |           |                |   - /mcstd %TEMP%\\                                                 |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %APPDATA%\\Mozilla\\plugins\\WebEx\\T30_MC                      |
|               |          |           |                |   - /mcstd %temp%\\                                                 |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * atmgr.exe                                                         |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_MC                                   |
|               |          |           |                |   - /mcstd %TEMP%\\                                                 |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %programfiles%\\WebEx\\WebEx                                    |
|               |          |           |                |   - /mcstd %temp%\\                                                 |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win7     | IE        | Active X       | * Lock ProgramData\\WebEx                                           |
|               | (64)     |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_MC                            |
|               |          |           |                |   - ".exe" /mcstd %USERPROFILE%\\AppData\\LocalLow\\WebEx           |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_MC                             |
|               |          |           |                |   - /mcstd %USERPROFILE%\\AppData\\LocalLow\\WebEx                  |
|               |          |           |                |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win8.0   | IE        | Active X       | * atmgr.exe                                                         |
|               |  (64)    |           |                | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %AppData%\\Local                                                |
|               |          |           |                |   - exe /mcstd %appdata%\\LocalLow\\                                |
|               |          |           |                |                                                                     |
|               |          |           |                | * Unlock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx                                            |
|               |          |           |                |   - /mcstd %appdata%\\LocalLow\\WebEx                               |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           | * jp2launcher.exe, atinst.exe                                       |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_MC                             |
|               |          |           |                |   - "*.exe" /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\             |
|               |          |           |                |                                                                     |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_MC                            |
|               |          |           |                |   - /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_MC                            |
|               |          |           |                |   - ".exe" /mcstd %USERPROFILE%\AppData\LocalLow\\WebEx\\           |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_MC                             |
|               |          |           |                |   - /mcstd %USERPROFILE%\AppData\LocalLow\\WebEx\\                  |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_MC                            |
|               |          |           |                |   - /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * CiscoWebExStart.exe , atmgr.exe                                   |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_MC                             |
|               |          |           |                |   - /mcstd %USERPROFILE%\AppData\LocalLow\\We..                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
+---------------+----------+-----------+----------------+---------------------------------------------------------------------+
| EC            | Win XP3  | IE        | Active X       | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramFiles%\\WebEx\\WebEx\\T30_EC                            |
|               |          |           |                |   - /ec %TEMP%                                                      |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock  (%APPDATA%\\Mozilla\\plugins\\WebEx)                        |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_EC                                   |
|               |          |           |                |   - /ec %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %APPDATA%\\Mozilla\\plugins\\WebEx\\T30_EC                      |
|               |          |           |                |   - /ec %temp%\\                                                    |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * atmgr.exe                                                         |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_EC                                   |
|               |          |           |                |   - /ec %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %programfiles%\\WebEx\\WebEx                                    |
|               |          |           |                |   - /ec %temp%\\                                                    |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win7     | IE        | Active X       | * Lock ProgramData\\WebEx                                           |
|               | (64)     |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_EC                            |
|               |          |           |                |   - ".exe" /ec %USERPROFILE%\\AppData\\LocalLow\\WebEx              |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_EC                             |
|               |          |           |                |   - /ec %USERPROFILE%\\AppData\\LocalLow\\WebEx                     |
|               |          |           |                |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win8.0   | IE        | Active X       | * atmgr.exe                                                         |
|               |          |           |                | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %AppData%\\Local                                                |
|               |          |           |                |   - exe /ec %appdata%\\LocalLow\\                                   |
|               |          |           |                |                                                                     |
|               |          |           |                | * Unlock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx                                            |
|               |          |           |                |   - /ec %appdata%\\LocalLow\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           | * jp2launcher.exe, atinst.exe                                       |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_EC                             |
|               |          |           |                |   - "*.exe" /ec %USERPROFILE%\AppData\LocalLow\\WebEx\\             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_EC                            |
|               |          |           |                |   - ".exe" /ec %USERPROFILE%\AppData\LocalLow\\WebEx\\              |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_EC                             |
|               |          |           |                |   - /ec %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_EC                            |
|               |          |           |                |   - /ec %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           |                |                                                                     |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * CiscoWebExStart.exe , atmgr.exe                                   |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_EC                             |
|               |          |           |                |   - /ec %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
+---------------+----------+-----------+----------------+---------------------------------------------------------------------+
| TC            | Win XP3  | IE        | Active X       | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramFiles%\\WebEx\\WebEx\\T30_TC                            |
|               |          |           |                |   - /mc %TEMP%                                                      |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock  (%APPDATA%\\Mozilla\\plugins\\WebEx)                        |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_TC                                   |
|               |          |           |                |   - /mc %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %APPDATA%\\Mozilla\\plugins\\WebEx\\T30_TC                      |
|               |          |           |                |   - /mc %temp%\\                                                    |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_TC                                   |
|               |          |           |                |   - /mc %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %programfiles%\\WebEx\\WebEx                                    |
|               |          |           |                |   - /mc %temp%\\                                                    |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win7     | IE        | Active X       | * Lock ProgramData\\WebEx                                           |
|               | (64)     |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_TC                            |
|               |          |           |                |   - ".exe" /mc %USERPROFILE%\\AppData\\LocalLow\\WebEx              |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_TC                             |
|               |          |           |                |   - /mc %USERPROFILE%\\AppData\\LocalLow\\WebEx                     |
|               |          |           |                |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win8.0   | IE        | Active X       | * atmgr.exe                                                         |
|               |          |           |                | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %AppData%\\Local                                                |
|               |          |           |                |   - exe /mc %appdata%\\LocalLow\\                                   |
|               |          |           |                |                                                                     |
|               |          |           |                | * Unlock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx                                            |
|               |          |           |                |   - exe /mc %appdata%\\LocalLow\\WebEx                              |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           | * jp2launcher.exe, atinst.exe                                       |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_TC                             |
|               |          |           |                |   - "*.exe" /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atmgr.exe                                                         |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_TC                            |
|               |          |           |                |   - ".exe" /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\              |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_TC                             |
|               |          |           |                |   - /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atmgr.exe                                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_TC                            |
|               |          |           |                |   - /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           |                |                                                                     |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * CiscoWebExStart.exe , atmgr.exe                                   |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_TC                             |
|               |          |           |                |   - /mc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
+---------------+----------+-----------+----------------+---------------------------------------------------------------------+
| SC            | Win XP3  | IE        | Active X       | * atscmgr.exe                                                       |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramFiles%\\WebEx\\WebEx\\T30_SC                            |
|               |          |           |                |   - /sc %TEMP%                                                      |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atscmgr.exe                                                       |
|               |          |           |                | * Lock  (%APPDATA%\\Mozilla\\plugins\\WebEx)                        |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_SC                                   |
|               |          |           |                |   - /sc %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %APPDATA%\\Mozilla\\plugins\\WebEx\\T30_SC                      |
|               |          |           |                |   - /sc %temp%\\                                                    |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * atscmgr.exe                                                       |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_SC                                   |
|               |          |           |                |   - /sc %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %programfiles%\\WebEx\\WebEx                                    |
|               |          |           |                |   - /sc %temp%\\                                                    |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win7     | IE        | Active X       | * Lock ProgramData\\WebEx                                           |
|               | (64)     |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atscmgr.exe                                                       |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SC                            |
|               |          |           |                |   - ".exe" /sc %USERPROFILE%\\AppData\\LocalLow\\WebEx\\WebEx.ini   |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SC                             |
|               |          |           |                |   - /sc %USERPROFILE%\\AppData\\LocalLow\\WebEx\\WebEx.ini          |
|               |          |           |                |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * atscmgr.exe                                                       |
|               |          |           |                | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win8.0   | IE        | Active X       | * atscmgr.exe                                                       |
|               |          |           |                | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %AppData%\\Local\\WebEx                                         |
|               |          |           |                |   - exe exe /sc %AppData%\\LocalLow\\~\\*.ini                       |
|               |          |           |                |                                                                     |
|               |          |           |                | * Unlock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx                                            |
|               |          |           |                |   - exe /sc %appdata%\\LocalLow\\WebEx                              |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           | * jp2launcher.exe, atinst.exe                                       |
|               |          |           |                | * atscmgr.exe                                                       |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SC                             |
|               |          |           |                |   - "*.exe" /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\             |
|               |          |           |                |                                                                     |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atscmgr.exe                                                       |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SC                            |
|               |          |           |                |   - ".exe" /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\WebEx.ini     |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SC                             |
|               |          |           |                |   - /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\WebEx.ini            |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atscmgr.exe                                                       |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SC                            |
|               |          |           |                |   - /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * CiscoWebExStart.exe , atscmgr.exe                                 |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SC                             |
|               |          |           |                |   - "*.exe"  /sc                                                    |
|               |          |           |                |   - %USERPROFILE%\AppData\LocalLow\\WebEx\\.ini                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
+---------------+----------+-----------+----------------+---------------------------------------------------------------------+
| SCC           | Win XP3  | IE        | Active X       | * ieatgpc.dll                                                       |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * plugin-container.exe (npatgpc.dll)                                |
|               |          |           |                | * Lock  (%APPDATA%\\Mozilla\\plugins\\WebEx)                        |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_SCC                                  |
|               |          |           |                |   - "..container.exe" --channel                                     |
|               |          |           |                |     "%APPDATA%\\..\\plugins\\npatgpc.dll"                           |
|               |          |           |                |     \-\- greomni                                                    |
|               |          |           |                |     "%programfiles%\\Mozilla Firefox\\omni.jar"                     |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %APPDATA%\\Mozilla\\plugins\\WebEx\\T30_SCC                     |
|               |          |           |                |   - "..container.exe" --channel                                     |
|               |          |           |                |     "%APPDATA%\\..\\plugins\\npatgpc.dll"                           |
|               |          |           |                |     \-\- greomni                                                    |
|               |          |           |                |     "%programfiles%\\Mozilla Firefox\\omni.jar"                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * atscmgr.exe                                                       |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\T30_SCC                                  |
|               |          |           |                |   - /sc %TEMP%\\                                                    |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %programfiles%\\WebEx\\WebEx                                    |
|               |          |           |                |   - /sc %TEMP%\\                                                    |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win7     | IE        | Active X       | * Lock ProgramData\\WebEx                                           |
|               | (64)     |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atscmgr.exe                                                       |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SCC                           |
|               |          |           |                |   - ".exe" /sc %USERPROFILE%\\AppData\\LocalLow\\WebEx\\WebEx.ini   |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SCC                            |
|               |          |           |                |   - /sc %USERPROFILE%\\AppData\\LocalLow\\WebEx\\WebEx.ini          |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atscmgr.exe                                                       |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SCC                           |
|               |          |           |                |   - /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * atscmgr.exe                                                       |
|               |          |           |                | * Lock ProgramData\\WebEx                                           |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %appdata%\\local\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData\\WebEx                                             |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
|               +----------+-----------+----------------+---------------------------------------------------------------------+
|               | Win8.0   | IE        | Active X       | * atscmgr.exe                                                       |
|               |          |           |                | * Lock %ProgramData%\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %AppData%\\Local                                                |
|               |          |           |                |   - exe exe /sc %AppData%\\LocalLow\\~\\.ini                        |
|               |          |           |                |                                                                     |
|               |          |           |                | * Unlock ProgramData\\WebEx                                         |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx                                            |
|               |          |           |                |   - exe /sc %appdata%\\LocalLow\\WebEx                              |
|               |          |           |                |                                                                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | JAVA           | * jp2launcher.exe, atinst.exe                                       |
|               |          |           |                | * atscmgr.exe                                                       |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SCC                            |
|               |          |           |                |   - "*.exe" /sc  %USERPROFILE%\AppData\LocalLow\\WebEx\\            |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            |                                                                     |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | FireFox   | NPAPI          | * atscmgr.exe                                                       |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SCC                           |
|               |          |           |                |   - ".exe" /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\WebEx.ini     |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock %ProgramData%\\WebEx\\WebEx                                |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SCC                            |
|               |          |           |                |   - /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\WebEx.ini            |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | TFS            | * t29de02*.exe                                                      |
|               |          |           |                | * atscmgr.exe                                                       |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %LOCALAPPDATA%\\WebEx\\WebEx\\T30_SCC                           |
|               |          |           |                |   - /sc %USERPROFILE%\AppData\LocalLow\\WebEx\\                     |
|               |          |           |                |                                                                     |
|               |          |           |                | * Lock %ProgramData%\\WebEx\\WebEx                                  |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          +-----------+----------------+---------------------------------------------------------------------+
|               |          | Chrome    | Native Message | * CiscoWebExStart.exe , atmgr.exe                                   |
|               |          |           |                | * Lock                                                              |
|               |          |           |                |                                                                     |
|               |          |           |                |   - Meeting can't start                                             |
|               |          |           |                |                                                                     |
|               |          |           |                | * UnLock                                                            |
|               |          |           |                |                                                                     |
|               |          |           |                |   - %ProgramData%\\WebEx\\WebEx\\T30_SCC                            |
|               |          |           |                |   - "*.exe"  /sc                                                    |
|               |          |           |                |   - %USERPROFILE%\AppData\LocalLow\\WebEx\\.ini                     |
|               |          |           +----------------+---------------------------------------------------------------------+
|               |          |           | NPAPI          |                                                                     |
+---------------+----------+-----------+----------------+---------------------------------------------------------------------+


#. WebEx meeting *work directory* occupied by *other process*
#. Admin User
#. Non-Admin User
#. The same type meeting, mutile meeting

::

 +-----------------+--------+----------+--------+----------+--------+-----------------+
 |                 | IE                         | FireFox  | Chrome                   |
 + Service Type    +----------+--------+--------+----------+--------+-----------------+
 |                 | Active X | JAVA   | TFS    | NPAPI    | NPAPI  | Native Message  |
 +=================+==========+========+========+==========+========+=================+
 | MC              |          |        |        |          |        |                 |
 +-----------------+----------+--------+--------+----------+--------+-----------------+
 | EC              |          |        |        |          |        |                 |
 +-----------------+----------+--------+--------+----------+--------+-----------------+
 | TC              |          |        |        |          |        |                 |
 +-----------------+----------+--------+--------+----------+--------+-----------------+
 | SC              |          |        |        |          |        |                 |
 +-----------------+----------+--------+--------+----------+--------+-----------------+
 | SCC             |          |        |        |          |        |                 |
 +-----------------+----------+--------+--------+----------+--------+-----------------+



.. code:: c++

    #include <stdio.h>
    
    int main()
    {
         printf("hello, world.\n");
         return 0;
    }


.. role:: html(raw)
   :format: html

:html:`<strike>striken out text</strike>`.

:strike:`22222`

