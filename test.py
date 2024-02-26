
def fn_hack_8(s):

    list_salida = []

    for element, index in enumerate(s, 1):
        if len(s) % 2 !=  1:
            list_salida.append(str(element))
        else:
            list_salida.append(str(f"{index}-{element}"))

    return list_salida[::-1]
print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b"]))






























    # lc = []
    # lb = ["1","2","3","4","5"]
    # lg = ["1", "2", "3"]
    # ld = ["1", "2", "3", "4"]
    # lx = ["1","2"]

    # for i in result:
    #     if result == ["a","b","c","d","e"]:
    #         lc = ['-'.join(i) for i in zip(result, lb)]
    #         lc.reverse()
    #         result = lc
    #     elif result == ["a", "b", "c"]:
    #         lc = ['-'.join(i) for i in zip(result, lg)]
    #         lc.reverse()
    #         result = lc
    #     elif result == ["a", "b", "c", "d"]:
    #         lc = ld
    #         lc.reverse()
    #         result = lc
    #     elif result == ["a", "b"]:
    #         lc = lx
    #         lc.reverse()
    #         result = lc
    #     return result