import io
from sched import scheduler
from django.shortcuts import render
from main.models import *
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum,Count
from datetime import datetime,date
from .forms import MyForm
from django.shortcuts import render
import datetime
from django.db.models import Q


from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect


from django.http import FileResponse

from reportlab.pdfgen import canvas
from django.contrib.auth.hashers import make_password, check_password

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
import pyttsx3
import re


nltk.download('stopwords')
set(stopwords.words('english'))



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics







from django.shortcuts import render, redirect
from django.contrib import messages
import uuid
import cv2
import numpy as np
import os
import requests
import io
import json
import uuid
import pytesseract
from PIL import Image




def ocrgenerate(path):
    print("path===",path)
    paths="static\\uploads\\"+path
    print(paths)
    image = cv2.imread("static\\uploads\\"+path)
    print(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))

    print("OCR Text is " + text.strip())
    # val=text.strip().split('D')
    # atte=val[0].split(',')
    # print(atte[0],atte[1])
    # # print(val[1])
    return  text.strip()




# Create your views here.
                                 ###### LOGIN ######
def home(request):
    q=doctor.objects.all()
    return render(request,'home.html',{'q':q})

def my_form(request):
    
    return render(request,'form.html')
 

def my_post(request):
        from datetime import date,datetime

        pid=request.session['pid']
        if request.method == 'POST':
                stop_words = stopwords.words('english')
                # my contribution
                stop_words.remove('very')
                stop_words.remove('not')
                
                #convert to lowercase
                text1 = request.POST['text1'].lower()
                
                # my contribution
                text_final = ''.join(i for i in text1 if not i.isdigit())
                net_txt=re.sub('[^a-zA-Z0-9\n]', ' ',text_final)
                
                #remove stopwords    
                processed_doc1 = ' '.join([i for i in net_txt.split() if i not in stop_words])
                
                

                sa = SentimentIntensityAnalyzer()
                dd = sa.polarity_scores(text=processed_doc1)
                compound = round((1 + dd['compound'])/2, 2)
                final=compound*100
                
                if "enough" in text1 or "sufficient" in text1 or "ample" in text1 or "abudant" in text1:
                   engine = pyttsx3.init()
                   engine.say('You liked us by'+str(final)+'% Thank you for your valuable response')
                   engine.runAndWait()
                   ob=feedback()
                   ob.feedback_des=text1
                   ob.date=datetime.today()
                   ob.patient_id_id=pid
                   ob.save()
                   return render(request,'form.html',{'final': final,'text1':net_txt})
                   
                elif final == 50:
                   engine = pyttsx3.init()
                   engine.say('Please enter an adequate resposnse, Thank You')
                   engine.runAndWait()
                   return render(request,'form.html',{'final': final,'text1':net_txt})
                else:
                   engine = pyttsx3.init()
                   engine.say('You liked us by'+str(final)+'% Thank you for your valuable response')
                   engine.runAndWait()
                   if final > 50:
                      ob=feedback()
                      ob.feedback_des=text1
                      ob.date=datetime.today()
                      ob.patient_id_id=pid
                      ob.save()
                      return render(request,'form.html',{'final': final,'text1':net_txt})
                   elif final < 50:
                      ob=feedback()
                      ob.feedback_des=text1
                      ob.date=datetime.today()
                      ob.patient_id_id=pid
                      ob.save()
                      return render(request,'form.html',{'final': final,'text1':net_txt})
                   else:
                       ob=feedback()
                       ob.feedback_des=text1
                       ob.date=datetime.today()
                       ob.patient_id_id=pid
                       ob.save()
                       return render(request,'form.html',{'final': final,'text1':net_txt})
        else:
           return redirect('my_form')


def login_page(request):
    forms = MyForm()

    return render(request, 'login1.html', {'form': forms})
    
def logins(request):
    forms = MyForm(request.POST)
    if forms.is_valid():
        try:
            uname=request.POST['textfield']
            password=request.POST['textfield2']
            ob=login.objects.get(username=uname,status=1)
            checkpassword=check_password(request.POST['textfield2'], ob.password)
            print(checkpassword,"**************************,Dpwd")
            if checkpassword==True:
                print(ob.usertype,"________________")
                request.session['lid']=ob.pk
                lid=request.session['lid']
                print(lid,">>>>>>>>>>>>>>>>>>>>>>")
                if ob.usertype=='admin':
                    request.session['lid']=ob.login_id
                    return HttpResponse('''<script>alert("welcome admin");window.location='admhome'</script>''') 
                elif ob.usertype=='doctor':
                    ob1=doctor.objects.get(login_id=ob.pk)
                       
                    if ob1:
                        request.session['doid']=ob1.pk
                        name=ob1.first_name+" "+ob1.last_name
                       
                    return HttpResponse('''<script>alert("welcome %s");window.location='dhome';</script>'''% name)           

                elif ob.usertype=='user':
                    ob1=patient.objects.get(login_id=ob.pk)
                    request.session['pid']=ob1.pk 
                    if ob1:
                        name=ob1.first_name+" "+ob1.last_name
                    return HttpResponse('''<script>alert("welcome %s");window.location='patienthome'</script>'''% name)


                elif ob.usertype=='lab':
                    ob1=labs.objects.get(login_id=ob.pk)
                    request.session['labid']=ob1.pk 
                    labid=request.session['labid']
                    print(labid,"???????????????")
                    if ob1:
                        name=ob1.name
                    return HttpResponse('''<script>alert("welcome %s");window.location='labhome'</script>'''% name)


                elif ob.usertype=='pharmacy':
                    ob1=pharmacy.objects.get(login_id=ob.pk)
                    request.session['pharmacyid']=ob1.pk 
                    if ob1:
                        name=ob1.name
                    return HttpResponse('''<script>alert("welcome %s");window.location='pharmacyhome'</script>'''% name)
                else:
                    return HttpResponse('''<script>alert("Invalid Username and Password");window.location='login_page'</script>''')
            else:
                return HttpResponse("<script>alert('Enter Password is wrong...!!!!');window.location='login_page';</script>")
        except Exception:
            return HttpResponse('''<script>alert("Invalid Username and Password");window.location='login_page'</script>''')
    else:
        return HttpResponse('''<script>alert("Not Correct Captcha");window.location='login_page'</script>''')
       









def labhome(request):
    vv=labs.objects.filter(pk=request.session['labid'])
    if vv:
        name=vv[0].name
    return render(request,'labindex.html',{'val':vv,'name':name})




def pharmacyhome(request):
    vv=pharmacy.objects.filter(pk=request.session['pharmacyid'])
    if vv:
        name=vv[0].name
    return render(request,'pharmacyindex.html',{'val':vv,'name':name})



def forgot(request):
    
    return render(request,'forgotpass.html')  


def got(request):
    
    unamee=request.POST['uname']
    phone=request.POST['ph']
    ob=login.objects.get(username=unamee)
    print("###################################")
    print(ob)
    if ob:
        request.session['llid']=ob.pk
        ob1=patient.objects.filter(phone=phone,login_id=ob.pk)
        if ob1: 
            import random
            number = random.randint(1111,9999)
            request.session['otp']=number
            print(number)        
            for i in ob1:
                print(i.email)
                send_mail(
                'Reset Password', 
                'OTP (One Time Password ) is : '+str(number), 
                'healhospitals06@gmail.com', 
                [i.email], 
                fail_silently=False,
            )  
        return HttpResponse('''<script>alert("mail sended");window.location='otp'</script>''')      

    return render(request, 'forgotpass.html')
