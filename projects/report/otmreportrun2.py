import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.manager.template_manager import TemplateManager
from src.manager.otm_manager_file import OtmManagerFile
from src.manager.run_manager import RunManager
from src.run.report import Report
from src import setup


MARK_RWD_IRFFILE = '$#@IRFFILE@#$'
MARK_RWD_RWOFILE = '$#@RWOFILE@#$'


Report.set_exe(setup.LOCAL_REPO_EXE)
OtmManagerFile.set_default_simulation_folder_prefix('otm_IT')
OtmManagerFile.set_default_simulation_file_prefix('run')
OtmManagerFile.set_default_result_file('otm.otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

files = []
files.append("W:\OTM_GOR_ICV5_1")

rms = []

for file in files:

    omf = OtmManagerFile(project_root=file)
        
    reports = []
        
    for irf_path in omf.simulation_file_paths('.irf'):
        rwd_path = irf_path.with_suffix('.rwd')
        rwo_path = irf_path.with_suffix('.rwo')
    
        tlp = TemplateManager(template_file_path='../template/main.rwd.tlp')
        tlp.replace_mark(MARK_RWD_IRFFILE, str(irf_path))
        tlp.replace_mark(MARK_RWD_RWOFILE, str(rwo_path))
        tlp.write(rwd_path)
       
        reports.append(Report(path_to_rwd=rwd_path, path_to_rwo=rwo_path, verbose=True, run=False))
         
    rms.append(RunManager(reports, 10))    
    
               
#for rm in rms:
#    rm.start()
          