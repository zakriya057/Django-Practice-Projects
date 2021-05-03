from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'test.Html')

def g2f(grade):
	if grade=='A':
		return 4.0
	elif grade=='A-':
		return 3.67
	elif grade=='B+':
		return 3.33
	elif grade=='B':
		return 3.00
	elif grade=='B-':
		return 2.67
	elif grade=='C+':
		return 2.33
	elif grade=='C':
		return 2.00
	elif grade=='C-':
		return 1.67
	elif grade=='D+':
		return 1.33
	elif grade=='D':
		return 1.00
	else:
		return 0

	

def cgpa(request):
	g1=request.GET["G1"]
	c1=int(request.GET["C1"])
	g2=request.GET["G2"]
	c2=int(request.GET["C2"])
	g3=request.GET["G3"]
	c3=int(request.GET["C3"])
	g4=request.GET["G4"]
	c4=int(request.GET["C4"])
	g5=request.GET["G5"]
	c5=int(request.GET["C5"])
	gr=[]
	gr1=g2f(g1)
	gr.append(gr1)
	gr2=g2f(g2)
	gr.append(gr2)
	gr3=g2f(g3)
	gr.append(gr3)
	gr4=g2f(g4)
	gr.append(gr4)
	gr5=g2f(g5)
	gr.append(gr5)
	cr=[]
	cr.append(c1)
	cr.append(c2)
	cr.append(c3)
	cr.append(c4)
	cr.append(c5)
	s=0
	r=0
	for x in cr:
		s+=x
	for x in range(len(cr)):
		r=r+(cr[x]*gr[x])
	r=r/s
	return render(request,'result.html',{"r":r})
		




	