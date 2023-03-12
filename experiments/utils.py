import requests
from bs4 import BeautifulSoup
import re
import time
from copy import deepcopy
import string
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import roc_auc_score
import numpy as np

API_KEY = "<GOOGLE_API_KEY>"
SEARCH_ENGINE_ID = "<SEARCH_ENGINE_ID>"

template_url = "https://pubmed.ncbi.nlm.nih.gov/<doc_id>/"

clean_punct_regexp = re.compile(r'[^\w\s]')
clean_space_regexp = re.compile(" +")
lemmatizer = WordNetLemmatizer()

def get_abstract(doc_id: str, template_url=template_url) -> str:
    """
    Obtain PubMed paper abstract by its ID
    """
    
    time.sleep(0.1)
    
    url = deepcopy(template_url)
    url = url.replace("<doc_id>", doc_id)
    
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    res = bs.find_all("div", {"abstract-content selected"})
    
    if not res: # no abstract
        return ""
    
    res = " ".join([str(item) for item in res[0].find_all("p")])
    
    def clean_abstract(text):
        text = re.sub("(<strong class=\"sub-title\">|</strong>|<p>|</p>|<i>|</i>|<b>|</b>|<sub>|</sub>|\&lt\;|\\n)", " ", text)
        text = re.sub(" +", " ", text).strip()
        return text

    return clean_abstract(str(res))


def get_title(doc_id: str, template_url=template_url) -> str:

    """
    Obtain PubMed paper title by its ID
    """
    
    
    # time.sleep(0.1)
    
    url = deepcopy(template_url)
    url = url.replace("<doc_id>", doc_id)
    
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    res = bs.find_all("h1", {"heading-title"})
    
    if not res:
        return ""
    
    text = res[0].text
    text = re.sub("\\n", " ", res[0].text)
    text = re.sub(" +", " ", text).strip()
    
    return text

def normalize_text(
    text: str, 
    need_lemmatize = True, 
    clean_punct_regexp = clean_punct_regexp,
    clean_space_regexp = clean_space_regexp
) -> str:
    
    """
        Remove punctuation and lemmatize text (if needed)
        
    """
    
    text = text.lower()
    clean_text = clean_punct_regexp.sub(" ", text)
    clean_text = clean_space_regexp.sub(" ", clean_text)
    
    if need_lemmatize:
        clean_text = " ".join([lemmatizer.lemmatize(token) for token in clean_text.split()])
        
    return clean_text
    
    
def calc_auc(df, agg_method, agg_col="prediction", label_col="label"):
    """
    Calculate AUC-ROC based on predictions
    
    agg_method values:
        'avg' - by prediction averaging
        'top1' - by top-1 document
        'norm_linear' - by linear scaling
        'norm_log' - by log scaling    
    """
    
    true = []
    pred = []
    
    for _, group in df.groupby(["query_id", "data_source"]):
        true.append(group[label_col].tolist()[0])
        
        if agg_method == "avg":
            new_pred = group.prediction.mean()
            pred.append(new_pred)
            
        elif agg_method == "top1":
            new_pred = group['prediction'].tolist()[0]
            pred.append(new_pred)
            
        elif agg_method == "norm_linear":
            pred_list = group['prediction'].tolist()
            coefs = np.linspace(0, 1, len(group) + 1)[1:]
            normed_coefs = (coefs / np.sum(coefs))[::-1]
            
            new_pred = np.dot(normed_coefs, pred_list)
            pred.append(new_pred)
            
        elif agg_method == "norm_log":
            pred_list = group['prediction'].tolist()
            coefs = np.logspace(0, 1, len(group) + 1)[1:]
            normed_coefs = (coefs / np.sum(coefs))[::-1]
            
            new_pred = np.dot(normed_coefs, pred_list)
            pred.append(new_pred)
            
        else:
            raise NotImplementedError
            
    return roc_auc_score(true, pred)
            