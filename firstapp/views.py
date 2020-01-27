from django.shortcuts import render
from django.http import JsonResponse
import pickle
 
def index(request):
    return render(request, "index.html")

def Data():
	with open("C:\\Users\\AAAAAA\\some.txt", 'rb') as filehandle:
		pagesets = pickle.load(filehandle)
	filehandle.close()
	return(pagesets)

def AjaxData(request):
	return JsonResponse({"data": Data()})
