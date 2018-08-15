from flask import Flask, render_template, redirect, url_for, request,session
from flaskext.mysql import MySQL
from datetime import datetime
import os
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'Destiny_87'
mysql = MySQL()
mail = Mail(app)

# MySQL Configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ISEER'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'theiseer@gmail.com'
app.config['MAIL_PASSWORD'] = 'Distinct@2018'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def root():
    return render_template('login.html')


@app.route('/login')
def success2():
    return render_template('login.html')


@app.route('/failure/')
def failure():
    return render_template('failure.html')


@app.route('/empty')
def empty():
    return 'ErroR! :-('

@app.route("/mail")
def mail():
   msg = Message('Performance Evaluation', sender = 'theiseer@gmail.com', recipients = ['1keysuccess@gmail.com'])
   msg.body = "Please complete your performance evaluation and return to me."
   mail.send(msg)
   return "Sent"


@app.route('/home',methods = ['POST','GET'])
def home():
    if request.method=='GET':
        session[userid] = userid
    return render_template('home.html')


@app.route('/superhome')
def superhome():
    if request.method=='GET':
        session[userid] =userid
        return render_template('superhome.html')



@app.route('/registration', methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        empid = request.form['empid']
        first_name = request.form['fname']
        last_name = request.form['lname']
        sex = request.form['sex']
        dob = request.form ['dob']
        email = request.form ['email']
        department = request.form['department']
        jobtitle = request.form['jobtitle']
        hiredate = request.form['hiredate']
        supervisor = request.form['supervisor']
        emptype = request.form['emptype']
        password = request.form['password']

        print(first_name)
        print(last_name)

        conn = mysql.connect()
        cursor = conn.cursor()

        try:
            query = "INSERT Into Employee values ('"+ empid + "','" + first_name + "','" + last_name + "', '" + sex + "' , '" + dob + "','" + email + "','" + department + "','" + jobtitle + "','" + hiredate + "', '" + supervisor + "' , '" + emptype + "','" + password + "') ;"
            cursor.execute(query)
            conn.commit()
            Print ('Employee Successfully Added')
            return redirect(url_for('superhome'))


        finally:
            conn.close()
    return render_template('registration.html')


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        session['userid'] = userid
        #print('username  %s' % userid)
        #print('password  %s' % password)

        if not userid or (not password):
            return redirect(url_for('failure'))
        #Create the MySQL connection
        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()
        cursor2 = conn.cursor()


        try:
            query="SELECT role from Users where empid='"+userid+"' and password=('"+password+"');"
            query2="SELECT FirstName, JobTitle, Department, Supervisor, HireDate, EmpType from Employee where empid = '"+userid+"';"

            print(query)
            print(query2)

            cursor.execute(query)
            cursor2.execute(query2)


            data = cursor.fetchone()
            data3 = cursor2.fetchall()
            data2 = data3[0]
            print(data)
            print(data2)


            if data is None:
                return redirect(url_for('failure'))

            elif data[0]=='Supervisor':
                return render_template('superhome.html', FirstName=data2[0], JobTitle=data2[1], HireDate=data2[4],   EmpType=data2[5])
            else:
                return render_template('home.html',FirstName=data2[0], JobTitle=data2[1], Department=data2[2], Supervisor=data2[3], HireDate=data2[4], EmpType=data2[5])

        except Exception as e:
            print(e)
        finally:
            conn.close()
    #return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/myemployees',methods=['GET'])
def myemployees():
        #Create the MySQL connection
        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()

        try:
            query="SELECT * from  employee where Supervisor IS NOT NULL;"
            cursor.execute(query)
            data = cursor.fetchall()
            for row in data:
                EmpID = [0]
                FirstName = [1]
                LastName = [2]
                Sex = [3]
                DOB = [4]
                Email = [5]
                Department = [6]
                JobTitle = [7]
                HireDate = [8]
                Supervisor = [9]
                print(EmpID, FirstName,LastName,Sex,DOB,Email,Department,JobTitle,HireDate,Supervisor)
            #print(data)

        except Exception as e:
            print(e)
        finally:
            conn.close()
        #if username=='admin' and password=='password123':
            #return redirect(url_for('success', name=username))
        #else:
            #return redirect(url_for('failure', name=username))

        return render_template('myemployees.html', name = data)



@app.route('/kpi',methods=['POST','GET'])
def kpiAssessment():
    if request.method == 'POST':
        kpi_one = request.form['kpi_one']
        myeval_1 = request.form['myeval_1']
        supereval_1 = request.form['supereval_1']
        mycom_1 = request.form['mycom_1']
        supercom_1 = request.form['supercom_1']

        kpi_two = request.form['kpi_two']
        myeval_2 = request.form['myeval_2']
        supereval_2= request.form['supereval_2']
        mycom_2 = request.form['mycom_2']
        supercom_2 = request.form['supercom_2']


        kpi_three = request.form['kpi_three']
        myeval_3 = request.form['myeval_3']
        supereval_3 = request.form['supereval_3']
        mycom_3 = request.form['mycom_3']
        supercom_3 = request.form['supercom_3']

        kpi_four = request.form['kpi_four']
        myeval_4 = request.form['myeval_4']
        supereval_4 = request.form['supereval_4']
        mycom_4 = request.form['mycom_4']
        supercom_4 = request.form['supercom_4']

        kpi_five = request.form['kpi_five']
        myeval_5 = request.form['myeval_5']
        supereval_5 = request.form['supereval_5']
        mycom_5 = request.form['mycom_5']
        supercom_5 = request.form['supercom_5']

        kpi_six = request.form['kpi_six']
        myeval_6 = request.form['myeval_6']
        supereval_6 = request.form['supereval_6']
        mycom_6 = request.form['mycom_6']
        supercom_6 = request.form['supercom_6']

        print(kpi_two)

        #if kpi_one or kpi_two or kpi_three or kpi_four or kpi_five or kpi_six is empty:
         #   return ['Atleast One Field is Empty']
          #  print()

        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()


        try:
            query="INSERT into kpiAssessment values (10005,'" + kpi_one + "','" + myeval_1 + "','" + supereval_1 + "', '" + mycom_1 + "' , '" + supercom_1 + "','" + kpi_two + "','" + myeval_2 + "','" + supereval_2 + "', '" + mycom_2 + "' , '" + supercom_2 + "','" + kpi_three + "','" + myeval_3 + "','" + supereval_3 + "', '" + mycom_3 + "' , '" + supercom_3 + "', '" + kpi_four + "','" + myeval_4 + "','" + supereval_4 + "', '" + mycom_4 + "' , '" + supercom_4 + "' , '" + kpi_five + "','" + myeval_5 + "','" + supereval_5 + "', '" + mycom_5 + "' , '" + supercom_5 + "','" + kpi_six + "','" + myeval_6 + "','" + supereval_6 + "', '" + mycom_6 + "' , '" + supercom_6 + "');"
            cursor.execute(query)
            print(query)
            conn.commit()
            return redirect(url_for('engage'))

        #except Exception as e:
         #   print(e)
            #return redirect(url_for('', name=username))
        finally:
            conn.close()
            #conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        #cursor = conn.cursor()
    return render_template('kpi.html')


@app.route('/engage',methods=['POST','GET'])
def engage():
    if request.method == 'POST':
        assess_4 = request.form['assess4']
        myeval_4 = request.form['myeval4']
        supeval_4 = request.form['supeval4']
        mycom_4 = request.form['mycom4']
        supcom_4 = request.form['supcom4']
        print(assess_4)

        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()

        return redirect(url_for('competence'))

        #finally:
        #    conn.close()
    return render_template('engage.html')



@app.route('/competence', methods = ['POST','GET'])
def competence():
    print('Ker')
    if request.method=='POST':
        knowledge = request.form['knowledge']
        service = request.form['service']
        communication = request.form['communication']
        decisions = request.form['decisions']
        initiative = request.form['initiative']
        lead = request.form['lead']

        print(knowledge)

        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()

        try:
            query="INSERT into competencies values (10005,'"+knowledge + "','" + service + "','" + communication + "', '" + decisions + "' , '" + initiative + "','" + lead + "');"
            cursor.execute(query)
            conn.commit()
            return redirect(url_for('anchors'))

        #except Exception as e:
         #   print(e)
            #return redirect(url_for('', name=username))
        finally:
            conn.close()
        #conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        #cursor = conn.cursor()
    return render_template('competence.html')


@app.route('/anchors', methods=['POST','GET'])
def anchors():
    print('me')
    if request.method=='POST': 
        punctual = request.form['punctual']
        depends = request.form['depends']
        adapt = request.form['adapt']
        personality = request.form['personality']
        teamwork = request.form['teamwork']
        cooperate = request.form['cooperate']

        print("pun: " + punctual)

        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()

        try:
            query="INSERT into anchors values (10005,'"+punctual + "','" + depends + "','" + adapt + "', '" + personality + "' , '" + teamwork + "','" + cooperate + "');"
            cursor.execute(query)
            conn.commit()
            return redirect(url_for('recommend'))

        #except Exception as e:
            #print(e)
            #return redirect(url_for('', name=username))
        finally:
            conn.close()
        #conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        #cursor = conn.cursor()
    return render_template('anchors.html')


@app.route('/recommend', methods=['POST' ,'GET'])
def recommend():
    if request.method=='POST':
        assess_1 = request.form['assess_1']
        assess_2 = request.form['assess_2']
        assess_3 = request.form['assess_3']
        assess_4 = request.form['assess_4']
        assess_5 = request.form['assess_5']
        assess_6 = request.form['assess_6']
        attitude   = request.form['attitude']
        initiative = request.form['initiative']
        timely    = request.form['timely']
        personality = request.form['personality']
        teamwork    = request.form['teamwork']
        promote   = request.form['promote']
        train     = request.form['train']
        nochange    = request.form['nochange']
        demote    = request.form['demote']
        dismiss   = request.form['dismiss']

        print(assess_1)

        try:
            query="INSERT  into recommendations values  (10005,'"+ assess_1 + "','" + assess_2 + "','" + assess_3 + "', '" + assess_4 + "' , '" + assess_5 + "','" + assess_6 + "', '" + attitude + "' '" + initiative + "', '" + timely + "', '" + personality + "', '" + teamwork + "', '" + promote + "', '" + train + "', '" + nochange + "', '" + demote + "', '" + dismiss + "');"
            cursor.execute(query)
            conn.commit()
            return redirect(url_for('review'))

        #except Exception as e:
        #    print(e)
            #return redirect(url_for('', name=username))
        finally:
            conn.close()
        #conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        #cursor = conn.cursor()
    return render_template('recommend.html')


@app.route('/review', methods=['POST','GET'])
def review():
    if request.method==('POST'):
        performanceIndicators = request.form['kpi']
        competencies = request.form['competence']
        anchors  = request.form['anchors']
        strengths = request.form['strengths']
        improvement = request.form['improve']
        training = request.form['training']
        employeecomments = request.form['empcomments']
        futureGoals = request.form['goals']
        confirm = request.form['confirm']
        print(competencies)

        try:
            query="INSERT * into review;"
            cursor.execute(query)
            conn.commit()
            return redirect(url_for('home'))

        except Exception as e:
            print(e)
            #return redirect(url_for('', name=username))
        finally:
            conn.close()
        conn = mysql.connect()
        #create a cursor to traverse the dataset using the connection
        cursor = conn.cursor()
    return render_template('review.html')


def department():
    deptId = request.form['deptId']
    deptName = request.form['deptName']
    print (deptName)



def supervisor():
    supId = request.form['supId']
    empId = request.form['empId']
    print (supId)


def dept_manager():
    deptId = request.form['deptId']
    empId = request.form['empId']
    appt_date = request.form['appt_date']
    rsgn_date = request.form['rsgn_date']
    print (deptId)


def works_in():
    empId = request.form['empId']
    deptId = request.form['deptId']
    appt_date = request.form['appt_date']
    rsgn_date = request.form['rsgn_date']
    print (empId) 



if __name__ == '__main__':
	#app.run()
	app.run(debug=True)
