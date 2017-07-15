def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    exceeded_input_flag = False
    greatest_integer = 1
    integer_list = [1]
    current_triangle = 1
    triangular_flag = False
    while exceeded_input_flag == False:
        if current_triangle == k:
            triangular_flag = True
            return triangular_flag
        elif current_triangle > k:
            return triangular_flag
        elif current_triangle < k:
            greatest_integer += 1
            integer_list.append(greatest_integer)
            current_triangle = sum(integer_list)
            print integer_list
            print current_triangle