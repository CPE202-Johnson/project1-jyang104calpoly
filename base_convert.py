# num is a int
# b is a int
# int int -> str
# converts a base 10 number to base b by returning a string representation of it, using recursion
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num//b == 0: 
        a = str(num%b)
        if a == "10":
            return "A"
        elif a == "11":
            return "B"
        elif a == "12":  
            return "C"
        elif a == "13":  # converts a number greater than 10 at the very front into alphabet                         
            return "D"   # ex) "10BCDEF" -> "ABCDEF"
        elif a == "14":
            return "E"
        elif a == "15":
            return "F"
        else:
            return a
    else:
        """solve for remainder (num%b) and quotient (num//b) and return the string representation of the remainder by using recursion"""
        if num%b == 10: # a case where a remainder is 10
            return  convert(num//b,b) + "A"
        elif num%b == 11: # a case where a remainder is 11
            return  convert(num//b,b) + "B"
        elif num%b == 12: # a case where a remainder is 12
            return  convert(num//b,b) + "C"
        elif num%b == 13: # a case where a remainder is 13
            return  convert(num//b,b) + "D"
        elif num%b == 14: # a case where a remainder is 14
            return  convert(num//b,b) + "E"
        elif num%b == 15: # a case where a remainder is 15
            return  convert(num//b,b) + "F"
        else:
            return convert(num//b,b) + str(num%b) # recursion happens