import json
import os
import pandas as pd
from stopwords import stop_words
import unicodedata
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from pandas.io.json import json_normalize

###################################################
##                                               ##
##     NOT WORKING - Recursive fun is broken     ##            
##          and don't work as expected           ##
##                                               ##
###################################################

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)

def remove_stop_words_from_text(text):
    filtered_word=[]
    tokenized_word = word_tokenize(text)#, language='french')

    for w in tokenized_word:
        word_lower = w.lower()
        if word_lower not in stop_words:
            # remove virgule is there is some in the word
            remove_comas_word = word_lower.replace(',', '') # remove comas
            remove_dots_word = word_lower.replace('.', '') # remove dots
            clean_word = strip_accents(remove_dots_word) # remove accent
            # remove ["l", "'","incompa"]
            filtered_word.append(clean_word)
    return ' '.join(filtered_word)

def read_file():
    with open(os.path.join("dataset", "code-construction-habitation-all.json"), mode="r",  encoding="utf8") as laws_file:
        json_file_dict = json.loads(laws_file.read())
        return json_file_dict

laws_dict = read_file()

global all_things 
all_things = []
def get_edges(treedict, parent=None, current_row={}):
    name = treedict["data"]["id"]
    if parent is not None:
        if "title" in treedict["data"]:
            # problem here is pandas will use the first "IDs" as column name. So may we create generate custom column name as parent1
            i = 0
            key = "parent_"+str(i)
            i += 1
            while key in current_row:
                key += "_"+str(i)
                i += 1
            current_row[key] = name
    if "children" not in treedict:
        text = treedict["data"]["texte"]
        current_row["text"] = text
        current_row["text_to_index"] = remove_stop_words_from_text(text)
        current_row["article_id"] = name
        all_things.append(current_row.copy())
        current_row = {}
    else:
        for item in treedict["children"]:
            if isinstance(item, dict):
                get_edges(item, parent=name, current_row=current_row)

get_edges(laws_dict)
df = pd.DataFrame(all_things)
print (df.head())
# df.to_csv('test-legi-text-transfo.csv',index=None)
# df.to_json("test-legi-text-transfo.json", orient = "records", force_ascii=False)
