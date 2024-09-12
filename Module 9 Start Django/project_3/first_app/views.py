from django.shortcuts import render

import datetime

# Create your views here.

# def home(request):
#     d={'author':'Rahim','age':5, 'list':[1,2,3]}
#     return render(request,'home.html',d) # contex=d or d are same

 
# def course(request):
#     d={'author':'Rahim','age':5, 'list':[1,2,3], 'courses_list':[
#         {
#             'id':1,
#             'name':'Python',
#             'fee':5000
#         },
#         {
#             'id':2,
#             'name':'Django',
#             'fee':10000
#         },
#         {
#             'id':3,
#             'name':'C',
#             'fee':60000
#         },
#         {
#             'id':4,
#             'name':'C++',
#             'fee':40000
#         },

#     ]}
#     return render(request,'home.html',d)
 
def filtering(request):
    d={'author':'Rahim','age':5, 'list':['Python ','is','Best'],'birthday':datetime.datetime.now(),'val':"",}
    return render(request,'home.html',d)



