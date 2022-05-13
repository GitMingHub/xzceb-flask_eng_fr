"""IBM Translator API"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2020-10-23',authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """English to French translation"""
    if english_text != "":
        french_translation=language_translator.translate(
            text=english_text, model_id = "en-fr").get_result()

        trans_french_text=french_translation['translations'][0]['translation']
    else:
        print ("Erreur, aucune entree (Error no Input)")
        trans_french_text = "Pas d'entree (No Input)"
    return trans_french_text

def french_to_english(french_text):
    """English to French translation"""
    if french_text != "":
        english_translation=language_translator.translate(
            text=french_text, model_id = "fr-en").get_result()

        trans_english_text=english_translation['translations'][0]['translation']
    else:
        print ("Error no Inputx (Error no Input)")
        trans_english_text = "No Input (Pas d'entree)"
    return trans_english_text
