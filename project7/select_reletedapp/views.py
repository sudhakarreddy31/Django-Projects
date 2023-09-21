from django.shortcuts import render

from select_reletedapp.models import Employee,Book, Songs,Story

# Create your views here.

# Retriving all Employee data with theair name

def home(request):
    employees = Employee.objects.all().select_related('department')
    for employee in employees:
        print(employee.name,employee.department.name)


def index(request):
    books=Book.objects.all().select_related('author')
    for book in books:
        print(book.title,book.author.name)



def select(request):
    songs = Songs.objects.all().select_related('song_writer')
    for song in songs:
        print(song.song_writer.name)


def selec(request):
    storys = Story.objects.all().prefetch_related('reader')
    for story in storys:
        print(story.name,story.reader.name)













