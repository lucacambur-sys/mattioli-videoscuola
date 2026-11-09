from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/courses')
def get_courses():
    courses = [
        {"id": 1, "title": "Python Avanzato & Web Scraping", "category": "Python", "progress": 85, "duration": "4.5 ore", "lessons": 12},
        {"id": 2, "title": "Intelligenza Artificiale & Flask Integration", "category": "AI", "progress": 40, "duration": "6 ore", "lessons": 15},
        {"id": 3, "title": "Cybersecurity & Ethical Hacking Base", "category": "Security", "progress": 10, "duration": "5 ore", "lessons": 10},
        {"id": 4, "title": "Algoritmi e Strutture Dati in C++", "category": "C++", "progress": 60, "duration": "8 ore", "lessons": 20}
    ]
    return jsonify(courses)

@app.route('/api/quiz/submit', methods=['POST'])
def submit_quiz():
    data = request.json
    score = data.get('score', 0)
    total = data.get('total', 1)
    passed = score >= (total * 0.6)
    return jsonify({
        "success": True,
        "score": score,
        "total": total,
        "passed": passed,
        "message": "Quiz completato con successo! Ottimo lavoro." if passed else "Risposta errata, puoi riprovare."
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)