from src.nlp_utils import clean_tokens

def test_clean_tokens():
    text = "Esta es una prueba simple con NLTK y análisis."
    tokens = clean_tokens(text)
    # Debe mantener "prueba" y quitar "esta" (stopword)
    assert "prueba" in tokens
    assert "esta" not in tokens
    # Sólo letras
    assert all(t.isalpha() for t in tokens)
