#Descargar canción

from pytube import YouTube

def descargaCancion(url:str):
    youtube = YouTube(url)
    print (youtube.author)
    print ("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

descargaCancion("https://www.youtube.com/watch?v=X9obsPrmJCk")