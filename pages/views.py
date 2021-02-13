from django.shortcuts import render
import pandas as pd
def get_data(mat,df):
    i = 0
    while i < len(df):
        if str(mat) in str(df['mat_no']): 
            if str(df['mat_no'][i]) == str(mat):
                name = df['names'][i]
                bat = df['Batch'][i]
        else:
            name = 'none'
            bat = 'none'
        i = i+1    
    return name , bat
df = pd.read_csv('/home/jay/Unfinished Projects/lasu/pages/Needed.csv')
# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html',context)

def action(request):
    matric_no = request.POST.__getitem__("matric_no")
    name , bat = get_data(matric_no,df)
    if name == 'none':
        context = {
            'message':'Not Enrolled For This Exam'
        }
        return render(request,'index.html',context )
    else: 
        context = {
            'mat':matric_no,
            'name': name,
            'bat':bat
    }
    return render(request,'index.html',context )
