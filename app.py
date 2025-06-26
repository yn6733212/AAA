from flask import Flask, request

app = Flask(__name__)

@app.route('/recording-handler', methods=['POST'])
def handle_recording():
    print("📥 התקבלה בקשת הקלטה מימות המשיח:")
    print(request.form.to_dict())  # מדפיס את הנתונים שהגיעו

    # מחזירים תגובה פשוטה שהמערכת תוכל להמשיך
    return "תקין, אפשר להמשיך הלאה", 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/', methods=['GET'])
def index():
    return "🔥 שרת פעיל – ממתין לבקשות מימות", 200

if __name__ == "__main__":
    app.run()
