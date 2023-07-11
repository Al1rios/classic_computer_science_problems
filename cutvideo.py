from moviepy.editor import VideoFileClip

def cortar_video(input_path, output_path, start_time, end_time):
    video = VideoFileClip(input_path)
    novo_video = video.subclip(start_time, end_time)
    novo_video = novo_video.set_audio(None)
    novo_video.write_videofile(output_path, codec="libx264", audio=False)

# Caminho do vídeo de entrada
input_path = "pele.mp4"

# Caminho para salvar o novo vídeo
output_path = "video4.mp4"

# Tempo de início e fim em minutos e segundos
start_time = '00:26:29'
end_time = '00:27:00'

# Chama a função para cortar o vídeo
cortar_video(input_path, output_path, start_time, end_time)

