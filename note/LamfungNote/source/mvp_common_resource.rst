MVP Common Resource
===================

Windows Topic
-------------

#. How To Insert TrustInfo into Manifest to Identify the Application Security Requirements on Windows Vista

   http://www.restuner.com/howto-insert-trust-info-manifest.htm 

#. How to remote debug with VS2013

   http://blog.sina.com.cn/s/blog_a459dcf5010153o7.html

#. novtable
	+ https://msdn.microsoft.com/en-us/library/k13k85ky(v=vs.71).aspx
	+ http://xuxueliang.blog.51cto.com/5576502/1393366
#. region, endregion
	+ https://msdn.microsoft.com/en-us/library/b6xkz944.aspx
	+ http://blog.csdn.net/kencaber/article/details/51525991
#. learncpp
	+ http://www.learncpp.com/cpp-tutorial/125-the-virtual-table/
	
#. Determining HResult Error Codes
	+ https://support.microsoft.com/en-us/kb/178081
#. Debugging LoadLibrary Failures
	+ https://blogs.msdn.microsoft.com/junfeng/2006/11/20/debugging-loadlibrary-failures/

#. Software Reverse Engineering Tools
	+ https://www.apriorit.com/dev-blog/366-software-reverse-engineering-tools
#. PDB viewer, cvdump.exe
	+ https://github.com/Microsoft/microsoft-pdb/blob/master/cvdump/cvdump.exe
#. PDB2MAP
	+ dumpbin /map application.exe > application.map
	+ https://stackoverflow.com/questions/2451369/how-to-create-a-map-file-from-a-pdb-file

#. User Mode Callbacks In Windows
	+ http://eugeii.com/posts/user-mode-callbacks-in-windows/
#. C++ Linker
	+ http://www.airs.com/blog/archives/38
#. C++ PLT & GOT
	+ https://www.technovelty.org/linux/plt-and-got-the-key-to-code-sharing-and-dynamic-libraries.html
#. sxstrace.exe
	+ The application has failed to start because its side-by-side configuration is incorrect
		- https://blogs.msdn.microsoft.com/cesardelatorre/2011/03/27/the-application-has-failed-to-start-because-its-side-by-side-configuration-is-incorrect-error-related-to-mmc-exe-programs-and-weird-cause-simple-solution/
	+ https://knowledge.autodesk.com/support/3ds-max/troubleshooting/caas/sfdcarticles/sfdcarticles/The-application-has-failed-to-start-because-its-side-by-side-configuration-is-incorrect.html
	+ sxstrace.exe usage
		- Before running your application, run sxstrace in trace mode:
     	- sxstrace.exe Trace -logfile:C:\MySxSTrace.log
    	- Reproduce the error by starting your application
    	- Now stop the trace by using the below command
     	- sxstrace.exe Parse -logfile:C:\MySxSTrace.log -outfile:C:\MySxSTrace.txt
#. Monitoring Silent Process Exit
	+ https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/registry-entries-for-silent-process-exit
#. Find out who killed a process in Windows
	+ http://techibee.com/sysadmins/find-out-who-killed-a-process-in-windows/2286
	
#. Valgrind
	+ http://valgrind.org/docs/manual/cl-manual.html

#. WinObj, Kernel Object
	+ https://www.remkoweijnen.nl/blog/2009/01/27/accessing-kernel-objects-in-other-sessions/
	+ https://msdn.microsoft.com/en-us/library/aa382954(VS.85).aspx

#. How to view the environment variables of a process
	+ View environment variables of a process in the visual studio debugger
		- https://blogs.msdn.microsoft.com/habibh/2009/06/08/how-to-display-the-environment-variables-for-a-process-in-the-visual-studio-debugger/
	+ View environment variables of a process in **Process Explorer**

#. Process and Environment
	+ https://www.ics.com/designpatterns/book/environment.html

#. WMIC (Windows Management Instrumentation)
	+ http://blog.csdn.net/hxh129/article/details/8721406
	+ wmic.exe is a powerful command line utility for interacting with WMI. 
	+ https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf
	+ http://la.trendmicro.com/media/misc/understanding-wmi-malware-research-paper-en.pdf
	
#. mock objects
	+ http://clean-cpp.org/mock-objects/
	
#. IE Protect Mode
	+ https://blogs.msdn.microsoft.com/ieinternals/2009/11/30/understanding-the-protected-mode-elevation-dialog/

