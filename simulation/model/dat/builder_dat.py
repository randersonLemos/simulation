import pathlib
import shutil

class Builder_Dat:
    _frameRoot = pathlib.Path('')
    _datRoot   = pathlib.Path('')

    @classmethod
    def set_frameRoot(cls, path):
        cls._frameRoot = pathlib.Path(path)

    @classmethod
    def set_datRoot(cls, path):
        cls._datRoot = pathlib.Path(path)

    def __init__(self, frameFile, frameIncludeFolder):
        self.path_to_file = self._frameRoot / frameFile
        self.path_to_include = self._frameRoot / frameIncludeFolder
        with self.path_to_file.open(mode='r') as fh: self.frame = fh.read()

    def replace_mark(self, mark, stg):
        if self.frame.find(mark) != -1:
            self.frame = self.frame.replace(mark, stg)
            return
        raise  NameError('Mark \"{}\" not find...'.format(mark))

    def write(self, datFile):
        datFile = self._datRoot / pathlib.Path(datFile)
        datRoot = datFile.parent
        datName = pathlib.Path(datFile).stem
        datRoot.mkdir(parents=True, exist_ok=True)
        with (datRoot / '{}.dat'.format(datName)).open('w') as fh: fh.write(self.frame)
        for orin in self.path_to_include.glob('**/*'):
            if orin.is_file():
                idx = orin.parts.index(str(self._frameRoot))
                dest = datRoot.joinpath(*orin.parts[idx+1:])
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(str(orin), str(dest))
