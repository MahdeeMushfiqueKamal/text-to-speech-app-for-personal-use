# Import the required libraries
import os
import traceback
from flask import Flask, render_template, request, redirect
from google.cloud import texttospeech
from google.cloud import storage

# # Set up the authentication credentials
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "mobile-doc-key.json"

# define your bucket name
bucket_name = 'sunny-bastion-375508.appspot.com'


# Set up the Flask app
app = Flask(__name__)
global_input_text = ""
global_audio_url = ""

# Define the home route
@app.route("/")
def home():
    return render_template("index.html", global_input_text=global_input_text, global_audio_url=global_audio_url)


# Define the text-to-speech route
@app.route("/tts", methods=["POST"])
def tts():
    try:
        # # Set up the Text-to-Speech client
        client = texttospeech.TextToSpeechClient()
    except: 
        return f"<p> {traceback.print_exc()} </p>"
    
    ## Create a Cloud Storage client
    storage_client = storage.Client()

    # Get the Cloud Storage bucket that you want to use
    bucket = storage_client.bucket(bucket_name)

    # Create a new Blob and specify the audio file name
    blob = bucket.blob('output.mp3')
    
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

    # Save the audio content to a file in Cloud Storage
    blob.upload_from_string(response.audio_content, content_type='audio/mpeg')
    blob.make_public()


    # Get the URL of the audio file
    global global_audio_url
    global_audio_url = blob.public_url

    # Return the audio URL to the user
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
