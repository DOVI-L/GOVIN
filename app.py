from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # מאפשר לאתר שלך ב-GitHub Pages לתקשר עם השרת

@app.route('/fetch')
def fetch_url():
    target_url = request.args.get('url')
    if not target_url:
        return "נא לספק כתובת אתר", 400
    
    try:
        # שליחת בקשה לאתר המבוקש
        response = requests.get(target_url, timeout=10)
        return response.text
    except Exception as e:
        return f"שגיאה בגישה לאתר: {str(e)}", 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
