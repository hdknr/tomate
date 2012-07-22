import os
import sys 
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

APP_DIR=os.path.dirname(__file__)
LOG_FILE="/Users/hide/Desktop/tomate.log"  #: celery worker logfile 
PID_FILE="/Users/hide/Desktop/tomate.pid"  #: celery worker PID file
NODE="celery"           #: celery = default node
LOG_LEVEL="DEBUG"       #: celery log level

# Unfortunately, -B/--beat options doesn't seem to work
# - http://docs.celeryproject.org/en/latest/faq.html#the-b-beat-option-to-celeryd-doesn-t-work 
#
def configure(args):
    ''' return django-celery parameter for specified args

        - args[0] : tomate.py
        - args[1] : path this django project application 
        - args[2] : command
    '''

    if  len(args) < 3 or args[2] == "start" :
        #: start worker
        return [ args[0], "celeryd",
                "--loglevel=%s" % LOG_LEVEL,
                "--pidfile=%s" % PID_FILE, 
                "--logfile=%s" % LOG_FILE ,
                "--scheduler=djcelery.schedulers.DatabaseScheduler",
            ]   

    if  len(args) >2 and args[2] == "stop":
        #: stop worker
        return [ args[0],"celeryd_multi",
                 "stop",NODE,
                "--pidfile=%s" % PID_FILE, 
            ]   
