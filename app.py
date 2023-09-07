from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/api', strict_slashes=False)
def api():
    """Returns a JSON-formatted dict"""
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    return {
        "slack_name": slack_name,
        "current_day": datetime.today().strftime("%A"),
        "utc_time": datetime.now().isoformat(),
        "track": track,
        "github_file_url": "https://github.com/BobadeKenny/stage1api/blob/main/app.py",
        "github_repo_url": "https://github.com/BobadeKenny/stage1api",
        "status": 200
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

    