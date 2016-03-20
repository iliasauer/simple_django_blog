from django.shortcuts import render_to_response


def basic(request):
    return render_to_response('index.html')