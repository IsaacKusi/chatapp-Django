from django.contrib import admin

from .models import Chatroom, Message

admin.site.register([Chatroom, Message])
