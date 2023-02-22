from django.forms import ModelForm

from .models import *


class createInForum(ModelForm):
    class Meta:
        model = forum
        fields = "__all__"


class createInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
