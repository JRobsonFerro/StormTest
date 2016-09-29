from django.http import HttpResponse

def index(request):
	return HttpResponse("Aqui vai ficar o Filme.")
