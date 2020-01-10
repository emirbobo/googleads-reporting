import os
import google.ads.google_ads.client
from googleads import adwords

import app_path
from accounts import auth, ad_config


def get_ads_api_client_service():

    if not os.path.exists(app_path.cur_path() + '/ggads_conf.yaml'):
    # if not os.path.exists(ad_config.get_config_path()):
        auth.init_ads_yaml()
    return (google.ads.google_ads.client.GoogleAdsClient
            .load_from_storage(ad_config.ads_conf_path))

def get_adwords_api_service():
    if not os.path.exists(app_path.cur_path() + '/adwords_conf.yaml'):
    # if not os.path.exists(ad_config.get_config_path()):
        auth.init_adwords_yaml()
    return (adwords.AdWordsClient.LoadFromStorage(ad_config.adwords_conf_path))
