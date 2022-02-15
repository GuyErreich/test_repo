from flask import Flask, jsonify
from base_config.environments.dev.dev_config import DevConfig
from base_config.environments.prod.prod_config import ProdConfig
from argparse import ArgumentParser

app = Flask(__name__)

@app.route('/prod/service-a/config/', methods=['GET', 'POST'])
def prod_config():
    A = ProdConfig()
    return jsonify(A.convert_to_json())

@app.route('/dev/service-a/config/', methods=['GET', 'POST'])
def dev_config():
    A = DevConfig()
    return jsonify(A.convert_to_json())

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--address', type=str, default='localhost', help='on what port the service listens')
    parser.add_argument('--port', type=int, default=5000, help='on what port the service listens')

    args = parser.parse_args()

    app.run(host=args.address, port=args.port)