from .models import Category

def category(request):
    categories = Category.objects.filter(actif=True)
    
    context = {
            'categories' : categories,
    }
    return context
    

