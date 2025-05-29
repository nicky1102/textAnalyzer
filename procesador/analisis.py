# Funciones de análisis de texto

def contarPalabras(texto):
    texto = texto.split() # dividiendo texto en palabras
    return len(texto) # regresando la cantidad de palabras

def contarCaracteres(texto):
    return len(texto)

def detectarTokensEnTexto(texto, claves):
    texto = texto.lower().split()
    tokensEnTexto = [palabra for palabra in texto if palabra in claves]
    return tokensEnTexto