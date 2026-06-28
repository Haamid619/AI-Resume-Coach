from flask import Flask, render_template, request
import os
import pdfplumber
from gemini_service import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if file:

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = ""

        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    resume_text += text + "\n"

        job_description = request.form["job_description"]

        analysis = analyze_resume(resume_text, job_description)

        return f"""
        <h2>AI Resume Analysis</h2>

        <pre>{analysis}</pre>
        """

    return "No file selected."


if __name__ == "__main__":
    app.run(debug=True)