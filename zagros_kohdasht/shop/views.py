from django.shortcuts import render, get_object_or_404
from . import models
from .filters import FabricFilter
from django.views.generic import TemplateView, ListView

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
class IndexView(TemplateView):
    template_name = 'shop/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fabrics_data = models.Fabric.objects.all()
        usages = models.Usage.objects.filter(fabric__in = fabrics_data).distinct().order_by('-first_page')[:5]
        context['usages'] = usages
        return context


class ProductListView(ListView):
    template_name = 'shop/product_list.html'
    model = models.Fabric
    paginate_by = 30
    context_object_name = 'fabrics_data'

    def get_queryset(self):
        queryset = super().get_queryset()
        fabrics_data = models.Fabric.objects.all()
        filter = FabricFilter(fabrics_data)
        filter_data = filter.run(self.request)
        self._filter_data = filter_data
        return queryset.filter(id__in = filter_data['fabrics_data']).order_by('-first_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_attributes'] = self._filter_data['filter_attributes']
        querydict = self.request.GET.copy()
        querydict.pop('page', None)
        context['querydict'] = querydict.urlencode()
        return context


class ProductItemView(TemplateView):
    template_name = 'shop/product_item.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fabric'] = get_object_or_404(models.Fabric, id = kwargs.get('id'))
        return context


class CategoriesView(TemplateView):
    template_name = 'shop/categories_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fabrics_data = models.Fabric.objects.all()
        categories_list = {}
        items_list = ['pattern', 'usage', 'material', 'color', 'width']
        for item in items_list:
            model_class = getattr(models, item.capitalize())
            objects_list = model_class.objects.filter(fabric__in = fabrics_data).distinct()
            verbose_name = model_class._meta.verbose_name
            categories_list[item] = [verbose_name, objects_list]
        context['categories_list'] = categories_list
        return context


class ContactUsView(TemplateView):
    template_name = 'shop/contact_us.html'


class AddressView(TemplateView):
    template_name = 'shop/address.html'
    


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