from googletrans import Translator

def translate(text):
    translator = Translator()
    t = translator.translate(text=text, dest='ja')
    return t.text
