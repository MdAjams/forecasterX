from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>🌦️ Weather Forecast API</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                background: linear-gradient(to right, #9face6, #74ebd5);
                color: #222;
                animation: fadeIn 1.5s ease-in-out;
                transition: background 0.5s, color 0.5s;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .logo {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                margin-bottom: 20px;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 30px;
                text-align: center;
                max-width: 90%;
            }
            a {
                padding: 12px 24px;
                font-size: 1rem;
                background-color: #333;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            a:hover {
                background-color: #555;
            }
            .controls {
                margin-top: 20px;
                display: flex;
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            button {
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                background: #f0f0f0;
                cursor: pointer;
                font-weight: bold;
            }
            canvas {
                margin-top: 40px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                padding: 10px;
                width: 90%;
                max-width: 600px;
            }
        </style>
    </head>
    <body>
        <img class="logo" src="https://cdn-icons-png.flaticon.com/512/1779/1779940.png" alt="Weather Logo">
        <h1>🌤️ Welcome to the Weather Forecast API</h1>
        <p>Predict temperature and weather conditions using machine learning.<br>
        Use the button below to explore the API endpoints.</p>
        <a href="/docs">Open API Docs</a>

        <canvas id="tempChart"></canvas>

        <div class="controls">
            <button onclick="toggleMusic()">🎵 Toggle Music</button>
            <button onclick="toggleTheme()">🌓 Toggle Theme</button>
        </div>

        <audio id="bg-music" loop>
            <source src="https://www.bensound.com/bensound-music/bensound-sunny.mp3" type="audio/mp3">
        </audio>

        <script>
            const ctx = document.getElementById('tempChart').getContext('2d');
            const tempChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                    datasets: [{
                        label: 'Temperature (°C)',
                        data: [22, 24, 23, 26, 25, 27, 28],
                        borderColor: '#FF5733',
                        backgroundColor: 'rgba(255, 87, 51, 0.2)',
                        tension: 0.4,
                        fill: true,
                        pointRadius: 4,
                        pointBackgroundColor: '#FF5733'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top',
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            function toggleMusic() {
                const audio = document.getElementById('bg-music');
                if (audio.paused) {
                    audio.play();
                } else {
                    audio.pause();
                }
            }

            function toggleTheme() {
                const isDark = document.body.style.background.includes("#222");
                if (isDark) {
                    document.body.style.background = "linear-gradient(to right, #9face6, #74ebd5)";
                    document.body.style.color = "#222";
                } else {
                    document.body.style.background = "#222";
                    document.body.style.color = "#eee";
                }
            }
        </script>
    </body>
    </html>
    """
