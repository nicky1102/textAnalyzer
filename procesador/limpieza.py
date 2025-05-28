import re # expresiones regulares de python. Sirve para buscar, reemplazar o validar patrones dentro de cadenas de texto.

def limpiarTexto(texto):
    texto = texto.lower() # 1. pasando a minúscula
    texto = re.sub(r'[^a-z\s]', '', texto) # re.sub(patrón, reemplazo, texto) # 2. Eliminando todo lo que no es letra abecedario y espacios 
    texto = re.sub(r'\s+', ' ', texto).strip() # encuentra uno o más espacios seguidos y los reemplaza por un solo espacio.
    return texto