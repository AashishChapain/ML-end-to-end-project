from flask import Flask
from src.logger import logging
from src.execption import CustomException
import os, sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception("testing our exception")
    except Exception as e:
        ml = CustomException(e, sys)
        print(ml.error_message)
        logging.info(ml.error_message)


        logging.info("testing logging file")
        return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)