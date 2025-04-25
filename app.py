from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from sharedvalkey import SharedValkey

wsgi_app = Flask(__name__)
shared_valkey = SharedValkey()

@wsgi_app.route('/', methods=['GET'])
async def index():
    client = await shared_valkey.get_or_create_client()
    await client.set("key1", "value1")
    value = await client.get("key1")
    print(f"GET key1 in /: {value}")
    return 'Index Page'

@wsgi_app.route('/hello', methods=['GET'])
async def hello():
    client = await shared_valkey.get_or_create_client()
    await client.set("key2", "value2")
    value = await client.get("key2")
    print(f"GET key2 in /hello: {value}")
    return 'Hello, World'

app = WsgiToAsgi(wsgi_app)