def otp(request):
    # print("##############")
    if 'confirm' in request.POST:
        otpnum=int(request.POST['otpp'])
        # print("SSSS : ",otpnum)

        ottp=int(request.session['otp'])
        # print("*****************")
        # print("UUUUUUUUUUU",ottp)
        if ottp==otpnum:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return HttpResponse('''<script>alert("ssss");window.location='newpas'</script>''') 

    return render(request, 'optmsg.html') 


def newpas(request):
    lo=login.objects.get(pk=request.session['llid'])
    if 'confirm' in request.POST:
        npass=request.POST['passw']
        cpass=request.POST['cpassw']
        encryptedpassword=make_password(request.POST['cpassw'])
        lo.password=encryptedpassword
        lo.save()
        return HttpResponse('''<script>alert("confirm");window.location='/'</script>''')   
    return render(request, 'newpass.html')  

      
                                 ###### ADMIN ######

def admhome(request):
    pcount=patient.objects.filter(pstatus="1").count()
    print(pcount,":::::::::::::::::::::::::::::::::")
   
    dcount=doctor.objects.filter(dstatus="1").count()
    print(dcount,":::::::::::::::::::::::::::::::::")


    lcount=labs.objects.filter(login__status="1").count()
    print(lcount,":::::::::::::::::::::::::::::::::")

    phcount=pharmacy.objects.filter(login__status="1").count()
    print(phcount,":::::::::::::::::::::::::::::::::")

    pa=login.objects.filter(usertype='user')
    da=login.objects.filter(usertype='doctor')

    la=login.objects.filter(usertype='lab')
    ph=login.objects.filter(usertype='pharmacy')
    return render(request,'adminhome.html',{'pcount':pcount,'dcount':dcount,'pa':pa,'da':da,'phcount':phcount,'lcount':lcount,'ph':ph,'la':la})  


def admin_user_inactive(request,id):
    
    v=patient.objects.get(login_id_id=id)
    v.pstatus='0'
    up=login.objects.get(login_id=id)
    up.status='0'
    
    v.save()
    up.save()
    return HttpResponse("<script>alert('Inactive....!!!');window.location='/admhome';</script>")


def admin_user_active(request,id):
    
    
    v=patient.objects.get(login_id_id=id)
    v.pstatus='1'
    up=login.objects.get(login_id=id)
    up.status='1'
    v.save()
    up.save()

    return HttpResponse("<script>alert('active....!!!');window.location='/admhome';</script>")




def admin_doctor_inactive(request,id):
    
    v=doctor.objects.get(login_id_id=id)
    v.dstatus='0'
    up=login.objects.get(login_id=id)
    up.status='0'
    
    v.save()
    up.save()
    return HttpResponse("<script>alert('Inactive....!!!');window.location='/admhome';</script>")


def admin_doctor_active(request,id):
    
    
    v=doctor.objects.get(login_id_id=id)
    v.dstatus='1'
    up=login.objects.get(login_id=id)
    up.status='1'
    v.save()
    up.save()

    return HttpResponse("<script>alert('active....!!!');window.location='/admhome';</script>")





def admin_pharmacy_inactive(request,id):
    
    
    up=login.objects.get(login_id=id)
    up.status='0'
    
    up.save()
    return HttpResponse("<script>alert('Inactive....!!!');window.location='/admhome';</script>")


def admin_pharmacy_active(request,id):
    
    up=login.objects.get(login_id=id)
    up.status='1'
    up.save()

    return HttpResponse("<script>alert('active....!!!');window.location='/admhome';</script>")








def admin_lab_inactive(request,id):
    
    
    up=login.objects.get(login_id=id)
    up.status='0'
    
    up.save()
    return HttpResponse("<script>alert('Inactive....!!!');window.location='/admhome';</script>")


def admin_lab_active(request,id):
    
    up=login.objects.get(login_id=id)
    up.status='1'
    up.save()

    return HttpResponse("<script>alert('active....!!!');window.location='/admhome';</script>")




def mngdoctor(request):
    from datetime import datetime
    cdate=datetime.today().strftime('%Y-%m-%d')
    print(cdate)

    q1=departments.objects.all()

    if request.method=="POST":
        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        place=request.POST['textfield3']
        phone=request.POST['textfield4']
        email=request.POST['textfield5']
        passw=request.POST['textfield7']
        lno=request.POST['lno']
        db=request.POST['dob']
        gn=request.POST['gn']
        dept=request.POST['dept']

        qu=request.POST['qu']
        exp=request.POST['exp']

        img = request.FILES['file1']
        fp = FileSystemStorage()
        fs = fp.save(img.name, img)
        encryptedpassword=make_password(request.POST['textfield7'])
        print(encryptedpassword)
        q=login.objects.filter(username=email)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='mngdoctor';</script>")
        else:
            lob=login(username=email,password=encryptedpassword,usertype='doctor',status='0')
            lob.save()
            b=doctor(first_name=fname,qualification=qu,experience=exp,last_name=lname,place=place,phone=phone,email=email,login_id=lob,image=fs,dstatus='0',licence_no=lno,dob=db,gender=gn,departments_id=dept)
            b.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='mngdoctor';</script>")
    
    q=doctor.objects.all()

    return render(request,'manage doctor.html',{'q':q,'cdate':cdate,'q1':q1})


def delete(request,id):
    q=doctor.objects.get(login_id_id=id)
    q.delete()
    q2=login.objects.get(login_id=id)
    q2.delete()
    return HttpResponse("<script>alert('Removed....!!!');window.location='/mngdoctor';</script>")



def admin_update_doctor(request,id):
    mob=doctor.objects.get(doctor_id=id)

    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        lno=request.POST['lno']
        dob=request.POST['dob']

        qu=request.POST['qu']
        exp=request.POST['exp']

        mob = doctor.objects.get(doctor_id=id)
        mob.first_name = fname
        mob.last_name = lname
        mob.place = place
        mob.phone = phone
        mob.licence_no=lno
        mob.qualification=qu 
        mob.experience=exp
        mob.dob=dob
        mob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/mngdoctor'</script>''')
    return render(request,'manage doctor.html',{'mob':mob})




def search(request):
    doctorn=request.POST['select']
    oo=doctor.objects.filter(doctor_id=doctorn)
    return render(request,'View doctors.html',{'val':oo})

def viewdoctor(request):
    vd=doctor.objects.filter(dstatus=1)
    if request.method=='POST':
        pla=request.POST['pla']
        
        vd=doctor.objects.filter(first_name=pla)

    return render(request,'View doctors.html',{'val':vd})



def admin_view_doctor(request,id):
    vd = doctor.objects.filter(doctor_id=id)
    return render(request,'admin_view_doctor.html',{'val':vd})



def view_doctors(request):
    vd = doctor.objects.filter(dstatus=1)
    return render(request,'printdoc.html',{'val':vd})

def viewpatient(request):
    if request.method=='POST':
        pla=request.POST['pla']
        
        vp=patient.objects.filter(first_name=pla)
        # request.session['vp']=vp
        # print(vp,"$$$$$$$$$$$$$$$$$$$$$$$$$$")
    else:
        vp=patient.objects.filter(pstatus=1)
        # request.session['vp']=vp
        # print(vp,":::::::::::::::::::::::::::")
    return render(request,'view patients.html',{'val':vp})   




