# Funciones de análisis de texto

def contarPalabras(texto):
    texto = texto.split() # dividiendo texto en palabras
    return len(texto) # regresando la cantidad de palabras

def contarCaracteres(texto):
    return len(texto)

def detectarTokensEnTexto(texto, claves):
    texto = texto.lower().split() # Convierte todo el texto a minúsculas para que la búsqueda no dependa de mayúsculas/minúsculas.
                                  # divide el texto en palabras usando split(), que por defecto separa por espacios.
    tokensEnTexto = [palabra for palabra in texto if palabra in claves] # Si esa palabra está dentro de la lista claves, se guarda.
    return tokensEnTexto # Devuelve una lista solo con las coincidencias encontradas.