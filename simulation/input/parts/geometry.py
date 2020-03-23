from simulation.common.keywords import Keywords as Kw

class Geometry:
    def __init__(self, dir, rw, geofac, wfrac, skin, wdfac=0):
        self.dir = dir
        self.rw = rw
        self.geofac = geofac
        self.wfrac = wfrac
        self.skin = skin
        self.wdfac = wdfac

    def __call__(self):
        if self.wdfac:
            return '{} {:5.4f} {:5.4f} {:5.4f} {:5.4f} {:5.4f}'.format(
                    self.dir,
                    self.rw,
                    self.geofac,
                    self.wfrac,
                    self.skin,
                    self.wdfac
                    )

        return '{} {:5.4f} {:5.4f} {:5.4f} {:5.4f}'.format(
                        self.dir,
                        self.rw,
                        self.geofac,
                        self.wfrac,
                        self.skin,
                        )
