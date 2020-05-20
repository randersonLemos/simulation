import re
import pathlib

class OtmManagerFile():
    @classmethod
    def set_default_simulation_folder_prefix(cls, name):
        cls._default_simulation_folder_prefix = name
        return cls


    @classmethod
    def set_default_simulation_file_prefix(cls, name):
        cls._default_simulation_file_prefix = name
        return cls


    @classmethod
    def set_default_result_file(cls, file):
        cls._default_result_file = file
        return cls


    @classmethod
    def set_default_hldg_sample_file(cls, file):
        cls._default_hldg_sample_file = file
        return cls


    def __init__(self, project_root):
        self._project_root = pathlib.Path(project_root)

        self._simulation_folder_prefix = ''
        self._simulation_file_prefix = ''
        self._result_file = ''
        self._hldg_sample_file = ''


    def set_simulation_folder_prefix(self, name):
        self._simulation_folder_prefix = name
        return self


    def set_simulation_file_prefix(self, name):
        self._simulation_file_prefix = name
        return self


    def set_result_file(self, file):
        self._result_file = file
        return self


    def set_hldg_sample_file(self, file):
        self._hldg_sample_file = file
        return self


    def simulation_folder_paths(self, to_string=False, sort=True):
        simulation_folder_prefix = self._simulation_folder_prefix
        if self._simulation_folder_prefix == '':
            simulation_folder_prefix = self._default_simulation_folder_prefix

        root = self._project_root
        prefix = '{}*'.format(simulation_folder_prefix)
        lst = []
        for simulation_folder in root.glob(prefix):
            lst.append(simulation_folder)

        if sort: lst = sorted(lst)
        if to_string: lst = list(map(str, lst))
        return lst


    def simulation_file_paths(self, ext='', to_string=False, sort=True):
        simulation_file_prefix = self._simulation_file_prefix
        if self._simulation_file_prefix == '':
            simulation_file_prefix = self._default_simulation_file_prefix

        prefix = '{}*'.format(simulation_file_prefix)
        pattern = re.compile('{}\d\d\d\d{}'.format(simulation_file_prefix, ext))
        if ext:
            prefix = '{}*{}'.format(simulation_file_prefix, ext)
            pattern = re.compile('{}\d\d\d\d{}'.format(simulation_file_prefix, ext))

        lst = []
        for simulation_folder_path in self.simulation_folder_paths():
            for simulation_file in simulation_folder_path.glob(prefix):
                if pattern.search(str(simulation_file)):
                    lst.append(simulation_file)

        if sort: lst = sorted(lst)
        if to_string: lst = list(map(str, lst))
        return lst


    def result_file_path(self):
        result_file = self._result_file
        if self._result_file == '':
            result_file = self._default_result_file

        return self._project_root / result_file


    def hldg_sample_file_paths(self):
        hldg_sample_file = self._hldg_sample_file
        if self._hldg_sample_file == '':
            hldg_sample_file = self._default_hldg_sample_file

        lst = []
        for simulation_folder_path in self.simulation_folder_paths():
            lst.append(simulation_folder_path / hldg_sample_file)
        return lst

