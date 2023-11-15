import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        # Cargar el JSON
        data = json.loads(response.text)

        # Extraer las puntuaciones de emoción
        emotion_scores = data['emotionPredictions'][0]['emotion']

        # Calcular la emoción dominante
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Crear el formato deseado
        formatted_result = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        formatted_result = None
    return formatted_result