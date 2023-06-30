from flask import Flask, render_template, request
import spacy
import septima

app = Flask(__name__)

# Carga el modelo de Spacy
nlp = spacy.load("es_core_news_sm")

# Ruta principal de la aplicación
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtiene el texto y la cantidad de preguntas enviados desde el formulario
        texto = request.form.get("texto")
        cantidad_preguntas = int(request.form.get("cantidad_preguntas"))

        # Genera las preguntas utilizando el código que hemos desarrollado
        preguntas_generadas = septima.generar_preguntas(texto, cantidad_preguntas)

        # Renderiza la plantilla de resultados y pasa las preguntas generadas
        return render_template("resultados.html", preguntas=preguntas_generadas)
    
    # Renderiza la plantilla del formulario
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
