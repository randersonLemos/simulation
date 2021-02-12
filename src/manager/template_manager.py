import pathlib

class TemplateManager:
    def __init__(self, template_file_path):
        self.template_file_path = pathlib.Path(template_file_path)
        with self.template_file_path.open(mode='r') as fh: self.template_file = fh.read()
        return
    
    
    def replace_mark(self, marks, values):
        self.marks = marks
        if not isinstance(marks, list):
            self.marks = [marks]
        self.values = values
        if not isinstance(values, list):
             self.values = [values]
        
        for mark, value in zip(self.marks, self.values):
            if self.template_file.find(mark) != -1:
                self.template_file = self.template_file.replace(mark, value)
            else:
                raise  NameError('Mark \"{}\" not find...'.format(mark))
        return
        
    
    def write(self, file_path):
        file_path = pathlib.Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)        
        with file_path.open('w') as fh: fh.write(self.template_file)
        return