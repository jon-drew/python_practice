def permutation_flag(L1, L2):
    if [[element, L1.count(element)] for element in set(L1)] == [[element, L2.count(element)] for element in set(L2)]:
        return dict([[element, L1.count(element)] for element in set(L1)])
    else:
        return {False}

def most_common_element(dict):
    current_most_common = [0, 0, 0]
    for key in dict:
        if key == False:
            return False
        elif dict.get(key) > current_most_common[-2]:
            current_most_common = [key, dict.get(key), type(key)]
    return tuple(current_most_common)

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
    If they are permutations of each other, returns a tuple of 3 items in this order: 
    the element occurring most, how many times it occurs, and its type
    '''
    if most_common_element(permutation_flag(L1, L2)) == (0, 0, 0):
        return (None, None, None)
    return most_common_element(permutation_flag(L1, L2))
