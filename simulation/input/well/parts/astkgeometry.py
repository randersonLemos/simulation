from simulation.common.keywords import Keywords as Kw

class AstkGeometry:
    def __init__(self):
        self._dir = ''
        self._rw = ''
        self._geofac = ''
        self._wfrac = ''
        self._skin = ''
        self._wdfac = ''

    def set_dir(self, dir):
        self._dir = dir
        return self

    def set_rw(self, rw):
        self._rw = '{:.4f}'.format(rw)
        return self

    def set_geofac(self, geofac):
        self._geofac = '{:.4f}'.format(geofac)
        return self

    def set_wfrac(self, wfrac):
        self._wfrac = '{:.4f}'.format(wfrac)
        return self

    def set_skin(self, skin):
        self._skin = '{:.4f}'.format(skin)
        return self

    def set_wdfac(self, wdfac):
        self._wdfac = '{:.4f}'.format(wdfac)
        return self

    def __call__(self):
        stg = '{} {} {} {} {} {} {}'.format(Kw.geometry(), self._dir, self._rw, self._geofac, self._wfrac, self._skin, self._wdfac).strip()
        return stg
