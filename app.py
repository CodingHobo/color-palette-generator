import openai
from flask import Flask, render_template, request
import json

from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key=config["OPENAI_API_KEY"]

app = Flask(__name__,
    template_folder="templates",
    static_url_path="",
    static_folder="static"
)

def get_colors(msg):
    messages = [
            {"role": "system",
             "content": """You are a color palette generating assistant that responds to text prompts for color palettes.
             You should generate color palettes that fit the theme, mood, or instrcutions in the prompt.
             The palettes should be between 2 and 8 colors.
             Desired format: JSON array of hexidecimal color codes."""
            },
            {"role": "user",
             "content": "Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea"
            },
            {"role": "assistant",
             "content": '["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]'
            },
            {"role": "user",
             "content": "Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea"
            },
            {"role": "assistant",
             "content": '["#EDF1D6", "#9DC08B", "#609966", "#40513B"]'
            },
            {"role": "user",
             "content": f"Convert the following verbal description of a color palette: {msg}"
            },

        ]

    resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
    )

    colors = json.loads(resp["choices"][0]["message"]["content"])
    return colors

@app.route("/palette", methods=["POST"])
def palette_prompt():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)