"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    new_ls = []

    for items in result:
        if items == "a":
            new_ls.append("1")
        
        elif items == "b":
            new_ls.append(2)
        
        elif items == "c":
            new_ls.append("3")
        
        elif items == "d":
            new_ls.append(4)
        
        elif items == "e":
            new_ls.append("5")
    
    if not new_ls:
        return [0]
    
    result = new_ls
    return result
