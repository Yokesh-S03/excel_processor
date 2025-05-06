from django.shortcuts import render, redirect
from .forms import FolderUploadForm
from .models import ProcessedFile
from .utils import process_folder
import os
import tempfile
from django.conf import settings

def upload_folder(request):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        if form.is_valid():
           
            temp_dir = tempfile.mkdtemp(dir=os.path.join(settings.MEDIA_ROOT, 'temp'))

            temp_base_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
            os.makedirs(temp_base_dir, exist_ok=True)
         
            temp_dir = tempfile.mkdtemp(dir=temp_base_dir)
            for file in request.FILES.getlist('folder'):
                with open(os.path.join(temp_dir, file.name), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            
         
            result = process_folder(temp_dir)
            
            if result:
               
                processed = ProcessedFile.objects.create(
                    original_folder=result['original_folder'],
                    master_file=result['master_file'],
                    summary_file=result['summary_file']
                )
                return redirect('results', pk=processed.pk)
    
    else:
        form = FolderUploadForm()
    
    return render(request, 'processor/upload.html', {'form': form})

def results(request, pk):
    processed = ProcessedFile.objects.get(pk=pk)
    return render(request, 'processor/results.html', {'processed': processed})
