from flask import Flask, render_template, request, url_for, redirect
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/form-pesan", methods=["GET", "POST"])
def form_pesan():
    error = None

    selected_order = request.args.get("selected_order")

    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        phone = request.form["phone"]
        service_type = request.form["service_type"]

        admin_number = "6282133019386"

        message = f"""
        Halo Admin CoolService, saya ingin memesan layanan dengan detail sebagai berikut:
        Nama: {name}
        Alamat: {address}
        No. HP: {phone}
        Jenis Layanan: {service_type}

        Terima kasih!
        """

        wa_url = f"https://wa.me/{admin_number}?text={quote(message)}"

        if service_type == "":
            error = "Silakan pilih jenis layanan!"
        else:
            return redirect(wa_url)

    return render_template(
        "form_pesan.html",
        error=error,
        selected_order=selected_order
    )


if __name__ == '__main__':
    app.run(debug=True)