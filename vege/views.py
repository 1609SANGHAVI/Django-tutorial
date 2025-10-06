from django.shortcuts import render,redirect

# Create your views here.
from .models import Receipe  # make sure this import is present

def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipeName')
        receipe_description = data.get('receipeDescription')
        receipe_image = request.FILES.get('receipeImage')

        # Save to database
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect("/receipes/")

    return render(request, "receipes.html")
