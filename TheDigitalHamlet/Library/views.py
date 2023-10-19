from django.shortcuts import render
from django.shortcuts import render

from Library.models import LibraryAgent
from TheDigitalHamlet.base_models import BaseUserProxyAgent
from traits import get_traits

def library_agent_chat(request):
    lib_agent = LibraryAgent("Tim", 20, "New York", get_traits())
    user = BaseUserProxyAgent(
        name="Ben"
        )
    chat = user.initiate_chat(user.name, True, False, context={"message": "Hello there! How are you?"})
    chat_history = user._oai_messages
    return render(request, 'library_agent_chat.html', {'chat_history': chat_history})
