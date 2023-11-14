import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": { "text": text_to_analyze }}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]
    dicc = {}
    for tipos in emotion:
        dicc[tipos] = emotion[tipos]
    emociones = {}
    emociones = dicc['emotion'].copy()
    label = []
    score = []
    for feel in emociones:
        label.append(feel)
        score.append(emociones[feel])
    score_dominat_emotion = max(score)
    dominat_emotion = next(key for key, value in emociones.items() if value == score_dominat_emotion)
    emociones["emocion dominante"] = dominat_emotion
    return emociones