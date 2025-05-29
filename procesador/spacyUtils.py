import spacy

# Cargar el modelo de spaCy solo una vez
nlp = spacy.load("en_core_web_sm") # función que carga un modelo y devuelve un objeto. En este caso, un objeto de la clase Language

def obtenerLemas(texto):
    documento = nlp(texto) # texto procesado por spaCy, dividido en tokens (palabras, signos de puntuación, etc.).
    lemas = [token.lemma_ for token in documento]
    # for token in doc = para cada token (cada palabra o signo) en el texto procesado devuelvame el token.lemma_
    # token.lemma_ = es un atributo que contiene el lema de esa palabra, es decir, la forma base o raíz.
    entidades = [(ent.text, ent.label_) for ent in documento.ents]
    return lemas, entidades