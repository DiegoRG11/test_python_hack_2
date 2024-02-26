"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    nueva_lista = []
    contador = 1
    
    for _ in result:
        nuevo_diccionario = {}
        nuevo_diccionario[str(contador)] = str(contador + 1)
        contador += 2
        
        nueva_lista.append(nuevo_diccionario)
    
    return nueva_lista
