from django.shortcuts import render

# Create your views here.
def index(request):
    print('I am in view.py')
    return render(request, 'learning_logs/index.html')
