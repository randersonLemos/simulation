import pathlib

class Builder_Rwd:
    def __init__(self, frameRoot, frameFile):
        self.root = pathlib.Path(frameRoot)
        self.path_to_frame = self.root / frameFile
        with self.path_to_frame.open(mode='r') as fh: self.frame = fh.read()

    def replace_mark(self, mark, stg):
        if self.frame.find(mark) != -1:
            self.frame = self.frame.replace(mark, stg)
            return
        raise  NameError('Mark \"{}\" not find...'.format(mark))
        
    def write(self, rwdRoot, rwdFile):
        path_to_rwd = pathlib.Path(rwdRoot) / rwdFile
        path_to_rwd.parent.mkdir(parents=True, exist_ok=True)        
        with path_to_rwd.open('w') as fh: fh.write(self.frame)