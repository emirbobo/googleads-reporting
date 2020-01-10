
import requests


def report(data):
    print('start report data......%s' % data)
    postdata = {'data': data, 'adPlatfrom': 'google'}
    r = requests.post('https://xxxxxxx.com/doReport', data=postdata)
    print('report done .', r.text)