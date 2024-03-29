# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:58:55 2019

@author: randerson
"""

import subprocess
from . import setup
class Qxxx:
    @classmethod
    def _cmd_qstat_username(cls, username, verbose):
        command = str(setup.LOCAL_PUTT_EXE) +\
                " -load {} qstat -u {}".format(setup.CLUSTER_NAME, username)
        if verbose: print("qstat command:\n\t{}".format(command))
        return command

    @classmethod
    def _cmd_qstat_pid(cls, pid, verbose):
        command = str(setup.LOCAL_PUTT_EXE) +\
                " -load {} qstat {}".format(setup.CLUSTER_NAME, pid)
        if verbose: print("qstat command:\n\t{}".format(command))
        return command

    @classmethod
    def _cmd_qstat_all(cls, verbose):
        command = str(setup.LOCAL_PUTT_EXE) +\
                " -load {} qstat".format(setup.CLUSTER_NAME)
        if verbose: print("qstat command:\n\t{}".format(command))
        return command

    @classmethod
    def qstat(cls, pid='', username='', verbose=False):
        if pid and username:
            raise Exception("Use of both arguments 'pid' and 'username' not allowed.")
        elif pid:
            process = subprocess.Popen(cls._cmd_qstat_pid(pid, verbose), shell=True, stdout=subprocess.PIPE)
        elif username:
            process = subprocess.Popen(cls._cmd_qstat_username(username, verbose), shell=True, stdout=subprocess.PIPE)
        else:
            process = subprocess.Popen(cls._cmd_qstat_all(verbose), shell=True, stdout=subprocess.PIPE)
            
        stdout, _ = process.communicate()
        
        if stdout: print(stdout.decode('utf-8'))
        else: raise ProcessLookupError              
        
    @classmethod
    def _cmd_qdel_username(cls, username, verbose):
        raise NotImplementedError
        
    @classmethod
    def _cmd_qdel_pid(cls, pid, verbose):
        command = str(setup.LOCAL_PUTT_EXE) +\
                " -load {} qdel {}".format(setup.CLUSTER_NAME, pid)
        if verbose: print("qdel command:\n\t{}".format(command))
        return command

    @classmethod
    def _cmd_qdel_all(cls, verbose):
        command = str(setup.LOCAL_PUTT_EXE) +\
                " -load {} qdel all".format(setup.CLUSTER_NAME)
        if verbose: print("qstat command:\n\t{}".format(command))
        return command    
    
    @classmethod
    def qdel(cls, pid='', username='', verbose=False):
        if pid and username:
            raise Exception("Use of both arguments 'pid' and 'username' not allowed.")
        elif pid:
            process = subprocess.Popen(cls._cmd_qdel_pid(pid, verbose), shell=True, stdout=subprocess.PIPE)
        elif username:
            process = subprocess.Popen(cls._cmd_qdel_username(username, verbose), shell=True, stdout=subprocess.PIPE)
        else:
            process = subprocess.Popen(cls._cmd_qdel_all(verbose), shell=True, stdout=subprocess.PIPE)
            
        stdout, _ = process.communicate()
        
        if stdout: print(stdout.decode('utf-8'))
        else: raise ProcessLookupError