def dict_invert(d):
'''Returns a dictionary with the key-value pairings reversed'''
    invert_dict = {}
    for key, value in dict.items():
        invert_dict[value] = sorted(invert_dict.get(value, []))
        invert_dict[value].append(key)
    return invert_dict
