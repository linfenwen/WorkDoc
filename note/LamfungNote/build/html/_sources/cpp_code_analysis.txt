C++ Code Analysis
==================

Windows deprecated API
----------------------

#. Using *GetTickCount64* to replace *GetTickCount*
	+ Reason: GetTickCount overflows roughly every 49 days. 
	+ Code that does not take that into account can loop indefinitely.  
	+ GetTickCount64 operates on 64 bit values and does not have that problem

JME
---

#. Crash Issue
	+ CJmeUpdateMgrImpl::pickNextPendingSection
	+ *CJmeUpdateMgrImpl::hasPendingSection*
#. Memory Leak
	+ *CJmeClientFileListImpl::ParseFileItemHash*
	+ CJmeClientFileListImpl::ParseFileListItem



