import os
import time
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.model.rwd.builder_rwd import Builder_Rwd
from simulation.utils.otm_manager_file import OtmManagerFile
from simulation.utils.run_manager import RunManager
from simulation.run.report import Report
from simulation import setup


MARK_RWD_IRFFILE = '$#@IRFFILE@#$'
MARK_RWD_RWOFILE = '$#@RWOFILE@#$'



Report.set_exe(setup.LOCAL_REPO_EXE)


if __name__ == '__main__':   
    omf = OtmManagerFile()
    omf.set_project_root('H:/OTM_ICV_01S_WIDE')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    
    reports = []
    
    for irf_path in  omf.simulation_file_paths('.irf'):
        rwd_path = irf_path.with_suffix('.rwd')
        rwo_path = irf_path.with_suffix('.rwo')

        brwd = Builder_Rwd(frame_file_path='./frame/main.rwd.frame')
        brwd.replace_mark(MARK_RWD_IRFFILE, irf_path)
        brwd.replace_mark(MARK_RWD_RWOFILE, rwo_path)
        brwd.write(rwd_path)
    
        reports.append(Report(path_to_rwd=rwd_path, path_to_rwo=rwo_path, verbose=True, run=False))
      
    rm = RunManager(reports, 20)                 