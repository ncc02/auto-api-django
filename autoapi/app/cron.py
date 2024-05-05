# Create your views here.
import os
from django_cron import CronJobBase, Schedule
from datetime import datetime

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.my_cron_job'    # a unique code

    def do(self):
        # Create and write to the file
        with open('./test.txt', "w") as file:
            file.write("This is a new file created at now ")