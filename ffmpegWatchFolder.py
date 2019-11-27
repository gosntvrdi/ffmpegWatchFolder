import os
import time
import datetime
import subprocess
import sys
import shutil
from apscheduler.schedulers.blocking import BlockingScheduler


dirname = os.path.dirname(__file__)
my_path = os.path.abspath(os.path.dirname(__file__))
absolute = os.path.abspath(os.getcwd())
tmpExtension = '.tmp'
videos = '/app/videos'
app = '/app'
processed = '/app/processed'

def convertFFmpeg():
	for fileName in os.listdir(videos):
		os.chdir(videos)
		fileNameWithoutExtension = os.path.splitext(fileName)[0]
		tmpFileName = os.rename(fileName, fileNameWithoutExtension + tmpExtension)
		tmpFileName
		os.chdir(app)
		subprocess.call('./ffmpegContainer.sh')
		os.chdir(videos)
		os.remove(fileNameWithoutExtension + tmpExtension)
		shutil.move(fileName, ('/app/processed/' + fileName))


scheduler = BlockingScheduler()
scheduler.add_job(convertFFmpeg, 'interval', seconds=120, max_instances=1)
scheduler.start()