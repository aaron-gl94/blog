from django.shortcuts import render
from django.views.generic import View

class Blog(View):
	def get(self,request):
		template_name = 'blog.html'
		return render (request,template_name)
