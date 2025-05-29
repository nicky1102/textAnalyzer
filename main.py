from procesador import limpiarTexto,contarPalabras, contarCaracteres,obtenerLemas

# __name__ == "__main__" sirve para:
# 1. Separar el código que define funciones y clases del código que las ejecuta.
#    Así puedes importar tus funciones desde otro archivo sin que se ejecute todo el programa.
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto = limpiarTexto(texto)
    print(f'Texto limpio: {texto}')
    
    cantPalabras = contarPalabras(texto)
    print(f'La cantidad de palabras en el texto brindado son: {cantPalabras}')
    
    cantCaracteres = contarCaracteres(texto)
    print(f'La cantidad de caracteres en el texto brindado son: {cantCaracteres}')
    
    lemas, entidades = obtenerLemas(texto)
    print("Lemas:")
    print(lemas)

    print("\nEntidades nombradas:")
    for entidad, tipo in entidades:
        print(f"{entidad} ({tipo})")