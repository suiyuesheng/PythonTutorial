#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	#return HttpResponse('hello')
	return render(request,'home.html')


def count(request):
	#return HttpResponse('hello')
	input_text = request.GET['text']

	total_count = len(input_text)

	word_dict = {}

	for word in input_text:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1

	sorted_dict = sorted(word_dict.items(), key=lambda w:w[1], reverse=True)


	
	return render(request,'count.html', 
		{'total_count': total_count, 'input_text' : input_text, 
		'word_dict' : word_dict, 'sorted_dict' : sorted_dict })