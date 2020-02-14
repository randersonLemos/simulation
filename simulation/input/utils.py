def gather_wells_names(well_spec_obj_lst):
    names = []
    for well in well_spec_obj_lst:
        names.append(well.name)
    return names
