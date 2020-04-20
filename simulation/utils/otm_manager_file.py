import re
import pathlib

class OtmManagerFile():           
    def set_project_root(self, path):
        self._project_root = pathlib.Path(path)
        return self
    
    
    def set_simulation_folder_prefix(self, name):
        self._simulation_folder_prefix = name
        return self
    
    
    def set_simulation_file_prefix(self, name):
        self._simulation_file_prefix = name
        return self
    
   
    def set_result_file(self, file):
        self._result_file = file
        
    
    def set_hldg_sample_file(self, file):
        self._hldg_sample_file = file
     
    
    def simulation_folder_paths(self, to_string=False, sort=True):
        root = self._project_root
        prefix = '{}*'.format(self._simulation_folder_prefix)
        lst = []
        for simulation_folder in root.glob(prefix):
            lst.append(simulation_folder)
            
        if sort: lst = sorted(lst)
        if to_string: lst = list(map(str, lst))
        return lst
    
    
    def simulation_file_paths(self, ext='', to_string=False, sort=True):
        prefix = '{}*'.format(self._simulation_file_prefix)
        if ext:
            prefix = '{}*{}'.format(self._simulation_file_prefix, ext)            
            pattern = re.compile('{}\d\d\d\d{}'.format(self._simulation_file_prefix, ext))    
                
        lst = []
        for simulation_folder_path in self.simulation_folder_paths():
            for simulation_file in simulation_folder_path.glob(prefix):
                if pattern.search(str(simulation_file)):
                    lst.append(simulation_file)
         
        if sort: lst = sorted(lst)
        if to_string: lst = list(map(str, lst))
        return lst

    
    def result_file_path(self):
        return self._project_root / self._result_file
    
    
    def hldg_sample_file_paths(self):
        lst = []
        for simulation_folder_path in self.simulation_folder_paths():
            lst.append(simulation_folder_path / self._hldg_sample_file)
        return lst
            
        