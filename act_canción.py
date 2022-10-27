#Descargar canción

from pytube import YouTube
from pytube import Playlist

def descargaCancion(url:str):
    youtube = YouTube(url)
    print (youtube.author)
    print ("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()
#descargaCancion("https://www.youtube.com/watch?v=X9obsPrmJCk")


def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        print (f"Descargando canción: {cancion.title}")
        #descagarCancion(cancion)         
        cancion.streams.get_audio_only().download("canciones/")
        print ("*************\n")

#Programa principal

url = "https://www.youtube.com/watch?v=NN1f066QTMU&list=PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J"

descargarLista(url)

