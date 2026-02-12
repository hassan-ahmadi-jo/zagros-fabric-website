from django.shortcuts import render
from . import models
from .filters import FabricFilter
from django.views.generic import TemplateView


def get_usage_object(fabrics_data):
    usage_dic = {}
    
    usages = (models.Usage.objects
              .filter(fabric__in = fabrics_data).distinct().order_by('-first_page')[:5])
    
    for usage in usages:
        patterns = (models.Pattern.objects
                    .filter(fabric__usage = usage, fabric__in = fabrics_data).distinct())
        usage_dic[usage] = patterns
    return usage_dic

def get_pattern_object(fabrics_data):
    pattern_dic = {}

    patterns = (
        models.Pattern.objects
        .filter(fabric__in=fabrics_data)
        .distinct().order_by('-first_page')[:5]
    )

    for pattern in patterns:
        usages = (
            models.Usage.objects
            .filter(fabric__pattern=pattern, fabric__in=fabrics_data)
            .distinct()
        )
        pattern_dic[pattern] = usages

    return pattern_dic

        

# Create your views here.
def index_page(request):
    fabrics_data = models.Fabric.objects.all()
    usages = models.Usage.objects.filter(fabric__in = fabrics_data).distinct().order_by('-first_page')[:5]
    context = {'usages': usages}
    return render(request, "shop/index.html", context)

def product_list_page(request):
    fabrics_data = models.Fabric.objects.all().order_by('-first_page')
    filter = FabricFilter(fabrics_data)
    context = filter.run(request)
    return render(request, "shop/product_list.html", context)
    


def product_item_page(request, id):
    context = {'fabric':models.Fabric.objects.get(id=id)}
    return render(request, "shop/product_item.html", context)

def categories_page(request):
    fabrics_data = models.Fabric.objects.all()
    categories_list = {}
    items_list = ['pattern', 'usage', 'material', 'color', 'width']
    for item in items_list:
        model_class = getattr(models, item.capitalize())
        objects_list = model_class.objects.filter(fabric__in = fabrics_data).distinct()
        verbose_name = model_class._meta.verbose_name
        categories_list[item] = [verbose_name, objects_list]
    context = {'categories_list': categories_list}
    return render(request, 'shop/categories_page.html', context)

def contact_us_page(request):
    return render(request, 'shop/contact_us.html')

def address_page(request):
    return render(request, 'shop/address.html')


class HeaderPartialView(TemplateView):
    template_name = 'shop/header_partial.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fabrics_data = models.Fabric.objects.all().order_by("-first_page")
        pattern_dict = get_pattern_object(fabrics_data)
        usage_dict = get_usage_object(fabrics_data)
        context['pattern_dict'] = pattern_dict
        context['usage_dict'] = usage_dict
        return context
    
class FooterPartialView(TemplateView):
    template_name = 'shop/footer_pertial.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fabrics_data = models.Fabric.objects.all()
        usages = models.Usage.objects.filter(fabric__in = fabrics_data).distinct().order_by('-first_page')[:5]
        context['usages'] = usages
        return context