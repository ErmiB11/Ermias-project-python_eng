"""
This module contains functions for translating text from 
English to French and from French to English.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator(os.environ['LANGUAGE_TRANSLATOR_APIKEY'])
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(os.environ['LANGUAGE_TRANSLATOR_URL'])

def english_to_french(input_text):
    """
    Translates English text to French.
    """
    response = language_translator.translate(
        text=input_text,
        source='en',
        target='fr'
    ).get_result()

    french_text = response['translations'][0]['translation']

    return french_text

ENGLISH_TEXT = "Hello, how are you?"
french_text = english_to_french(ENGLISH_TEXT)
print(french_text) 

def french_to_english(input_text):
    """
    Translates French text to English.
    """
    response = language_translator.translate(
        text=input_text,
        source='fr',
        target='en'
    ).get_result()

    english_text = response['translations'][0]['translation']

    return english_text

french_text = "Bonjour, comment ça va?"
english_text = french_to_english(french_text)
print(english_text)
