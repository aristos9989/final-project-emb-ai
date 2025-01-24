from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detector")

@app.route("/")
def get_index_template():
    return render_template("index.html")

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detection(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, \
                'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
