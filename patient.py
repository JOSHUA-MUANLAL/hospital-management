import mysql.connector as my
from mysql.connector import Error
from flask import*


class patient:
    __patient_id=""
    __patient_password=""
    __patient_phone=""
    
    def patient_log(self,id,passowrd):
        #login phase
        __patient_id=id
        __patient_password=passowrd
        
    
        
        try:#try if databse exist or not
            mydb=my.connect(host="localhost",
                            user="root",
                            password="9596802233",
                            database="hospitalmanage")
            mycursor=mydb.cursor()
            cs="select * from patient where id=%s AND password='%s'"%(__patient_id,__patient_password)
            mycursor.execute(cs)
            
            if mycursor.fetchone()!=None:#we will check if result exist
                #if result exist we will put id and pass in session
                
                ph="select Phone_no from patient where id=%s"%(__patient_id)
                mycursor.execute(ph)
                __patient_phone=mycursor.fetchone()
                
                session['patient_id']=__patient_id 
                session["patient_password"]=__patient_password
                session["phone_no"]=__patient_phone
                cs1="select id,first_name,last_name from patient where id=%s AND password='%s'"%(__patient_id,__patient_password)
                mycursor.execute(cs1)
                result=mycursor.fetchone()
                mycursor.close()
                mydb.close()
                __patient_id=""
                __patient_password=""
                #here we will fetch first name , last name and id
                return render_template("patient.html",id=result[0],f_name=result[1],l_name=result[2])
            else:
                #if no id exist it will return false
                return "False"
        except Error as e:
            #if no database exist it will return no user found
            return "no user found"
        
    def patient_record(self,f_name,l_name):
        #method for checking the record of a specific patient
        if session:
            #if session exist it will allow access and if not it will tell the user to login first
            try:
                d2=str(request.form['dd2'])
                d1=str(request.form['dd1'])
                
                m1=str(request.form['mm1'])
                m2=str(request.form['mm2'])
                y1=str(request.form['yyyy1'])
                y2=str(request.form['yyyy2'])
                date1=y1+"-"+m1+"-"+d1
                date2=y2+"-"+m2+"-"+d2
                #we fetch input from the record form
                __patient_id=session.get('patient_id')
                __patient_password=session.get('patient_password')
                #fetching id and password from session
             
            
                mydb=my.connect(host="localhost",
                            user="root",
                            password="9596802233",
                            database="hospitalmanage")
                
                mycursor=mydb.cursor()
                
                p="select Phone_no from patient where id=%s and password='%s'"%(__patient_id,__patient_password)
                mycursor.execute(p)
                phone=mycursor.fetchone()
                
                patient_rec=str(f_name)+str(phone[0])
                
                cs="select * from %s where check_up_date BETWEEN '%s' AND '%s'"%(patient_rec,date1,date2)
                mycursor.execute(cs)
                
                rec_result=mycursor.fetchall()
                mycursor.close()
                return render_template("patient.html",f_name=f_name,l_name=l_name,data=rec_result)
            except Error as e:
                a=str(e)
                return a
        else:
            return "login first"
        
        
    def appointment_set(self,department,doctor,date,f_name,l_name):
        if session:
            patient_account=""
            
            try:
                
                mydb=my.connect(host="localhost",
                                user="root",
                                password="9596802233",
                                database="hospitalmanage")
                
                mycursor=mydb.cursor()
                __patient_id=session.get('patient_id')
                __patient_password=session.get('patient_password')
                
                
                cs="select check_up_date from %s where check_up_date ='%s' "%(doctor,date)
                
                mycursor.execute(cs)
                results=mycursor.fetchall()
                if(len(results)>40):
                    #if total appointment for doctor is more than 40 then it will show not available
                    avail="not available"
                    return "error"
                else:
                    phone_cs="select Phone_no from patient where id=%s and password='%s'"%(__patient_id,__patient_password)
                    mycursor.execute(phone_cs)
                    __patient_phone=mycursor.fetchone()
                    patient_account=f_name+str(__patient_phone[0])
                    
                    
                    patient_cs="insert into %s(check_up_date,med_prescribed,doc_appointed,appointment_attended,department)values('%s','null','%s','null','%s')"%(patient_account,date,doctor,department)
                    mycursor.execute(patient_cs)
                    mydb.commit()
                    
                    p_cs="select disease from patient where id=%s and password='%s'"%(__patient_id,__patient_password)
                    mycursor.execute(p_cs)
                    
                    
                    disease=mycursor.fetchone()
                    doctor_cs="insert into %s(check_up_date,patient_name,med_prescribed,disease) values('%s','%s', 'null','%s')"%(doctor,date,f_name,disease[0])
                    mycursor.execute(doctor_cs)
                    mydb.commit()
                    mydb.close()
                    mycursor.close()
                    
                    return "done"
                    
                    
                    
            except Error as e:
                a=str(e)
                
                return a
                        
        
            
                
            
    
        