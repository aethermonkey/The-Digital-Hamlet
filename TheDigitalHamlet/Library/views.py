from django.shortcuts import render
from django.shortcuts import render

def library_agent_chat(request):
    chat_history = ["Welcome to the Library!", "How can I assist you today?"]
    return render(request, 'library_agent_chat.html', {'chat_history': chat_history})
