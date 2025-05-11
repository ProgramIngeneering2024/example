from flask import Flask
from prometheus_client import make_wsgi_app, Counter, generate_latest
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
requests_counter = Counter('http_requests_total', 'Total HTTP Requests')

# Основное приложение
@app.route('/')
def hello():
    requests_counter.inc()
    return "Hello World!"

# Метрики Prometheus
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
