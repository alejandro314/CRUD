
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

usuarios =[]




@app.route("/", methods=["GET","POST"])
def crud():
    nombre = request.form.get("nombre")
    email = request.form.get("email") 
    usuarios.append({"username":nombre,"email":email})

    return render_template("registro.html", usuarios = usuarios)










if __name__ == "_main_":
    app.run(debug=True)

