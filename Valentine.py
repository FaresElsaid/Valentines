from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Be My Valentine ❤️</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
            text-align: center;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
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

        .corner {
            position: fixed;
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .top-left { top: 50px; left: 50px; }
        .top-right { top: 50px; right: 50px; }
        .bottom-left { bottom: 50px; left: 50px; }
        .bottom-right { bottom: 50px; right: 50px; }
    </style>
</head>
<body>

    <img src="/static/Pic 1.jpg" class="corner top-left">
    <img src="/static/Pic 2.jpg" class="corner top-right">
    <img src="/static/Pic 3.jpg" class="corner bottom-left">
    <img src="/static/Pic 4.jpeg" class="corner bottom-right">

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
    app.run()
