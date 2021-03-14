from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():

    if request.method == "POST":
        ariv = request.form.get("ariv")
        dep = request.form.get("dep")
        airline = request.form.get("airline")
        stopage = request.form.get("stopage")
        source = request.form.get("source")
        des = request.form.get("des")

        print(dep)
        print(ariv)
        print(airline)
        print(stopage)
        print(source)
        print(des)
        return render_template('home.html', price="99")

    return render_template('home.html')
