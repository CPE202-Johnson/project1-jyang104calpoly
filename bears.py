# CPE 202 Project 1
# n is an integer
# int -> bool
# returns true if the given number ends up by 42 after applying conditions, false otherwise.
def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""
    if n == 42:
        return True # base case
    elif n < 42:
        return False # base case 
    else:
        if n % 2 == 0 and bears(int(n/2)): # if n is divisible by 2, divide n by 2
            return True
        if n % 3 == 0 or n % 4 == 0: 
            ls_t_f = int(str(n)[-1]) # first digit from the right
            ls_t_s = int(str(n)[-2]) # second digit from the right
            mult_digt = ls_t_f * ls_t_s
            if mult_digt != 0 and bears(n-mult_digt): # if n is divible by 3 or 4, multiply n's first and second digit from the right and subtract that value from n
                return True                           # mult_digit != 0 prevents infinite recursion 
        if n % 5 == 0 and bears(int(n-42)): # if n is divisible by 5, subtract n by 42
            return True
        else:
            return False

