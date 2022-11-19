import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
global slowo
slowo = ""
global dlugosc
import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)

global mdlugosc


def chat():
    pytanie = 0
    global slowo
    global mdlugosc
    marzec = ""
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    while True:
        global dlugosc
  #      print(dlugosc)
        while True:
            if dlugosc == mdlugosc:
                break

            if (inp[dlugosc] != " ") and (inp[dlugosc] != "Ω"):
                slowo = slowo+inp[dlugosc]

                dlugosc = dlugosc+1

            else:

                break
        if (slowo == "?"):
            pytanie = 1
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([slowo]),
                                             truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                marzec = marzec+str(np.random.choice(i['responses']))


           #         dlugosc = dlugosc-1

                if inp[dlugosc] == "Ω":
                    if pytanie == 1 or inp[dlugosc-1]=="?":
                        marzec=marzec+"❓"
                    print(" ")
                    print("Result:")
                    print(marzec)
                    print("Generated from text with Bird EmojiAI, powered by Google TensorFlow")
                    slowo = str(input("Press ENTER/RETURN to quit"))
                    quit()
                else:
                    if inp[dlugosc]==" ":
                        dlugosc=dlugosc+1
                    slowo = ""
                
                    break



print(Fore.YELLOW + "Type text to convert to Discord emojis" + Style.RESET_ALL)
inp = str(input())
inp = inp+"Ω"
dlugosc = len(inp)
mdlugosc = dlugosc
dlugosc = dlugosc * -1
chat()
print("Done")
