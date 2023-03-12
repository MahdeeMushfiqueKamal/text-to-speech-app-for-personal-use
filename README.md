## Text-to-Speech Flask App Documentation

This Flask app allows users to convert text to speech using Google's Text-to-Speech API. The user inputs text into a form on the homepage, and the app generates an MP3 file containing the speech output. The app also provides a player on the homepage that allows the user to play the most recent MP3 file that was generated.

#### Installation
- Install Python 3.x and pip (if not already installed).
- Clone the repository or download the files.
- Open a command prompt or terminal and navigate to the root directory of the app.
- Create a new virtual environment (recommended): python -m venv venv
- Activate the virtual environment:
    On Windows: `venv\Scripts\activate.bat`
    On Unix or Linux: `source venv/bin/activate`
- Install the required packages: `pip install -r requirements.txt`

#### Configuration
- Sign up for a Google Cloud account and create a new project.
- Enable the Text-to-Speech API in the Google Cloud Console.
- Create a new service account and download the JSON credentials file.
- Rename the JSON credentials file to credentials.json and place it in the root directory of the app.
- Update the GOOGLE_APPLICATION_CREDENTIALS environment variable in the config.py file to point to the location of the credentials.json file.