import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')


def clean_text(text: str) -> str:
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    cleaned_tokens = []
    for token in tokens:
        lower_token = token.lower()
        len_check = len(lower_token) >= 3
        start_check = not (lower_token.startswith('http') or lower_token.startswith('\\') or lower_token.startswith(':'))
        stop_word_check = lower_token not in stop_words
        if len_check and start_check and stop_word_check:
            cleaned_tokens.append(re.sub('[,.!?]|<br \/>\+|<br \/>', '', lower_token))
    return ' '.join(cleaned_tokens)


