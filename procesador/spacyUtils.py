import spacy

# Cargar el modelo de spaCy solo una vez
nlp = spacy.load("en_core_web_sm") # función que carga un modelo y devuelve un objeto. En este caso, un objeto de la clase Language

def obtenerLemas(texto):
    
    try:
        # Usamos assert para asegurar que no sea None
        assert texto is not None, "El texto no debe ser None"

        # Validación de tipo (si no es str, lanzamos TypeError)
        if not isinstance(texto, str):
            raise TypeError("Se esperaba un texto de tipo 'str'")

        # Validación de valor (texto vacío o solo espacios)
        if texto.strip() == "":
            raise ValueError("El texto no puede estar vacío")
        
        documento = nlp(texto) # texto procesado por spaCy, dividido en tokens (palabras, signos de puntuación, etc.).
        lemas = [token.lemma_ for token in documento] # for dentro de lista por comprensión (list comprehension)
        # for token in doc = para cada token (cada palabra o signo) en el texto procesado devuelvame el token.lemma_
        # token.lemma_ = es un atributo que contiene el lema de esa palabra, es decir, la forma base o raíz.
        entidades = [(ent.text, ent.label_) for ent in documento.ents] # lista comprehension de tuplas con for
        return lemas, entidades
    
    except (TypeError, ValueError, AssertionError) as e:
        print(f"[ERROR] Entrada inválida: {e}")
        return [], []
    
    except Exception as e:
        print(f'[Error Inesperado] {e}')
        return [], []