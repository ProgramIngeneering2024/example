from bottle import route, run

@route('/')
def index():
    return '<b>Hello World! at 10:21:27</b>!'

run(host='0.0.0.0', port=8080)
