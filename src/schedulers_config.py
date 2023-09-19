from apscheduler.schedulers.background import BackgroundScheduler
from src.statistics.tasks import add_data


schedulers = BackgroundScheduler()
schedulers.add_job(add_data, 'interval', seconds=5)