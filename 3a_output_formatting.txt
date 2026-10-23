import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }

    res = requests.post(url, headers=header, json=input_json ) 
    formatted_res = json.loads(res.text)
    emotions = formatted_res['emotionPredictions'][0]['emotion']
    max_emotion = max(emotions, key=emotions.get )
    emotions['dominant_emoiton'] = max_emotion

    return emotions