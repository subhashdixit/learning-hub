## flask app for hello world

from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"



if __name__=="__main__":
    # With host as 0.0.0.0, we can run this app on localhost, host address and with 127.0.0.1 as well
    app.run(host="0.0.0.0",port=5000)
