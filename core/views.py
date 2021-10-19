from atributes.models import Cheveux, Tag
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, request
from .forms import ContactForm
from delivery.models import Wilaya, Commune
from django.views.generic import TemplateView, DetailView, ListView, CreateView, View
from .models import Gamme, Product, Category, SubCategory
from business.models import Business, Slide, Banner
from cart.forms import CartAddProductForm
from django.db.models import Q 
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(top=True)
        context["slide"] = Slide.objects.first()
        context["banner"] = Banner.objects.first()
        context["new_products"] = Product.objects.filter(new=True)
        context["top_selling"] = Product.objects.filter(top= True) 
        context["random_3_1"] = Product.objects.all().order_by('?')[:3]
        context["random_3_2"] = Product.objects.all().order_by('?')[:3]
        context["random_3_3"] = Product.objects.all().order_by('?')[:3]
        context["random_3_4"] = Product.objects.all().order_by('?')[:3]
        context["random_3_5"] = Product.objects.all().order_by('?')[:3]
        context["random_3_6"] = Product.objects.all().order_by('?')[:3]
        return context
#  STATIC


class AboutView(TemplateView):
    template_name = "about.html"

class VirementBancaireView(TemplateView):
    template_name = "paiement/virement-bancaire.html"

class CarteBancaireView(TemplateView):
    template_name = "paiement/carte-bancaire.html"

class PaiementView(TemplateView):
    template_name = "paiement/paiement.html"

class PaiementEspecesView(TemplateView):
    template_name = "paiement/paiement-especes.html"


#  LIVRAISON

class EchangeView(TemplateView):
    template_name = "livraison/echange.html"

class LivraisonView(TemplateView):
    template_name = "livraison/livraison.html"

class RetourView(TemplateView):
    template_name = "livraison/retours.html"




class CategoryProductsView(ListView):
    context_object_name = 'products'
    model = Product
    paginate_by = 15
    template_name = "products.html"

    def get_queryset(self, *args, **kwargs): # new
        
        products = Product.objects.filter(actif=True)
        try:
            category = get_object_or_404(Category, slug=self.kwargs['slug'])
            products = products.filter(sous_category__category=category)
        except:
            category = get_object_or_404(SubCategory, slug=self.kwargs['slug'])
            products = products.filter(sous_category=category)
        return products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["sous_categories"] = SubCategory.objects.all()
        # context["products"] = Product.objects.all()
        return context



# for django-filter pagination
class PaginatedFilterViews(View):
    def get_context_data(self, **kwargs):
        context = super(PaginatedFilterViews, self).get_context_data(**kwargs)
        if self.request.GET:
            querystring = self.request.GET.copy()
            if self.request.GET.get('page'):
                del querystring['page']
            context['querystring'] = querystring.urlencode()
        return context

class ProductsView(PaginatedFilterViews, ListView):
    context_object_name = 'products'
    model = Product
    template_name = "products.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searched'] = self.request.GET.get('name') 
        context["filters"] = ProductFilter(self.request.GET, queryset= Product.objects.all())
        context["sous_categories"] = SubCategory.objects.all()
        context["tags"] = Tag.objects.all()
        context["cheveux"] = Cheveux.objects.all()
        context["gammes"] = Gamme.objects.all()
        # context["products"] = Product.objects.all()
        return context



def filtered_view(request):
    filter = ProductFilter(request.GET, queryset= Product.objects.all())
    html = render_to_string('snipetts/ajax-product-block.html', {'filter': filter}, request=request)
    # paginator = Paginator(filter.qs, 4)
    # page = request.GET.get('page')
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)
    return JsonResponse({'form': html})

# class ProductsView(ListView):
#     context_object_name = 'products'
#     model = Product
#     paginate_by = 15
#     template_name = "products.html"

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         min = self.request.GET.get('min')
#         max = self.request.GET.get('max')
#         new = self.request.GET.get('new')
#         top = self.request.GET.get('top')
#         if max and new and top:
#             products = Product.objects.filter(price__range=[min, max], actif=True, new= True, top=True)
#         elif max and new:
#             products = Product.objects.filter(price__range=[min, max], actif=True,new= True)
#         elif max and top:
#             products = Product.objects.filter(price__range=[min, max], actif=True, top=True)
#         elif top and new:
#             products = Product.objects.filter(actif=True,new= True, top=True)
#         elif max:
#             products = Product.objects.filter(price__range=[min, max], actif=True)
#         elif new:
#             products = Product.objects.filter(actif=True,new= True)
#         elif top:
#             products = Product.objects.filter(actif=True, top=True)
#         elif query:
#             if len(query) > 2:
#                 by_2 = [query[i:i+2] for i in range(0, len(query), 2)][0]
#                 by_1 = [query[i:i+2] for i in range(0, len(query), 2)][1:]
#                 print('the sring split one  ', by_2)
#                 print('the sring towo', by_1)
#                 for i in by_1:
#                     products = Product.objects.filter(
#                             Q(name__icontains=by_2) & Q(name__icontains=i)
#                             )
#                     if not len(products):
#                         products = Product.objects.filter(
#                             Q(name__icontains=by_2) | Q(name__icontains=i)
#                             )
#             else: 
#                 products = Product.objects.filter(name__icontains=query)
#         else :
#             products = Product.objects.all()
#         return products

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context["categories"] = Category.objects.all()
#         context["sous_categories"] = SubCategory.objects.all()
#         # context["products"] = Product.objects.all()
#         return context




class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "product-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Product.objects.all().order_by('?')[:4] 
        context["wilayas"] = Wilaya.objects.all().order_by('name') 
        return context



class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
  
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
      
        message = 'Une erreur est survenue, veuillez réessayer.'
        success = False
        try:
            #save the form   
            if form.is_valid():
                form.save()
                #messages.success(request, 'Votre message a bien été envoyé')
                message = 'Votre message a bien été envoyé!'
                success = True
                print(success)
                return render(request, 'other/contact.html', {'message': message, 'success': success})
            else:
                print(success)
                message = 'Une erreur est survenue, veuillez réessayer.'
                return render(request, 'contact.html', {'message': message, 'failure': True})
        except:
            return render(request, 'contact.html', {'message': message, 'failure': True})
        return render(request, 'contact.html', {'message': message, 'failure': True})




