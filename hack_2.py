"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vocales = ["a", "e", "i", "o", "u"]
    new_txt = []
    for txt in result:
        if txt not in vocales:
            new_txt.append(txt)
    result = "".join(new_txt)
    return result
