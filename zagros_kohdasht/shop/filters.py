from . import models

class FabricFilter():
    def __init__(self, context, fabrics_data, primary_filter = {}):
        self.filter_items = ['usage', 'color', 'material', 'pattern', 'width', 'thickness']
        self.context = context
        self.fabrics_data = fabrics_data
        self.all_filter_items = {}
        self.selectes_items = {}
        self.primary_filter = primary_filter
        self.THICKNESS_CHOICES = dict(models.Fabric.THICKNESS_CHOICES)
        

        
    def get_verbose_name(self):
        verbose = {}
        for item in self.filter_items:
            verbose[item] = models.Fabric._meta.get_field(item).verbose_name
        self.verbose = verbose
    
    def get_all_data_for_one_item(self, item_name):
        if item_name == 'thickness':
            thickness_list = list(self.context['fabrics_data'].values_list('thickness', flat=True).distinct())
            return [self.THICKNESS_CHOICES.get(thickness) for thickness in list(dict.fromkeys(thickness_list))]
        model_class = getattr(models, item_name.capitalize())
        fabric_ids = self.context['fabrics_data'].values_list('id', flat=True)
        return model_class.objects.filter(
            fabric__id__in=fabric_ids).distinct()
    
    def get_all_data_for_all_items(self, item_not_get = None):
        for item in self.filter_items:
            if item != item_not_get:
                self.all_filter_items[item] = self.get_all_data_for_one_item(item)

        
    def get_selected_items(self, request):
        for item in self.filter_items:
            self.selectes_items[item] = request.GET.getlist(item)
            if item in self.primary_filter:
                self.selectes_items[item].extend(self.primary_filter[item])
            
        
    
    def get_filtered_data(self):
        for item in self.filter_items:
            if item == 'thickness' and self.selectes_items['thickness']:
                selected_thickness = []
                for i in self.selectes_items['thickness']:
                    selected_thickness.append(next(k for k, v in self.THICKNESS_CHOICES.items() if v == i))
                self.context['fabrics_data'] = self.context['fabrics_data'].filter(thickness__in=selected_thickness)
            elif self.selectes_items[item]:
                lookup = f"{item}__name__in"
                self.context['fabrics_data'] = self.context['fabrics_data'].filter(
                    **{lookup: self.selectes_items[item]}).distinct()
            # self.get_all_data_for_all_items()
    
    def get_filter_attributes_data(self):
        all_filter_items_list, selectes_items_list, verbose_list = [], [], []
        for item in self.filter_items:
            if self.all_filter_items[item]:
                all_filter_items_list.append(self.all_filter_items[item])
                
            else:
                all_filter_items_list.append(None)
                
            if self.selectes_items[item]:
                selectes_items_list.append(self.selectes_items[item])
            else:
                selectes_items_list.append(None)
                
            if self.verbose[item]:
                verbose_list.append(self.verbose[item])
            else:
                verbose_list.append(None)
                
        self.context['filter_attributes'] = list(zip(all_filter_items_list, selectes_items_list, verbose_list, self.filter_items))
            
            
    def run(self, request):
        self.get_selected_items(request)
        self.context['fabrics_data'] = self.fabrics_data
        self.get_all_data_for_all_items()
        self.get_filtered_data()
        self.get_verbose_name()
        self.get_filter_attributes_data()
        return self.context