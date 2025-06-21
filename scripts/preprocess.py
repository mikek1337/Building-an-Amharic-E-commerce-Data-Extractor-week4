import re
from etnltk.lang.am import normalize
from etnltk.lang.am.stop_words import STOP_WORDS
from etnltk.lang.am.preprocessing import remove_punct
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def remove_emojis(data:str):
    """
    Removes URLs, usernames, hashtags, and emojis from the input string.

    Args:
        data (str): The input string to be cleaned.

    Returns:
        str: The cleaned string with URLs, usernames, hashtags, and emojis removed.
    """
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
    """
    Replaces all tab characters in the input string with spaces.

    Args:
        data (str): The input string potentially containing tab characters.

    Returns:
        str: The modified string with all tab characters replaced by spaces.
    """
    content = data.replace('\t',' ')
    return content

def remove_newline(data:str):
    """
    Removes all newline characters from the input string and replaces them with spaces.

    Args:
        data (str): The input string from which newline characters will be removed.

    Returns:
        str: The modified string with newline characters replaced by spaces.
    """
    return data.replace('\n', ' ')

def remove_spacing_dots(data:str):
    """
    Removes all dot ('.') characters from the input string.

    Args:
        data (str): The input string from which dots will be removed.

    Returns:
        str: The string with all dots removed.
    """
    return data.replace('.','')

def process_text(data:str):
    """
    Removes unnessary characters

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word contains any Amharic characters (Unicode range U+1200 to U+137F), False otherwise.
    """
    data = remove_emojis(data)
    data = replace_tabs_with_space(data)
    data = remove_newline(data)
    return remove_spacing_dots(data)


def is_amharic(word:str):
    """
    Checks if a given word contains at least one Amharic (Ethiopic) character.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word contains any Amharic characters (Unicode range U+1200 to U+137F), False otherwise.
    """
    return any('\u1200' <= char <= '\u137f' for char in word)

def process_language(text:str):
    """
    Processes a given text by tokenizing, normalizing, and filtering out stop words for both Amharic and English languages.

    For Amharic tokens:
        - Normalizes the token.
        - Removes the token if it is a stop word.

    For English tokens:
        - Converts the token to lowercase.
        - Applies stemming.
        - Removes the token if it is a stop word.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: A string of processed tokens joined by spaces.

    Raises:
        Exception: Prints the exception message if an error occurs during processing.
    """
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
            
