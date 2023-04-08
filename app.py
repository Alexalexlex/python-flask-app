from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from services.audio_service import AudioUpload

load_dotenv()

app = Flask(__name__)
api = Api(app)

api.add_resource(AudioUpload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
