import openai
from django.db import models

class ModerationRecord(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    flagged = models.BooleanField(default=False)
    categories = models.JSONField()
    category_scores = models.JSONField()
    
    def __str__(self):
        return f"{self.flagged} | {self.content}"
    
class ModerationAttempt:
    def __init__(self, api_key):
        openai.api_key = api_key
        
    def get_results(self, message):
        moderation = None
        response = openai.Moderation.create(
            input=message,
            )
        if 'results' in response and response['results']:
            results = response['results'][0]
            moderation = ModerationRecord.objects.create(
                content=message,
                flagged=results['flagged'],
                categories=results['categories'],
                category_scores=results['category_scores'],
                )
            moderation.save()
            results['id'] = moderation.id
        else: 
            raise Exception(f'Failed to receive results: {response}')
        return results
    
