""" This Server.js file uses Flask and emotion detection API
"""

from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_det():
    """ This function calls '/emotionDetector' API
    which takes paragraph and detects emotions and
    return emotion stats.
     """
    res = emotion_detector('')
    return res


if __name__ == '__main__':
    app.run()
