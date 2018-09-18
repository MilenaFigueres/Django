from django.shortcuts import render
from django.utils import timezone
#DESCOMENTAR
#from .models import Personal_list

def post_list(request):
	posts = Personal_list.objects.all()#.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'lists/post_list.html', {'posts': posts})
