from flask import Flask, request, render_template, session
from googletrans import Translator
import os
from dotenv import load_dotenv

# Load environment variable.
load_dotenv()
secret_key = os.environ["SECRET_KEY"]


app = Flask(__name__)
app.secret_key = secret_key


def translate_google(text, target_language):
  
    trans = Translator()
    result = trans.translate(text=text, dest=target_language)
    translated_text = result.text
    return translated_text


@app.route("/", methods=["POST", "GET"])
def translate():

    languages = {
        "en": "English",
        "es": "Spanish",
        "zh-cn": "Chinese (Mandarin)",
        "hi": "Hindi",
        "ar": "Arabic",
        "fr": "French",
        "ru": "Russian",
        "pt": "Portuguese",
        "ja": "Japanese",
        "de": "German",
        "sw": "Swahili",
    }

    if request.method == "POST":
        src_text = request.form["source_text"]
        target_lang = request.form["target_language"]
        translated_text = translate_google(src_text, target_lang)

        # Store the target language in session.
        session["target_language"] = target_lang

        return render_template(
            "index.html",
            source_text=src_text,
            translated_text=translated_text,
            target_language=languages[target_lang],
        )
    else:
        # Check if target language is stored in session.
        target_lang = session.get("target_language", "en")
        return render_template("index.html", target_language=languages[target_lang])


if __name__ == "__main__":
    app.run(debug=True)
