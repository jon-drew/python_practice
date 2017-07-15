def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    s = str(s)
    string_list = []
    string_value = str(string_list)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in list(s):
        if letter not in vowels:
            string_list.append(letter)
        elif letter in vowels:
            continue
    print (''.join(string_list))