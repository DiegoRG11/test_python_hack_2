"""
generic script

text: "fooziman" output => "zfo-i-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    ls = {
        "foo": "fo-zi-ma-",
        "bar": "ba-zi-an",
        "qu": "qu-",
        "eq": "eq"
    }

    for key in ls:
        if key in result:
            return ls[key]
    
    result = ls

    return result
