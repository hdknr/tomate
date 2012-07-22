from django.conf import settings
from django.core.mail import get_connection

from celery.task import task

import commands

@task
def pomodoro(sender=None,id=None):
    ''' 
    '''
    
    commands.getoutput("open http://www.google.com")
