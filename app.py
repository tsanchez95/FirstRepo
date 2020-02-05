# compose_flask/app.py
from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')
	
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
	

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)