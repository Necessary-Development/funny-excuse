import os

import openai
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET","POST"))
@cross_origin()
def index():
    # user_suggestion = request.form["excuse"]
    # result = request.args.get("result")
    if request.method == 'POST':
        openai_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(
                "seductive quality", "rusty watering can", "build the Addlestone coal mine"),
            temperature=0.6,
            max_tokens=400
        )
        statement_text = openai_response.choices[0].text;
        return jsonify({"statementText": statement_text})
    else:
        return redirect("https://rishiGPT.com")


""" 
Example of grammar used below:
    noun_prepostion: "threat from"
    reason: "flying cheese balls"
    decision: "build the Addlestone coal mine"

Idea: 404 - an error has occurred. Rishi's voice saying this would be funny.
 """


def generate_prompt(noun_preposition, reason, decision):
    return """
    Please produce a statement from Prime Minister Rishi Sunak for why the {} {} means that he has decided to {}.
    """.format(
        noun_preposition, reason, decision,
    )
