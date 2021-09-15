import os
import pathlib
from pathlib import Path
from typing import Text, Union

from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask.wrappers import Response
from werkzeug.wrappers import response
from password_complexity.pipelines.predict_model import predict_model
from password_complexity.pipelines.train_model import train_model
from password_complexity.features.generate import generate_features
# from lstm_model.base_model import PasswordLSTM
# from lstm_model.utils import response_json

CONFIG_PATH= 'CONFIG_PATH.yaml'
# Flask instance
app = Flask(__name__)
# config = toml.load("config.toml")
# # TODO: model_folder should be in config
# model_folder = "model"

# Model class instance
# password_model = PasswordLSTM(
#     config=config,
#     model_serialized=os.path.join(model_folder, "one_epoch_model"),
#     tokenizer=os.path.join(model_folder, "tokenizer.pickle"),
# )





app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['POST', "GET"])
def index() -> Union[Response, Text]:
    """Password prediction form processing.

    Returns:
        Text: Form with frequency prediction if password was provided, otherwise - empty form.
    """
    if request.method == "POST":
        password = request.form['password']
        prediction = str(predict_model(password, CONFIG_PATH))
        return render_template('index.html', prediction=prediction)
    # else:
    return render_template('index.html')


@app.route("/predict", methods=["POST", "GET"])
def predict():
    password = request.args['password']

    prediction = str(predict_model(password, CONFIG_PATH))

    return prediction 


# @app.route('/train_model', methods=['GET'])
# def train_model_() -> str:
#     """
#     load last model config pipeline and train model with tuning hyperparameters
#     """



#     return train_model

@app.route("/update_dataseet")
def update_dataseet():
    return "Привет Нелли!"

if __name__ == "__main__":
    # for development set "debug=True" in app.run
    app.run(host="0.0.0.0", threaded=False, debug=True)



