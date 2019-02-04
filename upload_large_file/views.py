from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView

from .forms import UploadFileForm
from .models import FileUpload


class UserFilesView(LoginRequiredMixin, ListView):
    model = FileUpload
    context_object_name = 'user_files'
    template_name = 'upload_large_file/index.html'

    def get_queryset(self):
        return FileUpload.objects.filter(user=self.request.user)


class UserFileDetialView(LoginRequiredMixin, DetailView):
    model = FileUpload
    context_object_name = 'user_file'
    template_name = 'upload_large_file/file_detail.html'


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            user_file_obj = FileUpload()
            user_file_obj.file = file
            user_file_obj.user = request.user
            user_file_obj.save()
            return redirect('files')
    else:
        form = UploadFileForm()
    return render(request, 'upload_large_file/fileupload_form.html', {'form': form})


class UserFileDelete(LoginRequiredMixin, DeleteView):
    model = FileUpload

    success_url = reverse_lazy('files')
