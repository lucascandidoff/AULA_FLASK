from app import app

@app.route('/index')
@app.route("/")
def index():
    return "Hello world!"

@app.route('/test', defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return 'Olá, %s!' %name
    else:
        return 'Olá, usuário!'