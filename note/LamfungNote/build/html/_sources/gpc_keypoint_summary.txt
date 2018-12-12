GPC Key point Summary 
=====================

URL Protocol
------------

#. URL Protocol Parameter
	::
	 
	 wbx:f7295_Aqa_Awebex_Acom,f7295,105830700001791171,733007,MC,1-1-0,SDJTSwAAAIX6QjpHaTetQN7HGVbe-or7bP6an8tlRRwsA5BciDQ1lg2,15,t=1536642732758_webex.exe
	

#. URL Protocol Register
	+ CUrlProtocol::RegisterURLProtocol
		- CUrlProtocol::Register
		
#. URL Protocol Registry Editor
	::
	 
	 Computer\\HKEY_CURRENT_USER\\Software\\Classes\\wbx
	 	Default : Cisco Webex Meeting
	 	Content Type : application/wbx
	 	URL Protocol : ""
	 
	 	Computer\\HKEY_CURRENT_USER\\Software\\Classes\\wbx\\DefaultIcon
	 		Default : C:\\Users\\lawen\\AppData\\Local\\WebEx\\webex.exe
	 	
	 	Computer\\HKEY_CURRENT_USER\\Software\\Classes\\wbx\\shell
	 		Default : ""
	 		
	 		Computer\\HKEY_CURRENT_USER\\Software\\Classes\\wbx\\shell\\open
	 			Default : ""
	 		
	 			Computer\\HKEY_CURRENT_USER\\Software\\Classes\\wbx\\shell\\open\\command
	 				Default : C:\\Users\\lawen\\AppData\\Local\\WebEx\\webex.exe "%1"
	 
	 Computer\\HKEY_CURRENT_USER\\Software\\Classes\\MIME\\Database\\Content Type\\application/wbx
	 	Default : ""
	 	Extension : ".wbx"
	 
	 Computer\\HKEY_CURRENT_USER\\Software\\Classes\\.wbx
	 	Default : "wbx"
	 
	 Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\5.0\User Agent\Post Platform
	 	Default : ""
	 	wbx 1.0.0 : ""
	 
	 Computer\\HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\ProtocolExecute
	 	Default : ""
	 	
	 	Computer\\HKEY_CURRENT_USER\\Software\\Microsoft\\Internet Explorer\\ProtocolExecute\\wbx
	 		Default : ""
	 		WarnOnOpen : 0
	 		For more info about WarnOnOpen, please refer to https://blogs.msdn.microsoft.com/ieinternals/2011/07/13/understanding-protocols/

FQA
---

#. Identify product version
	+ gpcproductversion
		- T32_TC
		- T32_MC
		
#. atgpcdec version
	+ gpcunpackversion
		- 27.17.2017.317

#. meeting id
	+ meetingid
		- 103917954415114443
	
#. Browser type
	+ preJME>>ciscoWebexStart,Chrome/Firefox/3rd Extention
	+ CWSGPCWrapper::SetBrowserAgentType
	+ jme>>CJmeBrowserAgent>>GetBrowserType>> browser type
		- BROWSE_TYPE_FROM_PAGE_UNKNOWN = -1,
		- BROWSE_TYPE_FROM_PAGE_IE = 0,
		- BROWSE_TYPE_FROM_PAGE_FIREFOX = 9,
		- BROWSE_TYPE_FROM_PAGE_SAFARI = 10,
		- BROWSE_TYPE_FROM_PAGE_CHROME = 12,
		- BROWSE_TYPE_FROM_PAGE_EDGE = 15,
		- BROWSE_TYPE_FROM_PT = 101,
		- BROWSE_TYPE_FROM_JABBER = 102,

#. Browser Agent Type
	+ BROWSER_AGENT_TYPE_UNKNOW = 0,
	+ BROWSER_AGENT_TYPE_ACTIVEX = 1,
	+ BROWSER_AGENT_TYPE_NPAPI = 2,
	+ BROWSER_AGENT_TYPE_EXTENSION = 3,
	+ BROWSER_AGENT_TYPE_TFS = 4,
	+ BROWSER_AGENT_TYPE_URLPROTOCOL = 5,
	+ BROWSER_AGENT_TYPE_THIRDPARTY = 6,
	+ BROWSER_AGENT_TYPE_STAND_ALONE = 7, // just for Legacy logic standalone download
	+ BROWSER_AGENT_TYPE_OTHERS = 100,
		
