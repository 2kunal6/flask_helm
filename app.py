from flask import Flask

import os
import logging


app = Flask(__name__)


@app.route('/')
def hello():
    #os.mkdir(f'{in_container_location}/test_folder')
    logging.warning(os.getcwd())
    logging.warning(os.listdir('/app/in_container_location/'))
    logging.warning(os.listdir(f'{os.getcwd()}/in_container_location/'))
    #return f'Hello, World! {os.listdir(in_container_location)}'
    return f'Hello, World! 3'
