from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
    return "300"
def run():
    app.run(host="0.0.0.0", port=80)
server = Thread(target=run)
server.start()
