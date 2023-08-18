#import important and necessary packages 

import mysql.connector as my
from mysql.connector import Error
from flask import*
from datetime import date


class admin:
    __admin_id=""
    __admin_password=""
    __phone_no=0
    def admin_log(self,a_id,a_password):
        __admin_id=a_id
        __admin_password=a_password
        
        
        try:
            mydb=my.connect(host="localhost",
                            user="root",
                            password="9596802233",
                            database="hospitalmanage")
            
            mycursor=mydb.cursor()
            cs="select *from admin where admin_id=%s AND admin_password='%s'"%(__admin_id,__admin_password)
            mycursor.execute(cs)
            #if admin id and password exist it will direct to admin page
            
            if mycursor.fetchone()!=None:
                session['admin_id']=__admin_id
                session['admin_password']=__admin_password
                
                cs2="select name from admin where admin_id=%s AND admin_password='%s'"
                
                
                result=mycursor.fetchone()
                session['admin_name']=result
                mycursor.close()
                mydb.close()
                
                __admin_id=""
                __admin_password=""
                
                return render_template("admin.html",NAME=result)
            else:
                return "no admin found"
        except Error as e:
            return "no database"
        
    def admin_addpatient(self,f_name,l_name,phone_no,dob,gender,disease,occupation,year,NAAM):
        
        if session:
            
            try:
            
                current_date = date.today()
 
                age=int(current_date.strftime("%Y"))-int(year)
                
                mydb=my.connect(host="localhost",
                            user="root",
                            password="9596802233",
                            database="hospitalmanage")
                mycursor=mydb.cursor()
                password=f_name+year
                #password will be combination of first name and year of birth
                cs="insert into patient(first_name,last_name,password,dob,age,Phone_no,gender,disease,occupation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                code=(f_name,l_name,password,dob,age,phone_no,gender,disease,occupation)
                mycursor.execute(cs,code)
                mydb.commit()
                newuser=f_name+str(phone_no)
                cs2="create table %s (check_up_date date,med_prescribed varchar(255),doc_appointed varchar(255),appointment_attended varchar(20),department varchar(255))"%(newuser)
                mycursor.execute(cs2)
                return render_template("admin.html",NAME=NAAM)
                
            except Error as e:
                return str(e)
        else:
            return "Log in required"
        
    def appointment_check(self,p_id,p_name,p_date):
        if session:
            mydb=my.connect(host="localhost",
                            user="root",
                            password="9596802233",
                            database="hospitalmanage")
            mycursor=mydb.cursor()
            cs="select Phone_no from patient where first_name='%s' and id=%s"%(p_name,p_id)
            mycursor.execute(cs)
            phone=mycursor.fetchone()
            patient_account=p_name+str(phone[0])
            
            cs2="select * from %s"%(patient_account)
            mycursor.execute(cs2)
            result=mycursor.fetchall()
            return render_template("admin.html",result=result)
            
            
            
            
              
            
            
        
        
        