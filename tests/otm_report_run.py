import os
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.template_manager import TemplateManager
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.run_manager import RunManager
from simulation.run.report import Report
from simulation import setup


MARK_RWD_IRFFILE = '$#@IRFFILE@#$'
MARK_RWD_RWOFILE = '$#@RWOFILE@#$'



Report.set_exe(setup.LOCAL_REPO_EXE)


if __name__ == '__main__':   
    omf = OtmManagerFile(project_root='H:\OTM_ICV1_TIME1_RANGE1_3')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    
    reports = []
    
    for irf_path in omf.simulation_file_paths('.irf'):
        rwd_path = irf_path.with_suffix('.rwd')
        rwo_path = irf_path.with_suffix('.rwo')

        tlp = TemplateManager(template_file_path='./template/main.rwd.tlp')
        tlp.replace_mark(MARK_RWD_IRFFILE, str(irf_path))
        tlp.replace_mark(MARK_RWD_RWOFILE, str(rwo_path))
        tlp.write(rwd_path)
    
        reports.append(Report(path_to_rwd=rwd_path, path_to_rwo=rwo_path, verbose=True, run=False))
      
    rm = RunManager(reports, 30)                 