from django.shortcuts import render
from django.db.models import Q
from .models import Pet

def search_pet(request):
    if 'species' in request.GET and 'age' in request.GET:
        species = request.GET['species']
        age_input = request.GET['age']

        # Convert age_input to an integer (if possible)
        try:
            age = int(age_input)
        except ValueError:
            age = None

        # Prepare query for age filtering
        age_query = Q()
        if age is not None:
            if age_input.startswith('l'):
                age_query &= Q(age__lt=age)
            elif age_input.startswith('g'):
                age_query &= Q(age__gt=age)
            else:
                age_query &= Q(age=age)

        # Filter pets based on species and age
        pets = Pet.objects.filter(Q(species__icontains=species) & age_query).order_by('age')
        return render(request, 'search/search_results.html', {'pets': pets, 'species': species, 'age_input': age_input})
    else:
        return render(request, 'search/search.html')

