import subprocess
from pathlib import Path

class Report:
    exe = 'NEED TO BE SET VIA SET CLASS METHOD'

    @classmethod
    def set_exe(cls, exe):
        cls.exe = exe
    
    
    def __init__(self, path_to_rwd , path_to_rwo, verbose, run):        
        self.path_to_rwd = Path(path_to_rwd)        
        self.path_to_rwo = Path(path_to_rwo)
        self.verbose = verbose
        if run: self.run()


    def run(self):
        self.path_to_rwo.parent.mkdir(parents=True, exist_ok=True)
               
        command = str(self.exe)+\
                  ' /f '+str(self.path_to_rwd)+\
                  ' /o '+str(self.path_to_rwo)

        if self.verbose: print('command run:\n\t{}'.format(command))
        self.process = subprocess.Popen(command, shell=True)
        return self
        
    
    def kill(self):
        command = 'taskkill /F /T /PID {}'.format(self.process.pid)
        if self.verbose: print('command kill:\n\t{}'.format(command))
        subprocess.Popen(command, shell=True)
        return self
        
        
    def is_alive(self):
        return True if self.process.poll() == None else False