#. IE Plugin Auto Update
	+ CExtensionManagerImpl::LoadUpdateSetting
		- 
	+ Jme_UpdateMgr_CheckUpdate.cpp
	+ Register
		- HKEY_CURRENT_USER
		- HKEY_LOCAL_MACHINE
		- SOFTWARE\\JME_PRODUCT_ROOT\\JME_PARAM_GPC_PRODUCT_VERSION\\autoupdate
	+ JME_PRODUCT_ROOT
		- GpcProductRoot_Value
	+ JME_PARAM_GPC_PRODUCT_VERSION
		- GpcProductVersion
	+ jme>>updateMgr>>checkUpdate>>initAutoUpdate
	+ jme>>updateMgr>>checkNeedUpdate
	
		
#. GPC download logic
	+ download filelist
		- gpcurlroot
		- gpcinifilename
		- filelist = gpcurlroot + "\\" + gpcinifilename
	+ #MTD# Add URL
	+ jme>>updateMgr>>fileList
	+ jme>>updateMgr>>doCheckUpdate
	+ jme>>updateMgr>>checkUpdate
	+ jme>>updateMgr>>checkNeedUpdate
	+ #MTD# Started download
	+ #MTD# Downloaded
	
#. IsDBCSLeadByte
	+ 判断某字节是否在双字节字符集(例如汉字)的前导字节集中(GB   2312-80)   汉字编码中的第一个字节。DBCS：双字节字符集。
	
#. Filelist Info
	+ File List Item and GPCFilesHash Item
	::
	 
	 "AppSharing.dll; AppSharing.7z;;1032, 1811, 100, 1600;937016;238936;N;VERSION;IGNORE;0"
	 Source Name : appsharing.dll,Url : appsharing.7z,Target : ,Version : 1032, 1811, 100, 1600,
	 File size : 924216,Compressed size : 234785,Action : N,UpdateControl : VERSION,FailureControl : IGNORE,OS version : 0
	 
	 AppSharing.7z:o9m/RkCkONW33qbNTe/0NelbXkx94fensENAdClfCdM=:1032, 1811, 100, 1600:937016:238936::Cisco WebEx LLC;

	+ Target
		- %system% : GetSystemDirectory
		- %window% : GetWindowsDirectory
		- %pdriver% : GetPrinterDriverDirectory, C:\\Windows\\system32\\spool\\DRIVERS\\W32X86
		- %kdriver% : GetSystemDirectory
		- %uninstall% : 
	+ Action
		- "r" : DllRegisterServer
		- "e" : ShellExecuteEx, lpParameters = _T("/r")
		- "p" : ShellExecuteEx, lpParameters = _T("/p")
	+ FailureControl
		- HandleGetFileCallback
		- FailureControl = "ignore"
		- FailureControl = "redirect"
		- FailureControl = "reboot"
		- FailureControl != "ignore", Stop
	+ UpdateControl
		- CATGpcInstallationMgr::CItem::NeedUpdate
		- "NEWVER" : _IsNeedUpdateByCheckingNewerVersion
		- "version" : _IsNeedUpdateByCheckingVersion, _IsNeedUpdateByCheckingSize
		- "size" : _IsNeedUpdateByCheckingSize
		- "existence" : return FALSE
		- "vertag" : _IsNeedUpdateByCheckingVerTag, "#~@WebexVersionTag@~#"
	+ GPCFilesHash Item
		- JmeSecurityHashItem
		- ParseGPCFileHash
		- ParseOneHashItem
		- m_vtSecurityHashItems
		
#. Check Proxy
	+ CheckJscriptProxy
		- InternetOpen
		- InternetQueryOption
	+ RemoveProxySet
		- InternetOpen
		- InternetQueryOption
		- InternetSetOption	

#. CASL
	+ CANADA
	+ GetUserGeoID, 39
	+ ReadCASLFlagFromReg
	+ ReadCASLFlagFromIni
	
#. After file downloaded, verify file integrity
	+ doInstallFile
		- check7zFileHash : CalHashOfFile, Base64Encode
		- Unzip .7z file : GpcDecompressFileW, GpcDecompressFile
		- checkInstallFileSecurity : CheckWebExFileDigitalSignature, VerifyModuleSignatureAndSubject
		- SetSecurityDesc

