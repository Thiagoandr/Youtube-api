

def apply_custom_css():
  
    return """
    <style>
    /* Configurações gerais */
    .main {
        padding-top: 2rem;
    }
    
    /* Botões de download */
    .stDownloadButton button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    
    .stDownloadButton button:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    /* Inputs */
    .stTextInput input {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        border-radius: 8px;
    }
    
    /* Botões primários */
    .stButton button[kind="primary"] {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
    }
    
    .stButton button[kind="primary"]:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    /* Botões secundários */
    .stButton button:not([kind="primary"]) {
        border: 2px solid #667eea;
        color: #667eea;
        background: #D3D3D3;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton button:not([kind="primary"]):hover {
        background: #f0f3ff;
        border-color: #764ba2;
        color: #764ba2;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 8px;
        border-left: 4px solid;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
    }
    
    /* Cards */
    .video-info-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    /* Imagens */
    img {
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        font-weight: 600;
        font-size: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    
    /* Captions */
    .stCaption {
        color: #6c757d;
        font-size: 0.875rem;
    }
    
    /* Headers personalizados */
    h1 {
        color: #1a1a1a;
        font-weight: 700;
    }
    
    h2 {
        color: #2d3748;
        font-weight: 600;
        margin-top: 2rem;
    }
    
    h3 {
        color: #4a5568;
        font-weight: 600;
    }
    
    /* Divisor */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 2px solid #e2e8f0;
    }
    
    /* Footer customizado */
    .footer {
        text-align: center;
        color: #718096;
        font-size: 0.9em;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 2px solid #e2e8f0;
    }
    
    /* Animações */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main > div {
        animation: fadeIn 0.5s ease-in-out;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        
        h1 {
            font-size: 1.75rem;
        }
        
        .stButton button {
            font-size: 0.9rem;
            padding: 0.6rem 1rem;
            color: #667eea;
        }
    }
    </style>
    """


def get_page_config():
    """Retorna as configurações da página"""
    return {
        "page_title": "YouTube Downloader",
        "page_icon": "📹",
        "layout": "centered",
        "initial_sidebar_state": "collapsed"
    }


def get_footer_html():
    """Retorna o HTML do rodapé"""
    return """
   
    """


def get_help_content():
    """Retorna o conteúdo da seção de ajuda"""
    return """
    ### 🎥 Vídeo + Áudio (Recomendado)
    Download completo com áudio. Geralmente disponível até 720p.
    
    **Quando usar:** Para assistir normalmente no celular, computador ou TV.
    
    ---
    
    ### 🎬 Só Vídeo (Sem Áudio)
    Vídeo em alta qualidade (1080p, 4K), mas **SEM áudio**.
    
    **Quando usar:** 
    - Se você for combinar com áudio depois usando software de edição
    - Para projetos de vídeo profissionais
    - Para análise de qualidade de vídeo
    
    ---
    
    ### 🎵 Só Áudio
    Apenas o áudio do vídeo em alta qualidade.
    
    **Quando usar:**
    - Para criar podcasts ou músicas
    - Para combinar com vídeo de alta qualidade
    - Para ouvir sem vídeo
    
    ---
    
    ### 💡 Dica Pro
    
    **Para ter 1080p ou 4K COM áudio:**
    
    1. **Instale o FFmpeg** (ferramenta de conversão de vídeo)
       - Windows: https://ffmpeg.org/download.html
       - Com isso, você pode combinar vídeo e áudio automaticamente
    
    2. **Ou use software de edição:**
       - Shotcut (gratuito)
       - DaVinci Resolve (gratuito)
       - Adobe Premiere
    
    3. **Ou use yt-dlp** (ferramenta de linha de comando):
       ```bash
       yt-dlp -f "bestvideo+bestaudio" URL
       ```
    
    ---
    
    ### ❓ Por que vídeos em alta qualidade não têm áudio?
    
    O YouTube separa vídeo e áudio em qualidades altas (1080p+) para:
    - Economizar banda durante streaming
    - Permitir trocar qualidade sem recarregar o áudio
    - Oferecer mais opções de qualidade
    
    No player do YouTube, vídeo e áudio são combinados automaticamente.
    Para download, você precisa baixar e combinar manualmente (ou usar FFmpeg).
    """


# Emojis e ícones
ICONS = {
    'video': '🎥',
    'audio': '🎵',
    'download': '📥',
    'info': 'ℹ️',
    'warning': '⚠️',
    'success': '✅',
    'error': '❌',
    'search': '🔍',
    'link': '🔗',
    'file': '💾',
    'stats': '📊',
    'duration': '⏱️',
    'views': '👁️',
    'quality': '🎬',
}
