from procesador import limpiarTexto
from procesador import contarPalabras

# __name__ == "__main__" sirve para:
# 1. Separar el código que define funciones y clases del código que las ejecuta.
#    Así puedes importar tus funciones desde otro archivo sin que se ejecute todo el programa.
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto = limpiarTexto(texto)
    print(f'Texto limpio: {texto}')
    
    cantPalabras = contarPalabras(texto)
    print(f'La cantidad de palabras en el texto brindado son: {cantPalabras}')