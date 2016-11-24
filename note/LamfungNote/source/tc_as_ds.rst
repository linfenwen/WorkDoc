TC AS DS Introduce
==================

Where is the *SC*
-----------------

* Source code directory : 029/src/windows/SC
* Project name : sc.sln

TC Owner
--------

#. Dev: 
#. QA: Nick Zhang

How to build unifiedAppShare
----------------------------

#. Enter *020p\\src\\windows\\unifiedAppShare*
#. Run *OneClickBuild.bat*
#. Enter *bld* folder

Change List
-----------

#. Menu : Share => Application => Running Application
#. Menu : Share => Application => Running Application
#. update msi package
#. update resource file


Known Issue
-----------

* UI Issue
* Accessibility Issue
* TC HOL In Session Case Depend on Agent (RA)
* TC HOL OnDemand Case Depend on Agent (RA)

Test Scope
----------

* OS

	+ Server 2008
	
		- Icon Issue
		
	+ Win7
	
		- Avoid Regression Issue
	
	+ Win10
	
		- Verify New Feature
	
* Session

	+ Normal TC
	+ BO
	+ HOL

* Test Entry

	+ Main Menu
	+ Quick Start (UCF)
	+ Quick Start (Non-UCF)
	+ FIT Menu
	+ Indicator

Test Case
---------

* Server 2008 : Check App Icon Issue
* BO
* HOL 

	+ Access Another Application

* TC => Menu
* TC => Quick Start Button
* TC => FIT => Menu
* TC corner case :

	+ Leave or End conference when the running application dialog show
	+ Role Change

Key note
--------

* CTCUIMgr::OnApplication
* CTCBOUIMgr::OnApplicationBO
* CTCBOSessionMgr::CreateBOShareSession


Test Env
--------

* T30.1 site In VSCM
  
  + Nick Zhang
  + http://t2web1.qa.webex.com/got2wdt30  nick/P@ss123
  
* T30 Out of VSCM
  
  + Super Admin
  + https://hasuper.qa.webex.com/  nick/nickpass
  + Normal Site: nick30sp
  + http://nick30sp.qa.webex.com/  nick/pass
  
Wiki
----

* http://wikicentral.cisco.com/display/PROJECT/SC+Client+Knowledge+Transfer
* http://wikicentral.cisco.com/display/ASDS/WIN10-SC
* http://wikicentral.cisco.com/display/GROUP/T30.2
* win10 env https://csg-hgh-rapid2.cisco.com/

Recording
---------

* https://ha3web.qa.webex.com/nick30/ldr.php?RCID=8d2eb11b29f3c4c4704789def23c29fe

Rally
-----

* Prepare Env & Fix Build Issue : 6H
* Study TC Code : 6H
* TC Coding & Debug : 12H
* BO Coding & Debug : 6H
* HOL Coding & Debug : 12H
* Self Test & Fix : 12H


