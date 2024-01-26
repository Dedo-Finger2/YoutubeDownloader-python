import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, VideoPrivate
from pathlib import Path

# Criando caminho para onde os vídeos serão baixados
VIDEO_END_PATH = Path.home() / "Videos/PyTubeDownloads"

# Criar pasta destino para os vídeos caso ela não exista
VIDEO_END_PATH.mkdir(parents=True, exist_ok=True)

# Pegar o link do vídeo
video_link = input("Digite o link do vídeo do YouTube: ")

# Buscar o vídeo
try:
    print("Buscando vídeo...")
    youtube_video = YouTube(video_link)
except (VideoUnavailable, VideoPrivate) as e:
    print("ERRO: Vídeo indisponível!")
    exit(1)

print("Vídeo encontrado!")

print("Pegando a melhor resolução...")
# Pegar a melhor resolução do vídeo
youtube_video_stream = youtube_video.streams.get_highest_resolution()

print(f"Baixando video com a resolução {youtube_video_stream.resolution} - ({round(youtube_video_stream.filesize_mb)} Mbs)...")
# Baixar o vídeo no caminho de destino
youtube_video_stream.download(output_path=VIDEO_END_PATH)

print("Concluído!")