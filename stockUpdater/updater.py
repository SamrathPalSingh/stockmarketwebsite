from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from stockUpdater import update
def start():
    scheduler = BackgroundScheduler()
    #scheduler.add_job(update.updateStocks, 'interval', minutes=1)
    scheduler.add_job(update.updateStocks, 'interval', seconds=10)
    scheduler.start()
