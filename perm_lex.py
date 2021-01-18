# a is a string
# str -> list
# returns all the permutations of the characters in a given string
def perm_gen_lex(a): 
    """ returns all the permutations of the characters of the given string"""
    fin_list = []
    if len(a) == 1: 
        return [a] # a case where the given string contains only a single character
    elif len(a) < 1:
        return [] # a case where the given string is blank
    else:
        """loop through the string to remove each character and add that character to the front, 
        combining with the remaining characters"""
        for rmvd_alph in a:
            rest = a.replace(rmvd_alph, "") # reduction
            for i in perm_gen_lex(rest): # recursion happens
                fin_list.append(rmvd_alph+i) # appending combined string to the list
    return fin_list            
            
            


    