from flask import Flask, request, jsonify, Response,render_template,json
import nmt as pz

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/')
def home():
     return render_template('index.html')
 
 
@app.route('/api',methods=['POST'])
def entry():
    data = request.get_json()
    print('Data from browser: ', data)
    text=data['text']
    js = json.dumps({'text':pz.predict(text)})    
    # js = 'hi testing'
    print('Predicted text: ', js)
    resp = Response(js, status=200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
  
if __name__ == '__main__':
      app.run(debug=True)