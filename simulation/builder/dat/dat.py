import pathlib
import shutil

class Builder_Dat:
    def __init__(self, frameRoot, frameFile, frameIncludeFolder):
        self.root = pathlib.Path(frameRoot)
        self.path_to_frame = self.root / frameFile
        self.path_to_frameInclude = self.root / frameIncludeFolder
        with self.path_to_frame.open(mode='r') as fh: self.frame = fh.read()

    def replace_mark(self, mark, stg):
        if self.frame.find(mark) != -1:
            self.frame = self.frame.replace(mark, stg)
            return
        raise  NameError('Mark \"{}\" not find...'.format(mark))

    def write(self, datRoot, datFile):
        path_to_dat = pathlib.Path(datRoot) / datFile
        path_to_dat.parent.mkdir(parents=True, exist_ok=True)        
        with path_to_dat.open('w') as fh: fh.write(self.frame)
        for orin in self.path_to_frameInclude.glob('**/*'):
            if orin.is_file():
                idx = orin.parts.index(self.path_to_frameInclude.parts[-1])
                dest = path_to_dat.parent.joinpath(*orin.parts[idx:])
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(str(orin), str(dest))
