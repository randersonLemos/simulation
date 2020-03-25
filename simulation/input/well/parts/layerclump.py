class Layerclump:
    def __init__(self, name_mode=False, base_name_mode=False):
        if sum([name_mode, base_name_mode]) != 1:
            raise ValueError('Necessary to select only one mode...')

        self._name_mode = name_mode
        self._base_name_mode = base_name_mode

        self._lst = []

        if name_mode:
            raise NotImplementedError()

        if base_name_mode:
            self._base_name = ''
            self._suffix = ''

            self.name = self._name_base_name_mode
            self.add = self._add_base_name_mode
            self.set_base_name = self._set_base_name
            self.set_suffix = self._set_suffix
            self.base_name = self._get_base_name
            self.suffix = self._get_suffix

    def is_name_mode(self):
        return self._name_mode

    def is_base_name_mode(self):
        return self._base_name_mode

    def _add_base_name_mode(self, x, y, z):
        self._lst.append((x, y, z, ))

    def _set_base_name(self, name):
        self._base_name = name

    def _get_base_name(self):
        return self._base_name

    def _set_suffix(self, suffix):
        self._suffix = suffix

    def _get_suffix(self):
        return self._suffix

    def _name_base_name_mode(self):
        if not self._base_name:
            raise ValueError("Define a value for 'base_name'")
        name = self._base_name + self._suffix
        lst = []
        for idx in range(len(self._lst)):
            lst.append('{}{}'.format(name, idx+1))
        return lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, idx):
        return self.name()[idx], self._lst[idx]

    def __call__(self):
        return self._lst
