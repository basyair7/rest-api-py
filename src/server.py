from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from dotenv import load_dotenv, dotenv_values
import os

app = Flask(__name__);
api = Api(app, prefix='/api/v1');
auth = HTTPBasicAuth();

load_dotenv();
USER_DATA = {
    os.getenv("USERNAME") : os.getenv("PASSWORD")
};

class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {"Maybe": 30};

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False;
    return USER_DATA.get(username) == password;
    
api.add_resource(PrivateResource, '/private');

if(__name__ == '__main__'):
    app.run(debug=True);
