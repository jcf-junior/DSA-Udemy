def first_non_repeating_char(string):
    repeats = {}
    
    for i in string:
        if i not in repeats:
            repeats[i] = False
        elif i in repeats:
            repeats[i] = True

    for i in repeats:
        if repeats[i] == False:
            return i
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""