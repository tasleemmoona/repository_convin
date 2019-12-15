from django.shortcuts import render
from django.http import HttpResponse
from test_task.forms import SampleForm 
from test_task.models import mytable_test

# Create your views here.

def index(request):
	if request.method == 'POST':
		c = request.POST['char']
		f = request.POST['file']
		n = mytable_test.objects.count()
		if n == 0:
			mytable_test.objects.create(char=c,file=f)
			ov = ''
			nv = ''
		else:
			ob = mytable_test.objects.get(id = 1)
			ov = ob.char
			nv = str(ob.file)
			ob.char = c
			ob.file = f
			ob.save()
		ol = [ov,nv]
		nl = [c,f]
		return render(request,"result.html",{'ol': ol, 'nl': nl})
	else:
		form = SampleForm()
		return render(request,"index.html",{'form': form})