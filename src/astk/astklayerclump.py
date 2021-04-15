from src.dict.keywords import Keywords as Kw

class AstkLayerclump:
    def __init__(self, dual_mode_on=False):
        self._dual_mode = dual_mode_on
        self._name = ''
        self._lst = []

    def set_name(self, name):
        self._name = "'" + name + "'"
        return self

    def add_layers(self, well_name, layer):
        self._lst.append(("'" + well_name + "'", layer, ))

    def __call__(self):
        if self._dual_mode:
            return self._repr_dual_mode()
        return self._repr_single_mode()

    def _repr_single_mode(self):
        raise NotImplementedError('Not implemented...')

    def _repr_dual_mode(self):
        lst = []
        lst.append('{} {}'.format(Kw.layerclump(), self._name))

        for well_name, layer in self._lst:
            stg = '{} {} {}'.format(well_name, layer, Kw.mt())
            lst.append(stg)

            stg = '{} {} {}'.format(well_name, layer, Kw.fr())
            lst.append(stg)

        return '\n'.join(lst)


class AstkLayerclumps():
    def __init__(self, dual_mode_on=False):
        self._dual_mode = dual_mode_on
        self._root_name = ''
        self._lst_lst = []
        self._n_layerclumps = 0


    def set_root_name(self, name):
        self._root_name = "'" + name + "'"
        return self


    def set_suffix_name(self, suffix):
        self._suffix = suffix
        return self


    def add_layers(self, well_name, layer, new_layerclump=False):
        if len(self._lst_lst) == 0 or new_layerclump:
            self._lst_lst.append([])
            self._n_layerclumps += 1
        self._lst_lst[-1].append(("'" + well_name + "'", layer))


    def __call__(self):
        if self._dual_mode:
            return self._repr_dual_mode()
        return self._repr_single_mode()


    def _repr_single_mode(self):
        raise NotImplementedError('Not implemented...')


    def _repr_dual_mode(self):
        lst = []
        suffixes = ['{}{}'.format(self._suffix, i+1) for i in range(self._n_layerclumps)]
        for suffix, layers in zip(suffixes, self._lst_lst):
            name = "'{}{}'".format(self._root_name.strip("'"), suffix)

            lst.append('{} {}'.format(Kw.layerclump(), name))

            for well_name, layer in layers:
                stg = '{} {} {}'.format(well_name, layer, Kw.mt())
                lst.append(stg)

                stg = '{} {} {}'.format(well_name, layer, Kw.fr())
                lst.append(stg)

        return '\n'.join(lst)
