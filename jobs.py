from apscheduler.schedulers.blocking import BlockingScheduler
# from home.management.commands.starter import test
sched = BlockingScheduler()
import os, sys
sys.path.append('C:/Users/BEST BUY/Documents/django/stockmarketwebsite/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockmarketwebsite.settings'
import django
django.setup()
import subprocess

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='11', minute='10', timezone='America/New_York')
def update_a():
    # print(os.popen('py manage.py starter').())
    command = "python manage.py starter"  # the shell command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    #Launch the shell command:
    output = process.communicate()
    print(output[0])
sched.start()
