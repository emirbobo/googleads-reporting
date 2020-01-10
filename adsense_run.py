

#'LAST_7_DAYS'
import json
import os
import sys

import frozen_dir

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
appPath = frozen_dir.app_path()
adsense_conf = ''

with open(appPath + '/adsense_run.conf', 'r', encoding='utf-8') as fileJson:
    adsense_conf = json.load(fileJson)

from adsense import adsense_service

import datetime

def getDate(days):
    start = datetime.date.today() + datetime.timedelta(days)
    return str(start)


if __name__ == '__main__':
    start = getDate(adsense_conf['days'])
    end = getDate(-1)
    account_id = adsense_conf['account_id']
    metrics = adsense_conf['metrics']
    dimensions = adsense_conf['dimensions']
    sort = adsense_conf['sort']
    adsense_service.cron_report(sys.argv, account_id, start, end, metrics, dimensions, sort)
