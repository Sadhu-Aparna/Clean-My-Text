# Complete Text Cleaning (Multiple techniques comined)
import streamlit as st
import string
import re
import unicodedata
# import contractions
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

st.title(" Clean My Text 🧼")
text = st.text_area("Enter Your Text:")

lower = st.checkbox("Convert to Lowercase")
remove_punc = st.checkbox("Remove Punctuation")
remove_num = st.checkbox("Remove Numbers")
remove_stopwords = st.checkbox("Remove Stopwords")
remove_html = st.checkbox("Remove HTML Tags")
remove_urls = st.checkbox("Remove URLs")
remove_extra_space = st.checkbox("Remove Extra Spaces")
expand_contractions = st.checkbox("Expanding Contractions")
remove_emojis = st.checkbox("Removing Emoji's")
replace_emojis = st.checkbox("Converting Emoji's")
remove_accents = st.checkbox("Removing Accents")

if st.button("Clean My Text"):
    result = text
    # Lowercase
    if lower:
        result = result.lower()
    # Remove Punctuation
    if remove_punc:
        result = ''.join(c for c in result if c not in string.punctuation)
    # Remove digits(using isdigit)
    if remove_num:
        result = ''.join(c for c in result if not c.isdigit())
    # Remove stopwords
    if remove_stopwords:
        words = word_tokenize(result)
        result = ' '.join([word for word in words
                           if word not in stopwords.words('english')])
    # Remove HTML Tags
    if remove_html:
        result = re.sub(r'<.*?>','',result)
    # Remove URLs
    if remove_urls:
        result = re.sub(r'http\S+','',result)
    # Remove Extra Spaces
    if remove_extra_space:
        result = " ".join(result.split())
    # Expanding Contractions
    if expand_contractions:
        result = contractions.fix(result)
    # Removing Emoji's
    if remove_emojis:
        result = emoji.replace_emoji(result, replace='')
    # Replacing emojis
    if replace_emojis:
        result = emoji.demojize(result)
    # Removing Accents
    if remove_accents:
        result = unidecode(result)

    st.subheader("Cleaned Text:")
    st.write(result)
