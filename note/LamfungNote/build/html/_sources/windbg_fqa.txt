Windbg
======

#. symchk.exe
#. symstore.exe

Frequent used command
---------------------

#. !sym noisy
#. ld *
	+ load all symbols
#. !wow64exts.sw
#. !analyze -v
#. kp or kP
#. ~* kv
#. lm
	+ lm
		- show all modules and symbols
	+ lma address
		- Specifies an address that contained in this module.
	+ lmvm modulename
		- Get more details of the specify module
	+ lml
		- Displays only loaded modules whose symbol information has been loaded.
#. *.ecxr*
	+ Displays the context record that is associated with the current exception.
#. Output logs to file
	+ .logopen /u /t fullpath
	+ .logclose
#. View the exception context(stored in ContextRecord field)
	+ .cxr dwo(arg1+4);kb
#. Displays the conetnts of an exception record
	+ *.exr -1*
#. View OS version from dump file
	+ vertarget
#. View Critical sestion
	+ RtlEnterCriticalSection
	+ 02 0042efe8 7054edf9 70620e28 0042f024 0042f008 ntdll_77940000!RtlEnterCriticalSection+0x150 (FPO: [Non-Fpo])
	+ !cs 70620e28
#. !uniqstack 
	+  It enumerates all the thread call stacks and eliminates duplicates, so that you can understand at a glance what these hundreds of threads are doing.

Handle
------

#. !handle
	+ Displays information about a handler or handles that one or all processes in the target system own
#. !handle 0 f thread
	+ Displays all the threads handle
#. !handle 0 f semaphore
	+ Displays all the semaphores handle
#. !handle 0 f file
	+ Displays all the file's handle
#. !handle 0 f event
#. !handle 0 f section
#. !handle 0 f directory
#. !handle 0 f mutant
#. !handle 0 f windowstation
#. !handle 0 f key
#. !handle 0 f desktop
#. !handle 0 f iocompletion
#. !handle 0 f timer
#. !handle 0 f tpworkerfactory

Thread
------

#. Switch thread
	+ ~<thread number>s (e.g. ~21s to switch to thread 21)
	+ ~~[thread id]s (e.g. ~~[1de4]s to switch to thread 1de4)
#. ~
	+ Display status all threads in the current process
#. .ttime
	+ Show current thread time info
#. !runaway 7
	+ Show all the threads of current process time info with 3 format
#. dt nt!_TEB @$teb
	+ Display the complete TEB structure

Frame
-----

#. How to switch frame
	+ kn
		- .frame N (e.g. .frame 3)
	+ .frame @$frame-1 or .frame @$frame+1
	+ .f- or .f+
	+ https://blogs.msdn.microsoft.com/doronh/2006/07/21/debuger-commands-stack-frame-navigation-that-makes-life-easier/
	


WebEx PDB file
--------------

* Train Symbol files
	#. http://ccatg-build2.cisco.com/cirepo/Train/
	#. http://ccatg-build2.cisco.com/cirepo/artifacts/
* PDB Symbol Server
	#. http://10.194.242.175/er
	#. http://10.194.242.175/daily

Detail for call stack
---------------------

#. EBP
	+ The place where EBP refers to is really the Data sections of the memory. You can read and write to it.
#. RetAddr
	+ The return address would point to the code sections of the memory. This portion is read-only.

Load Library failure
--------------------

#. Config gflags
	+ cd %programdata%/WebEx/T31_UMC
	+ gflags.exe -i atmgr.exe +sls
#. Start MC meeting and kill atmgr.exe
#. Use WinDbg to start meeting
	+ Windbg - Open executable - OK
	+ %programdata%/WebEx/T31_UMC/atmgr.exe /mcstd ..\%AppData%\LocalLow\WebEx
#. 0:000 g
#. Clear gflags trace
	+ gflags -i atmgr.exe -sls

80000003 issue
--------------

#. Hardcode interrupt request, like: __asm int 3 (ASM), System.Diagnostics.Debugger.Break (C#), DebugBreak() (WinAPI). 
#. OS enable memory runtime check, like Application Verifier can trigger after heap corruption, memory overrun. 
#. Compiler can have some configuration to enble what should be filled for the uninitialized memory block and end of function(blank area, after retun..). 
   For example, Microsoft VC complier can fill 0xCC if enable /GZ. 0xCC is actually a opcode of __asm int 3
#. http://stackoverflow.com/questions/3306235/what-is-the-break-instruction-exception-in-windbg
#. RtlEnterCriticalSection
	+ http://stackoverflow.com/questions/26573238/windbg-how-to-read-the-locks-output


Reference
---------

#. Symbols loading
	+ !sym noisy
	+ http://www.technlg.net/windows/symbol-server-path-windbg-debugging/
#. http://www.godevtool.com/Other/pdb.htm
#. http://www.debuginfo.com/tools/chkmatch.html
#. https://log0.wordpress.com/2008/12/05/how-to-debug-a-stack-overflow-for-beginners/
#. Dump Analysis Via WinDbg
	+ https://www.nicologies.tk/posts/DumpAnalysisViaWinDbg
#. How to switch to 32bit mode when you use windbg to debug a dump of a 32bit application running on an x64 operating system.
	+ https://blogs.msdn.microsoft.com/msdnforum/2010/03/14/how-do-i-switch-to-32bit-mode-when-i-use-windbg-to-debug-a-dump-of-a-32bit-application-running-on-an-x64-machine/
#. kernel32!UnhandledExceptionFilter
	+ www.debuginfo.com/articles/easywindbg2.html
#. Deep Dive into Process Environment Block with Windbg
	+ http://garage4hackers.com/showthread.php?t=1902
#. Why don’t critical sections work cross process?
	+ https://blogs.msdn.microsoft.com/larryosterman/2005/08/24/why-dont-critical-sections-work-cross-process/
#. Obscure WinDbg Commands
	+ http://blogs.microsoft.co.il/sasha/2013/08/12/obscure-windbg-commands-part-1/





