
from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Be My Valentine ❤️</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
            text-align: center;
            overflow: hidden;
        }

        h1 {
            font-size: 3rem;
        }

        #yesBtn {
            padding: 15px 30px;
            font-size: 20px;
            border: none;
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            margin: 20px;
            transition: transform 0.2s;
        }

        #noBtn {
            padding: 15px 30px;
            font-size: 20px;
            border: none;
            border-radius: 10px;
            background-color: #f44336;
            color: white;
            cursor: pointer;
            position: absolute;
        }
    </style>
</head>
<body>

    <h1>Will you be my Valentine? 💘</h1>

    <button id="yesBtn" onclick="yesClicked()">Yes 💕</button>
    <button id="noBtn" onmouseover="moveNo()">No 🙄</button>

    <script>
        let yesSize = 1;

        function yesClicked() {
            document.body.innerHTML = "<h1>YAYYY ❤️🥰 I love you!</h1>";
        }

        function moveNo() {
            const noBtn = document.getElementById("noBtn");
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 50);

            noBtn.style.left = x + "px";
            noBtn.style.top = y + "px";

            yesSize += 0.1;
            document.getElementById("yesBtn").style.transform = "scale(" + yesSize + ")";
        }
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

