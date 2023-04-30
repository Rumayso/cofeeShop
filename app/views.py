from django.shortcuts import render
from django.views.generic import TemplateView , CreateView
from .models import Contact
# Create your views here.

class Home(TemplateView):
    template_name = "index.html"

class About(TemplateView):
    template_name = "about.html"

class Contact(CreateView):
    model = Contact
    template_name = "contact.html"
    fields = "__all__"

class Menu(TemplateView):
    template_name = "menu.html"

class Reservation(TemplateView):
    template_name = "reservation.html"

class Service(TemplateView):
    template_name = "service.html"

class Testimonial(TemplateView):
    template_name = "testimonial.html"
