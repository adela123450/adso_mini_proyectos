import nltk
from typing import List

def _safe_download(pkg: str):
    try:
        nltk.data.find(pkg)
    except LookupError:
        nltk.download(pkg.split('/')[-1], quiet=True)

# Descarga silenciosa de recursos mínimos
_safe_download('tokenizers/punkt')
_safe_download('corpora/stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_ES = set(stopwords.words('spanish'))

def clean_tokens(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        return []
    tokens = [t.lower() for t in word_tokenize(text)]
    tokens = [t for t in tokens if t.isalpha() and t not in STOP_ES and len(t) > 2]
    return tokens
