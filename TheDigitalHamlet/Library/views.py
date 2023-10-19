from django.shortcuts import render
from django.shortcuts import render

from Library.models import LibraryAgent
from TheDigitalHamlet.base_models import BaseUserProxyAgent
from autogen import config_list_from_json


def library_agent_chat(request):
    lib_agent = LibraryAgent(name="Tim")
    
    user = BaseUserProxyAgent(
        name="Ben",
        code_execution_config=False
        )
    
    chat_history = user._oai_messages
    return render(request, 'library_agent_chat.html', {'chat_history': chat_history, "user": user, "lib_agent": lib_agent})
