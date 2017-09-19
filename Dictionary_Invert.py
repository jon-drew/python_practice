def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invert_dict = {}
    for key, value in d.items():
        invert_dict[value] = sorted(invert_dict.get(value, []))
        invert_dict[value].append(key)
    return invert_dict