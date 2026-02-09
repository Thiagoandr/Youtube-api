"""
Funções utilitárias para o YouTube Downloader
"""
import os
import tempfile
from pytubefix import YouTube


def format_duration(seconds):
    """Converte segundos em formato MM:SS"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


def format_views(views):
    """Formata número de visualizações"""
    if views >= 1_000_000:
        return f"{views/1_000_000:.1f}M"
    elif views >= 1_000:
        return f"{views/1_000:.1f}K"
    else:
        return str(views)


def format_filesize(size_bytes):
    """Formata tamanho de arquivo em MB"""
    if not size_bytes:
        return "N/A"
    return f"{size_bytes / 1024 / 1024:.1f} MB"


def get_video_info(url):
    """
    Obtém informações do vídeo do YouTube
    
    Args:
        url (str): URL do vídeo
        
    Returns:
        dict: Dicionário com informações do vídeo ou None em caso de erro
    """
    try:
        yt = YouTube(url)
        return {
            'title': yt.title,
            'author': yt.author,
            'length': yt.length,
            'views': yt.views,
            'thumbnail': yt.thumbnail_url,
            'yt_object': yt
        }
    except Exception as e:
        return None


def get_progressive_streams(yt_object):
  
    streams = yt_object.streams.filter(progressive=True).order_by('resolution').desc()
    
    options = {}
    for stream in streams:
        size_mb = format_filesize(stream.filesize)
        res = stream.resolution or "N/A"
        fps = stream.fps or "N/A"
        ext = stream.mime_type.split('/')[-1].upper()
        label = f"{res} - {fps}fps - {ext} ({size_mb})"
        options[label] = stream
    
    return options


def get_video_only_streams(yt_object):
 
    streams = yt_object.streams.filter(adaptive=True, only_video=True).order_by('resolution').desc()
    
    options = {}
    for stream in streams:
        size_mb = format_filesize(stream.filesize)
        res = stream.resolution or "N/A"
        fps = stream.fps or "N/A"
        ext = stream.mime_type.split('/')[-1].upper()
        label = f"{res} - {fps}fps - {ext} ({size_mb}) - SEM ÁUDIO"
        options[label] = stream
    
    return options


def get_audio_streams(yt_object):
    
    streams = yt_object.streams.filter(only_audio=True).order_by('abr').desc()
    
    options = {}
    for stream in streams:
        size_mb = format_filesize(stream.filesize)
        abr = stream.abr or "N/A"
        ext = stream.mime_type.split('/')[-1].upper()
        label = f"{abr} - {ext} ({size_mb})"
        options[label] = stream
    
    return options


def download_stream(url, stream, progress_callback=None):
 
    temp_dir = tempfile.mkdtemp()
    
    # Criar novo objeto YouTube com callback
    yt = YouTube(url, on_progress_callback=progress_callback)
    stream_download = yt.streams.get_by_itag(stream.itag)
    
    # Baixar
    file_path = stream_download.download(output_path=temp_dir)
    
    # Ler arquivo
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    
    # Limpar arquivo temporário
    os.remove(file_path)
    
    return file_bytes


def get_file_extension(stream):
    """Retorna a extensão do arquivo baseada no stream"""
    return stream.mime_type.split('/')[-1]


def sanitize_filename(filename):
    """Remove caracteres inválidos do nome do arquivo"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename
