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
		if fileName=='ffmpegContainer.sh':
			continue
		fileNameWithoutExtension = os.path.splitext(fileName)[0]
		tmpFileName = os.rename(fileName, fileNameWithoutExtension + tmpExtension)
		tmpFileName
		subprocess.call('/app/ffmpegContainer.sh')
		os.remove(fileNameWithoutExtension + tmpExtension)
		shutil.move(('/app/videos/' + fileNameWithoutExtension + '.mp4'), ('/app/processed/' + fileNameWithoutExtension + '.mp4'))


scheduler = BlockingScheduler()
scheduler.add_job(convertFFmpeg, 'interval', seconds=6, max_instances=1)
scheduler.start()
