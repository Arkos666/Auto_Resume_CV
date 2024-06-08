from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.db.utils import IntegrityError


def home(request):
    actual_tag = "Genérico"

    qs_company = Company.objects.all()
    qs_position = Position.objects.all()
    qs_action = Action.objects.order_by('position')

    if request.method == 'POST':
        postreq = request.POST
        if 'tag' in postreq:
            actual_tag = postreq['tag']
            qs_company = Company.objects.filter(position__action__tag_job__tag__in=[actual_tag]).distinct()
            qs_position = Position.objects.filter(action__tag_job__tag__in=[actual_tag]).distinct()
            qs_action = Action.objects.filter(tag_job__tag=actual_tag,)

    return render(request, "resume_app/index.html", {
        "companies": qs_company,
        "positions": qs_position,
        "actions": qs_action,
        "tagsjob": TagJob.objects.exclude(tag__exact='<Generic>').order_by('tag'),
        "actual_tag": actual_tag,
    })


def skills(request):
    return render(request, "resume_app/skills.html", {
        "tagsjob": TagJob.objects.all(),
    })
