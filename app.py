from flask import Flask, render_template_string

app = Flask(__name__)

# Definir los datos
nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]


# Funciones equivalentes a las de JavaScript
def hacer_grandioso(magos):
    return [f"El gran {mago}" for mago in magos]


def filtrar_nombres():
    magos_grandiosos = hacer_grandioso(magos)
    otros = [
        nombre
        for nombre in nombres
        if nombre not in magos and nombre not in cientificos
    ]
    return nombres, magos_grandiosos, cientificos, otros


@app.route("/")
def home():
    # Filtrar y generar las listas
    nombres_completos, magos_grandiosos, cientificos_lista, otros = filtrar_nombres()

    # Usar render_template_string para generar el HTML en Python
    return render_template_string(
        """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Filtrado de Nombres</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h2 {
                color: #333;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                padding: 5px 0;
            }
        </style>
    </head>
    <body>
        <h1>Filtrado de Nombres</h1>

        <h2>Lista Completa de Nombres</h2>
        <ul>
            {% for nombre in nombres_completos %}
                <li>{{ nombre }}</li>
            {% endfor %}
        </ul>

        <h2>Magos Grandiosos</h2>
        <ul>
            {% for mago in magos_grandiosos %}
                <li>{{ mago }}</li>
            {% endfor %}
        </ul>

        <h2>Científicos</h2>
        <ul>
            {% for cientifico in cientificos_lista %}
                <li>{{ cientifico }}</li>
            {% endfor %}
        </ul>

        <h2>Otros</h2>
        <ul>
            {% for otro in otros %}
                <li>{{ otro }}</li>
            {% endfor %}
        </ul>

    </body>
    </html>
    """,
        nombres_completos=nombres_completos,
        magos_grandiosos=magos_grandiosos,
        cientificos_lista=cientificos_lista,
        otros=otros,
    )


if __name__ == "__main__":
    app.run(debug=True)
