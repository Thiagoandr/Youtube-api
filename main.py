
import streamlit as st
from pytubefix import YouTube

# Imports 
from style import apply_custom_css, get_page_config, get_footer_html, get_help_content
from utils import (
    get_video_info, 
    get_progressive_streams, 
    get_video_only_streams, 
    get_audio_streams,
    download_stream,
    get_file_extension,
    sanitize_filename
)
from components import (
    show_video_info,
    create_download_section,
    show_welcome_screen,
    show_error,
    show_success
)


def main():

    
    # Configuração da página
    st.set_page_config(**get_page_config())
    
    # Aplicar CSS customizado
    st.markdown(apply_custom_css(), unsafe_allow_html=True)
    
    st.title("Downloader")
    st.markdown("---")
    
    # Input da URL
    url = st.text_input(
        "🔗 Cole a URL do vídeo do YouTube:", 
        placeholder="https://www.youtube.com/watch?v=..."
    )
    
    # Inicializar session state
    if 'video_info' not in st.session_state:
        st.session_state.video_info = None
    
    # Botão para carregar informações do vídeo
    if url and st.button("🔍 Buscar Informações do Vídeo", use_container_width=True):
        with st.spinner("Carregando informações..."):
            video_info = get_video_info(url)
            
            if video_info:
                st.session_state.video_info = video_info
            else:
                show_error("Erro ao carregar vídeo. Verifique a URL e tente novamente.")
                st.session_state.video_info = None
    
    # Exibir informações do vídeo se disponíveis
    if st.session_state.video_info:
        show_video_info(st.session_state.video_info)
        
        st.markdown("---")
        st.subheader("⬇️ Opções de Download")
        
        yt = st.session_state.video_info['yt_object']
        
        # Criar tabs
        tab1, tab2, tab3 = st.tabs([
            "🎥 Vídeo + Áudio", 
            "🎬 Só Vídeo (Sem Áudio)", 
            "🎵 Só Áudio"
        ])
        
        # TAB 1: Vídeo + Áudio
        with tab1:
            handle_progressive_download(url, yt)
        
        # TAB 2: Só Vídeo
        with tab2:
            handle_video_only_download(url, yt)
        
        # TAB 3: Só Áudio
        with tab3:
            handle_audio_download(url, yt)
    
    else:
        # Tela de boas-vindas
        show_welcome_screen()
        
        # Seção de ajuda
        with st.expander("📖 Como usar"):
            st.markdown(get_help_content())
    
    # Rodapé
    st.markdown("---")
    st.markdown(get_footer_html(), unsafe_allow_html=True)


def handle_progressive_download(url, yt):
    """Gerencia download de vídeos progressivos (vídeo + áudio)"""
    
    def download_callback(stream, label):
        try:
            with st.spinner("Baixando..."):
                # Progress tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def progress_callback(stream, chunk, bytes_remaining):
                    total_size = stream.filesize
                    bytes_downloaded = total_size - bytes_remaining
                    percentage = bytes_downloaded / total_size
                    progress_bar.progress(percentage)
                    status_text.text(f"📥 Baixando... {percentage*100:.1f}%")
                
                # Download
                file_bytes = download_stream(url, stream, progress_callback)
                
                progress_bar.progress(1.0)
                status_text.text("✅ Download concluído!")
                
                # Botão de download
                file_ext = get_file_extension(stream)
                filename = sanitize_filename(yt.title)
                
                st.download_button(
                    label=f"💾 Salvar ({label.split(' - ')[0]})",
                    data=file_bytes,
                    file_name=f"{filename}.{file_ext}",
                    mime=stream.mime_type,
                    use_container_width=True
                )
                
                show_success("Pronto para download!")
                
        except Exception as e:
            show_error(f"Erro ao baixar: {str(e)}")
    
    stream_options = get_progressive_streams(yt)
    
    create_download_section(
        stream_options=stream_options,
        selected_key="prog_select",
        button_text="📥 Baixar Vídeo + Áudio",
        button_key="prog_btn",
        download_callback=download_callback,
        info_message="📦 Vídeo com áudio já combinado - Melhor opção para a maioria dos casos"
    )


def handle_video_only_download(url, yt):
    """Gerencia download de vídeo sem áudio"""
    
    def download_callback(stream, label):
        try:
            with st.spinner("Baixando vídeo..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def progress_callback(stream, chunk, bytes_remaining):
                    total_size = stream.filesize
                    bytes_downloaded = total_size - bytes_remaining
                    percentage = bytes_downloaded / total_size
                    progress_bar.progress(percentage)
                    status_text.text(f"📥 Baixando... {percentage*100:.1f}%")
                
                file_bytes = download_stream(url, stream, progress_callback)
                
                progress_bar.progress(1.0)
                status_text.text("✅ Download concluído!")
                
                file_ext = get_file_extension(stream)
                filename = sanitize_filename(yt.title)
                
                st.download_button(
                    label=f"💾 Salvar Vídeo SEM Áudio ({label.split(' - ')[0]})",
                    data=file_bytes,
                    file_name=f"{filename}_video_only.{file_ext}",
                    mime=stream.mime_type,
                    use_container_width=True
                )
                
                show_success("Vídeo (sem áudio) pronto!")
                
        except Exception as e:
            show_error(f"Erro ao baixar: {str(e)}")
    
    stream_options = get_video_only_streams(yt)
    
    create_download_section(
        stream_options=stream_options,
        selected_key="video_select",
        button_text="📥 Baixar Só Vídeo",
        button_key="video_btn",
        download_callback=download_callback,
        warning_message="⚠️ **ATENÇÃO:** Estes vídeos NÃO têm áudio!"
    )


def handle_audio_download(url, yt):
    """Gerencia download de áudio"""
    
    def download_callback(stream, label):
        try:
            with st.spinner("Baixando áudio..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def progress_callback(stream, chunk, bytes_remaining):
                    total_size = stream.filesize
                    bytes_downloaded = total_size - bytes_remaining
                    percentage = bytes_downloaded / total_size
                    progress_bar.progress(percentage)
                    status_text.text(f"🎵 Baixando... {percentage*100:.1f}%")
                
                file_bytes = download_stream(url, stream, progress_callback)
                
                progress_bar.progress(1.0)
                status_text.text("✅ Download concluído!")
                
                extension = get_file_extension(stream)
                filename = sanitize_filename(yt.title)
                
                st.download_button(
                    label=f"💾 Salvar Áudio ({label.split(' - ')[0]})",
                    data=file_bytes,
                    file_name=f"{filename}.{extension}",
                    mime=stream.mime_type,
                    use_container_width=True
                )
                
                show_success("Áudio pronto para download!")
                
        except Exception as e:
            show_error(f"Erro ao baixar: {str(e)}")
    
    stream_options = get_audio_streams(yt)
    
    create_download_section(
        stream_options=stream_options,
        selected_key="audio_select",
        button_text="📥 Baixar Áudio",
        button_key="audio_btn",
        download_callback=download_callback,
        info_message="🎵 Baixe apenas o áudio em alta qualidade"
    )


if __name__ == "__main__":
    main()
