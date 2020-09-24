from django.shortcuts import render
from .models import Blog, Entry, Author




def homework(request):
    #query = Blog.objects.all()
    #print([e.name for e in query])
    a = Entry.objects.all().filter(pub_date__year=2006)
    a.delete()
    b = Blog.objects.create(name="Akuala Temple", tagline="Plein succes") 
    
   

    #a = Blog(name='Beatles Blog', tagline='All the latest Beatels news.')
    #b = Blog(name='Beatles Blog BAd', tagline='All the latest Beatels news !.')
    #b.save()
    #its save also in the database, reflect even in the shell
    # it will render the name of queries according to dunder __str__ methode
    template_name= 'queries/home.html'
    context = {'a':a , "b":b}
    return render( request, template_name, context)


