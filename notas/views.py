from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Notas Colab</h1><p>Bienvenido al proyecto.</p>")

