from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Company


def index(request):
    latest_company_list = Company.objects.order_by("-incorporation_date")[:5]
    output = ", ".join([c.__str__() for c in latest_company_list])
    context = {
        "latest_company_list": latest_company_list
    }
    return render(request, "companies/index.html", context)

def detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, "companies/detail.html", {"company": company})

def profits(request, company_id):
    response = "You're looking at the profit margins of company %s."
    return HttpResponse(response % company_id)

def relocate(request, company_id):
    return HttpResponse("You're relocating company %s." % company_id)