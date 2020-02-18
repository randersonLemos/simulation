import re
from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd

class ICV:

    @staticmethod
    def deafult(agr, well_name, layerclump, icv_operation, icv_control_law):
        agr.add_one('**ICV control')
        name = "'ICVs_{}'".format(well_name.strip("'"))
        nr1, nr2, nr3 = icv_operation
        timsim = "{} {} {}".format(kw.timsim(), kw.greater_than(), nr1)
        increment = "{} {}".format(kw.increment(), nr2)
        apply_times = "{} {}".format(kw.apply_times(), nr3)
        agr.add_seven(kw.trigger(), name, kw.on_elapsed(), wrd.time()
                , timsim, increment, apply_times)
        for idx, layer in enumerate(layerclump):
            controls = icv_control_law[idx]
            for idx2, control in enumerate(controls):
                act = control[-1]
                name1 = "'ICV_{}_Z{}_{}'".format(well_name.strip("'"),idx+1,idx2+1)
                name2 = "'{}_Z{}'".format(well_name.strip("'"),idx+1)
                conditions = re.sub('__LAYER__',name2,' '.join(control[:-1]))
                agr.add_four(kw.trigger(), name1, conditions, '*TEST_TIMES 1', pre='   ')
                agr.add_three(kw.clumpsetting(), name2, act, pre='      ')
                agr.add_one(kw.end_trigger(), pre='   ')
        agr.add_one(kw.end_trigger())
