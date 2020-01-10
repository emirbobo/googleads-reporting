import app_path

adwords_conf_path = app_path.cur_path() + '/adwords_conf.yaml'
ads_conf_path = app_path.cur_path() + '/ggads_conf.yaml'
ads_conf_base = app_path.cur_path() + '/base_dev.yaml'

# def init_env(env):
#     if env is None or env == '':
#         env = 'dev'
#     global config_file_path
#     if config_file_path is None or len(config_file_path) == 0:
#         config_file_path = app_path.cur_path() + '/base_%s.yaml' % env
#
#
# def get_config_path():
#     return config_file_path
