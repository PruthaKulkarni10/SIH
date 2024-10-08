import pickle
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import os
from models.QuestionsModel import * 
from models.UserModel import *
from .analyze import grade_student_response
from flask import jsonify,request
from video_audio import video_to_audio

current=os.getcwd()
UPLOAD_FOLDER = os.path.join(current,'uploads')
print(UPLOAD_FOLDER)
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
def AudioProcessing():
    #when audio will be uploaded
    # if 'file' not in request.files:
    #     return "No file part", 400
    
    # file = request.files['file']
    
    # if file.filename == '':
    #     return "No selected file", 400
    # file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    # file_name = os.path.join(UPLOAD_FOLDER, file.filename)
    #verbal_score, abstract_score = grade_student_response(file_name)
    data=request.get_json()

    video_to_audio(os.path.join(UPLOAD_FOLDER,'Video.mp4'))
    scores = Scores.query.get(data['user_id'])

    

    verbal_score, abstract_score = grade_student_response(os.path.join(UPLOAD_FOLDER,'Audio.mp3'))
    if scores:
        scores.abstract = abstract_score
        scores.verbal=verbal_score

        db.session.commit()



    #os.remove(file_name)
    return jsonify({
        "Verbal_score": verbal_score,
        "Abstract_score": abstract_score
    })