#. Count Code Line
	+ http://cloc.sourceforge.net/
	
Common Topic
------------

#. Character set, like Unicode, UTF-8, ANSI ...
	https://blogs.msdn.microsoft.com/vcblog/2016/02/22/new-options-for-managing-character-sets-in-the-microsoft-cc-compiler/
#. How to quickly and effectively read other peoples code
	+ https://selftaughtcoders.com/how-to-quickly-and-effectively-read-other-peoples-code/
	+ http://programmers.stackexchange.com/questions/6395/how-do-you-dive-into-large-code-bases
#. Class relationship 
	+ http://creately.com/blog/diagrams/class-diagram-relationships/
#. Online draw chart
	https://www.draw.io/#G0B2Ykfab9ktB2Mkk3QkFkWUxMSnc
#. Lambdas VS Closures
	http://scottmeyers.blogspot.com/2013/05/lambdas-vs-closures.html
	http://www.aristeia.com/
#. www.devarticles.com
	http://www.devarticles.com/c/a/Cplusplus/C-plus-plus-In-Theory-The-Singleton-Pattern-Part-I/4/
#. Which is fastest: read, fread, ifstream or mmap?
	http://lemire.me/blog/2012/06/26/which-is-fastest-read-fread-ifstream-or-mmap/
#. Displaying a Critical Section
	https://msdn.microsoft.com/fr-fr/library/ff541979(v=vs.85).aspx
#. Hacker Rank
	https://www.hackerrank.com
#. BFCP
	https://tools.ietf.org/html/rfc4582#page-4
#. WPAD, Web Proxy Auto-Discovery protocol
	+ http://go.microsoft.com/fwlink/p/?linkid=392029
	+ https://tools.ietf.org/html/draft-ietf-wrec-wpad-01
#. Jenkins
	https://jenkins.io/index.html
#. Online x86 / x64 Assembler and Disassembler
	+ https://defuse.ca/online-x86-assembler.htm
	+ https://www.nayuki.io/page/a-fundamental-introduction-to-x86-assembly-programming
#. X86 opcode reference
	+ http://ref.x86asm.net/coder32.html
#. Intel developer site
	+ https://software.intel.com/en-us/search/site/language/en?query=x86
#. princeton course
	+ http://www.cs.princeton.edu/courses/archive/spr11/cos217/lectures/
#. x86 Architecture Overview
	+ http://cs.lmu.edu/~ray/notes/x86overview/
#. windbg-quickstart-guide
	+ https://blogs.msdn.microsoft.com/rihamselim/2012/02/25/windbg-quickstart-guide-part-1/
#. C++ Standards Committee Papers
	+ http://www.open-std.org/jtc1/sc22/wg21/docs/papers/?X-OpenDNS-Session=_dc7b20f201c5b0477e0a2f005ce7bc4ac6c39270ed45_e92cef02_
#. International Country Calling Codes and International Dialing Prefixes
	http://www.nationsonline.org/oneworld/international-calling-codes.htm
#. Understanding lvalues and rvalues in C and C++
	https://eli.thegreenplace.net/2011/12/15/understanding-lvalues-and-rvalues-in-c-and-c

#. c++11
	http://thispointer.com/
	
#. Out of Memory
	http://outofmemory.cn/#csdn
	
#. PDF books
	+ https://doc.lagout.org
	
#. The Secret behind the Single Responsibility Principle
	+ https://hackernoon.com/the-secret-behind-the-single-responsibility-principle-e2f3692bae25
	
#. Inheritance is evil. Stop using it.
	+ https://codeburst.io/inheritance-is-evil-stop-using-it-6c4f1caf5117
	
#. Do you need a Dependency Injection Container?
	+ http://fabien.potencier.org/do-you-need-a-dependency-injection-container.html
	
#. A simple C++11 IoC container that's all you need
	+ http://turncoder.blogspot.com/2014/02/a-simple-c11-ioc-container-thats-all.html

#. Inversion of control
	+ https://en.wikipedia.org/wiki/Inversion_of_control
	
#. Software People Inspiring
	+ http://www.codemanship.co.uk/parlezuml/blog/?postid=934 
	
#. Add coroutine task type
	+ http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1056r0.html
	
#. BFCP
	+ https://tools.ietf.org/html/rfc4582
	
