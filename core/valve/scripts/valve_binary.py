from dictionary.scripts.keywords import Keywords as kw

class Valve_Binary:
    def __init__(self, *operational_conditions):
        self.oc = operational_conditions

    def operational_rule(self):
        outer = []
        for conditions in self.oc:
            iter_conditions = iter(conditions)
            inner = []
            while True:
                try:
                    qty = next(iter_conditions)
                    ine = next(iter_conditions)
                    val = next(iter_conditions)
                    stg = '{} __LAYER__ {} {} {}'.format(kw.on_ctrllump(), qty, ine, val)
                    xxx = next(iter_conditions) # conditional or action
                    inner.append(stg)
                    inner.append(xxx)
                except StopIteration:
                    outer.append(inner)
                    break
        return outer

    def repr(self):
        outer = '###BINARY VALVE###\n'
        for conditions in self.oc:
            iter_conditions = iter(conditions)
            inner = 'Trigger\n'
            while True:
                inner += '  with {} {} {}\n'.format(
                          next(iter_conditions)
                        , next(iter_conditions)
                        , next(iter_conditions)
                        )
                try:
                    inner += '  {}\n'.format(next(iter_conditions))
                except StopIteration:
                    outer += inner
                    outer += '  do 0.0\n'
                    break
        return outer


