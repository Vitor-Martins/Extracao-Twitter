from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
from mysql.connector import errorcode
import time
import json


# Configurar o charset para 'utf8mb4' para suporte a emoji
cnx = mysql.connector.connect(user='usuário', password='senha',
                              host='localhost',
                              database='nome do banco',
                              charset='utf8mb4')
cursor = cnx.cursor()

# Twitter consumer key, consumer secret, access token, access secret - https://apps.twitter.com/
ckey = "consumer key"
csecret = "consumer secret"
atoken = "access token"
asecret = "access secret"


# Classe stream listener
class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        # collect all desired data fields 
        if 'text' in all_data:
            tweet = all_data["text"]
            created_at = all_data["created_at"]
            retweeted = all_data["retweeted"]
            username = all_data["user"]["screen_name"]
            user_tz = all_data["user"]["time_zone"]
            user_location = all_data["user"]["location"]
            user_coordinates = all_data["coordinates"]

            # Se as coordenadas não estiverem presentes, armazene o valor em branco
            # caso contrário, obtenha o valor coordinates.coordinates
            if user_coordinates is None:
                final_coordinates = user_coordinates
            else:
                final_coordinates = str(all_data["coordinates"]["coordinates"])

            # insere os valores no banco
            cursor.execute(
                "INSERT INTO Nome_da_tabela (created_at, username, tweet, coordinates, userTimeZone, userLocation, retweeted) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (created_at, username, tweet, final_coordinates, user_tz, user_location, retweeted))
            cnx.commit()

            # Vai imprimir no terminal o usuário e o tweet que estão sendo escutados
            print((username, tweet))

            return True
        else:
            return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# Cria um termo e filtro do que será escutado
twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["bolsonaro"], languages=["en"], stall_warnings=True)
twitterStream.filter(track=["flamengo"], stall_warnings=True)
