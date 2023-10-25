from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworld_function(request):
    returned_object = HttpResponse('<h1>HelloWold<h1>')
    return returned_object


class HelloWorld_class(TemplateView):
    # htmlファイルの場所指定しる
    template_name = 'hello.html'