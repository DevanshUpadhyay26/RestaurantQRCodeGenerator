from django.shortcuts import render
from django.conf import settings
from .forms import QRForm
import qrcode
import os

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_form']
            url = form.cleaned_data['url']

            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + "_menu.png"
            file_path  =os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)


            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            context= {
                'res_name' : res_name,
                'qr_url' : qr_url,
                'file_name' : file_name,
            }
            return render(request, "qr_res.html", context)
            # print("Res:", res_name, "url:", url)  #Debug
    else:
        form = QRForm()
        context = {
        'form':form
        }
        return render(request, 'generate_qr_code.html', context)