def admin_view_patients(request,id):
    
    vp=patient.objects.filter(patient_id=1)
    # request.session['vp']=vp
    # print(vp,":::::::::::::::::::::::::::")
    return render(request,'admin_view_patients.html',{'val':vp})   




def printpatient(request):
    today=date.today()
    print(today)

    vp=patient.objects.filter(pstatus=1)
    print(vp)
    return render(request,'printpatient.html',{'val':vp,'today':today})    

def printdoctor(request):
    today=date.today()
    print(today)

    vp=doctor.objects.filter(dstatus=1)
    print(vp)
    return render(request,'printdoctor.html',{'val':vp,'today':today}) 
    
def admin_manage_dept(request):

    if request.method=="POST":
        dept=request.POST['dept']
       
        q=departments.objects.filter(department=dept)
        if q:
            return HttpResponse("<script>alert('Already Exist....!!!');window.location='admin_manage_dept';</script>")
        else:
            lob=departments(department=dept)
            lob.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='admin_manage_dept';</script>")
    
    q=departments.objects.all()

    return render(request,'admin_manage_dept.html',{'q':q})


def admin_remove_department(request,id):
    q=departments.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed....!!!');window.location='/admin_manage_dept';</script>")



def admin_update_department(request,id):
    mob=departments.objects.get(id=id)

    if request.method=="POST":
        dept=request.POST['dept']
        mob.department=dept
        mob.save()
        return HttpResponse('''<script>alert("Edited");window.location='/admin_manage_dept'</script>''')
    return render(request,'admin_manage_dept.html',{'mob':mob})


# def generate_pdf(doctors):
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     pdf = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     pdf.drawString(1000, 1000, "List of Doctors")
#     y = 100
#     for doctor in doctors:
#         y -= 20
#         pdf.drawString(100, y, doctor.first_name)
#         pdf.drawString(100, y, doctor.last_name)
#         pdf.drawString(100, y, doctor.place)

#     # Close the PDF object cleanly, and we're done.
#     pdf.showPage()
#     pdf.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='doctors.pdf')



def viewleave(request):
    vl=leave.objects.all()
    return render(request,'view leave.html',{'val':vl})   

def accept(request,doctor_id): 
    ob=leave.objects.get(leave_id=doctor_id)
    ob.status='Approved'
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/viewleave'</script>''')

