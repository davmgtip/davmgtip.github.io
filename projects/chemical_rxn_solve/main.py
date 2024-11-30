from openai import OpenAI
import matplotlib.pyplot as plt
client = OpenAI(api_key='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')
from flask import *
import markdown

app = Flask(__name__)

def getChemRxn(message, temperature=0.1):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are the best chemistry teacher in the world. You are responsible for solving the chemical equation. You just have to give the full reaction and a little bit explanation. Make sure not to include anything other than that, lile 'As an LLM, ...' or anything like that."},
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=temperature
    )
    return completion.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def handleIndex():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        query = request.form.get('reactants')
        ai_resp = getChemRxn(query)
        html_content = markdown.markdown(ai_resp)
        return render_template("index.html", aiResp=html_content)

if __name__ == "__main__":
    app.run("localhost", 8888)
    # while True:
    #     user_input = input("Enter reactants: ")
    #     if user_input == 'bye':
    #         print("Bye!")
    #         break
    #     else:
    #         ai_resp = getChemRxn(user_input)
    #         print(ai_resp)
