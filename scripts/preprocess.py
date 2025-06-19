import re
def remove_emojis(data:str):
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