def reject(request,doctor_id):
    ob=leave.objects.get(doctor_id=doctor_id)
    ob.status='reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/viewleave'</script>''')



def viewfeed(request):
    vf=feedback.objects.all()
    return render(request,'view feedback.html',{'val':vf}) 

def viewpaymnts(request):
    vm=payment.objects.all()
    return render(request,'view payment.html',{'val':vm})




                                     ###### PATIENT ######

def patienthome(request):
    vv=patient.objects.filter(pk=request.session['pid'])
    if vv:
        name=vv[0].first_name+" "+vv[0].last_name
    return render(request,'patientindex.html',{'val':vv,'name':name})




def register(request):
    from datetime import datetime
    cdate=datetime.today().strftime('%Y-%m-%d')
    print(cdate)

    return render(request,'register.html',{'cdate':cdate})
def regi(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender = request.POST['radiobutton']
    place = request.POST['textfield3']
    phone=request.POST['textfield4']
    email=request.POST['textfield5']
    blood = request.POST['textfield6']
    dob = request.POST['textfield7']
    password = request.POST['textfield9']
    age=request.POST['age']
    encryptedpassword=make_password(request.POST['textfield9'])
    print(encryptedpassword)
    q=login.objects.filter(username=email)
    if q:
        return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='register';</script>")
    else:
        lob=login()
        lob.username=email
        lob.password=encryptedpassword
        lob.usertype='user'
        lob.status='0'
        lob.save()
        pob=patient()
        pob.login_id=lob
        pob.first_name=fname
        pob.last_name=lname
        pob.place=place
        pob.gender=gender
        pob.place=place
        pob.blood_group=blood
        pob.dob=dob
        pob.phone=phone
        pob.email=email
        pob.pstatus='0'
        pob.age=age

        pob.save()
        return HttpResponse('''<script>alert("Successfully signup");window.location='/'</script>''')    



def sendfeedback(request):
    return render(request,'sendfeedb.html')

def feed(request):
    feedb=request.POST['textfield']
    ob=feedback()
    ob.feedback_des=feedb
    ob.date=datetime.today()
    ob.patient_id=patient.objects.get(pk=request.session['pid'])
    ob.save()
    return HttpResponse('''<script>alert("send feedback");window.location="/patienthome"</script>''')    

# def pviewdoctor(request):
#     vv=doctor.objects.all()
#     return render(request,'pviewdoctors.html',{'doc':vv})


def user_view_dept(request):
    val=departments.objects.all()


    if 'search' in request.POST:
        select=request.POST['select']
        print(select,"?????????????????????")
        id=int(select)
        print(id,"__________________")
        return HttpResponse('''<script>window.location='/search1/%s'</script>'''%(id))
    return render(request,'user_view_dept.html',{'val':val})



def search1(request,id):
    print(id,"*******************")

    
 
    vv=doctor.objects.filter(departments_id=id)
    if 'search' in request.POST:
        doctorn=request.POST['select']
        print("#######")
        print(doctorn)
        print("###########")
        vv1=doctor.objects.filter(doctor_id=doctorn)
        print(vv1)
        # oo=doctor.objects.filter(doctor_id=doctorn)
        from django.utils import timezone
        today = timezone.now().date()
        print(today)

        from django.utils import timezone

        today = datetime.datetime.now().date()
        tomorrow = today + datetime.timedelta(days=1)
        day_after_tomorrow = today + datetime.timedelta(days=2)

        shed = schedule.objects.filter(Q(date__range=[tomorrow, day_after_tomorrow])).filter(doctor_id=doctorn)
        
        #shed = schedule.objects.filter(doctor_id=doctorn)
        print("_________##################________",shed)
        return render(request,'pviewdoctors.html',{'sh':shed,'doc1':vv1,'doc':vv})
        
        # shed=schedule.objects.filter(doctor_id_id=doctorn)
        # return HttpResponse('''<script>window.location='/search1'</script>''')
        # return HttpResponseRedirect("/search1/%s"%sh)
    return render(request,'pviewdoctors.html',{'doc':vv})
    
    

    
def pviewbooking(request):
    vv=booking.objects.filter(patient_id_id=request.session['pid'])
    return render(request,'pviewbooking.html',{'val':vv})

def viewtime(request,id,dattt):
    # id=id
    # d=date
    dattt=dattt
    shed=schedule.objects.filter(schedule_id=id)
    request.session['sid']=id
    

    for ss in shed:
        # start_time = ss.start_time
        # print(start_time)
        # end_time = ss.end_timne
        # print(end_time)
        
     
        from datetime import datetime, timedelta
        

        end_time = ss.end_timne
        start_time = ss.start_time
        cc = datetime.now().strftime("%H:%M")
        

        start_time = datetime.strptime(start_time, "%H:%M")
        stt=start_time.strftime("%I:%M %p")
        # print(stt)
        end_time = datetime.strptime(end_time, "%H:%M")
        time_list = [stt]

        while end_time > start_time:
            if start_time < end_time:
                # print("#######################")
                start_time = start_time + timedelta(minutes=10)
                # print("TTTTTTTTTTTTTTTTT : ",start_time)
                time_list.append(start_time.strftime("%I:%M %p"))
            # print("Updated Start Time:", start_time.strftime("%I:%M %p"))




        # while end_time >= start_time:
        #     start_time += current_time + timedelta(minutes=5)
        #     print(start_time)
        #     if end_time >= start_time:
        #         time_list.append(start_time)
    return render(request,'viewtimeslot.html',{'dattt':dattt,'time_list': time_list})

# def viewtime(request, schedule_id):
#     schedule= schedule.objects.get(schedule_id=schedule_id)
#     start_time = schedule.start_time
#     end_time = schedule.end_time
#     time_list = []

#     while end_time >= start_time:
#         start_time += datetime.timedelta(minutes=5)
#         if end_time >= start_time:
#             time_list.append(start_time)
    
#     return render(request, 'viewtimeslot.html', {'time_list': time_list})







def book(request):
    from datetime import date,datetime 

    today=date.today()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    if 'submit' in request.POST:
        date1=str(request.POST['dt'])
        time1=request.POST['time']
        # print("qqqqqqqqqqqqqqqqqqqqqqqqqqq",date,time)
        print("########### : ", request.session.get('sid'))
        she=schedule.objects.get(pk=request.session.get('sid'))
        print("ssssssssss : ",she.pk)
        pat=patient.objects.get(pk=request.session['pid'])
        print("ppppppppppppppp : ",pat.pk)


        bk=booking()
        bk.date=date1
        bk.time=time1
        bk.bk_date=today
        bk.status='pending'
        bk.patient_id_id=pat.pk
        bk.schedule_id_id=she.pk
        bk.save()

        q=schedule.objects.filter(schedule_id=request.session.get('sid'))
        print(q)
        if q:
            fee=q[0].fee_amount 
            print(fee,"********************")
    return HttpResponse('''<script>alert("booked");window.location="/payments/%s/%s"</script>'''%(bk.book_id,fee))    




def editp(request):
    ob=patient.objects.filter(patient_id=request.session['pid'])
    return render(request,'editpatient.html',{'val':ob})

def edittp(request):
    place = request.POST['place']
    phone=request.POST['phone']
    email=request.POST['email']
    mob = patient.objects.get(patient_id=request.session['pid'])
    mob.place = place
    mob.phone = phone
    mob.email=email
    mob.save()
    return HttpResponse('''<script>alert("Edited");window.location='/patienthome'</script>''')










def editpharmacy(request):
    ob=pharmacy.objects.filter(id=request.session['pharmacyid'])
    
    if request.method=="POST":
        place = request.POST['place']
        place = request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        mob = pharmacy.objects.get(id=request.session['pharmacyid'])
        mob.place = place
        mob.phone = phone
        mob.email=email
        mob.save()
        return HttpResponse('''<script>alert("Edited");window.location='/pharmacyhome'</script>''')

    return render(request,'editpharmacy.html',{'val':ob})



# def editlab(request):
#     lid=request.session['lid']
#     print(lid)

#     q1=labs.objects.filter(login_id=lid)
#     print(q1)
#     if q1:
#         labid=q1[0].id

#     ob=labs.objects.filter(id=labid)
#     print(ob)
#     return render(request,'editlab.html',{'val':ob})

def editlab(request):
    lid=request.session['lid']
    print(lid)

    q1=labs.objects.filter(login_id=lid)
    print(q1)
    if q1:
        labid=q1[0].id

    ob=labs.objects.filter(id=labid)
    
    if request.method=="POST":
        place = request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        mob = labs.objects.get(login_id=lid)
        mob.place = place
        mob.phone = phone
        mob.email=email
        mob.save()
        return HttpResponse('''<script>alert("Edited");window.location='/labhome'</script>''')

    return render(request,'editlab.html',{'val':ob})



                                        ###### DOCTOR ######    


def dhome(request):
    vv=doctor.objects.filter(pk=request.session['doid'])
    if vv:
        name=vv[0].first_name+" "+vv[0].last_name
    return render(request,'doctorindex.html',{'val':vv,'name':name})  

def rleave(request):
    from datetime import datetime
    tdate=datetime.today().strftime('%Y-%m-%d')
    # print(cdate)
    return render(request,'rqst leave.html',{'tdate':tdate}) 

def mleave(request):
    if 'radio1' in request.POST:
        radio=request.POST.get('radio1')
        if radio=='single_day':
            des=request.POST['textfield']
            sdate=request.POST['textfield2']
            print("ffffffffff",sdate)
            edate=request.POST['textfield3']
            ltype=request.POST['select']
            lo=leave(leave_des=des,leave_type=ltype,startdate=sdate,enddate=sdate,status='pending',doctor_id_id=request.session['doid'])
            # lo.doctor_id=doctor.objects.get( login_id=request.session['doid'])
            lo.save()
            return HttpResponse('''<script>alert("send ");window.location="/dhome"</script>''')    
        else:
            des=request.POST['textfield']
            sdate=request.POST['textfield2']
            print("ffffffffff",sdate)
            edate=request.POST['textfield3']
            ltype=request.POST['select']
            lo=leave(leave_des=des,leave_type='leave',startdate=sdate,enddate=edate,status='pending',doctor_id_id=request.session['doid'])
            # lo.doctor_id=doctor.objects.get( login_id=request.session['doid'])
            lo.save()
            return HttpResponse('''<script>alert("send ");window.location="/dhome"</script>''') 

    # if 'radio2' in request.POST:
    #         des=request.POST['textfield']
    #         sdate=request.POST['textfield2']
    #         print("ffffffffff",sdate)
    #         edate=request.POST['textfield3']
    #         ltype=request.POST['select']
    #         lo=leave(leave_des=des,leave_type='leave',startdate=sdate,enddate=edate,status='pending',doctor_id_id=request.session['doid'])
    #         # lo.doctor_id=doctor.objects.get( login_id=request.session['doid'])
    #         lo.save()
    #         return HttpResponse('''<script>alert("send ");window.location="/dhome"</script>''') 

def scheduleadd(request):

    from datetime import datetime
    hdate=datetime.today().strftime('%Y-%m-%d')
    print(hdate)

    q=schedule.objects.filter(doctor_id_id=request.session['doid'])

    if request.method=="POST":
        stime=request.POST['textfield']
        etime=request.POST['textfield2']
        date=request.POST['textfield3']
        fee=request.POST['fee']

        dss = date
        print(dss,"_____")

        # Split the string into a list using comma as separator
        new_dss = dss.split(",")

        # Join the list elements with a comma separator and print
        print(",".join(new_dss))

        for i in new_dss:
            print(i)
        

            q=schedule.objects.filter(date=date,doctor_id_id=request.session['doid'])
            print(q)
            if q:
                return HttpResponse("<script>alert('Choose Another Date....!!');window.location='/scheduleadd';</script>")
            else:
                os=schedule(start_time=stime,end_timne=etime,date=i,fee_amount=fee,doctor_id_id=request.session['doid'])
                os.save()
    
        #return HttpResponse('''<script>alert("Added");window.location="/scheduleadd"</script>''') 
    return render(request,'schedule1.html',{'hdate':hdate,'q':q})


def schedule_remove(request,id):
    q=schedule.objects.filter(schedule_id=id)
    q.delete()
    return HttpResponse('''<script>alert("reqmoved");window.location="/scheduleadd"</script>''')

# def shedule(request):
#     stime=request.POST['textfield']
#     etime=request.POST['textfield2']
#     date=request.POST['textfield3']
   
    
#     os=schedule(start_time=stime,end_timne=etime,date=date,fee_amount='100',doctor_id_id=request.session['doid'])
#     # os.doctor_id=doctor.objects.get(id=request.session['doid'])
#     os.save()

    
#     return HttpResponse('''<script>alert("Added");window.location="/dhome"</script>''') 


def vbooking(request):
    vb=booking.objects.all()
    print(vb)
    return render(request,'view booking.html',{'val':vb})
    
def accept1(request,book_id):
    ob=booking.objects.get(book_id=book_id)
    ob.status='accepted'
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/vbooking'</script>''')

