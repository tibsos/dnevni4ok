from django.shortcuts import render

def handler404(request, exception, template_name="e/404.html"):
    response = render(template_name)
    response.status_code = 404
    return response
def handler505(request, exception, template_name="e/404.html"):
    response = render(template_name)
    response.status_code = 505
    return response