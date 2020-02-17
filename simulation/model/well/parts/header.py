from simulation.common.keywords import Keywords as kw

class Header:

    @staticmethod
    def default(agr, name, type, group, fluid, operate, monitor, geometry, perf_ff):
       agr.add_four(kw.well(), name, kw.attachto(), group)
       agr.add_two(type, name)
       if fluid: agr.add_two(kw.incomp(), fluid)
       for ope in operate: agr.add_five(kw.operate(), *ope)
       for mon in monitor: agr.add_four(kw.monitor(), *mon)
       agr.add_six(kw.geometry(), *geometry)
       agr.add_three(kw.perf(), perf_ff, name)
