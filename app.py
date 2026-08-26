from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
 {"id": 1, "nombre": "Laptop", "precio": 1200},
 {"id": 2, "nombre": "Mouse", "precio": 25},
 {"id": 3, "nombre": "Teclado", "precio": 75}
]


@app.route("/")
def inicio():
    return "¡Hola! Mi primera aplicación Flask"

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
 return jsonify(productos)

if __name__ == "__main__":
    app.run(debug=True)
