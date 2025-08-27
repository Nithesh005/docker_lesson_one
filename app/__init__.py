from flask import Flask


def home():
    return {"message": "Hello, Docker + Flask! ok", "success": True}, 200


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', view_func=home)
    # @app.route('/')
    # def home():

    #     return {"message":"Hello, Docker + Flask! ok", "success":True}, 200
    
    return app