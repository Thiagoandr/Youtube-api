import streamlit as st
from utils import format_duration, format_views


def show_video_info(video_info):
   
    st.markdown("---")
    st.subheader("📺 Informações do Vídeo")
    
    # Criar duas colunas
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(video_info['thumbnail'], use_container_width=True)
    
    with col2:
        st.markdown(f"**Título:** {video_info['title']}")
        st.markdown(f"**Autor:** {video_info['author']}")
        st.markdown(f"**Duração:** {format_duration(video_info['length'])}")
        st.markdown(f"**Visualizações:** {format_views(video_info['views'])}")


def create_download_section(stream_options, selected_key, button_text, button_key, 
                           download_callback, info_message=None, warning_message=None):
   
    if info_message:
        st.info(info_message)
    
    if warning_message:
        st.warning(warning_message)
    
    if not stream_options:
        st.warning("⚠️ Nenhum stream disponível.")
        return
    
    # Selectbox de qualidade
    selected_label = st.selectbox(
        "Escolha a qualidade:",
        options=list(stream_options.keys()),
        index=0,
        key=selected_key
    )
    
    # Informações do stream selecionado
    selected_stream = stream_options[selected_label]
    
    # Mostrar codec
    codec_info = []
    if hasattr(selected_stream, 'video_codec') and selected_stream.video_codec:
        codec_info.append(f"Vídeo: {selected_stream.video_codec}")
    if hasattr(selected_stream, 'audio_codec') and selected_stream.audio_codec:
        codec_info.append(f"Áudio: {selected_stream.audio_codec}")
    
    if codec_info:
        st.caption(f"📊 {' | '.join(codec_info)}")
    
    # Botão de download
    if st.button(button_text, use_container_width=True, type="primary", key=button_key):
        download_callback(selected_stream, selected_label)


def show_progress(percentage, message="Baixando..."):
    
    progress_bar = st.progress(percentage)
    status_text = st.empty()
    status_text.text(f"📥 {message} {percentage*100:.1f}%")
    return progress_bar, status_text


def show_welcome_screen():
   
    st.info("👆 Cole uma URL do YouTube acima e clique em 'Buscar Informações' para começar!")
    
    # Dicas rápidas
    with st.expander("💡 Dicas Rápidas"):
        st.markdown("""
        - **Vídeo + Áudio:** Melhor para assistir (até 720p)
        - **Só Vídeo:** Alta qualidade sem áudio (1080p, 4K)
        - **Só Áudio:** Para músicas e podcasts
        
        **Nota:** Qualidades acima de 720p vêm sem áudio devido a limitações do YouTube.
        """)


def show_error(message):
   
    st.error(f"❌ {message}")


def show_success(message):
    st.success(f"✅ {message}")
