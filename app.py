from flask import Flask, request, jsonify
import subprocess
import whisper
import os

app = Flask(__name__)

# Charge le modèle Whisper
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe_video():
    data = request.json
    video_url = data.get("video_url")

    if not video_url:
        return jsonify({"error": "Aucune URL de vidéo fournie"}), 400

    # Utilisation de yt-dlp pour télécharger la vidéo
    output_path = "/data/audio/video_audio.mp3"
    command = f'yt-dlp -x --audio-format mp3 -o "{output_path}" {video_url}'
    subprocess.run(command, shell=True, check=True)

    # Transcription de l'audio avec Whisper
    result = model.transcribe(output_path)

    # Retourne la transcription en format JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
