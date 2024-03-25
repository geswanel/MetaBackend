from django.shortcuts import render
from django.views import View

from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .models import Book
from rest_framework.views import APIView


# Create your views here.
class BookList(APIView):
    def get(self, request):
        items = Book.objects.all()
        items_dicts = []
        for item in items:
            items_dicts.append(model_to_dict(item))
        return JsonResponse(items_dicts, safe=False)
    
    def post(self, request):
        try:
            title = request.POST["title"]
            author = request.POST["author"]
            price = float(request.POST["price"])
            inventory = int(request.POST["inventory"])
            return HttpResponse("Putted {} {} {} {}".format(title, author, price, inventory), status=200)
        except:
            return HttpResponse("Bad Request", status=400)

class BookItem(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return JsonResponse(model_to_dict(book))

    def put(self, request, pk):
        try:
            title = request.POST["title"]
            author = request.POST["author"]
            price = float(request.POST["price"])
            inventory = int(request.POST["inventory"])
            return HttpResponse("Putted {} {} {} {}".format(title, author, price, inventory), status=200)
        except:
            return HttpResponse("Bad Request", status=400)

    def patch(self, request, pk):
        try:
            title = request.POST.get("title")
            author = request.POST.get("author")
            price = float(request.POST.get("price"))
            inventory = int(request.POST.get("inventory"))
            return HttpResponse("Putted {} {} {} {}".format(title, author, price, inventory), status=200)
        except:
            return HttpResponse("Bad Request", status=400)