#. Gmock Enhancements: Mocking Global Functions and Methods with more than 10 Arguments
	+ https://www.apriorit.com/dev-blog/468-gmock-enchancements
	
#. C function UT
	+ https://accu.org/index.php/journals/2062
	
#. Google Mock进阶篇
	+ http://www.voidcn.com/article/p-hzghngiz-he.html
	+ https://onedrive.live.com/redir?resid=4C6FDC828365B80E%2128191&authkey=%21AtpjZailG7DIcVg&page=View&wd=target%28Design%20notes.one%7Ce625ee03-bb70-3e4d-b6a2-6eea23277768%2FCan%28if%20can%2C%20how%5C%29%20we%20mock%20non-%7Cdd2d9216-c645-bc4d-a0a5-549489f62b0e%2F%29

#. Unit Test Framework
	+ http://www.throwtheswitch.org/comparison-of-unit-test-frameworks
	
#. How to fake a singleton in C
	+ https://helpercode.com/2015/09/16/how-to-fake-a-singleton-in-c/
	
#. http://blog.guorongfei.com/2016/08/22/cpp-unit-test-catch/
	+ http://blog.guorongfei.com/2016/08/22/cpp-unit-test-catch/
	
#. Mockcpp
	+ https://bitbucket.org/godsme/mockcpp/src/06ad37ddc45cbbc5d5e42db925f72ebf9faaa0d4/src/?at=default	

#. Override, Overload, Overwrite
	+ https://wuciawe.github.io/object%20oriented/2014/08/29/override-overload-overwrite.html

#. C++ Memory access
	+ http://www.c-jump.com/bcc/c155c/MemAccess/MemAccess.html

#. Memory Region Attributes
	+ https://sourceware.org/gdb/onlinedocs/gdb/Memory-Region-Attributes.html

#. c++ blogs
	+ https://shaharmike.com/cpp/shared-ptr/

#. C++ Performance Benchmark
	+ http://blog.davidecoppola.com/2014/05/cpp-benchmarks-vector-vs-list-vs-deque/

#. Architecture Style
	+ https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ee658117(v=pandp.10)

#. Intel Threading Building Blocks Documentation 
	+ https://software.intel.com/en-us/tbb-documentation

#. Architecture Style And Design 
	+ https://www.tutorialspoint.com/software_architecture_design/introduction.htm

Java
----

#. 8 Graphs to understand Java
	+ http://www.importnew.com/11725.html
	
#. Java 8 User Guide
	+ http://www.cnblogs.com/ios9/p/7518519.html#_label1

#. Java.io.File
	+ http://developer.classpath.org/doc/java/io/File-source.html

#. Java System Properties
	+ https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html
	
#. System.out.println
	+ https://my.oschina.net/zjllovecode/blog/1538380
	+ https://javapapers.com/core-java/system-out-println/
	
#. Java.lang source code
	+ http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/lang

#. Java Example
	+ https://github.com/eugenp/tutorials/tree/master/core-java-io

#. Java World
	+ https://www.javaworld.com/article/2077496/testing-debugging/java-tip-130--do-you-know-your-data-size-.html

#. C like sizeof
	+ https://dzone.com/articles/how-to-write-a-c-like-sizeof-function-in-java

#. Java Performance
	+ http://java-performance.info/overview-of-memory-saving-techniques-java/
	
#. Java Unit Test
	+ https://zeroturnaround.com/rebellabs/how-to-mock-up-your-unit-test-environment-to-create-alternate-realities/

#. Java Test
	+ http://www.pskills.org/corejava.jsp
	
#. SpringFramework ClassPathXmlApplicationContext
	+ IOException parsing XML
	+ http://www.voidcn.com/article/p-uqvudlxb-bqu.html
	
#. What is Spring Framework
	+ https://www.edureka.co/blog/what-is-spring-framework/

#. Java mock introduction
	+ https://dzone.com/refcardz/mockito?chapter=1 
	
#. Java online regular
	+ http://www.regexplanet.com/advanced/java/index.html
	
#. Java mock static method, mock new object
	+ https://www.ibm.com/developerworks/cn/java/j-lo-powermock/index.html
	+ https://stackoverflow.com/questions/10327612/mock-static-methods-from-multiple-class-using-powermock
	+ https://automationrhapsody.com/mock-new-object-creation-powermock/
	+ https://examples.javacodegeeks.com/core-java/mockito/mockito-mock-static-method-example/
	+ https://examples.javacodegeeks.com/core-java/mockito/powermock-mockito-integration-example/
	+ https://www.jianshu.com/p/776871af8f82
	+ https://blog.csdn.net/Extra_warrior/article/details/53895524