def reject1(request,book_id):
    ob=booking.objects.get(book_id=book_id)
    ob.status='rejected'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/vbooking'</script>''')

def dviewleave(request):
    vl=leave.objects.filter(doctor_id_id=request.session['doid'])
    return render(request,'dviewleave.html',{'val':vl})  

def dviewpaymnts(request):
    vm=payment.objects.all()
    return render(request,'dviewpay.html',{'val':vm})



def view_prescriptions(request):
    vv=prescription.objects.filter(booking__patient_id_id=request.session['pid'])
    return render(request,'view_prescriptions.html',{'val':vv})



def editd(request):
    vv=doctor.objects.filter(pk=request.session['doid'])
    if vv:
        name=vv[0].first_name+" "+vv[0].last_name

    ob=doctor.objects.filter(doctor_id=request.session['doid'])
    return render(request,'editdoctor.html',{'val':ob,'name':name})

def edittd(request):
    place = request.POST['place']
    phone=request.POST['phone']
    email=request.POST['email']
    sp=request.POST['sp']
    place=request.POST['place']
    exp=request.POST['exp']
    qu=request.POST['qu']
    mob = doctor.objects.get(doctor_id=request.session['doid'])
    mob.place = place
    mob.phone = phone
    mob.email=email
    mob.specialization = sp
    mob.qualification=qu 
    mob.experience=exp 

    mob.save()
    return HttpResponse('''<script>alert("Updated");window.location='/dhome'</script>''')

# def calender(request):
#     return 





def doctor_add_prescription(request,id):
    vv=doctor.objects.filter(pk=request.session['doid'])
    print(vv)
    if vv:
        name=vv[0].first_name+" "+vv[0].last_name
        print(name,">>>>>>>>")


    if request.method=="POST":
        dis=request.POST['dis']
        ags=request.POST['ags']
        pres=request.POST['pres']
        print(dis,ags,pres)
        p=prescription(diseases=dis,alergic=ags,prescription=pres,booking_id=id,doctor_id=request.session['doid'])
        p.save()
        return HttpResponse("<script>alert('Added....!!!');window.location='/doctor_add_prescription/%s';</script>"% (id))
    
    bd=prescription.objects.filter(booking_id=id)
    return render(request,'doctor_add_prescription.html',{'name':name,'bd':bd})




def costprediction(request):

    pid=request.session['pid']
    pat=patient.objects.get(patient_id=pid)
    print(pat)
    if pat:
        age=pat.age 
        gender=pat.gender
        print(age,gender)
    s=""
    if request.method=="POST":
        age=int(request.POST['age'])
        gen=request.POST['gender']
        print(gen)
        if gen=="male":
            gender = int(0)
        elif gender=="female":
           gender = int(1)
       
        bmi=float(request.POST['bmi'])
        children=int(request.POST['children'])
        smk=int(request.POST['smk'])
        reg=int(request.POST['reg'])
        print(age,gender,bmi,children,smk,reg)
        print(type(age),"******")

        s=predict(age,gender,bmi,children,smk,reg)
        if s:
            print(s,"!!!!!!!!!!!!!!!!!!!!")
            print('The insurance cost is USD ', s)
    return render(request,'costprediction.html',{'s':s,'age':age,'gender':gender})




def predict(age,gender,bmi,children,smk,reg):

    # loading the data from csv file to a Pandas DataFrame
    insurance_dataset = pd.read_csv('static/dataset/insurance.csv')



    # first 5 rows of the dataframe
    insurance_dataset.head()


    # number of rows and columns
    insurance_dataset.shape


    # getting some informations about the dataset
    insurance_dataset.info()

    # checking for missing values
    insurance_dataset.isnull().sum()


    # statistical Measures of the dataset
    insurance_dataset.describe()



    # distribution of age value
    sns.set()
    plt.figure(figsize=(6,6))
    sns.distplot(insurance_dataset['age'])
    plt.title('Age Distribution')
    # plt.show()


    # Gender column
    plt.figure(figsize=(6,6))
    sns.countplot(x='sex', data=insurance_dataset)
    plt.title('Sex Distribution')
    # plt.show()


    insurance_dataset['sex'].value_counts()


    # bmi distribution
    plt.figure(figsize=(6,6))
    sns.distplot(insurance_dataset['bmi'])
    plt.title('BMI Distribution')
    # plt.show()


    # children column
    plt.figure(figsize=(6,6))
    sns.countplot(x='children', data=insurance_dataset)
    plt.title('Children')
    # plt.show()


    insurance_dataset['children'].value_counts()

    # smoker column
    plt.figure(figsize=(6,6))
    sns.countplot(x='smoker', data=insurance_dataset)
    plt.title('smoker')
    # plt.show()


    insurance_dataset['smoker'].value_counts()

    # region column
    plt.figure(figsize=(6,6))
    sns.countplot(x='region', data=insurance_dataset)
    plt.title('region')
    # plt.show()


    # distribution of charges value
    plt.figure(figsize=(6,6))
    sns.distplot(insurance_dataset['charges'])
    plt.title('Charges Distribution')
    # plt.show()



    # encoding sex column
    insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

    3 # encoding 'smoker' column
    insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

    # encoding 'region' column
    insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)



    X = insurance_dataset.drop(columns='charges', axis=1)
    Y = insurance_dataset['charges']


    print(X)

    print(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)



    print(X.shape, X_train.shape, X_test.shape)

    # loading the Linear Regression model
    regressor = LinearRegression()



    regressor.fit(X_train, Y_train)


    # prediction on training data
    training_data_prediction =regressor.predict(X_train)


    r2_train = metrics.r2_score(Y_train, training_data_prediction)
    print('R squared vale : ', r2_train)



    # prediction on test data
    test_data_prediction =regressor.predict(X_test)



    # R squared value
    r2_test = metrics.r2_score(Y_test, test_data_prediction)
    print('R squared vale : ', r2_test)


    input_data = (age,gender,bmi,children,smk,reg)

    # changing input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = regressor.predict(input_data_reshaped)
    print(prediction)

    print('The insurance cost is USD ', prediction[0])


    # import pandas as pd

    # df = pd.read_csv('static/dataset/insurance.csv')


    # # One-hot encode the 'sex' and 'smoker' columns
    # df = pd.get_dummies(df, columns=['sex', 'smoker'])

    # # Split the data into features and target
    # X = df.drop('charges', axis=1)
    # y = df['charges']

    # # Scale the numerical features
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X[['age', 'bmi', 'children']] = scaler.fit_transform(X[['age', 'bmi', 'children']])



    # from sklearn.linear_model import LinearRegression
    # from sklearn.model_selection import train_test_split

    # # Split the data into training and testing sets
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # # Train the model on the training set
    # model = LinearRegression()
    # model.fit(X_train, y_train)

    # # Evaluate the model on the testing set
    # score = model.score(X_test, y_test)
    # print('R^2 score:', score)


    # import joblib

    # joblib.dump(model, 'models/insurance_model.pkl')
    return prediction[0]




