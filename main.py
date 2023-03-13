# Import the required libraries
import os
from datetime import date
from flask import Flask, render_template, request, redirect
from google.cloud import texttospeech

# Set up the authentication credentials
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/home/mmk/codes/text_to_speech_mahdee/mobile-doc-key.json"

# Set up the Flask app
app = Flask(__name__)
global_input_text = ""

# Set up the Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Define the home route
@app.route("/")
def home():
    return render_template("index.html", global_input_text=global_input_text)


# Define the text-to-speech route
@app.route("/tts", methods=["POST"])
def tts():
    # Get the input text from the form
    input_text = request.form["input_text"]
    global global_input_text
    global_input_text = input_text

    # Set up the synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # Set up the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Set up the audio file parameters
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the response to a file
    with open("static/output.mp3", "wb") as out:
        out.write(response.audio_content)

    # Return the file as a response to the request
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
