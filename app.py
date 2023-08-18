#import necessary packages

from flask import *
import patient as pt
import admin as ad
import mysql.connector as my



app=Flask(__name__,static_url_path='/static', static_folder='static')
app.secret_key = 'joshua'
@app.route("/")
def home():
    return render_template('hospital.html')
#this render our home page [hospital management login interface]


@app.route("/patient",methods=["POST"])
def patientlog():
    id=request.form['user']
    password=request.form['password']
    #request id and password from form
    
    pat=pt.patient()
    #patient package and instance creation
    
    answer=pat.patient_log(id,password)
    #log input function call
    return answer


@app.route("/patient/<f_name>+<l_name>",methods=["POST"])
def patientrecord(f_name,l_name):#to check the patinet records
   
    precord=pt.patient()
    answer=precord.patient_record(f_name,l_name)
    return answer


@app.route("/admin",methods=['POST'])
def adminlog(): #for admin log in
    admin_id=request.form['admin']
    admin_password=request.form['password']
    ad_object=ad.admin()
    answer=ad_object.admin_log(admin_id,admin_password)
    
    return answer

@app.route("/admin/<NAAM>",methods=['POST'])
def admin_add_patient(NAAM): #for admin to add new patient
    f_name=request.form['first_name']
    l_name=request.form['last_name']
    phone_no=request.form['phoneno']
    day=request.form['dd']
    month=request.form['mm']
    year=request.form['yyyy']
    dob=str(year)+"-"+str(month)+"-"+str(day)
    gender=request.form['Gender']
    disease=request.form['disease']
    occupation=request.form['occupation']
    ad_object=ad.admin()
    answer=ad_object.admin_addpatient(f_name,l_name,phone_no,dob,gender,disease,occupation,year,NAAM)
    return answer

@app.route("/patient/appointment/<f_name>+<l_name>",methods=['POST'])
def appointment(f_name,l_name): #for patient to set appointment
    department=request.form['department']
    doctor=request.form['doctor']
    date=str(request.form['appointment_date'])
    p_obj=pt.patient()
    answer=p_obj.appointment_set(department,doctor,date,f_name,l_name)
    return answer
    
@app.route("/admin/appointment",methods=['POST'])
def appointment_check(): #for admin to check appointment
    p_id=request.form['id']
    p_name=request.form['name']
    p_date=request.form['date']
    
    ap_obj=ad.admin()
    answer=ap_obj.appointment_check(p_id,p_name,p_date)  
    return answer
   
@app.route("/doctor",methods=["POST"])  
def doctor():
    
    if session:#if session is already available then no log in is necessary
        n=session["doctor_name"]
        p=session["doctor_department"]
        return render_template("doctorlogin.html",name=n,department=p)
    
    
    
    
    
    id_doctor=request.form["doctorid"]
    pass_doctor=request.form['doctorpass']
    
    try:
        
        mydb=my.connect(
            host="localhost",
            user="root",
            password="9596802233",
            database="hospitalmanage"
        )
        
    except:
        return "no user found"
    
    mycursor=mydb.cursor()
    cs="select doctor_name,department from doctor where doctor_id=%s and doctor_password='%s'"%(int(id_doctor),pass_doctor)
    mycursor.execute(cs)
    d_doctor=mycursor.fetchone()
    if d_doctor!=None:
         
        session["doctor_id"]=id_doctor
        session["doctor_pass"]=pass_doctor
        doc_name=d_doctor[0]
        session["doctor_name"]=doc_name
        session["doctor_department"]=d_doctor[1]
        return render_template("doctorlogin.html",name=d_doctor[0],department=d_doctor[1])
    
@app.route("/doctor/check",methods=['POST'])
def doctorlogin():
    if session:
        name=session['doctor_name']
        department=session['doctor_department']
        p_id=request.form['p_id']
        med_p=request.form['med']
        check=request.form['appointment']
        p_name=""
        
        mydb=my.connect(
            host="localhost",
            user="root",
            password="9596802233",
            database="hospitalmanage"
        )
        mycursor=mydb.cursor()
        cs="select first_name,Phone_no from patient where id=%s"%(int(p_id))
        mycursor.execute(cs)
        result=mycursor.fetchone()
        p_name=str(result[0])
        p_database=str(p_name+str(result[1]))
        
        cs1="UPDATE %s SET med_prescribed='%s' where med_prescribed='null' and patient_name='%s'"%(name,med_p,p_name)
        mycursor.execute(cs1)
        mydb.commit()
        
        cs2="UPDATE %s SET med_prescribed='%s',appointment_attended='Done' where doc_appointed='%s' and appointment_attended='null'"%(p_database,med_p,name)
        mycursor.execute(cs2)
        mydb.commit()
        
        return render_template("doctorlogin.html",name=p_name,department=department)
    
    else:
        return "Log in first"
        



if __name__=="__main__":
    app.run(debug=True)