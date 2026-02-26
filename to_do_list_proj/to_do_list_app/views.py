from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm
# Create your views here.
def home(request):
    all_todos = ToDo.objects.all()
    return render(request, 'pages/home.html', {'all_todos': all_todos})
def add_to(request):
    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form': form}
    return render(request, 'pages/add_to.html', context)

def edit_to(request,pk):
    todo_id=ToDo.objects.get(id=pk)
    formedit=ToDoForm(instance=todo_id)
    if request.method=='POST':#نتاكد من الميثود بوست
        formedit=ToDoForm(request.POST,instance=todo_id)
        if formedit.is_valid():
            formedit.save()#نحفظ التعديلات
            return redirect('/')#نعيد التوجيه للصفحة الرئيسية
    context={'formedit':formedit}
    return render(request, 'pages/edit_to.html', context)
def delete_to(request,pk):
    todo_id_del=ToDo.objects.get(id=pk)
    if request.method=='POST':#نتاكد من الميثود بوست
        todo_id_del.delete()#نحذف الطلب
        return redirect('/')#نعيد التوجيه للصفحة الرئيسية
    context={'todo_id_del':todo_id_del}
    return render(request, 'pages/delete_to.html', context)
def details_to(request,pk):
    todo_id=ToDo.objects.get(id=pk)
    formedit=ToDoForm(instance=todo_id)
    if request.method=='POST':#نتاكد من الميثود بوست
        formedit=ToDoForm(request.POST,instance=todo_id)
    context={'formedit':formedit}
    return render(request, 'pages/details.html', context)
def search_to(request):
    search_results=ToDo.objects.all()  # Initialize with an empty queryset
    title_search = request.GET.get('title_search_html')
    if title_search:
        search_results = ToDo.objects.filter(title__icontains=title_search)
    context={'search_results': search_results}
    return render(request, 'pages/home.html', context)
def about(request):
    return render(request, 'pages/about.html')