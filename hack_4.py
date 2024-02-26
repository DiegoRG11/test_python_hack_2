"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    remove = ["f", "b", "n"]
    final = []

    for items in result:
        if items not in remove:
            final.append(items)
    
    result = "".join(final)
    return result
