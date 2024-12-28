from django.http import JsonResponse

def api_success(request):
    return JsonResponse({"message": "API is working successfully!"})

def root_success(request):
    return JsonResponse({"message": "Welcome to the CodeWithMuh YouTube Channel! Don't Forget to Subscribe and Like"})
