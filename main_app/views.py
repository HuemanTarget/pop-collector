from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pop
from .forms import DetailForm
from django.http import HttpResponse

# Create your views here.
# class Pop:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, category, description, price):
#     self.name = name
#     self.category = category
#     self.description = description
#     self.price = price

# pops = [
#   Pop('Big Boy', 'Other', 'Bobs Big Boy famous mascot.', 1140),
#   Pop('Morty(Scared)', 'Animation', 'Morty from Rick And Morty scared.', 22),
#   Pop('Black Widow', 'Movies', 'Black Widow from the Avengers movies.', 15)
# ]

class PopCreate(CreateView):
  model = Pop
  fields = '__all__'
  success_url = '/pops/'

class PopUpdate(UpdateView):
  model = Pop
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['category', 'description', 'price']

class PopDelete(DeleteView):
  model = Pop
  success_url = '/pops/'


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    # return HttpResponse('<h1>About The Pop Collector</h1>')
    return render(request, 'about.html')

def pops_index(request):
    pops = Pop.objects.all()
    return render(request, 'pops/index.html', { 'pops': pops })

def pops_detail(request, pop_id):
  pop = Pop.objects.get(id=pop_id)
  # instantiate FeedingForm to be rendered in the template
  detail_form = DetailForm()
  return render(request, 'pops/detail.html', {
    # include the cat and feeding_form in the context
    'pop': pop, 'detail_form': detail_form
  })

def add_detail(request, pop_id):
	# create the ModelForm using the data in request.POST
  form = DetailForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_detail = form.save(commit=False)
    new_detail.pop_id = pop_id
    new_detail.save()
  return redirect('detail', pop_id=pop_id)