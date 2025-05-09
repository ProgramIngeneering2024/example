from bottle import route, run


@route('/health')
def index():
    return 'HEALTHY\n'


@route('/ready')
def index():
    return 'READY\n'


@route('/')
def index():
    return '<b>Hello World! at 01:04:35</b>!\n'

run(host='0.0.0.0', port=80)
