import pathlib
from config.scripts import settings as sett
from dictionary.scripts.keywords import Keywords as kw

class ICV:
    def __init__(self, nr_valves):
        self.nr_valves = int(nr_valves)
        self.valve_obj = None
        self._rules = []

    def add_rule(self, rule):
        self._rules.append(rule)

    def get_control_law(self):
        control_law = self._rules_of_operation()
        return [control_law]*self.nr_valves

    def _rules_of_operation(self):
        outer = []
        for rules in self._rules:
            iter_rules = iter(rules)
            inner = []
            while True:
                try:
                    qty = next(iter_rules)
                    ine = next(iter_rules)
                    val = next(iter_rules)
                    stg = '{} __LAYER__ {} {} {}'.format(kw.on_ctrllump(), qty, ine, val)
                    xxx = next(iter_rules) # conditional or action
                    inner.append(stg)
                    inner.append(xxx)
                except StopIteration:
                    outer.append(inner)
                    break
        return outer

    def write(self, sim_folder):
        path_to_inf = sett.LOCAL_ROOT / sett.SIMS_FOLDER / sim_folder / sett.INF_NAME
        with path_to_inf.open('w') as handle:
            handle.write(self.repr())

    def repr(self):
        outer = '###OPERATIONAL RULES###\n'
        for rules in self._rules:
            iter_rules = iter(rules)
            inner = 'Trigger\n'
            while True:
                try:
                    qty = next(iter_rules)
                    ine = next(iter_rules)
                    val = next(iter_rules)
                    inner += '  with {} {} {}\n'.format(qty, ine, val)
                    xxx = next(iter_rules) # conditional or action
                    if isinstance(xxx, str):
                        inner += '  {}\n'.format(xxx)
                    else:
                        inner += '  do {}\n'.format(xxx)
                except StopIteration:
                    outer += inner
                    break
        return outer
