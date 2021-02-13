
from django.shortcuts import render

# Create your views here.
from .models import MyData
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from Face_recognizer.camera import webCamera
import csv
import pandas as pd
import numpy as np
from datetime import date

# Create your views here.

def home(request):
    return render(request,'home.html')


def recognizer(request):
	return render(request, 'recognizer.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def web_feed(request):
	return StreamingHttpResponse(gen(webCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')
def Attendence(request):
    data = MyData.objects.all()
    #print("working")
    return render(request,'./index.html',{"data": data})

def ExportCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer= csv.writer(response)
    writer.writerow(['Student','Date_Time'])

    data = MyData.objects.all().values_list('Student','Date_Time')
    for d in data:
        writer.writerow(d)
    return response

def daywise(request):
    data = MyData.objects.all().values_list('Student','Date_Time')
    df=pd.DataFrame(data,columns=["Student","Date_Time"])
    td=date.today()
    #td1=td.to_datetime("%yy:%mm:%dd")
    #print(td1)
    #a=(df['Date_Time']>=td1)
    #df1=df.loc[a]
    df2=df.groupby("Student").agg({"Date_Time":np.max})
    df3=df2.groupby("Student").agg({"Date_Time":np.min})
    df4=pd.concat([df2,df3])
    html=df4.to_html()
    
    #write html to file
    tfile=open("C:\\Users\\Vipin Kumar\\Desktop\\Attendance_Management\\Face_recognizer\\templates\\daywise.html","w")
    tfile.write(html)
    tfile.close()
    
    return render(request,'./daywise.html',{'data':html})
    #print(df4)
    #df5=df4.to_csv('ftrdata.csv',index=False)
    #print("data frame \n",df4)
    
    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="fltrdata.csv"'
    #writer= csv.writer(response)
    #writer.writerow(['Student','Date_Time'])
    
    
    #data = df5.values.tolist()
    #r=len(data)
    #print("list",df5)
    #for d in df5:
        #writer.writerow(d)
    #return response
    

    
    
