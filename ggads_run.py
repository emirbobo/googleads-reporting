import json
import sys
import os
import datetime
from accounts import api_client_service, ad_config
from ggads import googleads_service

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import frozen_dir

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
appPath = frozen_dir.app_path()
ads_conf = ''

with open(appPath + '/ggads_run.conf', 'r', encoding='utf-8') as fileJson:
    ads_conf = json.load(fileJson)

env = 'dev'
for i in range(len(sys.argv)):
    # print('sys.argv[', i, ']:', sys.argv[i])
    if sys.argv[i].find('segment=') >= 0:
        segment = sys.argv[i][len('segment='):]
        # break
    if sys.argv[i].find('env=') >= 0:
        env = sys.argv[i][len('env='):]


def getDate(days):
    start = datetime.date.today() + datetime.timedelta(days)
    return str(start)


if __name__ == '__main__':
    start = getDate(ads_conf['days'])
    end = getDate(0)
    google_ads_client = api_client_service.get_ads_api_client_service()
    googleads_service.report_by_date(google_ads_client, ads_conf['customer_id'], start, end)

