from django.db import models
import os 
from PIL import Image
import pytesseract
from reportlab.pdfgen import canvas
from django.conf import settings

# Create your models here.


class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    gender=models.CharField(max_length=225)
    blood_group=models.CharField(max_length=50)
    dob=models.DateField()
    pstatus=models.CharField(max_length=50)
    age=models.CharField(max_length=50)


class departments(models.Model):
    department=models.CharField(max_length=225)


class doctor(models.Model):
    doctor_id=models.AutoField(primary_key=True)
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    image = models.FileField()
    dstatus=models.CharField(max_length=50)
    licence_no=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    departments=models.ForeignKey(departments,on_delete=models.CASCADE)



class schedule(models.Model):
    schedule_id=models.AutoField(primary_key=True)
    doctor_id=models.ForeignKey(doctor, on_delete=models.CASCADE)
    start_time=models.CharField(max_length=50)
    end_timne=models.CharField(max_length=50)
    date=models.DateField()
    fee_amount=models.CharField(max_length=20)

class booking(models.Model):
    book_id=models.AutoField(primary_key=True)
    schedule_id=models.ForeignKey(schedule,on_delete=models.CASCADE)
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    status=models.CharField(max_length=50)
    bk_date=models.CharField(max_length=50)

class payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    book_id=models.ForeignKey(booking, on_delete=models.CASCADE)
    amount=models.CharField(max_length=20)
    date=models.CharField(max_length=50)
    type=models.CharField(max_length=100)



class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    patient_id=models.ForeignKey(patient,on_delete=models.CASCADE)
    feedback_des=models.CharField(max_length=225)
    date=models.DateField()

class leave(models.Model):
    leave_id=models.AutoField(primary_key=True)
    doctor_id=models.ForeignKey(doctor,on_delete=models.CASCADE)
    leave_des=models.CharField(max_length=225)
    leave_type=models.CharField(max_length=50)
    status=models.CharField(max_length=100)
    startdate=models.DateField()
    enddate=models.DateField()
    


class prescription(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)

    diseases=models.CharField(max_length=100)
    alergic=models.CharField(max_length=1000)
    prescription=models.CharField(max_length=1000)



class pharmacy(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=1000)
    phone=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    floor_no=models.CharField(max_length=1000)


# class lab(models.Model):
#     login=models.ForeignKey(login,on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     place=models.CharField(max_length=1000)
#     phone=models.CharField(max_length=1000)
#     email=models.CharField(max_length=1000)



class labs(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=1000)
    phone=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)


class medicine(models.Model):
    pharmacy=models.ForeignKey(pharmacy,on_delete=models.CASCADE)
    medicine=models.CharField(max_length=1000)
    quantity=models.CharField(max_length=1000)
    price=models.CharField(max_length=100)
    details=models.CharField(max_length=100)



class upload_pharmacy_prescription(models.Model):
    pharmacy=models.ForeignKey(pharmacy,on_delete=models.CASCADE)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    prescription=models.ForeignKey(prescription,on_delete=models.CASCADE)
    total_amt=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class medicine_details(models.Model):
    upload_pharmacy_prescription=models.ForeignKey(upload_pharmacy_prescription,on_delete=models.CASCADE)
    medicine=models.ForeignKey(medicine,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    total=models.CharField(max_length=100)




class user_image_prescription(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    booking = models.ForeignKey(booking, on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)






# class doctor_prescription(models.Model):
#     patient=models.ForeignKey(patient,on_delete=models.CASCADE)
#     booking = models.ForeignKey(booking, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     prescription_image = models.ImageField(upload_to='uploads/')

#     def __str__(self):
#         return self.name

#     def generate_pdf(self):
#         # Use Tesseract OCR to extract text from the image
#         text = pytesseract.image_to_string(Image.open(self.prescription_image))
#         # Generate a PDF or Word document using the extracted text
#         # (You'll need to use a library like reportlab or python-docx for this)
#         # ...
#         # Save the generated document to disk
#         # (Assuming you've generated a PDF document using reportlab)
#         file_path = os.path.join(settings.MEDIA_ROOT, 'prescriptions', f'{self.id}.pdf')
#         with open(file_path, 'wb') as file:
#             # Create a PDF file using reportlab
#             # ...
#             file.write(buffer.getvalue())
#         return file_path


class medicines(models.Model):
    prescription=models.ForeignKey(prescription,on_delete=models.CASCADE)
    medicine=models.CharField(max_length=50)
    freequency=models.CharField(max_length=1000)
    dosage=models.CharField(max_length=50)
    med_duration=models.CharField(max_length=50)


class test(models.Model):
    prescription=models.ForeignKey(prescription,on_delete=models.CASCADE)
    details=models.CharField(max_length=1000)



class upload_lab_prescription(models.Model):
    labs=models.ForeignKey(labs,on_delete=models.CASCADE)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    test=models.ForeignKey(test,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class lab_tests(models.Model):
    upload_lab_prescription=models.ForeignKey(upload_lab_prescription,on_delete=models.CASCADE)
    test_item=models.CharField(max_length=50)
    details=models.CharField(max_length=1000)
    date=models.CharField(max_length=50)
    image=models.CharField(max_length=1000)



class online_consultations(models.Model):
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=1000)
    bk_date=models.CharField(max_length=50)
    status=models.CharField(max_length=1000)