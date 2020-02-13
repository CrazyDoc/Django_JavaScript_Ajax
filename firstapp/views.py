from django.http import JsonResponse
from django.shortcuts import render
import pickle
 
def index(request):
    return render(request, "index.html")

def Data():
	with open("/tmp/some.txt", 'rb') as filehandle:
		pagesets = pickle.load(filehandle)
	filehandle.close()
	return(pagesets)

def AjaxData(request):
	return JsonResponse(Data())
