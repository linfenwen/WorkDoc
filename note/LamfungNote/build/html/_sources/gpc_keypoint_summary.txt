GPC Key point Summary 
=====================

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


#. TFS self delete
	+ TFS_CallDeleteSelf
		- VerifyModuleSignatureAndSubject
		::
		  
		 CSecurityUtilImpl::VerifyModuleSignature, Is Fail to verify [C:\\Users\\lawen\\AppData\\Local\\WebEx\\webex.exe]
		
		- CreateProcess
	+ TFS_DeleteSelf


Reference
---------

#. Security Descriptor String Format
	+ https://docs.microsoft.com/en-us/windows/desktop/secauthz/security-descriptor-string-format