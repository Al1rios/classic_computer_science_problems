# import pytube
# import pyglet

# # Função para reproduzir o vídeo
# def play_video(video_path):
#     player = pyglet.media.Player()
#     source = pyglet.media.StreamingSource()
#     media = pyglet.media.load(video_path)
#     player.queue(media)
#     player.play()

#     # Espera até que o vídeo termine de ser reproduzido
#     pyglet.app.run()

# # URL do vídeo do YouTube
# video_url = 'https://www.youtube.com/watch?v=1qNCGQyt1aU'

# # Baixa o vídeo usando pytube
# youtube = pytube.YouTube(video_url)
# video = youtube.streams.get_highest_resolution()
# video.download()

# # Caminho para o arquivo de vídeo baixado
# video_path = video.default_filename

# # Reproduz o vídeo
# play_video(video_path)


from pytube import YouTube

yt_video = YouTube("https://www.youtube.com/watch?v=iqAtv1ORcLc")

v_file = yt_video.streams.filter(file_extension="mp4").get_by_resolution("360p")

v_file.download(".")
