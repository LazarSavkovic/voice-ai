from flask import Flask, request, send_file, render_template
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

def text_to_audio_file(text):
    tts = gTTS(text)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    sentence = request.form.get('sentence')

    if not sentence:
        return {"error": "Please provide a sentence"}, 400

    audio_file = text_to_audio_file(sentence)
    return send_file(audio_file, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
