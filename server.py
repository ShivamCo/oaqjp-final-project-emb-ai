"""
Emotion Detection Server Application.  
This module sets up a Flask backend endpoint that 
analyzes text inputs by using the NLP 
emotion detection microservice.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_det():
    """
    This process examines the text string 
    provided as a query parameter and delivers a 
    comprehensive breakdown of the identified 
    emotion values, including the primary emotion that stands out.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return 'Invalid text! Please try again!.'


    res = emotion_detector(text_to_analyze)
    anger = res['anger']
    disgust = res['disgust']
    fear = res['fear']
    joy = res['joy']
    sadness = res['sadness']
    dominant_emotion = res['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!.'

    return (f"'anger': {anger}, 'disgust': {disgust},"
            f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}." 
            f"The dominant emotion is {dominant_emotion}."
    )

@app.route('/')
def index_page():
    """
    To render index.html home page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
