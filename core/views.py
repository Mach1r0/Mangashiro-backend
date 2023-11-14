from django.http import HttpResponse

def teste(request):
        return HttpResponse("Olá jp voce é bonito")

def teste2(request):
        return HttpResponse("Uma nova view")
def home(request):
        return HttpResponse("uma pagina de home")