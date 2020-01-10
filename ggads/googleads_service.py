# cost use ads
import google.ads.google_ads.client

from api import report_api

_DEFAULT_PAGE_SIZE = 1000


def get_last_7_day(client, customer_id, page_size):
    ga_service = client.get_service('GoogleAdsService', version='v2')

    query = ('SELECT campaign.id, campaign.name, ad_group.id, ad_group.name, '
             'ad_group_criterion.criterion_id, '
             'ad_group_criterion.keyword.text, '
             'ad_group_criterion.keyword.match_type, '
             'metrics.impressions, metrics.clicks, metrics.cost_micros '
             'FROM keyword_view WHERE segments.date DURING LAST_7_DAYS '
             'AND campaign.advertising_channel_type = \'SEARCH\' '
             'AND ad_group.status = \'ENABLED\' '
             'AND ad_group_criterion.status IN (\'ENABLED\', \'PAUSED\') '
             'ORDER BY metrics.impressions DESC '
             'LIMIT 50')

    response = ga_service.search(customer_id, query, page_size=page_size)

    try:
        for row in response:
            campaign = row.campaign
            ad_group = row.ad_group
            criterion = row.ad_group_criterion
            metrics = row.metrics

            print('Keyword text "%s" with match type "%d" and ID %d in ad '
                  'group "%s" with ID "%d" in campaign "%s" with ID %d had %s '
                  'impression(s), %s click(s), and %s cost (in micros) during '
                  'the last 7 days.'
                  % (criterion.keyword.text.value, criterion.keyword.match_type,
                     criterion.criterion_id.value,
                     ad_group.name.value, ad_group.id.value,
                     campaign.name.value, campaign.id.value,
                     metrics.impressions.value,
                     metrics.clicks.value, metrics.cost_micros.value))
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)


def get_report_30(client, customer_id):
    ga_service = client.get_service('GoogleAdsService', version='v2')

    query = ('SELECT CampaignId, AdGroupId, Impressions, Clicks,'
             ' Cost FROM ADGROUP_PERFORMANCE_REPORT WHERE AdGroupStatus IN [ENABLED, PAUSED] DURING LAST_7_DAYS')

    response = ga_service.search(customer_id, query, page_size=_DEFAULT_PAGE_SIZE)

    try:
        for row in response:
            campaign = row.campaign
            ad_group = row.ad_group
            criterion = row.ad_group_criterion
            metrics = row.metrics

            print('Keyword text "%s" with match type "%d" and ID %d in ad '
                  'group "%s" with ID "%d" in campaign "%s" with ID %d had %s '
                  'impression(s), %s click(s), and %s cost (in micros) during '
                  'the last 7 days.'
                  % (criterion.keyword.text.value, criterion.keyword.match_type,
                     criterion.criterion_id.value,
                     ad_group.name.value, ad_group.id.value,
                     campaign.name.value, campaign.id.value,
                     metrics.impressions.value,
                     metrics.clicks.value, metrics.cost_micros.value))
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)

def report_by_date(client,costomer_id, start_date, end_date):
    print('do get report')
    ga_service = client.get_service('GoogleAdsService', version='v2')

    query = ('SELECT campaign.id, campaign.name ,segments.date,metrics.impressions,'
             'metrics.average_cost ,metrics.clicks, metrics.average_cpc,'
             'metrics.average_cpv FROM campaign WHERE segments.date BETWEEN \'%s\' AND \'%s\' '
             'ORDER BY campaign.id' % (start_date, end_date))
    response = ga_service.search(costomer_id, query, page_size=1000)

    try:
        re = []
        for row in response:
            campaign = row.campaign
            # ad_group = row.ad_group
            # criterion = row.ad_group_criterion
            metrics = row.metrics
            r_dict = {}
            r_dict['campaign_id'] = campaign.id.value
            r_dict['campaign_name'] = campaign.name.value
            r_dict['metrics_impressions'] = metrics.impressions.value
            r_dict['metrics_clicks'] = metrics.clicks.value
            r_dict['metrics_average_cpc'] = metrics.average_cpc.value
            r_dict['metrics_average_cpv'] = metrics.average_cpv.value
            r_dict['metrics_average_cost'] = metrics.average_cost.value
            r_dict['date'] = row.segments.date.value

            print('date=%s, campaign.id=%s,campaign.name=%s,'
                  'metrics.impressions=%s,metrics.clicks=%s,metrics.average_cpc=%s,'
                  ' metrics.average_cpv=%s,metrics.average_cost=%s  '
                  % (
                     row.segments.date.value, campaign.id.value, campaign.name.value,
                     metrics.impressions.value,
                     metrics.clicks.value,
                     metrics.average_cpc.value,
                     metrics.average_cpv.value,
                     metrics.average_cost.value))
            re.append(r_dict)
        if re:
            report_api.report(str(re))
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)


def get_compaigns(client,customer_id):
    ga_service = client.get_service('GoogleAdsService', version='v2')

    query = ('SELECT campaign.id, campaign.name,campaign.campaign_budget FROM campaign '
             'ORDER BY campaign.id')

    results = ga_service.search(customer_id, query=query, page_size=_DEFAULT_PAGE_SIZE)

    try:
        for row in results:
            print('Campaign with ID %d and name "%s" and campaign.campaign_budget "%s"was found.'
                  % (row.campaign.id.value, row.campaign.name.value, row.campaign.campaign_budget.value))
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)

def get_ad_group(client,customer_id):
    ga_service = client.get_service('GoogleAdsService', version='v2')

    query = ('SELECT ad_group.id, ad_group.name,ad_group.target_cpa_micros FROM ad_group '
             'ORDER BY ad_group.id')

    results = ga_service.search(customer_id, query=query, page_size=_DEFAULT_PAGE_SIZE)

    try:
        for row in results:
            print('ad_group with ID %d and name "%s" and ad_group.target_cpa_micros "%s"was found.'
                  % (row.ad_group.id.value, row.ad_group.name.value, row.ad_group.target_cpa_micros.value))
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)

def get_ad(client,customer_id):
    ga_service = client.get_service('GoogleAdsService', version='v2')

    query = ('SELECT campaign.id, campaign.name, ad_group.id, ad_group.name, '
             'ad_group_criterion.criterion_id, '
             'ad_group_criterion.keyword.text, '
             'ad_group_criterion.keyword.match_type, '
             'metrics.impressions, metrics.clicks, metrics.cost_micros '
             'FROM keyword_view WHERE segments.date DURING LAST_7_DAYS '
             'AND campaign.advertising_channel_type = \'SEARCH\' '
             'AND ad_group.status = \'ENABLED\' '
             'AND ad_group_criterion.status IN (\'ENABLED\', \'PAUSED\') '
             'ORDER BY metrics.impressions DESC '
             'LIMIT 50')

    response = ga_service.search(customer_id, query, page_size=_DEFAULT_PAGE_SIZE)

    try:
        for row in response:
            campaign = row.campaign
            ad_group = row.ad_group
            criterion = row.ad_group_criterion
            metrics = row.metrics

            print('Keyword text "%s" with match type "%d" and ID %d in ad '
                  'group "%s" with ID "%d" in campaign "%s" with ID %d had %s '
                  'impression(s), %s click(s), and %s cost (in micros) during '
                  'the last 7 days.'
                  % (criterion.keyword.text.value, criterion.keyword.match_type,
                     criterion.criterion_id.value,
                     ad_group.name.value, ad_group.id.value,
                     campaign.name.value, campaign.id.value,
                     metrics.impressions.value,
                     metrics.clicks.value, metrics.cost_micros.value))
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)

