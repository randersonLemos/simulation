import pathlib
import shutil

class Builder_Rwd:
    _frameRoot = pathlib.Path('')
    _rwdRoot = pathlib.Path('')

    @classmethod
    def set_frameRoot(cls, path):
        cls._frameRoot = pathlib.Path(path)

    @classmethod
    def set_rwdRoot(cls, path):
        cls._rwdRoot = pathlib.Path(path)

    def __init__(self, frameFile):
        self.path_to_file = self._frameRoot / frameFile
        with self.path_to_file.open(mode='r') as fh: self.frame = fh.read()

    def replace_mark(self, mark, stg):
        if self.frame.find(mark) != -1:
            self.frame = self.frame.replace(mark, stg)
            return
        raise  NameError('Mark \"{}\" not find...'.format(mark))

    def write(self, rwdFile):
        rwdFile = self._rwdRoot / pathlib.Path(rwdFile)
        rwdRoot = rwdFile.parent
        rwdName = pathlib.Path(rwdFile).stem
        rwdRoot.mkdir(parents=True, exist_ok=True)
        with (rwdRoot / '{}.rwd'.format(rwdName)).open('w') as fh: fh.write(self.frame)
