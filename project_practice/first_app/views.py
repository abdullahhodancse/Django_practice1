from django.shortcuts import render
import  datetime 

# Create your views here.
def home(request):
    d={'aouthor':'Hodan','Age':1,'list':['i ','love','bd'],'lst':['I','Love','bd'],'Birthday':datetime.datetime.now(),'sum':[1,2,3],'furits':['Apple', 'Mango', 'Orange'],
         'course':[
        {
            'Id':1,
            'Name':'dPython',
            'Fee':100,
        },
        {
            'Id':2,
            'Name':'cython2',
            'Fee':200,
        },
        {
            'Id':3,
            'Name':'athon3',
            'Fee':300,
        },
    ]}
    return render(request,'home.html',d)
