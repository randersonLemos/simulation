import copy
import pathlib
import warnings
import functools

def handle_assignment(decoreted_method):
    @functools.wraps(decoreted_method)
    def wrapper(inst):
        attribute = decoreted_method.__name__[12:]
        attribute_data = getattr(inst, attribute)
        if attribute_data:
            stg  = "Attribute '{}' from well {} already has an assigned value.".format(attribute, inst.name)
            stg += " Value replacing by loading not allowed. Original value kept."
            warnings.warn(stg)
            return
        decoreted_method(inst)
    return wrapper

def handle_lst(decorated_method):
    @functools.wraps(decorated_method)
    def wrapper(inst, lst):
        if lst:
            decorated_method(inst, lst)
    return wrapper

class Well_Design:
    _rootPath = pathlib.Path('')

    @classmethod
    def set_rootPath(cls, path):
        cls._rootPath = pathlib.Path(path)

    def __init__(self, name, alias=[], file_name='', **kwargs):
        self.name = name; self.alias = alias
        self.group = ''
        self.operate = []
        self.monitor = []
        self.geometry = []
        self.perf_ff = ''
        self.perf_table = []
        self.layerclump = []
        self.open_time = ''
        self.on_time = ''
        self.icv_nr = ''
        self.icv_operation = []
        self.icv_control_law = []
        self.wag_operation = []

        if file_name: self.path_to_file = self._rootPath / file_name
        else: self.path_to_file = self._rootPath / '{}.input'.format(self.name)

        for key in kwargs:
            if hasattr(self, key): self.__dict__[key] = kwargs[key]
            else: raise AttributeError('{} is not an attribute class')

        self._load()

    def _load(self):
        self._outer_load_group()
        self._outer_load_icv_nr()
        self._outer_load_operate()
        self._outer_load_monitor()
        self._outer_load_geometry()
        self._outer_load_perf_ff()
        self._outer_load_perf_table()
        self._outer_load_open_time()
        self._outer_load_on_time()
        self._outer_load_layerclump()
        self._outer_load_icv_operation()
        self._outer_load_icv_control_law()
        self._outer_load_wag_operation()

    @handle_assignment
    def _outer_load_group(self):
        lst = self._data_picker('---GROUP---', self.path_to_file)
        self._load_group(lst)

    @handle_assignment
    def _outer_load_operate(self):
        lst = self._data_picker('---OPERATE---', self.path_to_file)
        self._load_operate(lst)

    @handle_assignment
    def _outer_load_monitor(self):
        lst = self._data_picker('---MONITOR---', self.path_to_file)
        self._load_monitor(lst)

    @handle_assignment
    def _outer_load_geometry(self):
        lst = self._data_picker('---GEOMETRY---', self.path_to_file)
        self._load_geometry(lst)

    @handle_assignment
    def _outer_load_perf_ff(self):
        lst = self._data_picker('---PERF_FF---', self.path_to_file)
        self._load_perf_ff(lst)

    @handle_assignment
    def _outer_load_perf_table(self):
        lst = self._data_picker('---PERF_TABLE---', self.path_to_file)
        self._load_perf_table(lst)

    @handle_assignment
    def _outer_load_layerclump(self):
        lst = self._data_picker('---LAYERCLUMP---', self.path_to_file)
        self._load_layerclump(lst)

    @handle_assignment
    def _outer_load_open_time(self):
        lst = self._data_picker('---OPEN_TIME---', self.path_to_file)
        self._load_open_time(lst)

    @handle_assignment
    def _outer_load_on_time(self):
        lst = self._data_picker('---ON_TIME---', self.path_to_file)
        self._load_on_time(lst)

    @handle_assignment
    def _outer_load_icv_nr(self):
        lst = self._data_picker('---ICV_NR---', self.path_to_file)
        self._load_icv_nr(lst)

    @handle_assignment
    def _outer_load_icv_operation(self):
        lst = self._data_picker('---ICV_OPERATION---', self.path_to_file)
        self._load_icv_operation(lst)

    @handle_assignment
    def _outer_load_icv_control_law(self):
        lst = self._data_picker('---ICV_CONTROL_LAW---', self.path_to_file)
        self._load_icv_control_law(lst)

    @handle_assignment
    def _outer_load_wag_operation(self):
        lst = self._data_picker('---WAG_OPERATION---', self.path_to_file)
        self._load_wag_operation(lst)

    @handle_lst
    def _load_group(self, lst):
        self.group = lst.pop()

    @handle_lst
    def _load_operate(self, lst):
        for line in lst:
            self.operate.append([el.strip() for el in line.split(',')])

    @handle_lst
    def _load_monitor(self, lst):
        for line in lst:
            self.monitor.append([el.strip() for el in line.split(',')])

    @handle_lst
    def _load_geometry(self, lst):
        self.geometry = [el.strip() for el in lst.pop().split(',')]

    @handle_lst
    def _load_perf_ff(self, lst):
        self.perf_ff = lst.pop()

    @handle_lst
    def _load_perf_table(self, lst):
        for line in lst:
            self.perf_table.append([el.strip() for el in line.split(',')])

    @handle_lst
    def _load_layerclump(self, lst):
        for line in lst:
            self.layerclump.append([el.strip() for el in line.split(',')])

    @handle_lst
    def _load_open_time(self, lst):
        self.open_time = lst.pop().split(',')
        if len(self.open_time) == 1:
            self.open_time = self.open_time.pop()

    @handle_lst
    def _load_on_time(self, lst):
        self.on_time = lst.pop()

    @handle_lst
    def _load_icv_nr(self, lst):
        self.icv_nr = lst.pop()

    @handle_lst
    def _load_icv_operation(self, lst):
        self.icv_operation = [el.strip() for el in lst.pop().split(',')]

    @handle_lst
    def _load_icv_control_law(self, lst):
        dic = {}
        for line in lst:
            lstt = line.split(',')
            idx = lstt[0].strip()
            instr = [el.strip() for el in lstt[1:]]
            if idx not in dic:
                dic[idx] = []
            dic[idx].append(instr)
        for i in range(len(dic)):
            self.icv_control_law.append(dic['{}'.format(i+1)])

    @handle_lst
    def _load_wag_operation(self, lst):
        self.wag_operation = [el.strip() for el in lst.pop().split(',')]


    def _data_picker(self, keyword, path_to_file):
        with path_to_file.open() as fh:
            content = iter(fh.read().split('\n'))
        chunk = []
        for line in content:
            if line == keyword:
                while True:
                    line = next(content)
                    if line == '---END---':
                        return chunk
                    elif self._comment(line):
                        pass
                    else:
                        chunk.append(line)
        stg  = "Keyword '{}' not found in file '{}'.".format(keyword, path_to_file)
        stg += " Returning empty list."
        warnings.warn(stg)
        return []

    def _comment(self, line):
        return line.strip()[0] == '#'
