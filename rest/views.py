# myapp/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    if request.method == 'GET':
        # Process GET request
        return HttpResponse('This is a GET request.')
    elif request.method == 'POST':
        # Process POST request
        data = request.POST.get('data')  # Assuming 'data' is the name of the input field
        return HttpResponse(f'This is a POST request. Data received: {data}')
    else:
        return HttpResponse('Invalid request method.')



# settings.py
# Make sure 'myapp' is added to the 'INSTALLED_APPS' list and the necessary settings are configured.
