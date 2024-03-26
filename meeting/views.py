from django.shortcuts import render
import random
from .models import meetings

# Create your views here.
def generate_meetingid():
    r = random.randint(100000, 999999)
    # while meetings.objects.filter(meeting_id=r).exists():
    #     r = random.randint(100000, 999999)
    return r


def meetings(request, meeting_id):
    name  = request.user.first_name + ' ' + request.user.last_name
    return render(request, 'config.html', {'fullname' : name, 'meeting_id' : meeting_id})