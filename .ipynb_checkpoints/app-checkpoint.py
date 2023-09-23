import openai
from dotenv import dotenv_values
from IPython.display import Markdown, display

config = dotenv_values(".env")
openai.api_key=config["OPENAI_API_KEY"]

prompt = """
    You are a color palette generating assistant that responds to text prompts for color palettes
    You should generate color palettes that fit the theme, mood, or instrcutions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

    Desired format: a JSON array of hexidecimal color codes

    Text: a beautiful sunset

    Result:
"""

resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
    )

print(resp["choices"][0]["text"])

def display_color(color):
    display(Markdown(f'<span style="color: {color}">{chr(9608)}></span>'))

display_color("#D299AB")