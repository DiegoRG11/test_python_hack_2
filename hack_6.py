"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    result = s
    new_ls = []

    for items in result:
        if items == "a": 
            new_ls.append("1")
        
        elif items == "b" or items == "d":   
            new_ls.append("-")
        
        elif items == "c":
            new_ls.append("3")
        
        elif items == "e":
            new_ls.append("5")
    
    if not new_ls:
        return ["0"]
    
    result = new_ls


    return result














# def fn_hack_6(s):
#     result = s
#     new_ls = []

#     for items in result:
#         if items == "a": 
#             new_ls.append("1")
        
#         elif items == "b":  
#             new_ls.append("-")
        
#         elif items == "c":
#             new_ls.append("3")
        
#         elif items == "d":
#             new_ls.append("-")
        
#         elif items == "e":
#             new_ls.append("5")
    
#     if not new_ls:
#         return ["0"]
    
#     result = new_ls


#     return result
