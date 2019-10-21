from flask import Flask,request,jsonify,render_template
import os
import io
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
	return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False,port=os.getenv('PORT',5000))
