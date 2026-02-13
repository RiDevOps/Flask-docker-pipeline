from flask import  Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello ! This is my Devops CI/CD Demo"
@app.route('/about')
def about():  
   return "This project demonstrates Flask, Docker and Github Actions"
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