#. Java Thread
	+ http://wiki.jikexueyuan.com/project/java-concurrent/creating-and-starting-java-threads.html

#. Modern CPP
	+ http://www.modernescpp.com/index.php/c-is-still-lazy

#. Web Based Code Browser
	+ https://code.woboq.org/qt5/include/c++/8.2.1/backward/auto_ptr.h.html#std::auto_ptr

Big Data, Data Analyze
----------------------

#. HQL
	+ https://www.oreilly.com/library/view/programming-hive/9781449326944/ch04.html

Design Priciple
---------------	

#. SOLID principle
	+ https://medium.com/@linfengwen

#. SLAP
	+ https://www.slideshare.net/skarpushin/solid-ood-dry

#. SOLID principle (plus DRY, YAGNI, KISS and other YAA)
	+ https://siderite.blogspot.com/2017/02/solid-principles-plus-dry-yagni-kiss-final.html

#. SOLID and DRY
	+ https://www.codeproject.com/Articles/36712/SOLID-and-DRY
	
#. DI vs DIP vs IoC
	+ http://lotabout.me/2018/Dependency-Inversion-Principle/
	+ http://www.tutorialsteacher.com/ioc/introduction
	+ https://coolshell.cn/articles/9949.html
	
#. Design Principle vs Design Pattern
	+ http://www.tutorialsteacher.com/articles/difference-between-design-principle-and-design-pattern
	
#. Service Locator Pattern
	+ http://gameprogrammingpatterns.com/service-locator.html

#. People Projects And Patterns
	+ http://wiki.c2.com/
	
#. The original of typename
	+ http://feihu.me/blog/2014/the-origin-and-usage-of-typename/
	
#. Object Oriented Design
	+ https://www.geeksforgeeks.org/null-object-design-pattern/
	+ https://www.tutorialspoint.com/design_pattern/null_object_pattern.htm
	+ https://sourcemaking.com/design_patterns/null_object
	+ https://www.oodesign.com/
		- Singleton
		- Factory
		- Factory Method
		- ...

#. MVC
	+ http://www.moock.org/lectures/mvc/

#. List many design principle
	+ https://www.ithome.com.tw/voice/97462
	+ Like Simple code
    	- Passes all the tests.
		- Expresses every idea that we need to express.
		- Says everything OnceAndOnlyOnce.
		- Has no superfluous parts. 

#. MVC, MVP, MVVM
	+ https://draveness.me/mvx

#. Machine Learning and Deep Learning
	+ https://yq.aliyun.com/articles/212563?spm=a2c4e.11153940.blogcont212311.12.4f8937eeMBlPk7

#. C++11 Features
	+ https://www.kancloud.cn/wangshubo1989/new-characteristics/99705

#. C++11 vs C++17 Performance
	https://www.bfilipek.com/2018/11/parallel-alg-perf.html

Log system
----------

#. Understand Log Theory
	+ http://feihu.me/blog/2014/insight-into-log/

Digital Signature vs Digital Certification
------------------------------------------

#. Windows View Local Installed Certification
	+ certmgr.msc

Open Source
-----------

#. Libc
	http://www.opensource.apple.com/source/Libc/Libc-167/gen.subproj/i386.subproj/
#. BinDiff
	http://www.zynamics.com/bindiff.html
#. Black Duck
	https://www.openhub.net/p/bindiff
#. OpenCV
	http://opencv.org/
#. log4cplus
	https://github.com/log4cplus/log4cplus
#. cflow
	http://www.gnu.org/software/cflow/
#. sonar
	+ https://www.ibm.com/developerworks/cn/java/j-lo-sonar/
	+ git://github.com/SonarSource/sonar.git
#. sonarqube
	+ http://www.sonarqube.org/
	+ http://docs.codehaus.org/display/SONAR/Documentation

#. Top 11 Open Source Test Automation Framework
	+ https://www.joecolantonio.com/automation-testing-framework/

Technical Blog
--------------

#. Computer World
	http://www.computerworld.com/article/3012033/it-skills-training/10-hottest-tech-skills-for-2016.html
