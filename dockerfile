FROM python:3.8-slim

# Installe yt-dlp, Whisper et Flask
RUN pip install --no-cache-dir yt-dlp openai-whisper Flask

# Copie le script Flask dans le container
COPY app.py /app/app.py
WORKDIR /app

# Expose le port 5000
EXPOSE 5000

# Commande pour démarrer le serveur Flask
CMD ["python", "app.py"]
