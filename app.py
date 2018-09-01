from flask import Flask, render_template, flash, request, redirect
from database_setup import Users, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import session as login_session
import requests


engine = create_engine('sqlite:////home/bhanu/Documents/final_build/flask5/marvin_test/marvin1.db')
Base.metadata.bind = engine

app = Flask(__name__)

DBsession = sessionmaker(bind=engine)
session = DBsession()
DBsession.autoflush = True


@app.context_processor
def Dashboard_details():
    navbar_items = {'Home':'/','Components':[{'name':'title1','link':'#'},{'name':'title2','link':'#'}], 'Dropdown':[{'name':'title1', 'link':'#'},{'name':'title2','link':'#'}]}
    user_menu_items = [{'name':'Profile','link':'#','class':'fe fe-user'},{'name':'Settings','link':'#','class':'fe-settings'},
    {'name':'Inbox','link':'#','class':'fe fe-mail'},{'name':'Message','link':'#','class':'fe-send'},
    {'name':'Need Help?','link':'#','class':'fe-help-circle'},{'name':'SignOut','link':"/logout",'class':'fe-log-out'}]
    sidebar_items = [{'name':'title1','link':'#','class':'fe-alert-triangle'},{'name':'title2','link':'#','class':'fe-user'},{'name':'title3','link':'#','class':'fe-image'}]
    return dict(navbar_items = navbar_items,user_menu_items = user_menu_items, sidebar_items = sidebar_items , type = type, str = str)



@app.route('/')
def home():
    if(request.method == 'GET'):
        try:
            if login_session['verified'] == True:
               return render_template('index.html')
            else:
               return redirect('/login')
        except:
            return redirect('/login')


@app.route('/otp', methods=['POST','GET'])
def OTP():
    if request.method == 'GET':
        try:
           if login_session['phone'] != '':
               return render_template('otp.html')
           elif login_session['phone'] != '' and login['verified'] == True:
               return redirect('/')
        except:
            return redirect('/login')
    if request.method == 'POST':
        otp = request.form['otp']
        resp = requests.get('https://api-v3.redcarpetup.com/app_number_verify', {'mobile':login_session['phone'],'code':otp})
        if resp.text != 'Code':
            login_session['verified'] = True
            return redirect('/')
        elif resp.text == 'Code':
            return render_template('otp.html')


@app.route('/login',methods=['GET','POST'])
def Login():
    if request.method == 'GET':
         return render_template('login.html')
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        login_session['phone'] = phone
        if(phone != '' and password != ''):
            r = requests.get('https://api-v3.redcarpetup.com/app_number', {'mobile':phone,'name': password,'email': 'aa@gmail.com'})
            return redirect('/otp')
        else:
            return render_template('login.html')
@app.route('/logout')
def Logout():
    del login_session['phone']
    del login_session['verified']
    return redirect('/')



if __name__ == '__main__':
    app.secret_key = 'new_secret_key'
    app.run(host = '0.0.0.0',port= 8000, debug = True)
