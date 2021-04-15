import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.astk.astktrigger import AstkTrigger
from src.astk.astkclumpsetting import AstkClumpsetting


class Icv:
    def __init__(self):
        self._name = ''
        self._layer = ''
        self._stage = []
        self._choke_position = {}
        self._trigger_rule = {}


    def set_name(self, name):
        self._name = name


    def set_layer(self, layer):
        self._layer = layer


    def add_stage(self, name, value):
        self._stage.append(name)
        self._choke_position[name] = value


    def add_trigger_rule(self, stage_name, trigger_obj):
        if stage_name in self._stage:
            self._trigger_rule[stage_name] = trigger_obj
            return
        raise ValueError('Stage name not found. Added it first...')


    def __call__(self):
        lst = []
        if self._name: lst.append('** *****{}*****'.format(self._name))
        for name in self._stage:
            astktrigger = AstkTrigger()
            astktrigger.set_name(name).set_test_times(1)
            astktrigger.add_trigger_obj(self._trigger_rule[name])
            astktrigger.add_action(AstkClumpsetting().set_layerclump_name(self._layer).set_value(self._choke_position[name]))
            lst.append(astktrigger())
        return '\n'.join(lst)

if __name__ == '__main__':
    icv = Icv()

    icv.set_name('ICV1')
    icv.set_layer('LAYER1')
    icv.add_stage('STAGE1', 1.0)
    icv.add_stage('STAGE2', 0.5)
    icv.add_stage('STAGE3', 0.0)
    
    from src.astk.triggerobject_onctrllump import OnCtrllump
    trigger_obj = OnCtrllump().set_layerclump_name('LAYER1')
    trigger_obj.set_condition('*GOR', '>', '#AAAAA#')
    icv.add_trigger_rule('STAGE1', trigger_obj)

    trigger_obj = OnCtrllump().set_layerclump_name('LAYER1')
    trigger_obj.set_condition('*GOR', '>', '#BBBBB#')
    icv.add_trigger_rule('STAGE2', trigger_obj)

    trigger_obj = OnCtrllump().set_layerclump_name('LAYER1')
    trigger_obj.set_condition('*GOR', '>', '#CCCCC#')
    icv.add_trigger_rule('STAGE3', trigger_obj)

    icv2 = Icv()

    icv2.set_name('ICV1')
    icv2.set_layer('LAYER1')
    icv2.add_stage('STAGE1', 1.0)
    icv2.add_stage('STAGE2', 0.5)
    icv2.add_stage('STAGE3', 0.0)

    from src.astk.triggerobject_onelapsed import OnElapsed
    trigger_obj = OnElapsed()
    trigger_obj.set_condition('*TIMSIM', '>', '#AAAAA#')
    icv2.add_trigger_rule('STAGE1', trigger_obj)

    trigger_obj = OnElapsed()
    trigger_obj.set_condition('*TIMSIM', '>', '#BBBBB#')
    icv2.add_trigger_rule('STAGE2', trigger_obj)

    trigger_obj = OnElapsed()
    trigger_obj.set_condition('*TIMSIM', '>', '#CCCCC#')
    icv2.add_trigger_rule('STAGE3', trigger_obj)
