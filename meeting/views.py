from django.shortcuts import render
import random
from .models import meetings

# Create your views here.
def generate_meetingid():
    r = random.randint(100000, 999999)
    # while meetings.objects.filter(meeting_id=r).exists():
    #     r = random.randint(100000, 999999)
    return r


def meetings(request):
    name  = "jerryhaxor"
    id  = 511231
    return render(request, 'config.html', {'fullname' : name, 'meeting_id' : id})