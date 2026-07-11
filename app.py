import os

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from image.encoder import encode_secret
from image.decoder import decode_secret
from audio.encoder import encode_secret as encode_audio_secret
from audio.decoder import decode_secret as decode_audio_secret
from pdf.encoder import encode_secret as encode_pdf_secret
from pdf.decoder import decode_secret as decode_pdf_secret
from text.encoder import encode_secret as encode_text_secret
from text.decoder import decode_secret as decode_text_secret

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# AUDIO PAGE
# ==========================================

@app.route("/audio")
def audio():
    return render_template("audio.html")


# ==========================================
# AUDIO ENCODE
# ==========================================

@app.route("/audio/encode", methods=["POST"])
def audio_encode():

    if "audio" not in request.files:

        return render_template(
            "result.html",
            title="Error",
            message="No audio selected."
        )

    audio = request.files["audio"]

    if audio.filename == "":

        return render_template(
            "result.html",
            title="Error",
            message="Please choose an audio file."
        )

    message = request.form["message"].strip()
    password = request.form["password"].strip()

    if message == "":

        return render_template(
            "result.html",
            title="Error",
            message="Secret message cannot be empty."
        )

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        audio.filename
    )

    name, ext = os.path.splitext(audio.filename)

    output_name = f"{name}_encoded.wav"

    output_path = os.path.join(
        app.config["OUTPUT_FOLDER"],
        output_name
    )

    audio.save(input_path)

    try:

        encode_audio_secret(
            input_path,
            output_path,
            message,
            password
        )

        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_name
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Encoding Failed",
            message=str(e)
        )


# ==========================================
# AUDIO DECODE
# ==========================================

@app.route("/audio/decode", methods=["POST"])
def audio_decode():

    if "audio" not in request.files:

        return render_template(
            "result.html",
            title="Error",
            message="No audio selected."
        )

    audio = request.files["audio"]

    if audio.filename == "":

        return render_template(
            "result.html",
            title="Error",
            message="Please choose an audio file."
        )

    password = request.form["password"].strip()

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        audio.filename
    )

    audio.save(input_path)

    try:

        secret = decode_audio_secret(
            input_path,
            password
        )

        return render_template(
            "result.html",
            title="Recovered Secret",
            message=secret
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Decoding Failed",
            message=str(e)
        )



# ==========================================
# IMAGE PAGE
# ==========================================
@app.route("/image")
def image():
    return render_template("image.html")


# ==========================================
# IMAGE ENCODE
# ==========================================

@app.route("/image/encode", methods=["POST"])
def image_encode():

    if "image" not in request.files:

        return render_template(
            "result.html",
            title="Error",
            message="No image selected."
        )

    image = request.files["image"]

    if image.filename == "":

        return render_template(
            "result.html",
            title="Error",
            message="Please choose an image."
        )

    message = request.form["message"].strip()
    password = request.form["password"].strip()

    if message == "":

        return render_template(
            "result.html",
            title="Error",
            message="Secret message cannot be empty."
        )

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    name, ext = os.path.splitext(image.filename)

    output_name = f"{name}_encoded.png"

    output_path = os.path.join(
        app.config["OUTPUT_FOLDER"],
        output_name
    )

    image.save(input_path)

    try:

        encode_secret(
            input_path,
            output_path,
            message,
            password
        )

        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_name
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Encoding Failed",
            message=str(e)
        )


# ==========================================
# IMAGE DECODE
# ==========================================

@app.route("/image/decode", methods=["POST"])
def image_decode():

    if "image" not in request.files:

        return render_template(
            "result.html",
            title="Error",
            message="No image selected."
        )

    image = request.files["image"]

    if image.filename == "":

        return render_template(
            "result.html",
            title="Error",
            message="Please choose an image."
        )

    password = request.form["password"].strip()

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(input_path)

    try:

        secret = decode_secret(
            input_path,
            password
        )

        return render_template(
            "result.html",
            title="Recovered Secret",
            message=secret
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Decoding Failed",
            message=str(e)
        )


# ==========================================
# PDF PAGE
# ==========================================
@app.route("/pdf")
def pdf():
    return render_template("pdf.html")


# ==========================================
# encode pdf
# ==========================================
@app.route("/pdf/encode", methods=["POST"])
def pdf_encode():

    pdf = request.files["pdf"]

    message = request.form["message"]

    password = request.form["password"]

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        pdf.filename
    )

    name, ext = os.path.splitext(pdf.filename)

    output_name = f"{name}_encoded.pdf"

    output_path = os.path.join(
        app.config["OUTPUT_FOLDER"],
        output_name
    )

    pdf.save(input_path)

    try:

        encode_pdf_secret(
            input_path,
            output_path,
            message,
            password
        )

        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_name
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Encoding Failed",
            message=str(e)
        )
# ==========================================
# decode pdf
# ==========================================
@app.route("/pdf/decode", methods=["POST"])
def pdf_decode():

    pdf = request.files["pdf"]

    password = request.form["password"]

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        pdf.filename
    )

    pdf.save(input_path)

    try:

        secret = decode_pdf_secret(
            input_path,
            password
        )

        return render_template(
            "result.html",
            title="Recovered Secret",
            message=secret
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Decoding Failed",
            message=str(e)
        )

# ==========================================
# TEXT PAGE
# ==========================================


@app.route("/text")
def text():
    return render_template("text.html")

# ==========================================
# TEXT ENCODE
# ==========================================

@app.route("/text/encode", methods=["POST"])
def text_encode():

    cover_text = request.form["cover"]
    message = request.form["message"]
    password = request.form["password"]

    try:

        result = encode_text_secret(
            cover_text,
            message,
            password
        )

        return render_template(
            "result.html",
            title="Encoded Text",
            message=result
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Encoding Failed",
            message=str(e)
        )
# ==========================================
# TEXT DECODE
# ==========================================

@app.route("/text/decode", methods=["POST"])
def text_decode():

    stego_text = request.form["stego"]
    password = request.form["password"]

    try:

        secret = decode_text_secret(
            stego_text,
            password
        )

        return render_template(
            "result.html",
            title="Recovered Secret",
            message=secret
        )

    except Exception as e:

        return render_template(
            "result.html",
            title="Decoding Failed",
            message=str(e)
        )

# ==========================================
# QR PAGE
# ==========================================

@app.route("/qr")
def qr():
    return render_template(
        "result.html",
        title="Coming Soon",
        message="QR Code Steganography will be added soon."
    )


# ==========================================
# GIT PAGE
# ==========================================

@app.route("/git")
def git():
    return render_template(
        "result.html",
        title="Coming Soon",
        message="Git Commit Steganography will be added soon."
    )


# ==========================================
# ABOUT PAGE
# ==========================================

@app.route("/about")
def about():
    return render_template(
        "result.html",
        title="About Steganography Multi Tool",
        message="""
Steganography Multi Tool

Developed by:
Darshan M

Features
✔ Image Steganography (LSB)
✔ Audio Steganography (LSB)
✔ AES-256 Encryption
✔ Password Protection

Upcoming Features
• PDF Steganography
• QR Code Steganography
• Zero Width Unicode Text
• Git Commit Steganography
• Batch Processing
• Capacity Calculator

Version: 1.0
"""
    )


# ==========================================
# ERROR HANDLER
# ==========================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "result.html",
        title="404",
        message="Page Not Found."
    ), 404


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
