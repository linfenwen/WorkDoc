import sys
import os
from subprocess import Popen, PIPE




def executeCmd(command, args=None) :
    try:
        if None == command :
            print("executeCmd command is None")
            return None
        
        cmd = None
        if None == args :
            cmd = command
        else :
            if isinstance(args, list) :
                cmd = command + ' ' + ' '.join(args)
            else :
                cmd = '%s %s' %(command, args)
        
        print(cmd, command, type(args))
        
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        
        if 0 != p.returncode :
            print('returncode: %s error:%s' %(p.returncode, err))
            return None
        
        return out
    except Exception, e:
        print("executeCmd Exception", e, command,args)
        return None


def git(args) :
    try:
        out = executeCmd('git', args)
        return out
    except Exception, e:
        print("git Exception", e)
        return None


# ?? ../029/anyone_can_share_action_state.svg
def GetUnCommitedFiles(strFiles) :
    try:
        if None == strFiles :
            print("GetUnCommitedFiles strFiles is None")
            return None
        
        strBaseDir = '/Users/lawen/workspace/WebEx/'
        retFileList = []
        fileList = strFiles.split('\n')
        for file in fileList :
            f1 = file[3:]
            if (f1.rfind('.uml') >= 0 ) or (f1.rfind('.dot') >= 0) :
                f2 = strBaseDir + f1[3:]
                retFileList.append(f2)
        
        return retFileList
    except Exception, e:
        print("GetUnCommitedFiles Exception", e)
        return None


def GenerateSvg(strUml) :
    try:
        
        out = None
        retSvg = strUml[0: (len(strUml)-4)] + '.svg'
        
        if (strUml.rfind('.dot') >= 0 ) :
            cmd = 'dot %s -Tsvg -o %s' %(strUml, retSvg)
        elif (strUml.rfind('.uml') >= 0 ) :
            cmd = 'java -jar /usr/bin/plantuml.jar -tsvg %s' %(strUml)
        else :
            return None
        
        out = executeCmd(cmd)
        if None == out :
            return None
        
        #print('GenerateSvg',retSvg, type(retSvg))
        return retSvg
    except Exception, e:
        print("GenerateSvg Exception", e)
        return None


def CopyFile(strSrcFile, strDestFolder) :
    try:
        #print(strSrcFile, strDestFolder)
        ret = executeCmd('cp', '"%s" "%s"' %(strSrcFile, strDestFolder))
        if None == ret :
            return False
        
        return True
    except Exception, e:
        print("CopyFile Exception", e)
        return False


def BuildSvgs(strFileList) :
    try:
        nCount = 0
        strDestFolder = '%s' %("/Users/lawen/workspace/note/Lamfung Note/source/_static")
        for file in strFileList :
            strSvg = GenerateSvg(file)
            nCount += CopyFile(strSvg, strDestFolder)
        
        print(nCount)
        return True
    except Exception, e:
        print("BuildSvgs Exception", e)
        return None


def BuildDocument() :
    print("BuildDocument")
    curWorkDir = os.getcwd()
    try:
        #print(curWorkDir)
        newWorkDir = "/Users/lawen/workspace/note/Lamfung Note"
        os.chdir(newWorkDir)
        print(os.getcwd())
        ret = executeCmd('make html')
        if None == ret :
            print("BuildDocument ret is None")
            os.chdir(curWorkDir)
            return None
        
        os.chdir(curWorkDir)
        print(os.getcwd())
        return True
    except Exception, e:
        print("BuildDocument Exception", e)
        os.chdir(curWorkDir)
        return None


if __name__ == '__main__' :
    try:
        args = sys.argv[1:]
        ret = git(args)
        
        print("aa",ret)
        fileList = GetUnCommitedFiles(ret)
        #print(fileList)
        BuildSvgs(fileList)
        BuildDocument()
    except Exception, e:
        print("__main__ Exception", e)
        sys.exit(-1)