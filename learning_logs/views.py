from django.shortcuts import render

def index(request):
    """The home page for Learning Log."""
    return render(request, 'C://Users/stgar/Learning-Log/learning_logs/templates/index.html')

