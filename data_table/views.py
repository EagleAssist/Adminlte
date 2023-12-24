

# Create your views here.
from django.shortcuts import render

from rest_framework import generics


from .models import Companies
from .serializers import CompaniesSerializer

class ModelList(generics.ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
def model_list(request):
    data = Companies.objects.all()
    return render(request, 'list.html', {'data': data})
# # class ItemUpdateView(UpdateView):
#     model = Item
#     form_class = ItemForm
#     template_name = 'myapp/item_edit_form.html'

#     def dispatch(self, *args, **kwargs):
#         self.item_id = kwargs['pk']
#         return super(ItemUpdateView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         form.save()
#         item = Item.objects.get(id=self.item_id)
#         return HttpResponse(render_to_string('myapp/item_edit_form_success.html', {'item': item}))