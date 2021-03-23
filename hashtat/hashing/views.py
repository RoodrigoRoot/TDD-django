from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib
from django.http import JsonResponse
# Create your views here.

def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data.get("text")
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

            try:

                haash = Hash.objects.get(haash=text_hash)
                return redirect('hash', haash=haash.haash)

            except Hash.DoesNotExist:
                hassh = Hash()
                hassh.text = text
                hassh.haash = text_hash
                hassh.save()
                return redirect('hash', haash=text_hash)
    form = HashForm()
    return render(request, "hashing/home.html", locals())


def hash_view(request, haash):

    hash_object = Hash.objects.get(haash=haash)
    return render(request, 'hashing/hash.html', locals())


def quickhash(request):

    text = request.GET.get("text")

    return JsonResponse({'hash':hashlib.sha256(text.encode('utf-8')).hexdigest()})