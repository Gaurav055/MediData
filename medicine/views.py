from django.shortcuts import render
from .models import Medicine
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        medicine=Medicine.objects.filter(sku_name__icontains=q)
    else:
        medicine=Medicine.objects.none()

    return render(request,'medicine/home.html',{'medicine':medicine})
    # Pagintion logic
    # paginator=Medicine(med,2)
    # page_number=request.GET.get('page')
    # med_obj=paginator.get_page(page_number)
  


# LOAD MORE PAGES
# def load_more(request):
#     offset=int(request.POST['offset'])
#     limit=2
#     posts=Post.objects.all()[offset:limit+offset]
#     totalData=Post.objects.count()
#     data={}
#     posts_json=serializers.serialize('json',posts)
#     return JsonResponse(data={
#         'posts':posts_json,
#         'totalResult':totalData
#     })