"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    new_dict = {}

    for key, value in result.items():
        if key == "foo":
            new_dict["Foo"] = value.capitalize().replace("k","")


    return new_dict
