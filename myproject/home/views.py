from django.shortcuts import render
from users.decorators import login_required_custom

@login_required_custom
def home(request):
    context = {
        'user': request.user,
    }
    return render(request, 'index.html', context)
