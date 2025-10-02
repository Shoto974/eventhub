from django import template

register = template.Library()

@register.filter
def is_participant(event, user):
    return event.participation_set.filter(user=user).exists()