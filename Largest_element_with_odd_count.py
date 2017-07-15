def biggest(listToMeasure):
    current_biggest = 0
    current_answer = None
    for element in listToMeasure:
        if element > current_biggest:
            current_biggest = element
            current_answer = element
    return current_answer

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    checked_elements = []
    elements_with_odd_counts = []
    for element in L:
        if L.count(element) % 2 != 0 and element not in checked_elements:
            checked_elements.append(element)
            elements_with_odd_counts.append(element)
    return biggest(elements_with_odd_counts)