Tiger Windows Meeting Client Task
=================================

CAP
---

#. GE
#. P&G
#. BOEING
#. GM
#. gosite

CFD bug
-------

All customer found defects have to be resolved in 21 days. There is no approval needed.
But the CFD bug needs to be added to the release wiki, so that QA can verify it. We ask
dev to provide the following items in CDETS.

	#. 3W analysis
	#. Attached code diff
	#. Code reviewer name
	#. Fill in Customer Release note Enclosure (RNE)



Main Component Own
--------------------

#. HZ
	+ DM 
		- Jack Zhang
	+ SM 
		- Danie Du
	+ Win
		- Baifer Yu
		- Lamfung Wen
	+ PD 
		- Cellion Ye
	+ AA/RA 
		- Tom Yan
	+ Mac
		- Wu Xi
	+ MMP 
		- Xinghai Li
	+ Eureka
		- Witty Xu
		- Oliver Zhu
	+ WME Video
		- Andrew Shen
	+ WME Audio
		- Keith
	+ TA / TS / Tahoe
		- Bin Xu
#. HF
	+ DM
		- Paul Chen
	+ Page
		- Michael Yang 
		- Keanu Cao
		- Phoebe Yan
	+ QA
		- Chaonan Huang
	+ Engineer 
		- Carl Zhu
		- Dean Chen
	+ Flash Client
		- Winter Yu
#. HZ MSO
	+ Sean
	+ George Ying
	+ Allison Guo
	+ Barton Yang
	+ Jason Gao
	+ Aier Huang





WIKI
----

#. Check Customer tickets
	+ HD tickets
		- https://cccm.my.salesforce.com/console
	+ WO Tickets
		- http://csgitsm.webex.com
	+ Webex ticket track
		- 10.224.17.80:8181/plist/html_index.html

#. mats :   
	+ https://mats.webex.com

#. tiger team:  
	https://wiki.cisco.com/display/LDU2/Tiger

#. CFD bug: 
	http://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=yuzchen-0

#. As:
	https://wiki.cisco.com/display/ASDS/513-+How+to+Disable+Indicator 

#. MTA: 
	https://wiki.cisco.com/display/CSGMSO/How+to+gather+more+computer+information+via+MTA+tool
	
	https://cisco.jiveon.com/docs/DOC-1075947

#. crash:
	https://wiki.cisco.com/display/CSGMSO/Windows.Crash+T31+wbxmgr.dll+OLEACC.dl+interacting+with+Participants+panel

#. code diff:
	https://ccollab.cisco.com:8080/uiji

#. webex utilities:
	https://help.webex.com/docs/DOC-2672

	
#. CFD status
	https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=yuzchen-0


* \\10.224.188.12\csg-hgh-VSCM-Vanoris\baiferYu\project_task_\rt
* rt_note_share.txt
* rt case.xlsx

WinDebug & symbol info
----------------------

#. symbol
	+ SRV*c:\MySymbols*http://msdl.microsoft.com/download/symbols;
	+ srv*c:\sym* http://10.194.242.175/daily; srv*c:\sym* http://10.194.242.175/er;

#. 64bit dump to 32 bit dump
	!wow64exts.sw

#. dump file format

	+ .dmp 
	+ mini dump
	+ full dump

#. default debugger

	::
	 
	 windbg.exe -I 
	 
	 or
	 
	 url: https://msdn.microsoft.com/en-us/library/windows/desktop/bb204634(v=vs.85).aspx
	 
	 To set a debugger as the postmortem debugger
	 Go to the following registry key:
	 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug
	 
	 Add or edit the Debugger value, using a REG_SZ string that specifies the command line for the debugger.
	 The string should include the fully qualified path to the debugger executable. Indicate the process ID and event handle with "%ld" parameters to the debugger command line. Different debuggers may have their own parameter syntaxes for indicating these values. When the debugger is invoked, the first "%ld" is replaced with the process ID and the second "%ld" is replaced with the event handle.
	 
	 The following text is an example of how to setup up WinDbg as the debugger.
	 "C:\debuggers\windbg.exe" -p %ld -e %ld -g


KB
--

#. wininet
#. Restful
#. SIP
#. RTP
#. SDP
#. PDU









