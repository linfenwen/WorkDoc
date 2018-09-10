F2017: VS2017, Chrome & Firefox Test
====================================

Test Case
---------

Chrome
~~~~~~

#. MC

	+ Without Install Extension
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_UMC\\atmgr.exe
		-  /mcstd C:\\Users\\lawen\\AppData\\LocalLow\\WebEx
		- **Setup was unsuccessful. Please try again**
		- **Error [15], File [c:\\users\\lawen\\appdata\\local\\webex\\webexAppLauncher.exe]**
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_UMC\\atmgr.exe
		-  /mcstd C:\\Users\\lawen\\AppData\\LocalLow\\WebEx
		- **Setup was unsuccessful. Please try again**
		- **Error [15], File [c:\\users\\lawen\\appdata\\local\\webex\\webexAppLauncher.exe]**

#. EC
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_UMC\\atmgr.exe
		-  /ec C:\\Users\\lawen\\AppData\\LocalLow\\WebEx

#. TC
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_TC\\atmgr.exe
		-  /mc C:\\Users\\lawen\\AppData\\LocalLow\\WebEx

#. SC
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_SC\\atscmgr.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_SC\\atscmgr.exe /sc C:\\Users\\lawen\\AppData\\LocalLow\\WebEx\\WebEx.ini

Firefox
~~~~~~~

#. MC
	+ Without Install Extension
		- Popup Install Extension
		- Download and Run Cisco_WebEx_Start.exe
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_UMC\\atmgr.exe
		-  /mcstd C:\\Users\\lawen\\AppData\\LocalLow\\WebEx

#. EC
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_UMC\\atmgr.exe
		-  /ec C:\\Users\\lawen\\AppData\\LocalLow\\WebEx

#. TC
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_TC\\atmgr.exe
		-  /mc C:\\Users\\lawen\\AppData\\LocalLow\\WebEx

#. SC
	+ After Install Cisco_WebEx_Add-On.exe
		- C:\\Users\\lawen\\AppData\\Local\\WebEx\\WebEx\\T33_SC\\atscmgr.exe
		- /sc C:\\Users\\lawen\\AppData\\LocalLow\\WebEx\\WebEx.ini

CiscoWebExStart.exe
-------------------

#. Chrome
	+ C:\\Users\\lawen\\AppData\\Local\\WebEx\\ciscowebexstart.exe
	+ C:\\Users\\lawen\\AppData\\Local\\WebEx\\CiscoWebExStart.exe  chrome-extension://jlhmfgmfgeifomenelglieieghnjghma/ --parent-window=0

#. Firefox
	+ C:\\Users\\lawen\\AppData\\Local\\WebEx\\CiscoWebExStart.exe
	+ C:\\Users\\lawen\\AppData\\Local\\WebEx\\CiscoWebExStart.exe C:\\Users\\lawen\\AppData\\Local\\WebEx\\firefox.json ciscowebexstart1@cisco.com

Test Env
--------

#. Site
	+ f2017.qa.webex.com
	+ admin/P@ss1234

Others
------

#. Chrome Extension Install Location
	+ C:\\Users\\User_Name\\AppData\\Local\\Google\\Chrome\\UserData\\Default\\Extensions

#. Firefox Extension Install Location
	+ C:\\Users\\<Windows login/user name>\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\<profile folder>. 
	+ http://kb.mozillazine.org/Profile_folder_-_Firefox
	
#. View Chrome Extensions
	+ chrome://extensions
	
#. View Firefox Extensions
	+ about:addons


Reference
---------

#. create user
	+ go to f2017.qa.webex.com
	+ use admin/P@ss1234 login, then add a new user belong to yourself, such as davisli/P@ss1234.

