from django.db import models
from django.utils.text import slugify
# Create your models here.
from atributes.models import Cheveux, Tag, Parfum
from django.urls import reverse
from tinymce import models as tinymce_models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
STATUS_PRODUIT = (
    ('N', _('Nouveau')),
    ('R', _('Rupture')),
    ('P', _('Promotion')),
)

class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class Gamme(models.Model):
    name = models.CharField(verbose_name ="nom", max_length=150)
    # hex_value   = models.CharField(max_length=7, verbose_name="Valeur hexadécimale")
    objects = ActiveManager()
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField( max_length=150, verbose_name='Nom')
    slug = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    # pixel = models.TextField(verbose_name='Facebook Pixel', blank=True, null=True)
    actif  = models.BooleanField(verbose_name='actif', default=True)
    objects = ActiveManager()
    class Meta:
        ordering = ('id',)
        verbose_name = 'Catégorie'
        verbose_name_plural = '1. Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +'-'+str(self.id))
        return super(Category, self).save(*args, **kwargs)

    def product_count(self):
        products = Product.objects.filter(sous_category__category=self.id).count()
        return products

    def get_absolute_url(self):
        return f"/produits/?sous_category__category={self.id}"


class SubCategory(models.Model):
    name = models.CharField( max_length=150, verbose_name='Nom')
    slug = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    actif  = models.BooleanField(verbose_name='actif', default=True)
    category = models.ForeignKey(Category, verbose_name="Catégorie",related_name="sub_categories" ,on_delete=models.CASCADE)
    objects = ActiveManager()
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Sous Catégorie'
        verbose_name_plural = '2. Sous Catégorie'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +'-'+str(self.id))
        return super(SubCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/produits/?sous_category={self.id}"


class Product(models.Model):
    name            = models.CharField( max_length=200, verbose_name='Nom')
    slug            = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    sous_category   = models.ForeignKey(SubCategory, verbose_name="Sous Catégorie",related_name="products" ,on_delete=models.CASCADE)
    description     = tinymce_models.HTMLField(verbose_name='Déscription du produit', blank=True, null=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    old_price       = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ancien prix",blank=True, null=True)
   
    volume     = models.IntegerField( blank=True, verbose_name="Contenance")
    gamme      = models.ForeignKey(Gamme, blank=True, null=True,related_name="products", on_delete=models.CASCADE)
    cheveux    = models.ManyToManyField(Cheveux, blank=True)
    parfum    = models.ManyToManyField(Parfum, blank=True)
    tag        = models.ManyToManyField(Tag, blank=True)

    actif      = models.BooleanField(verbose_name='actif', default=True)
    new        = models.BooleanField(verbose_name='Nouveau', default=True)
    top        = models.BooleanField(verbose_name='Meilleur vente', default=True)
    status     = models.CharField(choices=STATUS_PRODUIT, max_length=1, default='N', blank=True, null=True, verbose_name='Status')

    created = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    
    objects = ActiveManager()
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Produit'
        verbose_name_plural = '3. Produits'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +'-'+str(self.id))
        return super(Product, self).save(*args, **kwargs)    

    def get_absolute_url(self):
        return reverse("core:productDetail", args=[self.slug])

class PhotoProduct(models.Model):
    photo = models.ImageField(upload_to='images/produits') 
    produit = models.ForeignKey(Product, related_name="photos", on_delete=models.CASCADE)


class ContactForm(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank = True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulaire de contact'
        verbose_name_plural = 'Formulaire de contact'

