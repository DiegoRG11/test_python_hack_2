"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    letras = ["f","z","m","n","r","u"]
    mas_de_3 = []

    for i in result:
        if i not in letras:
            contenedor = f"{i.replace("o","0").replace("a","@").replace("i","¡").upper()}" 
            mas_de_3.append(contenedor)
        else:
            mas_de_3.append(i.replace("f","F").replace("n","N").replace("R","r").replace("U","v"))

    result = "".join(mas_de_3)
    return result.replace("u","v")
