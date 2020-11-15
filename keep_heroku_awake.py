import os
import time
import logging
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

HEROKU_URL="https://oolala.herokuapp.com"

sched = BlockingScheduler()

@sched.scheduled_job('cron', minute="*")
def keep_heroku_awake():
    res = requests.get(HEROKU_URL)
    if res.status_code != 200:
        logging.ERROR("heroku is dead")
    else:
        pass

if __name__ == "__main__":
    logging.getLogger('apscheduler')\
           .setLevel(logging.DEBUG)
    sched.start()
