from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Pop, Accessory, Photo
from django.views.generic import ListView, DetailView
from .forms import DetailForm
from django.http import HttpResponse

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'popcollector'

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

class PopCreate(LoginRequiredMixin, CreateView):
  model = Pop
  fields = '__all__'
  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  success_url = '/pops/'

class PopUpdate(UpdateView):
  model = Pop
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['category', 'description', 'price']

class PopDelete(DeleteView):
  model = Pop
  success_url = '/pops/'


def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>About The Pop Collector</h1>')
    return render(request, 'about.html')

@login_required
def pops_index(request):
    pops = Pop.objects.filter(user=request.user)
    # pops = Pop.objects.all()
    return render(request, 'pops/index.html', { 'pops': pops })

@login_required
def pops_detail(request, pop_id):
  pop = Pop.objects.get(id=pop_id)
  # instantiate FeedingForm to be rendered in the template
  accessorys_pop_doesnt_have = Accessory.objects.exclude(id__in = pop.accessorys.all().values_list('id'))
  detail_form = DetailForm()
  return render(request, 'pops/detail.html', {
    # include the cat and feeding_form in the context
    'pop': pop, 'detail_form': detail_form,
    'accessorys': accessorys_pop_doesnt_have
  })

@login_required
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

@login_required
def assoc_accessory(request, pop_id, accessory_id):
  Pop.objects.get(id=pop_id).accessorys.add(accessory_id)
  return redirect('detail', pop_id=pop_id)

@login_required
def unassoc_accessory(request, pop_id, accessory_id):
  Pop.objects.get(id=pop_id).accessorys.remove(accessory_id)
  return redirect('detail', pop_id=pop_id)

@login_required
def add_photo(request, pop_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, pop_id=pop_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pop_id=pop_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessory/'