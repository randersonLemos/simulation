import pathlib
import warnings
import shutil

class Builder_Dat:
    _frameRoot = pathlib.Path('')

    @classmethod
    def set_frameRoot(cls, path):
        cls._frameRoot = pathlib.Path(path)

    def __init__(self, frameFile='', frameIncludeFolder=''):
        if frameFile: self.path_to_file = self._frameRoot / frameFile
        else: self.path_to_file = self._frameRoot / 'main.frame'

        if frameIncludeFolder: self.path_to_include = self._frameRoot / frameIncludeFolder
        else: self.path_to_include = self._frameRoot / 'include'

        with self.path_to_file.open(mode='r') as fh: self.frame = fh.read()

    def replace_mark(self, mark, stg):
        if self.frame.find(mark) != -1:
            self.frame = self.frame.replace(mark, stg)
            return
        raise  NameError('Mark \"{}\" not find...'.format(mark))

    def write(self, path_to_folder):
        p = pathlib.Path(path_to_folder)
        p.mkdir(parents=True, exist_ok=True)
        with (p / '{}.dat'.format(self.path_to_file.stem)).open('w') as fh: fh.write(self.frame)
        for orin in self.path_to_include.glob('**/*'):
            if orin.is_file():
                dest = pathlib.Path(str(p / str(orin).replace(str(self._frameRoot)+'/','')))
                dest.mkdir(parents=True, exist_ok=True)
                shutil.copy(str(orin), str(dest))


