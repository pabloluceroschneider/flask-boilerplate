from flask import Flask
from src.responses.HttpError import HttpError

from src.users.routes import users

app = Flask(__name__)

# Routes
app.register_blueprint(users, url_prefix='/users')

# Error Handlers
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(e):
    return HttpError(e).send()
