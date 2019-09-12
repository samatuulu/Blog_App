from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import Things, STATUS_CHOICES


def home(request):
    jobs = Things.objects.all()
    return render(request, 'index.html', context={
        'jobs': jobs
    })


def detail_view(request, pk):
    job = get_object_or_404(Things, pk=pk)
    context = {'job': job}
    return render(request, 'detail_view.html', context)


def create(request, *args, **kwargs):

    context = {
        'status': STATUS_CHOICES
    }

    if request.method == 'GET':
        return render(request, 'create.html', context)
    elif request.method == 'POST':
        status = request.POST.get('status')
        description = request.POST.get('description')
        description_more = request.POST.get('description_more')
        date = request.POST.get('date')
        if date == '':
            date = None
        Things.objects.create(description=description, status=status, date_of_completion=date, description_more=description_more)
        response = redirect('home')
        return response


def job_update_view(request, pk):
    job = get_object_or_404(Things, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'job': job, 'status': STATUS_CHOICES})
    elif request.method == 'POST':
        job.status = request.POST.get('status')
        job.description = request.POST.get('description')
        job.description_more = request.POST.get('description_more')
        job.date_of_completion = request.POST.get('date')
        if job.date_of_completion == '':
            job.date_of_completion = None
        job.save()
        return redirect('detail', pk=pk)


def delete_task(request, pk):
    job = get_object_or_404(Things, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'job': job})
    elif request.method == 'POST':
        job.delete()
        return redirect('home')

