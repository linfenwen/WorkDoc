UnSafe C Relevant Issues
========================

1. **UnSafeC Functions & Original Safe C Solution**

.. csv-table:: UnSafeC Functions & Original Safe C Solution
   :header: "UnSafe C Functions", "Safe C Functions", "UnSafe C Head File", "Safe C Head File"
   :widths: 5, 5, 10, 10

   "vsprintf", "vsprintf_s", "tchar.h", "tchar.h"
   "vswprintf", "vswprintf_s", "tchar.h", "tchar.h"
   "_vstprintf", "_vstprintf_s", "tchar.h", "tchar.h"
   "strtok", "strtok_s", "tchar.h", "tchar.h"
   "wcstok", "wcstok_s", "tchar.h", "tchar.h"
   "_tcstok", "_tcstok_s", "tchar.h", "tchar.h"
   "strcat", "strcat_s", "tchar.h", "tchar.h"
   "wcscat", "wcscat_s", "tchar.h", "tchar.h"
   "_tcscat", "_tcscat_s", "tchar.h", "tchar.h"
   "strncat", "strncat_s", "tchar.h", "tchar.h"
   "wcsncat", "wcsncat_s", "tchar.h", "tchar.h"
   "_tcsnccat", "_tcsncat_s", "tchar.h", "tchar.h"
   "strcpy", "strcpy_s", "tchar.h", "tchar.h"
   "wcscpy", "wcscpy_s", "tchar.h", "tchar.h"
   "_tcscpy", "_tcscpy_s", "tchar.h", "tchar.h"
   "strncpy", "strncpy_s", "tchar.h", "tchar.h"
   "wcsncpy", "wcsncpy_s", "tchar.h", "tchar.h"
   "_tcsncpy", "_tcsncpy_s", "tchar.h", "tchar.h"
   "memcpy", "memcpy_s", "string.h", "tchar.h"
   "memmove", "memmove_s", "string.h", "tchar.h"
   "memset", "SecureZeroMemory", "string.h", "WinBase.h"


2. **UnSafeC Functions & Cisco Safe C Solution**

.. csv-table:: UnSafeC Functions & Cisco Safe C Solution
   :header: "UnSafe C Functions", "Cisco Safe C Functions", "UnSafe C Head File", "Safe C Head File"
   :widths: 5, 5, 10, 10

   "strspn", "strspn_s", "tchar.h", "safe_str_lib.h"
   "wcsspn", "", "tchar.h", ""
   "_tcsspn", "", "tchar.h", ""
   "strcspn", "strcspn_s", "tchar.h", "safe_str_lib.h"
   "wcscspn", "", "tchar.h", ""
   "_tcscspn", "", "tchar.h", ""
   "strpbrk", "strpbrk_s", "tchar.h", "safe_str_lib.h"
   "wcspbrk", "", "tchar.h", ""
   "_tcspbrk", "", "tchar.h", ""
   "memcmp", "memcmp_s", "string.h", "safe_mem_lib.h"


3. **UnSafeC Functions & STL Solution**

.. csv-table:: UnSafeC Functions & STL Solution
   :header: "UnSafe Functions", "Safe Functions", "Comments"
   :widths: 5, 10, 10

   "strstr", "std::string str; str.find", "tchar.h"
   "wcsstr", "std::wstring str; str.find", "tchar.h"
   "_tcsstr", "std::basic_string<TCHAR> str; str.find", "tchar.h"
   "strlen", "std::string str; str.size", "tchar.h"
   "wcslen", "std::wstring str; str.size", "tchar.h"
   "_tcslen", "std::basic_string<TCHAR> str; str.size", "tchar.h"
   "strchr", "", "tchar.h"
   "wcschr", "", "tchar.h"
   "_tcschr", "", "tchar.h"
   "strrchr", "", "tchar.h"
   "wcsrchr", "", "tchar.h"
   "_tcsrchr", "", "tchar.h"
   "strcmp", "", "tchar.h"
   "wcscmp", "", "tchar.h"
   "_tcscmp", "", "tchar.h"
   "strncmp", "", "tchar.h"
   "wcsncmp", "", "tchar.h"
   "_tcsncmp", "", "tchar.h"


4. **UnSafeC Functions & No Solution**

.. csv-table:: UnSafeC Functions & No Solution
   :header: "UnSafe C Functions", "Safe C Functions", "UnSafe C Head File", "Safe C Head File"
   :widths: 5, 5, 10, 10

   "strcoll", "", "tchar.h"
   "wcscoll", "", "tchar.h"
   "_tcscoll", "", "tchar.h"
   "strxfrm", "", "tchar.h"
   "wcsxfrm", "", "tchar.h"
   "_tcsxfrm", "", "tchar.h"



Env
---

#. Citrix XenApp7.5 for Windows 2008R2: 10.224.39.223, 


Reference
---------

#. https://github.com/coruus/safeclib
#. http://wikicentral.cisco.com/display/CSGSEC/Safe+C+Lib+Usage+Quick+Guide
#. https://msdn.microsoft.com/en-us/library/bb288454.aspx
#. http://www.cplusplus.com
#. https://www-01.ibm.com/support/knowledgecenter/ssw_aix_61/com.ibm.aix.basetrf2/strlen.htm
#. http://www.viva64.com/en/examples/
#. https://sourceware.org/bugzilla/show_bug.cgi?id=14552
#. http://www.opensource.apple.com/source/Libc/Libc-1082.20.4/
#. http://www.plauger.com/
#. https://www.gnu.org/software/libc/manual/html_mono/libc.html#Memory-Concepts



