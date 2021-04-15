from flask import Flask
import logging


logging.basicConfig(filename='record.log', level=logging.DEBUG)
app = Flask(__name__)
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"

from modules import routes