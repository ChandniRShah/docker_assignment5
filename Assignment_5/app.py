from flask import Flask,jsonify,render_template
import json

app = Flask(__name__, static_folder="./static/dist")


app = Flask(__name__)
jData = json.loads(open('./data.json').read())
data=jData["Food"]
# print (data[0]["id"])



@app.route('/')
def index():
   return render_template("index1.html")

@app.route('/getFood/')
@app.route('/getFood/<string:id>/')
def hello_world1(id=''):
    rdata = jsonify([])
    if not id:
        rdata = jsonify(data)
    else:
        for f in data:
            if f["id"] == id:
                rdata = jsonify([f])
    return rdata

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
