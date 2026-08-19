from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
        <head>
            <title>EKS Demo Application</title>
        </head>
        <body>
            <h1>Hello from Amazon EKS!</h1>
            <p>Application is running successfully.</p>
            <p>Pod Hostname: {hostname}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "Application is healthy", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    