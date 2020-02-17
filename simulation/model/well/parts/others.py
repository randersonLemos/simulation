from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd

class Others:
    class Open:
        @staticmethod
        def default(agr, name, open_time):
            agr.add_one('**Opening')
            name = "'OPEN_{}'".format(name.strip("'"))
            agr.add_seven(kw.trigger(), name, kw.on_elapsed()
                    , wrd.time(), kw.timsim(),kw.greater_than(), open_time)
            agr.add_two(kw.open(), name, pre='   ')
            agr.add_one(kw.end_trigger())


#def layerclump_default(agr, well_name, layerclump):
#    for idx, layer in enumerate(layerclump):
#        name = "'{}_Z{}'".format(well_name.strip("'"),idx+1)
#        agr.add_two(kw.layerclump(), name)
#        agr.add_three(well_name, ' '.join(layer), kw.mt())
#        agr.add_three(well_name, ' '.join(layer), kw.fr())
#
#def layerclump_wag_default(agr, well_name, layerclump):
#    #agr.add_one('**Layerclump')
#    for idx, layer in enumerate(layerclump):
#        name = "'{}_Z{}'".format(well_name['G'][:-3].strip("'"), idx+1)
#        agr.add_two(kw.layerclump(), name)
#        agr.add_three(well_name['G'], ' '.join(layer), kw.mt())
#        agr.add_three(well_name['G'], ' '.join(layer), kw.fr())
#        agr.add_three(well_name['W'], ' '.join(layer), kw.mt())
#        agr.add_three(well_name['W'], ' '.join(layer), kw.fr())
#
#def start_wag_default(agr, well_name, wag_cond):
#    other = {'G':'W', 'W':'G'}
#    mod, nr1, nr2, nr3 = wag_cond
#
#    nr1 = float(nr1)
#    nr2 = float(nr2)
#    nr3 = int(nr3)
#
#    agr.add_one('** Starting WAG cycle')
#    name = "'WAG_{}'".format(well_name[mod].strip("'"))
#    timsim = "{} {} {}".format(kw.timsim(), kw.greater_than(), nr1)
#    increment = "{} {}".format(kw.increment(), nr2*2)
#    apply_times = "{} {}".format(kw.apply_times(), nr3)
#
#    agr.add_seven(kw.trigger(), name, kw.on_elapsed(), wd.time()
#            , timsim, increment, apply_times)
#    agr.add_two(kw.open(), well_name[mod], pre='   ')
#    agr.add_two(kw.shutin(), well_name[other[mod]], pre='   ')
#    agr.add_one(kw.end_trigger())
#
#    name = "'WAG_{}'".format(well_name[other[mod]].strip("'"))
#    timsim = "{} {} {}".format(kw.timsim(), kw.greater_than(), nr1+nr2)
#    increment = "{} {}".format(kw.increment(), nr2*2)
#    apply_times = "{} {}".format(kw.apply_times(), nr3)
#
#    agr.add_seven(kw.trigger(), name, kw.on_elapsed(), wd.time()
#            , timsim, increment, apply_times)
#    agr.add_two(kw.open(), well_name[other[mod]], pre='   ')
#    agr.add_two(kw.shutin(), well_name[mod], pre='   ')
#    agr.add_one(kw.end_trigger())
