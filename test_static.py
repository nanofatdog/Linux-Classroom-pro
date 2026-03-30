from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def test():
    html = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Test Static Files</h1>
        <p>Testing if static files are accessible:</p>
        <ul>
            <li><a href="/static/lessons_en.json">English lessons</a></li>
            <li><a href="/static/lessons.json">Thai lessons</a></li>
        </ul>
        <p>URL for English lessons: {{ url_for('static', filename='lessons_en.json') }}</p>
        <p>URL for Thai lessons: {{ url_for('static', filename='lessons.json') }}</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)