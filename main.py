from bottle import route, run


@route('/health')
def index():
    return 'HEALTHY'


@route('/ready')
def index():
    return 'READY'


@route('/')
def index():
    return '<b>Hello World! at 10:49:27</b>!'

run(host='0.0.0.0', port=8080)
