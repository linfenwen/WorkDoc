Chrome NPAPI Replacement
========================

How to build **Cisco_WebEx_Add-On.exe**
---------------------------------------
1. Locate at *"/020p/bin/release"* directory and add 3 files

  + 'manifest.json'
  + extaction.bin
  + npapicfg

2. Add 2 projects

  + "020p\\src\\windows\\AtStart\\bind\\bind.vcproj"
  + "020p\\src\\windows\\AtStart\\Setup\\Setup.vcproj"

3. Output **Cisco_WebEx_Add-On.exe**

  + Execute command as below::
  
    bind.exe npapicfg setup.exe Cisco_WebEx-Add-On.exe

  + If *bind.exe* cannot be executed, rename *bind.exe* to *exebind.exe*, then execute below command::
  
    exebind.exe npapicfg setup.exe Cisco_WebEx-Add-On.exe

For a new release, you need send a mail to *Quick* ask to modify build script, for example::

 Please add the 2 projects below to T28L10NSP12 and T27L10NSP32.
 020p\src\windows\AtStart\bind\bind.vcproj
 020p\src\windows\AtStart\Setup\Setup.vcproj
 
 Excute command below after build successfully.
 bind.exe npapicfg setup.exe Cisco_WebEx_Add-On.exe

 For output, if bind.exe cannot be executed, please rename bind.exe to exebind.exe.
 And then excute below command:
 exebind.exe npapicfg setup.exe Cisco_WebEx_Add-On.exe

3 config files
--------------

* mainfest.json 

::
 
 {
 	"name": "com.webex.meeting",
 	"description": "com.webex.meeting",
 	"path": "CiscoWebExStart.exe",
 	"type": "stdio",
 	"allowed_origins": [ 
 		"chrome-extension://jlhmfgmfgeifomenelglieieghnjghma/"
 	]
 }

* extaction.bin 

::
 
 Path=#currentappdata#\WebEx\ChromeNativeHost
 Excute=#Path#\CiscoWebExStart.exe
 Argument=/r
 runasadmin=0

* npapicfg 

::
 
 npatgpc.dll
 manifest.json
 CiscoWebExStart.exe
 extaction.bin

4 When update **CiscoWebexStart.exe** version, need to sync following package config files
------------------------------------------------------------------------------------------

*  Locate to the repo *webex-cloudsapp-config* 
*  Sync up *CiscoWebexStartVersion* field with **CiscoWebexStart.exe** version

	#. GPC/package.event
	#. GPC/package.nbr
	#. GPC/package.nbr_orion
	#. GPC/package.ra
	#. GPC/package.smt
	#. GPC/package.support
	#. GPC/package.training
	#. GPC/package.webex
	#. GPC/package.webex_orion



**CiscoWebExStart.exe**
-----------------------

CiscoWebExStart main task :

* Use standard IO to receive *DocShow Parameters* from chrome
* Implement download logic by using *urlmon.dll*
* Use *atgpcext.dll* to start meeting by 
* Download or Upgrade *atgpcdec.dll*, then load *atgpcdec.dll*
* Download or Upgrade *atgpcext.dll*, then load *atgpcext.dll*



