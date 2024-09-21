from django.shortcuts import render
from django.views import View


class IndexPage(View):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)


class LoginPage(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)
    

class RegisterPage(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)