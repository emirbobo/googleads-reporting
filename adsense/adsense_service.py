from adsense.adsense_util_data_collator import DataCollator
from api import report_api

import argparse
from apiclient import sample_tools
from oauth2client import client

argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('--report_id', help='The ID of the saved report to generate')


def cron_report(argv, account_id, start_date, end_date, metrics, dimensions, sort):
    print('account_id=%s' % account_id)
    print('start_date=%s' % start_date)
    print('end_date=%s' % end_date)
    print('metrics=%s' % metrics)
    print('dimensions=%s' % dimensions)
    print('sort=%s' % sort)
    service, flags = sample_tools.init(
        argv, 'adsense', 'v1.4', __doc__, __file__, parents=[argparser],
        scope='https://www.googleapis.com/auth/adsense')

    try:
        r = service.accounts().reports().generate(
            accountId=account_id, startDate=start_date, endDate=end_date,
            metric=metrics,
            dimension=dimensions,
            sort=sort)
        result = r.execute()
        result = DataCollator([result]).collate_data()
        # report(result)
        re = []
        for row in result['rows']:
           r_dict = {}
           i = 0
           for header in result['headers']:
                if row[i] is not None:
                    r_dict[header['name']] = row[i]
                else:
                    r_dict[header['name']] = ''
                i = i + 1
           re.append(r_dict)
        print('Report from %s to %s success!' % (result['startDate'], result['endDate']))
        if re:
            report_api.report(str(re))
    except client.AccessTokenRefreshError:
        print('The AccessTokenRefreshError')
