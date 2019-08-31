from django.shortcuts import render
import datetime
# Create your views here.
def datetimeinfo(request):
    name='Ashish'
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    if(h<12):
        msg='Good Morning!!!'
    elif(h<16):
        msg="Good Afternoon!!!"
    elif(h<22):
        msg="Good Evening!!!"
    else:
        msg="Good Night!!!"

    my_dict={'name':name,'date':date,'msg':msg}

    return render(request,'dateApp/date.html',context=my_dict)
