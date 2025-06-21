import re
from etnltk.lang.am import normalize
from etnltk.lang.am.stop_words import STOP_WORDS
from etnltk.lang.am.preprocessing import remove_punct
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def remove_emojis(data:str):
    data = re.sub(r'http\S+', '', data)
    # Remove usernames and hashtags
    data = re.sub(r'@[A-Za-z0-9_]+', '', data)
    data = re.sub(r'#[A-Za-z0-9_]+', '', data)
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        u"\u00A0"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def replace_tabs_with_space(data:str):
    content = data.replace('\t',' ')
    return content

def remove_newline(data:str):
    return data.replace('\n', ' ')

def remove_spacing_dots(data:str):
    return data.replace('.','')

def process_text(data:str):
    data = remove_emojis(data)
    data = replace_tabs_with_space(data)
    data = remove_newline(data)
    return remove_spacing_dots(data)


def is_amharic(word:str):
    return any('\u1200' <= char <= '\u137f' for char in word)

def process_language(text:str):
    try:
        tokens = word_tokenize(text)
        processed_tokens = []
        stemmer = PorterStemmer()
        for token in tokens:
            remove_punct(token)
            if(is_amharic(token)):
                am_normalized_token = normalize(token)
                if am_normalized_token not in STOP_WORDS:
                    processed_tokens.append(am_normalized_token)
            else:
                stop_words = set(stopwords.words('english'))
                token = token.lower()
                en_token = stemmer.stem(token)
                if token is not stop_words:
                    processed_tokens.append(token)
        print(processed_tokens)
        return ' '.join(processed_tokens)
    except Exception as e:
        print(f"{e}")
            