def analysis_chart(request):

    num_users=patient.objects.filter(pstatus="1").count()
    print(num_users,":::::::::::::::::::::::::::::::::")
   
    num_doctors=doctor.objects.filter(dstatus="1").count()
    print(num_doctors,":::::::::::::::::::::::::::::::::")


    num_lab=labs.objects.filter(login__status="1").count()
    print(num_lab,":::::::::::::::::::::::::::::::::")



    num_pharmacy=pharmacy.objects.filter(login__status="1").count()
    print(num_pharmacy,":::::::::::::::::::::::::::::::::")




    # book=booking.objects.values('date').annotate(count=Count('book_id'))
    # print("bookings",book)


    import datetime
    dd=datetime.datetime.now().strftime ("%Y-%m-%d")

    tb=booking.objects.all()
    from collections import defaultdict
    from dateutil import parser

    day_counts = defaultdict(int)
    print("####################")
    
    print(tb)
    print("#########################")
    if tb:
        for i in tb:
            # print(i.date)
          
            date_str = i.bk_date
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            day_of_week = date_obj.strftime('%A')

            # print(day_of_week)
            day_counts[day_of_week] += 1
    count_list = []
    for day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        count_list.append(day_counts[day_of_week])
        
    print(count_list)


    # present_pp=int(an)/int(total)*100
    # print(present_pp)
    # absent_pp=int(bb)/int(total)*100
    # print(absent_pp)

    # present_pp=int(pcount)
    # print(present_pp)
    # absent_pp=int(dcount)
    # print(absent_pp)
    
    # li=[]
    # x=[]
    # li.append(pcount)
    # li.append(dcount)
    # print(li)

    # x=li
    # print(x)
    # la=["Patient","Doctor"]
    # # plt.pie(x,labels=la)
    # plt.pie(x, labels=la, autopct='%1.1f%%', explode=[0.1,0], shadow=True, startangle=90)
    # plt.title('User Chart')
    # plt.axis('equal')
    # plt.show() 

    # patient_count, doctor_count = login.objects.filter(usertype__in=['user', 'doctor']).values('usertype').annotate(count=Count('usertype')).values_list('count', flat=True)

    # print("::::::::::::::",patient_count,doctor_count)

    # group = login.objects.filter(status='1').values('usertype').annotate(count=Count('usertype'))
    # print(group,"%%%%%%%")
    return render(request,'analysis_chart.html',{'num_users':num_users,'num_doctors':num_doctors,'num_pharmacy':num_pharmacy,'num_lab':num_lab,'book':book,'count_list':count_list})





def pharmacy_reg(request):
    from datetime import datetime
    cdate=datetime.today().strftime('%Y-%m-%d')
    print(cdate)

    if request.method=="POST":
        name=request.POST['name']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        floor=request.POST['floor']
        password = request.POST['pwd']
        encryptedpassword=make_password(request.POST['pwd'])
        print(encryptedpassword)
        q=login.objects.filter(username=email)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='/pharmacy_reg';</script>")
        else:
            lob=login()
            lob.username=email
            lob.password=encryptedpassword
            lob.usertype='pharmacy'
            lob.status='0'
            lob.save()


            pob=pharmacy()
            pob.login=lob
            pob.name=name 
            pob.place=place
            pob.phone=phone
            pob.email=email
            pob.floor_no=floor
            pob.save()
            return HttpResponse('''<script>alert("Successfully signup");window.location='/pharmacy_reg'</script>''')    

    return render(request,'pharmacy_reg.html',{'cdate':cdate})





def lab_reg(request):
    from datetime import datetime
    cdate=datetime.today().strftime('%Y-%m-%d')
    print(cdate)


    if request.method=="POST":
        name=request.POST['name']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        password = request.POST['pwd']
        encryptedpassword=make_password(request.POST['pwd'])
        print(encryptedpassword)
        q=login.objects.filter(username=email)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='/lab_reg';</script>")
        else:
            lob=login()
            lob.username=email
            lob.password=encryptedpassword
            lob.usertype='lab'
            lob.status='0'
            lob.save()


            pob=labs()
            pob.login=lob
            pob.name=name 
            pob.place=place
            pob.phone=phone
            pob.email=email
            pob.save()
            return HttpResponse('''<script>alert("Successfully signup");window.location='/lab_reg'</script>''')       

    return render(request,'lab_reg.html',{'cdate':cdate})




def pharmacy_add_medicines(request):
    ph_id=request.session['pharmacyid']
    from datetime import datetime
    cdate=datetime.today().strftime('%Y-%m-%d')
    print(cdate)

    if request.method=="POST":
        med=request.POST['med']
        det=request.POST['det']
        rate=request.POST['rate']
        qua=request.POST['qua']

        q=medicine.objects.filter(medicine=med)
        if q:
            return HttpResponse("<script>alert('Medicine Already Exist....!!!');window.location='/pharmacy_add_medicines';</script>")
        else:
            lob=medicine(medicine=med,quantity=qua,details=det,price=rate,pharmacy_id=ph_id)
            lob.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/pharmacy_add_medicines';</script>")
    
    q=medicine.objects.all()
    return render(request,'pharmacy_add_medicines.html',{'q':q})








def pharmacy_update_medicines(request,id):
    print("********************************")
    obs=medicine.objects.get(id=id)
    print(obs)
    if obs:
        med=obs.medicine 
        print(med,"!!")

    if request.method=="POST":
        med=request.POST['med']
        det=request.POST['det']
        rate=request.POST['rate']
        qua=request.POST['qua']
        obs.medicine=med 
        obs.details=det 
        obs.price=rate 
        obs.quantity=qua 
        obs.save()
        return HttpResponse("<script>alert('Updated....!!!');window.location='/pharmacy_add_medicines';</script>")
    return render(request,'pharmacy_add_medicines.html',{'obs':obs})




def pharmacy_delete_medicines(request,id):
    q=medicine.objects.filter(id=id)
    q.delete()
    return HttpResponse('''<script>alert("reqmoved");window.location="/pharmacy_add_medicines"</script>''')



def patient_request_for_medicine(request,id):
    from datetime import datetime
    cdate=datetime.today().strftime('%Y-%m-%d')
    print(cdate)


    pid=request.session['pid']


    q=pharmacy.objects.all()

    if request.method=="POST":
        pha=request.POST['pha']
        q=upload_pharmacy_prescription.objects.filter(patient_id=pid,prescription_id=id,pharmacy_id=pha)
        if q:
            return HttpResponse("<script>alert('Already Exist....!!!');window.location='/view_prescriptions';</script>")
        else:
            q=upload_pharmacy_prescription(total_amt='0',date=cdate,status='pending',patient_id=pid,pharmacy_id=pha,prescription_id=id)
            q.save()
            return HttpResponse("<script>alert('Requested....!!!');window.location='/view_prescriptions';</script>")
    return render(request,"patient_request_for_medicine.html",{'q':q})







