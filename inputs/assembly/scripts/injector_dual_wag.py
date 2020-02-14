import pathlib


def injector_dual_wag(well, group, operate, monitor, geometry, perf
        , completion, open_time, on_time, wag_start, layerclump, output_folder):

    from well.scripts.frames.inje_dual_wag import Inje_Dual_Wag

    w = Inje_Dual_Wag(well, group)

    w.get_incomp('W','*WATER')
    w.get_incomp('G','*GAS')

    for ope in operate:
        w.get_operate(*ope)

    for mon in monitor:
        w.get_monitor(*mon)

    w.get_geometry(*geometry)
    w.get_perf(perf)

    for com in (completion):
        w.get_completion(com)

    if on_time:
        w.get_on_time(on_time)

    if open_time:
        w.get_open(*open_time)

    for lay in layerclump:
        w.get_layerclump(lay)

    if wag_start:
        w.get_wag(*wag_start)

    w.build()
    w.write(pathlib.Path(output_folder) / '{}.inc'.format(well))
