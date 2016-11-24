WebEx Meeting Folder
====================

Where to change the installation folder
---------------------------------------

* For Windows

  + https://wwwin-svn-sjc-2.cisco.com/csg/BuildTools/trunk/build/ec/train/pageclient/T30L10N/client/allpackaging.xml
  
* For Mac

  + https://wwwin-svn-sjc-2.cisco.com/csg/BuildTools/trunk/build/ec/train/pageclient/T30L10N/mac/allprojects.xml
  
T30 Installation folder changes
-------------------------------

We will change Cisco WebEx meeting folder name from digital number to string in T30 as following:

.. csv-table::
 :header: "Meeting Type", "Folder Name"
 :widths: 100, 50
 
 "Meeting Center", "T30_MC"
 "Event Center", "T30_EC"
 "Training Center", "T30_TC"
 "Support Center (Start a support session)", "T30_SC"
 "Support Center (Join a support session)", "T30_SCC"
 

SC folder special logic
-----------------------

Let's use T29 as example::

 Checked with Morgan Fang, SC use two folders, I will show you the details with T29 as example:
    1. For "Start a support session" case, will use "1530" as work directory
    2. For "Join a support session"case, will use "1532" as work directory
    
    The issue is,  after we changed SC folder (from 1530 to T30_SC), all "Start a support session" and "Join a support session" will use "T30_SC" as work directory.
    I had talked with Morgan, and he said there is a logic on the page:
    1.  If the page found the meeting is SC and the type is "Join a support session"
    2. Then it will add 2 (1530 + 2 = 1532) to generate "Join a support session" work directory
 
   So we need the page team help to correct this logic, we suggest them use the below logic to distinguish "Start a support session" and "Join a support session":
   1. If the page found the meeting is SC and the type is "Join a support session"
   2. Use "Start a support session" work directory add "C" to generate "Join a support session" work directory, use "T30_SC" as example, 
       the "Join a support session" work directory will be "T30_SCC"

