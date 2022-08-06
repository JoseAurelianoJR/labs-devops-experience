from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "As aulas da gaby são d+!!!"

if __name__ == '__main__':
    app.run()