from django.shortcuts import redirect, render 
from .models import Message

def chat(request):
    messages = Message.objects.order_by('-timestamp')[:50]
    return render(request, 'chat.html', {'messages': messages})

def post_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        content = request.POST.get('content')
        message = Message(sender=sender, content=content)
        message.save()
    return redirect('chat')
