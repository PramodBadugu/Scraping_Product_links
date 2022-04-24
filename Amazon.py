import requests
import json
import re
import time, random
from copy import deepcopy
from lxml import html
class listing:

    def __init__(self, crawl_options):
        self.product_type = "retail_product"
        self.crawl_options = crawl_options

        self.append = '&page='
        self.USER_AGENTS = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        ]

        self.headers = {
            'authority': 'www.amazon.ca',
            'cache-control': 'max-age=0',
            'rtt': '100',
            'downlink': '9.05',
            'ect': '4g',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'service-worker-navigation-preload': 'true',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': 'session-id=134-6885613-0530462; session-id-time=2082787201l; i18n-prefs=CAD; ubid-acbca=135-2038594-9626323; session-token=tQeg6DlykTbbJjJJPxGc0rhdI+gf/tlXVcrtYgb7bD20Kdkp3p/nXx8D19lj+dFuHQ2nIo3r0LQSnQ3w+b5Lt1wMhzI/koj5Q6zucfm7VpK8NqylzVvgb31PDhmCvWlEjbht0CGK1MkJ5IJ4Z6HXvmmI2eqsJoVB7vL4/EgB+OCYp1HCYbp1OmWgHk2AxUMi; csm-hit=tb:s-YC1ZZ058MT5S0DDCGZNN|1646149437544&t:1646149438679&adb:adblk_no',
        }

    def url_bridge(self, url):
        proxy_list = [{"http": "http://10.3.6.73:24009","https": "http://10.3.6.73:24009"}]
        resp = requests.get(url, headers=self.headers)#, proxies = proxy_list, verify= False)
        return resp

    def bridge_extraction(self, resp, all_extraction):
        response = html.fromstring(resp.content)
        try:
            all_data = []
            try :
                data = response.xpath('//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]//@href')
            except :
                data = ""
            if data:
                for i in data:
                    dit = {
                        'url': "https://www.amazon.in/"+i
                    }
                    # print(dit)
                    all_data.append(dit)
                return all_data
            else :
                pass
        except Exception as e:
            return [{}]
l = listing({})
resp = l.url_bridge("https://www.amazon.in/s?k=Mushroom&crid=1VFBK74FIN75C&sprefix=mushroom%2Caps%2C324&ref=nb_sb_noss_1")
data = l.bridge_extraction(resp, [])
print(json.dumps(data))