import copy
import pathlib
import warnings
import functools


def handle_assignment(decoreted_method):
    @functools.wraps(decoreted_method)
    def wrapper(inst):
        attribute = '_'.join(decoreted_method.__name__.split('_')[1:])
        attribute_data = getattr(inst, attribute)
        if attribute_data:
            stg  = "Attribute '{}' from well {} already has an assigned value.".format(attribute, inst.name)
            stg += ' Value replacing by loading not allowed. Original value kept.'
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


class Well_Spec:
    def __init__(self, name, alias_lst=[], file='', **kwargs):
        self.name = name
        self.alias_lst = alias_lst

        if file:
            self.file = pathlib.Path(file)
        else:
            self.file = pathlib.Path(__file__).parent.parent / '{}.input'.format(self.name)

        self.group = ''
        self.operate = []
        self.monitor = []
        self.geometry = []
        self.perf_ff = ''
        self.perf_table = []
        self.layerclump = []
        self.time_open = ''
        self.time_on = ''
        self.icv_nr = ''
        self.icv_operation = []
        self.icv_control_law = []
        self.wag_operation = []

        for key in kwargs:
            if hasattr(self, key):
                self.__dict__[key] = kwargs[key]
            else:
                raise AttributeError('{} is not an attribute class')

        self._not_loaded = True
        self._not_loaded_more = True
        self._not_loaded_more_more = True

    def load(self):
        if self._not_loaded:
            self.load_group()
            self.load_icv_nr()
            self._not_loaded = False
        return copy.deepcopy(self)

    def load_more(self):
        if self._not_loaded_more:
            if self._not_loaded:
                self.load()
            #self.load_group()
            self.load_operate()
            self.load_monitor()
            self.load_geometry()
            self.load_perf_ff()
            self.load_perf_table()
            self.load_time_open()
            self.load_time_on()
            self._not_loaded_more = False
        return copy.deepcopy(self)

    def load_more_more(self):
        if self._not_loaded_more_more:
            if self._not_loaded_more:
                self.load_more()
            #self.load_group()
            #self.load_operate()
            #self.load_monitor()
            #self.load_geometry()
            #self.load_perf_ff()
            #self.load_perf_table()
            self.load_layerclump()
            #self.load_time_open()
            #self.load_time_on()
            #self.load_icv_nr()
            self.load_icv_operation()
            self.load_icv_control_law()
            self.load_wag_operation()
            self._not_loaded_more_more = False
        return copy.deepcopy(self)

    @handle_assignment
    def load_group(self):
        lst = self._data_picker('---GROUP---', self.file)
        self._load_group(lst)

    @handle_assignment
    def load_operate(self):
        lst = self._data_picker('---OPERATE---', self.file)
        self._load_operate(lst)

    @handle_assignment
    def load_monitor(self):
        lst = self._data_picker('---MONITOR---', self.file)
        self._load_monitor(lst)

    @handle_assignment
    def load_geometry(self):
        lst = self._data_picker('---GEOMETRY---', self.file)
        self._load_geometry(lst)

    @handle_assignment
    def load_perf_ff(self):
        lst = self._data_picker('---PERF_FF---', self.file)
        self._load_perf_ff(lst)

    @handle_assignment
    def load_perf_table(self):
        lst = self._data_picker('---PERF_TABLE---', self.file)
        self._load_perf_table(lst)

    @handle_assignment
    def load_layerclump(self):
        lst = self._data_picker('---LAYERCLUMP---', self.file)
        self._load_layerclump(lst)

    @handle_assignment
    def load_time_open(self):
        lst = self._data_picker('---TIME_OPEN---', self.file)
        self._load_time_open(lst)

    @handle_assignment
    def load_time_on(self):
        lst = self._data_picker('---TIME_ON---', self.file)
        self._load_time_on(lst)

    @handle_assignment
    def load_icv_nr(self):
        lst = self._data_picker('---ICV_NR---', self.file)
        self._load_icv_nr(lst)

    @handle_assignment
    def load_icv_operation(self):
        lst = self._data_picker('---ICV_OPERATION---', self.file)
        self._load_icv_operation(lst)

    @handle_assignment
    def load_icv_control_law(self):
        lst = self._data_picker('---ICV_CONTROL_LAW---', self.file)
        self._load_icv_control_law(lst)

    @handle_assignment
    def load_wag_operation(self):
        lst = self._data_picker('---WAG_OPERATION---', self.file)
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
    def _load_time_open(self, lst):
        self.time_open = lst.pop().split(',')
        if len(self.time_open) == 1:
            self.time_open = self.time_open.pop()

    @handle_lst
    def _load_time_on(self, lst):
        self.time_on = lst.pop()

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


    def _data_picker(self, keyword, file):
        with file.open() as fh:
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
        stg  = "Keyword '{}' not found in file '{}'.".format(keyword, file)
        stg += " Returning empty list."
        warnings.warn(stg)
        return []

    def _comment(self, line):
        return line.strip()[0] == '#'