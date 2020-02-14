import pathlib


def producer_dual_icv(well, group, operate, monitor, geometry, perf
        , completion, open_time, on_time, layerclump
        , icv_start, icv_control, output_folder):

    from well.scripts.frames.prod_dual_icv import Prod_Dual_ICV

    w = Prod_Dual_ICV(well, group)

    for ope in operate:
        w.get_operate(*ope)

    for mon in monitor:
        w.get_monitor(*mon)

    w.get_geometry(*geometry)
    w.get_perf(perf)

    for com in completion:
        w.get_completion(com)

    if on_time:
        w.get_on_time(on_time)

    if open_time:
        w.get_open(open_time)

    for lay in layerclump:
        w.get_layerclump(lay)

    if icv_start:
        w.get_icv_start(icv_start)
        w.get_icv_control(icv_control)

    w.build()
    w.write(pathlib.Path(output_folder) / '{}.inc'.format(well))
