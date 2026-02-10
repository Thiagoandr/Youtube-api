# 📹 YouTube Downloader

Aplicação web para download de vídeos e áudios do YouTube em diversas qualidades.

## 🚀 Funcionalidades

- ✅ Download de vídeos com áudio (até 720p)
- ✅ Download de vídeos em alta qualidade sem áudio (1080p, 4K)
- ✅ Download de áudio separado
- ✅ Interface moderna e responsiva
- ✅ Informações detalhadas do vídeo

## 📁 Estrutura do Projeto

```
youtube_downloader/
├── main.py          # Aplicação principal
├── style.py         # Estilos CSS e configurações visuais
├── utils.py         # Funções utilitárias
├── components.py    # Componentes de UI reutilizáveis
```

## 🛠️ Instalação

### 1. Instalar dependências

```bash
pip install streamlit pytubefix
```

### 2. Executar a aplicação

```bash
cd youtube_downloader
streamlit run main.py
```

## 📖 Como Usar

1. **Cole a URL** do vídeo do YouTube
2. **Clique em "Buscar Informações"**
3. **Escolha a qualidade** desejada em uma das abas:
   - 🎥 **Vídeo + Áudio:** Download completo (até 720p)
   - 🎬 **Só Vídeo:** Alta qualidade sem áudio (1080p, 4K)
   - 🎵 **Só Áudio:** Apenas o áudio
4. **Clique em "Baixar"** e aguarde
5. **Salve o arquivo** quando aparecer o botão



## ⚠️ Limitações

- Vídeos acima de 720p não incluem áudio (limitação do YouTube)
- Para combinar vídeo e áudio em alta qualidade, é necessário FFmpeg
- Alguns vídeos podem ter restrições de download

## 🔧 Possíveis Melhorias Futuras

- [ ] Suporte a FFmpeg para combinar vídeo e áudio automaticamente
- [ ] Download de playlists
- [ ] Conversão de formatos
- [ ] Download simultâneo de múltiplos vídeos
- [ ] Histórico de downloads
- [ ] Temas claro/escuro

## 📝 Licença

Livre para uso pessoal e educacional.

## 🤝 Contribuindo

Sinta-se à vontade para fazer melhorias e enviar pull requests!

## 📧 Suporte

Em caso de problemas:
1. Verifique se todas as dependências estão instaladas
2. Certifique-se de que a URL do YouTube está correta
3. Verifique sua conexão com a internet

---

