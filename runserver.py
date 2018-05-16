"""
This script runs the MomentumWeb application using a development server.
"""

from os import environ
from MomentumWeb import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = 5555
    app.run(HOST, PORT)
