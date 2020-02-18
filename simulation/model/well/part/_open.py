from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd

class _Open:
    @staticmethod
    def default(agr, well_name, time_open):
        #agr.add_one('** OPEN **')
        name = "'OPEN_{}'".format(well_name.strip("'"))
        agr.add_seven(kw.trigger(), name, kw.on_elapsed()
                , wrd.time(), kw.timsim(),kw.greater_than(), time_open)
        agr.add_two(kw.open(), well_name, pre='   ')
        agr.add_one(kw.end_trigger())
