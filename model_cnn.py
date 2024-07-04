# Model
from tensorflow.keras.models import load_model
import numpy as np
# tokenizer
import pickle
import pythainlp as pythai
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pythainlp.tokenize import word_tokenize

# load model
model = load_model('./model/weight/model_cnn1.h5')
# load tokenizer
tokenizer_path = './model/weight/tokenizer_cnn1.pkl'
# tokenizer_path = './model/weight/tokenizer.pickle'
with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)


def convert_text(text):
    text = word_tokenize(text)
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text, maxlen=1191, padding='post', truncating='post')
    
    return text

def predict_cnn(inputText1, decode=False):
    inputText1 = convert_text(inputText1)
    predict = model.predict([inputText1])
    rounded = np.argmax(predict, axis=1)
    if decode:
        return 'ข้อความนี้มีลักษณะไปในทางเชิงบวก' if rounded[0] == 1 else 'ข้อความนี้มีลักษณะไปในทางเชิงลบ'
    return rounded