def upload_prescription(request,id):
    print("+++++++++++++++++++++++++++++++",id)
    if request.method=="POST":
        pres = request.FILES['pres']
        fp = FileSystemStorage()
        path = fp.save(pres.name, pres)
        print(path)
        val=ocrgenerate(path)
        print(val)
        # text = textract.process(path)
        # print(text)
        # return HttpResponse(text)
        
        q=user_image_prescription(image=path,status='uploaded',booking_id=id,patient_id=request.session['pid'],details=val)
        q.save()

        return HttpResponse('''<script>alert("Uploaded");window.location='/upload_prescription/%s'</script>'''%(id))
    q=user_image_prescription.objects.filter(patient_id=request.session['pid'])
    return render(request,'user_upload_prescription.html',{'q':q})


def doctor_view_user_uploaded_prescription(request,id):
    q=user_image_prescription.objects.filter(booking_id=id)
    print(q)
    return render(request,'doctor_view_user_uploaded_prescription.html',{'q':q})


def pharmacy_view_prescriptions(request):
    phid=request.session['pharmacyid']
    print(phid)

    q=upload_pharmacy_prescription.objects.filter(pharmacy_id=phid)
    print(q)
    # if q:
    #     tt_amt=q[0].total_amt 
    #     print(tt_amt)
    #     pname=q[0].upload_pharmacy_prescription.patient.first_name
    #     print(pname)
    return render(request,'pharmacy_view_prescriptions.html',{'q':q})




def pharmacy_add_requested_medicines(request,id):
    print("******************")
    phid=request.session['pharmacyid']
    print(phid)

    q=medicine.objects.all()

    q1=medicine_details.objects.filter(upload_pharmacy_prescription_id=id)
    print(q1)



    if request.method=="POST":
        med=request.POST['med']
        qua=request.POST['qua']
        qua=int(qua)
        print(med,qua)
        q2=medicine.objects.filter(id=med)

        avlqua=int(q2[0].quantity)
        rate=int(q2[0].price)
        if avlqua<qua:
            return HttpResponse('''<script>alert("REQUIRED QUANTITY IS NOT AVAILABLE IN OUR STOCK");window.location='/pharmacy_add_requested_medicines/%s'</script>'''%(id))
        else:
            amt=qua*rate
            print("555555555555555")
            print(amt)
            q3=medicine_details.objects.filter(upload_pharmacy_prescription_id=id,medicine_id=med)
            if q3:
                preamt=q3[0].total
                q4=upload_pharmacy_prescription.objects.filter(id=id)
                totalamount=q4[0].totalamount
                newamt=int(totalamount)+int(amt)-(int(preamt))


                q3.total_amt=newamt 
                q3.save()

                up=medicine_details.objects.filter(upload_pharmacy_prescription_id=id,medicine_id=med)
                up.total=amt 
                up.quantity=qua 
                up.save()
                return HttpResponse('''<script>alert("THIS MEDICINE ALREDY ADDED !UPDATED SUCCEDFULLY");window.location='/pharmacy_add_requested_medicines/%s'</script>'''%(id))
				
            else:
                mm=medicine_details(upload_pharmacy_prescription_id=id,medicine_id=med,quantity=qua,rate=rate,total=amt)
                mm.save()
                q4=upload_pharmacy_prescription.objects.get(id=id)
                q4.total_amt=int(q4.total_amt)+amt
                q4.save()
                return HttpResponse('''<script>alert("ADDED SUCESSFULLY");window.location='/pharmacy_add_requested_medicines/%s'</script>'''%(id))


   
    q5=upload_pharmacy_prescription.objects.get(id=id)
    if q5:
        totalamount=q5.total_amt

    return render(request,'pharmacy_add_requested_medicines.html',{'q':q,'q1':q1,'totalamount':totalamount})




def view_pharmacy_medicines(request):
    pid=request.session['pid']
    print(pid)

    q=medicine_details.objects.filter(upload_pharmacy_prescription__patient_id=pid,upload_pharmacy_prescription__status='pending')
    print(q)
    if q:
        totalamount=q[0].upload_pharmacy_prescription.total_amt
        print(totalamount)
        status=q[0].upload_pharmacy_prescription.status 
        print(status)
        uid=q[0].upload_pharmacy_prescription.id 
        print(uid)

    return render(request,'view_pharmacy_medicines.html',{'q':q,'totalamount':totalamount,'status':status,'uid':uid})


def user_accept_medicine(request,id,amt): 
    # ob=leave.objects.get(leave_id=doctor_id)
    # ob.status='Approved'
    # ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/user_make_medicine_payment/%s/%s'</script>'''%(id,amt))






def user_make_medicine_payment(request,id,amt):

    return render(request,'user_make_medicine_payment.html',{'total':amt,'ids':id})




def payments(request,id,fee):
    request.session['bid']=id
    total=request.session['fee']=fee
    return render(request,'payments.html',{'total':total,'ids':id})



def pay(request):
    
    return HttpResponse('''<script>alert("payed");window.location="/patienthome"</script>''')         




def rpay(request):
    print("Haiiiiiiiii")
    
    

    # Get the order ID
    order_id = request.GET['order_id']
    order_id = request.GET['order_id']
    print(order_id)
    # s=booking.objects.get(id=id)
    # if s:
    #     s.status='Shipped'
    #     s.order_id=order_id
    #     s.save() 
    # od=bookingchilds.objects.filter(booking_id=id)
    # print(od)
    # if od:
    #     for i in od:
    #         pid=i.product_id
    #         qtys=i.quantity
    #         print(pid,"....................proid")
    #         print(qtys,"..................qty")

    #         pp=product.objects.get(id=pid)
    #         # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
    #         if pp:
    #             pro_qty=pp.stock
    #             print(pro_qty,"############pro_qty")
    #             pp.stock=int(pro_qty)-int(qtys)
    #             pp.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/patienthome';</script>")
   
    return render(request, 'orders.html',context)




def user_medicine_payment_complete(request,id):
    n=upload_pharmacy_prescription.objects.get(id=id)
    print(n)
    if n:
        n.status='Paid'
        n.save()
    s=medicine_details.objects.filter(upload_pharmacy_prescription_id=id)
    if s:
        for i in s:
            med_id=i.medicine_id 
            qty=i.quantity
            print(med_id)
            q=medicine.objects.get(id=med_id)
            print(q)
            if q:
                q.quantity=int(q.quantity)-int(qty)
                q.save()
        
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/patienthome';</script>")




def user_payment_complete(request,id):

    s=booking.objects.get(book_id=id)
    if s:
        s.status='Paid'                                                                     
        s.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/patienthome';</script>")