#. File Security
	+ Advapi32.dll
		- ConvertStringSecurityDescriptorToSecurityDescriptorW
		- ConvertStringSecurityDescriptorToSecurityDescriptorA
		:: 
		 
		  	SecuDescAllUsers = _T("D:")						//DACL
		 					_T("(A;OICI;GA;;;BA)")			//Allow Admin Full Control
		 					_T("(A;OICI;GA;;;PU)")			//Allow Power User Full Control
		 					_T("(A;OICI;GA;;;BU)")			//Allow User Full Control
		 					_T("(A;OICI;GRGWGX;;;WD)");		//Allow Everyone RWX
		  	
		 	SecuDescCurrentUser = _T("D:")						//DACL
		 					_T("(A;OICI;GA;;;BA)")			//Allow Admin Full Control
		 					_T("(A;OICI;GA;;;PU)")			//Allow Power User Full Control
		 					_T("(A;OICI;GA;;;BU)");			//Allow User Full Control
		 	
		 	SecuDescAdministrator = _T("D:")					//DACL
		 					_T("(A;OICI;GA;;;BA)")			//Allow Admin Full Control
		 					_T("(A;OICI;GA;;;PU)")			//Allow Power User Full Control
		 					_T("(A;OICI;GRGX;;;BU)");		//Allow User Full Control
			
	+ SetFileSecurity


#. TFS Type
	+ IsDocShowCommandParameterFormat
		- ParseCommandParameterDochShow
		- DocShow:
	+ IsShotNameCommandParameterFormat
		- ParseCommandParameterShortFileName
		- "webex_"
	+ IsNewCommandParameterFormat
		- ParseCommandParameterNew
		- get meeting info ,****,***,*****_webexe.exe
	+ IsWebEx11CommandParameterFormat
		- ParseCommandParameterWebEx11
		- "__"
	+ Old Parameter
		- ParseCommandParameterOld

#. ParseCommandParameterNew
	+ Parameter Sample
		:: 
		 
		 wbx:f7295_Aqa_Awebex_Acom,f7295,105830700001791171,733007,MC,1-1-0,SDJTSwAAAIX6QjpHaTetQN7HGVbe-or7bP6an8tlRRwsA5BciDQ1lg2,15,t=1536642732758_webex.exe
		 f7295_Aqa_Awebex_Acom,f7295,105830700001791171,733007,MC,1-1-0,SDJTSwAAAIX6QjpHaTetQN7HGVbe-or7bP6an8tlRRwsA5BciDQ1lg2,15,t=1536642732758
	
	+ Parameter Element
		- Site Url : "_A" => ".", "_C" => "_", [0] = "," => siteurl + ".webex.com"
		- Site Name
		- Conference ID
		- User ID
		- Service Type
		- Flag : "-" => "%7C"
		- EMAC
		- Browser Type
		- jmtclicklog : "t="
		- Language ID

#. TFS self delete
	+ TFS_CallDeleteSelf
		- VerifyModuleSignatureAndSubject
		::
		  
		 CSecurityUtilImpl::VerifyModuleSignature, Is Fail to verify [C:\\Users\\lawen\\AppData\\Local\\WebEx\\webex.exe]
		
		- CreateProcess
	+ TFS_DeleteSelf


#. IE Protected Mode
	::
	 
		If your extension needs to run a separate EXE, you can add a registry key that tells IE that your EXE is trusted and can be run without a prompt. 
		The registry key that controls this behavior is
		
	 	HKLM\Software\Microsoft\Internet Explorer\Low Rights\ElevationPolicy
	 	
	 	Create a new GUID, then add a key under ElevationPolicy whose name is that GUID. In that new key, create three values:
		
		AppName: The filename of the executable, for example "DempApp.exe".
		AppPath: The directory where the EXE is located.
		Policy: A DWORD set to 3. 

Reference
---------

#. Security Descriptor String Format
	+ https://docs.microsoft.com/en-us/windows/desktop/secauthz/security-descriptor-string-format
	
#. Understanding Protocols
	+ https://blogs.msdn.microsoft.com/ieinternals/2011/07/13/understanding-protocols/
	
#. IE Protected Mode
	+ https://www.codeproject.com/Articles/18866/A-Developer-s-Survival-Guide-to-IE-Protected-Mode