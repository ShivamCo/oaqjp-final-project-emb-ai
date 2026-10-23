import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }

    if not text_to_analyze or not text_to_analyze.strip():
        return 'Invalid text! Please try again!.'
    
    res = requests.post(url, headers=header, json=input_json ) 
    if res.status_code == 200:
        formatted_res = json.loads(res.text)
        emotions = formatted_res['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions, key=emotions.get )
        emotions['dominant_emoiton'] = max_emotion

        if emotions['dominant_emoiton'] == None or emotions['dominant_emoiton'] == 'null':
            return 'Invalid text! Please try again!.'
        else:
            return emotions
    
    elif res.status_code == 500:
        emotions = {
            "anger": None,
            "disgust": None,
            "dominant_emoiton": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
        return emotions


    else:
        emotions = {
            "anger": None,
            "disgust": None,
            "dominant_emoiton": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
        return emotions


    