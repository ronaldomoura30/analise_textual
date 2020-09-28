# Importando os módulos Tweepy, Datetime MongoDB e Json
from pymongo import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json

# Adicione aqui sua Consumer Key
consumer_key = "MmJ63Oo0Jcq6lGgQkjD0QKOV7"

# Adicione aqui sua Consumer Secret
consumer_secret = "xNcTaurdvSgr1b9R9bDDlK5rvcmSU5m2SSo0QkEXskvtvgCC0z"

# Adicione aqui seu Access Token
access_token = "1083063439554154496-buvfzYLdWcE8pX0EM0JiUl0QN7Opcb"

# Adicione aqui seu Access Token Secret
access_token_secret = "tNrgARgvGW6oPEbvZOraqAXrYHuzEv9C7ht98PPMudzK1"

# Criando as chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

# Criando uma classe para capturar os stream de dados do Twitter e
# armazenar no MongoDB
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        print (obj)
        return True

# Criando o objeto mylistener
mylistener = MyListener()

# Criando o objeto mystream
mystream = Stream(auth, listener = mylistener)

# Preparando a Conexão com o MongoDB
# Criando a conexão ao MongoDB
client = MongoClient('localhost', 27017)

# Criando o banco de dados twitterdb
db = client.twitterdb

# Criando a collection "col"
col = db.tweets

# Criando uma lista de palavras chave para buscar nos Tweets
keywords = ['Big Data', 'Python', 'Data Mining', 'Data Science']

# Coletando os Tweets

# Iniciando o filtro e gravando os tweets no MongoDB
mystream.filter(track=keywords)



