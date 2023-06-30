from flask import Flask, render_template, request
import spacy
import septima

app = Flask(__name__)

nlp = spacy.load("es_core_news_sm")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texto = request.form.get("texto")
        cantidad_preguntas = int(request.form.get("cantidad_preguntas"))
        preguntas_generadas = septima.generar_preguntas(texto, cantidad_preguntas)

        return render_template("resultados.html", preguntas=preguntas_generadas)
    
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
