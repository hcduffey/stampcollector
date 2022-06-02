from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stamp, Collection, Store
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# CORE PAGE VEIWS
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(str(self.request.user) != 'AnonymousUser'):
            context["collections"] = Collection.objects.filter(user=self.request.user)
        else:
            context["collections"] = []
        
        return context

class About(TemplateView):
    template_name = 'about.html'


# COLLECTION VIEWS
@method_decorator(login_required, name='dispatch')
class CollectionCreate(CreateView):
    model = Collection
    fields = "__all__"
    template_name = "collections/collection_create.html"

    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CollectionCreate, self).form_valid(form)

    success_url = '/'

class CollectionList(View):
    def get(self, request):
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class CollectionDetail(DetailView):
    model = Collection
    template_name = 'collections/collection_detail.html'

@method_decorator(login_required, name='dispatch')
class CollectionUpdate(UpdateView):
    model = Collection
    fields = "__all__"
    template_name = 'collections/collection_update.html'

    def get_success_url(self):
        return reverse('collection_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class CollectionDelete(View):
    def get(self, _, pk):
        Collection.objects.get(pk=pk).delete()
        return redirect('home')


# STAMP VIEWS

class Stamp_List(TemplateView):
    template_name = 'stamps/stamp_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stamps"] = Stamp.objects.all()

        return context

@method_decorator(login_required, name='dispatch')
class StampCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        cost = int(request.POST.get("cost"))
        image = request.POST.get("image")
        country = request.POST.get("country")
        condition = request.POST.get("condition")
        centering = request.POST.get("centering")
        format = request.POST.get("format")
        year = request.POST.get("year")

        collection = Collection.objects.get(pk=pk)
        Stamp.objects.create(name=name, cost=cost, image=image, country=country, condition=condition, centering=centering, format=format, year=int(year), collection=collection)

        return redirect("collection_detail", pk=pk)


class StampDetail(TemplateView):
    template_name = "stamps/stamp_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stamp"] = Stamp.objects.get(pk=kwargs["stamp_pk"])

        return context

@method_decorator(login_required, name='dispatch')
class StampUpdate(UpdateView):
    model = Stamp
    fields = "__all__"
    template_name = "stamps/stamp_update.html"
    
    def get_success_url(self):
        return reverse('stamp_detail', kwargs={'pk': self.object.collection.pk, 'stamp_pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class StampDelete(View):
    def get(self, _, pk, stamp_pk):
        Collection.objects.get(pk=pk).stamps.get(pk=stamp_pk).delete()
        return redirect('collection_detail', pk)


# STORE VIEWS
@method_decorator(login_required, name='dispatch')
class StoreCreate(CreateView):
    model = Store
    fields = "__all__"
    template_name = "stores/store_create.html"

    success_url = '/'

class StoreList(TemplateView):
    template_name = 'stores/store_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stores"] = Store.objects.all()

        return context

class StoreDetail(DetailView):
    model = Store
    template_name = 'stores/store_detail.html'

@method_decorator(login_required, name='dispatch')
class StoreUpdate(UpdateView):
    model = Store
    fields = "__all__"
    template_name = 'stores/store_update.html'

    def get_success_url(self):
        return reverse('store_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class StoreDelete(View):
    def get(self, _, pk):
        Store.objects.get(pk=pk).delete()
        return redirect('store_list')


# AUTH VIEWS

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("collection_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
