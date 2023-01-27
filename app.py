from flask import Flask, render_template,request
from flask_jwt_extended import JWTManager
from eInterview.subject.subject import subject_bp
from auth.auth import auth_bp
from eInterview.questions.questions import questions_bp
from datetime import timedelta
from flask_cors import CORS, cross_origin
from utils.registerUser import registerUser, registerUserByApi
from utils.moduler import getDir
from utils.createDb import createDb
app = Flask(__name__)
CORS(app, support_credentials=True)

# configuration for JWT Tokens
app.config.from_object('config')
app.config['JWT_TOKEN_LOCATION']
app.config['JWT_COOKIE_CSRF_PROTECT']
app.config['JWT_COOKIE_SECURE']
app.config["JWT_SECRET_KEY"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

createDb()
registerUser()
getDir()


# register blueprints here
app.register_blueprint(auth_bp)
app.register_blueprint(subject_bp, url_prefix="/subject")
app.register_blueprint(questions_bp, url_prefix='/question')


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

@app.route('/registerUser', methods=['POST'])
def register_user():
    return registerUserByApi(request) 
# running app
if __name__ == '__main__':
    app.run(host="0.0.0.0")