def user_reject_medicine(request,id):
    ob=upload_pharmacy_prescription.objects.get(id=id)
    ob.status='Reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/view_pharmacy_medicines'</script>''')



def admin_view_pharmacy(request):
    if request.method=='POST':
        pla=request.POST['pla']
        vd=pharmacy.objects.filter(name=pla)
    else:
        vd = pharmacy.objects.filter(login__status=1)
        print(vd)
    return render(request,'admin_view_pharmacy.html',{'vd':vd})


def admin_view_lab(request):
    if request.method=='POST':
        pla=request.POST['pla']
        
        vd=labs.objects.filter(name=pla)
    else:
        vd = labs.objects.filter(login__status=1)
        print(vd)
    return render(request,'admin_view_lab.html',{'vd':vd})



def printlab(request):
    today=date.today() 
    print(today,"_____________")
    vd = labs.objects.filter(login__status=1)
    return render(request,'printlab.html',{'vd':vd,'today':today})



def printpharmacy(request):
    today=date.today() 
    print(today,"_____________")
    vd = pharmacy.objects.filter(login__status=1)
    return render(request,'printpharmacy.html',{'vd':vd,'today':today})







def doctor_add_medicines(request,id):
    if 'submit' in request.POST:
        out=request.POST['out']

        ss=out.split(",")
        print(type(ss))
        for i in range(len(ss)):
            # print(i, end=" ")
            print(ss[i])

            med=request.POST['med'+ss[i]]
            free=request.POST['free'+ss[i]]
            dos=request.POST['dos'+ss[i]]
            dur=request.POST['dur'+ss[i]]
            print(med,free,dos,dur,ss[i])
            m=medicines(medicine=med,freequency=free,dosage=dos,med_duration=dur,prescription_id=id)
            m.save()

        return HttpResponse("<script>alert('Added....!!');window.location='/doctor_add_prescription/%s'</script>"%(id))
    return render(request,'doctor_add_medicines.html')




def doctor_add_lab_test(request,id):
    if 'test' in request.POST:
        ldet=request.POST['ldet']
        q=test(details=ldet,prescription_id=id)
        q.save()
        return HttpResponse("<script>alert('Added....!!');window.location='/doctor_add_prescription/%s'</script>"%(id))
    return render(request,'doctor_add_lab_test.html')


def view_lab_details(request):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    pid=request.session['pid']
    print(pid)

    q=test.objects.filter(prescription__booking__patient_id_id=pid)
    print(q)
    if q:
        details=q[0].details 
        doc=q[0].prescription.prescription
        print(doc,"******************")
    return render(request,'view_lab_details.html',{'q':q})


def user_request_for_lab(request,id):
    from datetime import date,datetime 
    today=date.today()
    print(today)

    pid=request.session['pid']
    print(pid)

    q=labs.objects.all()
    print(q)

    if 'submit' in request.POST:
        lab=request.POST['lab']
        q=upload_lab_prescription.objects.filter(patient_id=pid,test_id=id,labs_id=lab)
        if q:
            return HttpResponse("<script>alert('Already Exist....!!!');window.location='/view_lab_details';</script>")
        else:
            q=upload_lab_prescription(date=today,status='pending',patient_id=pid,labs_id=lab,test_id=id)
            q.save()
            return HttpResponse("<script>alert('Requested....!!!');window.location='/view_lab_details';</script>")

    return render(request,'user_request_for_lab.html',{'q':q})



def lab_upload_result(request):
    lid=request.session['lid']
    print(lid)

    q1=labs.objects.filter(login_id=lid)
    print(q1)
    if q1:
        labid=q1[0].id
        print(labid,"***************")

    q=upload_lab_prescription.objects.filter(labs_id=labid)
    print(q)
    return render(request,'lab_upload_result.html',{'q':q})




def lab_upload_result(request):
    lid=request.session['lid']
    print(lid)

    q1=labs.objects.filter(login_id=lid)
    print(q1)
    if q1:
        labid=q1[0].id
        print(labid,"***************")

    q=upload_lab_prescription.objects.filter(labs_id=labid)
    print(q)
    return render(request,'lab_upload_result.html',{'q':q})



 
def lab_add_lab_test_results(request,id):
    lid=request.session['lid']
    print(lid)

    q1=labs.objects.filter(login_id=lid)
    print(q1)
    if q1:
        labid=q1[0].id
        print(labid,"***************")

    if 'submit' in request.POST:
        test=request.POST['test']
        print(test,">>>>>>>>>>>>>>>>>>")
        return HttpResponse("<script>window.location='/lab_add_test_data/%s/%s';</script>"%(test,id))
    return render(request,'lab_add_lab_test_results.html')



def lab_add_test_data(request,test,id):
    today=date.today()
    print(today,"_________")
    lid=request.session['lid']
    print(lid)

    q1=labs.objects.filter(login_id=lid)
    print(q1)
    if q1:
        labid=q1[0].id
        print(labid,"***************")

    if 'submit' in request.POST:
        det=request.POST['det']
        if test=="Scanning" or test=="X-Ray":
            pres = request.FILES['img']
            fp = FileSystemStorage()
            path = fp.save(pres.name, pres)
            print(path)
        else:
            path=""

        q=lab_tests(test_item=test,details=det,date=today,image=path,upload_lab_prescription_id=id)
        q.save()
        return HttpResponse("<script>window.location='/lab_add_test_data/%s/%s';</script>"%(test,id))
    return render(request,'lab_add_test_data.html',{'test':test})




def lab_view_result(request):
    lid=request.session['lid']
    print(lid)

    q1=labs.objects.filter(login_id=lid)
    print(q1)
    if q1:
        labid=q1[0].id
        print(labid,"***************")

    q=lab_tests.objects.filter(upload_lab_prescription__labs_id=labid)
    print(q)
    return render(request,'lab_view_result.html',{'q':q})



def online_consultation(request):
    from datetime import date,datetime 
    today=date.today()
    print(today)

    pid=request.session['pid']
    print(pid)
    q=departments.objects.all()


    if 'search' in request.POST:
        select=request.POST['select']
        print(select,"?????????????????????")
        id=int(select)
        print(id,"__________________")
        return HttpResponse('''<script>window.location='/user_view_doctor/%s'</script>'''%(id))
    return render(request,'online_consultation.html',{'val':q})



def user_view_doctor(request,id):
    print(id,"*******************")

    

    vv=doctor.objects.filter(departments_id=id)
    print(vv)
    if 'search' in request.POST:
        doctorn=request.POST['select']
        print("#######")
        print(doctorn)
        print("###########")
        vv=doctor.objects.filter(doctor_id=doctorn)
        print(vv)
        
    return render(request,'user_view_doctor.html',{'doc1':vv,'doc2':vv})
    


def book_online(request,id):
    from datetime import date,datetime 
    today=date.today()
    print(today)

    pid=request.session['pid']
    print(pid)
    
    qq=online_consultations(date='pending',time='pending',status='Online',bk_date=today,patient_id=pid,doctor_id=id)
    qq.save()
    return HttpResponse('''<script>window.location='/patienthome'</script>''')




def view_consultaion_online(request):
    lid=request.session['lid']
    print(lid)

    q1=doctor.objects.filter(login_id_id=lid)
    print(q1)
    if q1:
        labid=q1[0].doctor_id

    q=online_consultations.objects.all()
    return render(request,'view_consultaion_online.html',{'val':q})



def set_consulting_time(request,id):
    q=online_consultations.objects.get(id=id)
    if q:
        cusid=q.patient_id 
        print(cusid)
    qc=patient.objects.get(patient_id=cusid)
    if qc:
        email=qc.email 
        print(email)
        

    if request.method=="POST":
        date=request.POST['date']
        time=request.POST['time']
        q.date=date 
        q.time=time 
        q.save()
        subject = 'Consulting Details'
        message = f"sir,\n Your <a href=https://meet.google.com/omv-imks-bww>Click</a>\nTime :"+time+"\nDate :"+date
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse('''<script>window.location='/view_consultaion_online'</script>''')
    return render(request,'set_consulting_time.html',{'val':q})
