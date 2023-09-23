import openai
from flask import Flask, render_template, request
import json

from dotenv import dotenv_values

# Load configuration from the .env file
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__,
            template_folder="templates",
            static_url_path="",
            static_folder="static"
            )

def get_colors(msg):
    """
    Generate a list of colors based on a text prompt using OpenAI's GPT-3 model.

    Args:
        msg (str): The text prompt describing the color palette.

    Returns:
        list: A list of hexadecimal color codes.
    """
    # Define a list of messages for the conversation with the GPT-3 model
    messages = [
        {
            "role": "system",
            "content": """You are a color palette generating assistant that responds to text prompts for color palettes.
             You should generate color palettes that fit the theme, mood, or instructions in the prompt.
             The palettes should be between 2 and 8 colors.
             Desired format: JSON array of hexadecimal color codes."""
        },
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea"},
        {"role": "assistant", "content": '["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]'},
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea"},
        {"role": "assistant", "content": '["#EDF1D6", "#9DC08B", "#609966", "#40513B"]'},
        {"role": "user", "content": f"Convert the following verbal description of a color palette: {msg}"}
    ]

    # Request color palette from the GPT-3 model
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
    )

    # Parse the color palette from the response
    colors = json.loads(resp["choices"][0]["message"]["content"])
    return colors

@app.route("/palette", methods=["POST"])
def palette_prompt():
    """
    Generate a color palette based on a user's text prompt.

    Returns:
        dict: A dictionary containing the generated colors.
    """
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}

@app.route("/")
def index():
    """
    Render the main index.html page.

    Returns:
        render_template: The rendered HTML template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
