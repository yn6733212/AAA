from flask import Flask, request

app = Flask(__name__)

@app.route("/yemot", methods=["POST"])
def handle_yemot():
    try:
        data = request.form.to_dict()
        print("📥 התקבלה בקשה מימות:", data)

        # שמירה ללוג (לבדיקה)
        with open("yemot_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(str(data) + "\n")

        return "תקין אפשר להמשיך הלאה"
    
    except Exception as e:
        print("❌ שגיאה בטיפול בבקשה:", str(e))
        return "שגיאה"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
