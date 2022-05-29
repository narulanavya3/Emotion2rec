from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return('emotion2rec version 1.0')

@app.route("/emotion", methods = ['GET', 'POST'])
def emotion():
    emo_retrieved = request.get_json(force=False)
    emotion_text = emo_retrieved["emotions"]
    
    if emotion_text== 'angry':
        return "angry.html"
    elif emotion_text == 'sad':
        return "sad.html"      
    elif emotion_text == 'happy':
        return "happy.html"  
    elif emotion_text =='fear':
        return "fear.html"
    elif emotion_text == 'neutral':
        return "neutral.html"
    
if __name__ == '__main__':
    app.run(debug=True)     
   
       