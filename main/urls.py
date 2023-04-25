"""HospitalManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
# from captcha import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_page',views.login_page,name='login_page'),
    path('logins',views.logins,name='logins'),
    path('admhome',views.admhome,name='admhome'),
    path('mngdoctor',views.mngdoctor,name='mngdoctor'),
    # path('adddoctor',views.adddoctor,name='adddoctor'),
    path('viewdoctor',views.viewdoctor,name='viewdoctor'),
    path('viewpatient',views.viewpatient,name='viewpatient'),
    path('viewfeed',views.viewfeed,name='viewfeed'),
    path('viewpaymnts',views.viewpaymnts,name='viewpaymnts'),
    # path('add',views.add,name='add'),
    path('admin_update_doctor/<int:id>',views.admin_update_doctor,name='admin_update_doctor'),
    # path('editt',views.editt,name='editt'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('patienthome',views.patienthome,name='patienthome'),
    path('sendfeedback',views.sendfeedback,name='sendfeedback'),
    path('feed',views.feed,name='feed'),
    path('register',views.register,name='register'),
    path('regi',views.regi,name='regi'),
    # path('pviewdoctor',views.pviewdoctor,name='pviewdoctor'),
    path('search',views.search,name='search'),
    path('dhome',views.dhome,name='dhome'),
    path('rleave',views.rleave,name='rleave'),
    path('mleave',views.mleave,name='mleave'),
    path('viewleave',views.viewleave,name='viewleave'),
    path('accept/<int:doctor_id>',views.accept,name='accept'),
    path('reject/<int:doctor_id>',views.reject,name='reject'),
    path('scheduleadd',views.scheduleadd,name='scheduleadd'),
    # path('shedule',views.shedule,name='shedule'),
    path('vbooking',views.vbooking,name='vbooking'),
    path('accept1/<int:book_id>',views.accept1,name='accept1'),
    path('reject1/<int:book_id>',views.reject1,name='reject1'),
    path('viewtime/<id>/<dattt>',views.viewtime,name='viewtime'),
    path('book',views.book,name='book'),
    path('pviewbooking',views.pviewbooking,name='pviewbooking'),
   path('search1/<id>',views.search1),
    path('payments/<int:id>/<fee>',views.payments,name='payments'),
    path('pay',views.pay,name='pay'),
    path('dviewleave',views.dviewleave,name='dviewleave'),
    path('dviewpaymnts',views.dviewpaymnts,name='dviewpaymnts'),
    path('forgot',views.forgot,name='forgot'), 
    path('got', views.got, name='got'), 
    path('newpas',views.newpas,name='newpas'),  
    path('otp',views.otp,name='otp'),
    path('editp',views.editp,name='editp'),
    path('edittp',views.edittp,name='edittp'),
    path('editd',views.editd,name='editd'),
    path('edittd',views.edittd,name='edittd'),
    path('view_doctors',views.view_doctors,name='view_doctors'),
    path('printpatient',views.printpatient,name='printpatient'),
    path('admin_user_inactive/<id>',views.admin_user_inactive),
    path('admin_user_active/<id>',views.admin_user_active),
    path('admin_doctor_inactive/<id>',views.admin_doctor_inactive),
    path('admin_doctor_active/<id>',views.admin_doctor_active),
    path('printdoctor',views.printdoctor),
    path('schedule_remove/<id>',views.schedule_remove),
    path('my_form', views.my_form, name='my_form'),
    path('my_post', views.my_post, name='my_post'),
    # path('calender',views.calender),

    path('admin_manage_dept',views.admin_manage_dept,name='admin_manage_dept'),
   
    path('admin_update_department/<id>',views.admin_update_department,name='admin_update_department'),
    path('admin_remove_department/<id>',views.admin_remove_department,name='admin_remove_department'),
    path('user_view_dept',views.user_view_dept),
    path('costprediction',views.costprediction),
    path('user_payment_complete/<id>',views.user_payment_complete),
    path('rpay',views.rpay,name='rpay'),
    path('analysis_chart',views.analysis_chart,name='analysis_chart'),
    path('doctor_add_prescription/<id>',views.doctor_add_prescription),
    path('view_prescriptions',views.view_prescriptions),
    path('upload_prescription/<id>',views.upload_prescription),

    path('pharmacy_reg',views.pharmacy_reg),
    path('lab_reg',views.lab_reg),

    path('labhome',views.labhome),
    path('pharmacyhome',views.pharmacyhome),


    path('admin_lab_inactive/<id>',views.admin_lab_inactive),
    path('admin_lab_active/<id>',views.admin_lab_active),
    path('admin_pharmacy_inactive/<id>',views.admin_pharmacy_inactive),
    path('admin_pharmacy_active/<id>',views.admin_pharmacy_active),
    path('editpharmacy',views.editpharmacy),
    path('pharmacy_add_medicines',views.pharmacy_add_medicines),

    path('ocrgenerate',views.ocrgenerate),
    path('upload_prescription',views.upload_prescription),
    path('doctor_view_user_uploaded_prescription/<id>',views.doctor_view_user_uploaded_prescription),
    

    path('pharmacy_update_medicines/<id>',views.pharmacy_update_medicines),
    path('pharmacy_delete_medicines/<id>',views.pharmacy_delete_medicines),
    path('patient_request_for_medicine/<id>',views.patient_request_for_medicine),
    
    path('pharmacy_view_prescriptions',views.pharmacy_view_prescriptions),
    path('pharmacy_add_requested_medicines/<id>',views.pharmacy_add_requested_medicines),
    path('view_pharmacy_medicines',views.view_pharmacy_medicines),

    path('user_reject_medicine/<id>',views.user_reject_medicine),
    path('user_accept_medicine/<id>/<amt>',views.user_accept_medicine),
    path('user_make_medicine_payment/<id>/<amt>',views.user_make_medicine_payment),
    path('user_medicine_payment_complete/<id>',views.user_medicine_payment_complete),
    
    path('admin_view_pharmacy',views.admin_view_pharmacy),
    path('admin_view_lab',views.admin_view_lab),
    path('printlab',views.printlab),
    path('printpharmacy',views.printpharmacy),
    path('editlab',views.editlab),
    path('doctor_add_medicines/<id>',views.doctor_add_medicines),
    path('doctor_add_lab_test/<id>',views.doctor_add_lab_test),

    path('view_lab_details',views.view_lab_details),
    path('user_request_for_lab/<id>',views.user_request_for_lab),    
    path('lab_upload_result',views.lab_upload_result),
    path('lab_add_lab_test_results/<id>',views.lab_add_lab_test_results),
    path('lab_add_test_data/<test>/<id>',views.lab_add_test_data),
    path('lab_view_result',views.lab_view_result),
    path('admin_view_patients/<id>',views.admin_view_patients),
    path('admin_view_doctor/<id>',views.admin_view_doctor),
    path('online_consultation',views.online_consultation),
    path('user_view_doctor/<id>',views.user_view_doctor),

    path('book_online/<id>',views.book_online),
    path('view_consultaion_online',views.view_consultaion_online),
    path('set_consulting_time/<id>',views.set_consulting_time),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