#. InfoQ
	http://www.infoq.com/cn/articles?utm_source=infoq&utm_medium=breadcrumbs_feature&utm_campaign=breadcrumbs
#. CoolShell
	http://coolshell.cn/articles/7490.html
#. 云风Blog
	http://blog.codingnow.com/
#. 王银
	http://www.yinwang.org/
#. The Ken Thompson Hack
	http://c2.com/cgi/wiki?TheKenThompsonHack
#. Titus Qian (Cisco WebEx)
	https://www.evernote.com/shard/s164/sh/5142ad64-7100-4d47-8bb1-7a17df7e4e18/01b171d27368b173
#. 伯乐在线
	http://blog.jobbole.com/96225/
#. 牛人博客聚合
	http://www.udpwork.com/item/15211.html
#. 阮一峰的Blog
	http://www.ruanyifeng.com/blog/
#. stackoverflow
	http://stackoverflow.com/
#. Martin Fowler **Aigle** **Refactor**
	http://www.martinfowler.com
#. Design Patterns & Refactoring
	https://sourcemaking.com/design_patterns
#. Software optimization resources
	http://www.agner.org/optimize/
#. http://www.wintellect.com
	http://www.wintellect.com/devcenter/jrobbins/pdb-files-what-every-developer-must-know
#. firefox npapi
	https://developer.mozilla.org/en-US/docs/Plugins/Guide/Plug-in_Development_Overview#Windows_Installation_Using_the_Registry
#. C++11 - the new ISO C++ standard
	http://www.stroustrup.com/C++11FAQ.html
	
#. multi thread paralel computing
	http://www.parallellabs.com
	
	
	
Security Topic
--------------

#. CVE 
	+ https://cve.mitre.org/
#. MSDN
	+ https://msdn.microsoft.com/en-us/library/bb288454.aspx
	+ https://blogs.msdn.microsoft.com/michael_howard/2006/06/12/windows-vista-security-a-bigger-picture/
#. Sourceware Bugzilla
	+ https://sourceware.org/bugzilla/show_bug.cgi?id=16967
#. Static code analyse for C,C++, and C# 
	+ http://www.viva64.com/en/examples/
#. How to disable Address Space Layout Randomization (ASLR)
	https://blogs.msdn.microsoft.com/winsdk/2009/11/30/how-to-disable-address-space-layout-randomization-aslr/
#. Windows ISV Software Security Defenses
	https://msdn.microsoft.com/en-us/library/bb430720.aspx
#. Google Security Blog
	https://security.googleblog.com/2016/03/bindiff-now-available-for-free.html
#. Pwn2Own
	https://en.wikipedia.org/wiki/Pwn2Own
#. **看雪学院**
	www.pediy.com/kssd/pediy08/pediy8-364.htm
#. Cisco WebEx code execution hole
	+ This vulnerability was reported to Cisco by Tavis Ormandy of Google 
	+ https://nakedsecurity.sophos.com/author/pducklin/
	+ https://nakedsecurity.sophos.com/2017/01/26/cisco-webex-code-execution-hole-what-you-need-to-know/
	+ https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170124-webex
	+ https://security.googleblog.com/
	+ https://googleprojectzero.blogspot.com/2016/06/how-to-compromise-enterprise-endpoint.html
	+ http://taviso.decsystem.org/
	+ http://www.pctools.com/security-news/zero-day-vulnerability/
	+ http://www.securityweek.com/cisco-starts-patching-critical-webex-flaw
	+ http://www.zdnet.com/article/code-execution-hole-in-webex-meeting-manager/
	+ https://bugs.chromium.org/p/project-zero/issues/detail?id=1096
	
#. The Art of Unpacking
	+ http://www.youngroe.com/2017/05/23/Learning/The-Art-of-Unpacking/	

#. 逆向工程核心原理
	+ http://www.52bug.cn/%E9%80%86%E5%90%91%E7%B3%BB%E5%88%97/1641.html

	
Assembly Language 
-----------------

#. ODA
	https://www.onlinedisassembler.com/odaweb/1h5lTAyw/0
	
Auto Document
-------------

#. UML
	+ http://plantuml.com
	+ http://plantuml.com/plantuml/form
#. Graphviz dot
	+ http://www.graphviz.org/
	
	
	
Study Track
-----------

