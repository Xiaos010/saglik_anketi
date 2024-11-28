from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# SQLite veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('anket.db')
    conn.row_factory = sqlite3.Row
    return conn

# Veritabanı tablosunu oluştur
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS anket_sonuclari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender TEXT,
            age_range TEXT,
            q1 TEXT,
            q2 TEXT,
            q3 TEXT,
            q4 TEXT,
            q5 TEXT,
            q6 TEXT,
            q7 TEXT,
            q8 TEXT,
            q9 TEXT,
            q10 TEXT,
            q11 TEXT,
            q12 TEXT,
            q13 TEXT,
            q14 TEXT,
            q15 TEXT,
            q16 TEXT,
            q17 TEXT,
            q18 TEXT,
            q19 TEXT,
            q20 TEXT,
            q21 TEXT,
            q22 TEXT,
            q23 TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Ana Sayfa: HTML Formunu Göster
@app.route("/")
def index():
    return render_template("index.html")

# Anket Verisini Al ve Kaydet
@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.json  # Gelen JSON verisi
        conn = get_db_connection()
        cursor = conn.cursor()

        # Veriyi tabloya ekle
        cursor.execute('''
            INSERT INTO anket_sonuclari (
                gender, age_range, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            data.get("gender"),
            data.get("age_range"),
            data.get("q1"),
            data.get("q2"),
            data.get("q3"),
            data.get("q4"),
            data.get("q5"),
            data.get("q6"),
            data.get("q7"),
            data.get("q8"),
            data.get("q9"),
            data.get("q10"),
            data.get("q11"),
            data.get("q12"),
            data.get("q13"),
            data.get("q14"),
            data.get("q15"),
            data.get("q16"),
            data.get("q17"),
            data.get("q18"),
            data.get("q19"),
            data.get("q20"),
            data.get("q21"),
            data.get("q22"),
            data.get("q23")
        ))

        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Anket başarıyla kaydedildi."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    init_db() 
    app.run(debug=True)
