import json
import numpy as np
from numpy.linalg import eig
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

# Create your views here.



def index(request):
    return render(request,'index.html')

@csrf_exempt
def get_val(request):
    if request.method == 'POST':
        arr = np.array([])
        for data in request.POST.getlist('val[]'):
            arr = np.append(arr,[int(data)])
        
        arr = arr.reshape(int(request.POST.get('ele')),int(request.POST.get('ele')))
        w,v=eig(arr)
        # print('E-value:', w)
        # print('E-vector', v)
        print("E-Value:",str(v),"\nE-vector:",str(w))
        data = {'val':w.tolist(),'vec':v.tolist()}
    return HttpResponse("<h2>E-Value:</h2>"+str(v)+"\n\n<h2>E-vector:</h2>"+str(w))