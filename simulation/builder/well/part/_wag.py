from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd

class _Wag:
    @staticmethod
    def default(agr, well_name, wag_operation):
        other = {'G':'W', 'W':'G'}
        mod, nr1, nr2, nr3 = wag_operation

        nr1 = float(nr1)
        nr2 = float(nr2)
        nr3 = int(nr3)

        #agr.add_one('** WAG CYCLE **')
        name = "'WAG_{}'".format(well_name[mod].strip("'"))
        timsim = "{} {} {}".format(kw.timsim(), kw.greater_than(), nr1)
        increment = "{} {}".format(kw.increment(), nr2*2)
        apply_times = "{} {}".format(kw.apply_times(), nr3)

        agr.add_seven(kw.trigger(), name, kw.on_elapsed(), wrd.time()
                , timsim, increment, apply_times)
        agr.add_two(kw.open(), well_name[mod], pre='   ')
        agr.add_two(kw.shutin(), well_name[other[mod]], pre='   ')
        agr.add_one(kw.end_trigger())

        name = "'WAG_{}'".format(well_name[other[mod]].strip("'"))
        timsim = "{} {} {}".format(kw.timsim(), kw.greater_than(), nr1+nr2)
        increment = "{} {}".format(kw.increment(), nr2*2)
        apply_times = "{} {}".format(kw.apply_times(), nr3)

        agr.add_seven(kw.trigger(), name, kw.on_elapsed(), wrd.time()
                , timsim, increment, apply_times)
        agr.add_two(kw.open(), well_name[other[mod]], pre='   ')
        agr.add_two(kw.shutin(), well_name[mod], pre='   ')
        agr.add_one(kw.end_trigger())
