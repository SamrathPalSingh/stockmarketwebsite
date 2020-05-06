from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from stockUpdater import update
def start():
    scheduler = BlockingScheduler()
    #scheduler.add_job(update.updateStocks, 'interval', minutes=1)
    scheduler.add_job(update.updateStocks, 'interval', minutes=2)
    scheduler.start()
