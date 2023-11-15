''' Executing this function initiates the application of emotion detection 
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!."

    output_string = "For the given statement, the system response is: "
    output_string += ",".join(f"'{key}': {value}" for key, value in response.items()
     if key != "dominant_emotion")
    output_string += f". The dominant emotion is {response['dominant_emotion']}."
    return output_string

@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
