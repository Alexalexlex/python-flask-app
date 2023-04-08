from flask import request
from flask_restful import Resource
import os
from .recognizer_service import Recognizer
from .gpt_service import GPTService


class AudioUpload(Resource):
    def post(self):
        if 'audio' not in request.files:
            return {'message': 'No audio file provided'}, 400

        audio_file = request.files['audio']
        filename = audio_file.filename

        if not filename:
            return {'message': 'No audio file provided'}, 400

        UPLOAD_FOLDER = 'uploads'
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file_path = os.path.join(UPLOAD_FOLDER, filename)
        audio_file.save(os.path.join(UPLOAD_FOLDER, filename))

        transcript = Recognizer.recognize_speech(file_path)

        response = GPTService.generate_text("Hello Chat-GPT")

        return {'message': 'Audio file processed successfully', 'Chat-GPT answer:': response}, 200