#. Microsoft C++ Name Mangling Scheme
	http://mearie.org/documents/mscmangle/
#. Code Quality
	+ Optimizing CPP
		- P125/P165
		- file:///Users/lawen/Downloads/optimizing_cpp.pdf
	+ Tips for Optimizing C/C++ Code
		- P0/P4
		- http://people.cs.clemson.edu/~dhouse/courses/405/papers/optimize.pdf
#. C/C++ Advance Topic
	+ How to get the process resident set size (physical memory use)
		- http://nadeausoftware.com/articles/2012/07/c_c_tip_how_get_process_resident_set_size_physical_memory_use
	+ How to get the physical memory size of a system
		- http://nadeausoftware.com/articles/2012/09/c_c_tip_how_get_physical_memory_size_system
#. Memory Leak
	+ Memory leak analyse base on WinDbg
		- http://www.cppblog.com/weiym/archive/2015/11/15/198109.html#212269
#. Introducing Dynamic Link Libraries
	+ http://www.willus.com/mingw/colinp/win32/dll/intro.html
	+ http://www.willus.com/mingw/colinp/win32/dll/use.html
	+ http://www.iecc.com/linker/
#. RFC Protocol
	+ Hypertext Transfer Protocol Protocol 2 (HTTP/2)
		- https://tools.ietf.org/html/rfc7540
		- https://en.wikipedia.org/wiki/SPDY
		- https://en.wikipedia.org/wiki/HTTP/2
	+ RTP
		- https://datatracker.ietf.org/doc/rfc3550/?include_text=1
	+ RPC
		- https://tools.ietf.org/pdf/rfc5531.pdf
#. Compilers
	+ Compilers: Principles, Technique, and Tools
		- P1/P811
		- http://cs.uccs.edu/~gsc/pub/phd/ftorres/doc/Compiler.pdf
#. How do I execute a string containing Python code in Python?
	http://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
#. How do I get the return value when using Python exec on the code object of a function?
	http://stackoverflow.com/questions/23917776/how-do-i-get-the-return-value-when-using-python-exec-on-the-code-object-of-a-fun
#. **The Object Model**
	https://www.cgl.ucsf.edu/Outreach/pc204/TheObjectModel.pdf
#. **Relationships for object-oriented programming language**
	https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-702.pdf
#. EDA
	http://www.enterpriseintegrationpatterns.com/docs/EDA.pdf

Others
------

#. https://github.com/houshanren/hangzhou_house_knowledge#2018%E6%8B%86%E8%BF%81%E5%A4%A7%E5%B9%95-%E4%B8%BB%E5%9F%8E%E8%A6%81%E6%8B%864%E4%B8%87%E6%88%B7%E3%80%81%E8%90%A7%E5%B1%B18000%E6%88%B7%E3%80%81%E4%B8%B4%E5%AE%891500%E6%88%B7

2016-12-01, Refresh Mac Machine
-------------------------------

#. https://sqbu-github.cisco.com/WebExSquared/
#. http://windbg.info/doc/1-common-cmds.html
#. http://www.cnblogs.com/rolling-stone/p/3244254.html
#. http://www.technlg.net/windows/symbol-server-path-windbg-debugging/
#. www.cplusplus.com
#. cisco.jiveon.com/
#. http://www.cnblogs.com/kissdodog/p/3730598.html
#. tsphybrid.qa.webex.com/wbxadmin
#. http://nadeausoftware.com/articles
#. http://stackoverflow.com/questions/3973582/how-do-i-write-a-utf-8-encoded-string-to-a-file-in-windows-in-c
#. github.com  bindiff
#. http://timsplus.qa.webex.com/TimsPlus/login
#. http://creately.com/blog/diagrams/class-diagram-relationships/
#. http://english.stackexchange.com/
#. http://www.oreilly.com/pub/e/3357
#. https://www.hackerrank.com/
#. http://www.jantar.org/talks/zadarnowski03languages.pdf
#. http://www.ccs.neu.edu/home/matthias/369-s10/Transcript/anf-vs-cps.pdf
#. http://www.forbes.com/
#. http://www.gegeek.com/
#. http://www.gegeek.com/tech_reference/tech_shop_docs/Troubleshooting/Advanced%20Windows%20Debugging.pdf
#. more details please refer to
	+ https://drive.google.com/drive/folders/refresh mac(20161201)















































