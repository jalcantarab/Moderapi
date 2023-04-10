# Django Imports
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
# App Imports
from .models import ModerationAttempt
    
    
def moderation_view(request):
    moderation = None
    
    return render(request, 'moderation/moderation.html')

def moderation_api(request):
    if request.method == 'POST':
        moderation_attempt = ModerationAttempt(settings.OPENAI_API_KEY)
        message = request.POST['content']
        # Sending the message to the webservice
        moderation = moderation_attempt.get_results(message=message,)
        if moderation: 
            response_data = {
                'success': True,
                'categories': moderation['categories'],
                'scores': moderation['category_scores'],
                'flagged': moderation['flagged'],
                'id':moderation['id'],
            }
        else:
            response_data = {
                'success': False,
                'error': 'Failed to get moderation results.',
            }
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})
    
    return JsonResponse(response_data)
