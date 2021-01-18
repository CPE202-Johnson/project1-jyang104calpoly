# CPE 202 Project 1
# num is a int
# b is a int
# int int -> str
# converts a base 10 number to base b by returning a string representation of it, using recursion
def convert(num,b):
    num_alph_list = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"] # a list for converting numbers greater than 9 to alphabet
    if num//b == 0:
        return str(num_alph_list[num]) # base case
    else:
        return str(convert(num//b,b)) + str(num_alph_list[num%b]) # where recursion happens