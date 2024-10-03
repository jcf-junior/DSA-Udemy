def group_anagrams(strings):
    output = []
    
    if strings == None:
        return output

    my_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in my_dict:
            my_dict[sorted_string] = []
        my_dict[sorted_string].append(string)
    output = list(my_dict.values())
    return output 


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""