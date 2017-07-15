def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def finding_poly(x):
        current_total = 0
        for number in range(0, len(L)):
           exponent_count = (len(L)-1) - number
           current_total += L[number] * x ** exponent_count
           exponent_count -= 1
        return current_total
    return finding_poly