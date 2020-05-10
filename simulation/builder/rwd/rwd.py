import pathlib

class Builder_Rwd:
    def __init__(self, frame_file_path):
        self.frame_file_path = pathlib.Path(frame_file_path)
        with self.frame_file_path.open(mode='r') as fh: self.frame_file = fh.read()


    def replace_mark(self, mark, path):
        if isinstance(path, pathlib.Path):
            path = str(path)
        if self.frame_file.find(mark) != -1:
            self.frame_file = self.frame_file.replace(mark, path)
            return
        raise  NameError('Mark \"{}\" not find...'.format(mark))
       
        
    def write(self, rwd_file_path):
        rwd_file_path = pathlib.Path(rwd_file_path)
        rwd_file_path.parent.mkdir(parents=True, exist_ok=True)        
        with rwd_file_path.open('w') as fh: fh.write(self.frame_file)