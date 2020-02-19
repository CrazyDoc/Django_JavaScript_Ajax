from django.http import JsonResponse
from django.shortcuts import render
import pickle
import sqlib

def index(request):
	return render(request, "index.html")

def Data():
	with open("/tmp/some.txt", 'rb') as filehandle:
		pagesets = pickle.load(filehandle)
	filehandle.close()
	return(pagesets)

def DateData(request, dateinterval):
	interval = dateinterval.split('-')
	datedata = {}
	for i in range(int(interval[0]), int(interval[-1]) + 1):
		table_name = 'ps' + str(i)
		con = sqlib.connection('/sqlite3/sqlite3')
		for i in sqlib.listing_rows(con, table_name):
			PS = i[1]
			if datedata.get(PS) and datedata.get(PS).get('data'):
				datedata[PS] = dict(label = PS, data = (datedata.get(PS).get('data') + [[i[2], i[3]]]))
			else:
				datedata[PS] = datedata[PS] = dict(label = PS, data = [[i[2], i[3]]])
	return JsonResponse(datedata)

def AjaxData(request):
	return JsonResponse(Data())
