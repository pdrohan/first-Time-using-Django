from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def Home(request):
    return render(request, 'base/home.html')


def Contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_phone = request.POST['message-phone']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
        send_mail(
            'New Resume Website Message',
            message_text + "From: " + message_name,
            message_email,
            ['peterdrohan37@gmail.com']
        )
        context = {
            'message_name': message_name
        }
        return render(request, 'base/contact.html', context)

    else:
        return render(request, 'base/contact.html')
