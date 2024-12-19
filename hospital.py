import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# db = sqlite3.connect("hospital.db")
# db.execute("CREATE TABLE patients(username TEXT, id INTEGER, age INTEGER, address TEXT, phone_number INTEGER)")
# cr.execute("INSERT INTO admins(id, username, password) VALUES(1, 'admin', 123456)")
def check_usAndpass(username, password):
    db = sqlite3.connect("hospital.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM admins WHERE username = ? AND password = ?",(username, password))
    user = cr.fetchone()
    db.close()
    return user
def check_usAnid(username, id):
    db = sqlite3.connect("hospital.db")
    cr = db.cursor()
    cr.execute("SELECT username,id FROM patients WHERE username = ? AND id = ?",(username, id))
    user = cr.fetchone()
    db.close()
    return user
    

@app.route("/", methods=['GET', 'POST']) # loock how can run the program in index pag
def login():
   
    if request.method == "POST":
        # //////////////////////
        user_ad = request.form.get("user")
        password = request.form.get("password")
        
        if check_usAndpass(user_ad, password):
            return redirect(url_for("home"))
        else:
            return render_template("index.html")
    else:
        return render_template('index.html')
    
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        useranme = request.form.get("username").capitalize()
        id = request.form.get("id")
        age = request.form.get("age")
        address = request.form.get("address")
        phone = request.form.get("phoneNumber")
        
        db = sqlite3.connect("hospital.db")
        cr = db.cursor()
        cr.execute("INSERT INTO patients(username, id, age, address, phone_number) VALUES(?, ?, ?, ?, ?)", (useranme, id, age, address, phone))
        db.commit()
        db.close()
        return render_template('patient-page.html',  Name=useranme, id=id, age=age, add=address,Phone=phone)
    else:
    
        return render_template('register.html')

@app.route("/patient", methods=['GET', 'POST'])
def patient():
    if request.method == "POST":
        user = request.form.get("user").capitalize()
        id = request.form.get("id")
        
        db = sqlite3.connect("hospital.db")
        cr = db.cursor()
        cr.execute("SELECT age FROM patients WHERE username = ? AND id = ?",(user, id))
        age = cr.fetchone()
        cr.execute("SELECT address FROM patients WHERE username = ? AND id = ?",(user, id))
        add = cr.fetchone()
        cr.execute("SELECT phone_number FROM patients WHERE username = ? AND id = ?",(user, id))
        phone = cr.fetchone()
        db.close()
        
        
        if check_usAnid(user, id):
            return render_template('patient-page.html', Name=user.title(), id=id, age=str(age[0]), add=str(add[0]),Phone=str(phone[0]))
        else:
            return render_template("patient.html")
    
    return render_template('patient.html')

@app.route("/patient-page")
def patient_page():
    return render_template('patient-page.html')

@app.route("/interview", methods=['GET', 'POST'])
def intirview():
    if request.method == "POST":
        choss=request.form.get("sectios")
        return render_template("true.html",section=choss)
    
    return render_template('interview.html')

@app.route("/info")
def info():
    return render_template('info.html')

if(__name__) == "__main__":
    app.run(debug=True, port=5550)



