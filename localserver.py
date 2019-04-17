''' 
Local Server Holding Projects
'''
from flask import Flask, url_for, request, render_template, redirect, session, flash
import os 

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def layout():
    
    return render_template('layout.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!" 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
        else:
            flash('Invalid Credentials. Please try again.')       
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
  

