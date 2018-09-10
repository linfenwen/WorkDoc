VSCM PC Lists
=============


#. https://10.224.214.36:9443/vsphere-client/


Win8.1
------

#. Win8.1
	+ DNS Name: HGHVSCMW81-C047.prime.cisco.com
	+ IP : 10.224.172.102

#. Win8.0
	+ HGHVSCMW8-C021
	+ IP : 10.224.172.62

#. Win7-TC
	+ DNS Name: HGHVSCMW7-TC029
	+ 10.224.170.84

#. Win10
	+ https://10.224.214.37/vsphere-client/
	+ DNS Name: EngPri_w10_A
	+ 10.224.202.52
	+ User Name and PW: .\lawen | Linfeng1984
Others
------

#. 10.224.170.71
#. 10.224.172.121
#. 10.224.172.57

WebEx artifacts server decommission From Quick
----------------------------------------------

::
 
 We’ve planned this since last December, as part of Infosec requirement we decommission the old WebEx artifacts server:
 http://ccatg-build2.cisco.com/cirepo/artifacts/
 
 The replacement new server with https and CEC authentication enabled has been live for months:
 https://cctg-cirepo.cisco.com/cirepo/
  
 If you are current using our old artifacts server, please switch to the new one with CEC login.
 If you have any question, please contact WebExCI team.
 
manually update the artifices link on the build tools
-----------------------------------------------------

#. file://hzsmb.qa.webex.com//Anonymous//clientdev//GitDependenciesTool//
#. https://cctg-cirepo.cisco.com//cirepo//artifacts//32.12.0//
#. https://cctg-cirepo.cisco.com//cirepo//artifacts//buildtools//