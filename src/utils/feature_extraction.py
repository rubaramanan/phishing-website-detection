import re
import urllib.request
from datetime import datetime
from urllib.error import HTTPError

import requests
from bs4 import BeautifulSoup

from src.utils.helper import get_path, get_port, get_host_name, get_scheme, get_domain_details


def has_ip(url):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
    return 1 if re.findall(ip_pattern, url) else 0


def has_at(url):
    return 1 if '@' in url else 0


def has_redirection(url):
    return 1 if '//' in get_path(url) else 0


def has_hypen(url):
    return 1 if '_' in url else 0


def shortining_service(url):
    services = (
        'bit.ly', 'goo.gl', 'shorte.st', 'go2l.ink', 'x.co', 'ow.ly', 't.co', 'tinyurl', 'tr.im', 'is.gd', 'cli.gs',
        'yfrog.com', 'migre.me', 'ff.im', 'tiny.cc', 'url4.eu', 'twit.ac', 'su.pr', 'twurl.nl', 'snipurl.com',
        'short.to', 'BudURL.com', 'ping.fm', 'post.ly', 'Just.as', 'bkite.com', 'snipr.com', 'fic.kr', 'loopt.us',
        'doiop.com', 'short.ie', 'kl.am', 'wp.me', 'rubyurl.com', 'om.ly', 'to.ly', 'bit.do', 't.co', 'lnkd.in',
        'db.tt', 'qr.ae', 'adf.ly', 'goo.gl', 'bitly.com', 'cur.lv', 'tinyurl.com', 'ow.ly', 'bit.ly', 'ity.im',
        'q.gs', 'is.gd', 'po.st', 'bc.vc', 'twitthis.com', 'u.to', 'j.mp', 'buzurl.com', 'cutt.us', 'u.bb',
        'yourls.org',
        'x.co', 'prettylinkpro.com', 'scrnch.me', 'filoops.info', 'vzturl.com', 'qr.net', '1url.com', 'tweez.me',
        'v.gd',
        'tr.im', 'link.zip.net')

    is_service_exsist = [True if service in url else False for service in services]
    return 1 if any(is_service_exsist) else 0


def has_non_standard_ports(url):
    standard_ports = [21, 22, 23, 80, 443, 445, 1433, 1521, 3306, 3389]
    return 1 if get_port(url) not in standard_ports else 0


def has_suffix_prefix(url):
    return 1 if '-' in get_host_name(url) else 0


def has_subdomains(url):
    domain = get_host_name(url)
    if not has_ip(url) and domain.count('.') > 2:
        return 1
    if domain.count('.') == 2:
        return 0
    return -1


def is_https(url):
    return 1 if 'https' == get_scheme(url) else 0


def url_length_long(url):
    if len(url) > 70:
        return 1
    if 70 > len(url) >= 51:
        return 0
    return -1


def is_active(url):
    try:
        response = requests.get(url)
        return 1 if response.status_code == 200 else 0
    except Exception as error:
        print(f"While processing {url=} got the {error=}")
        return 0


def web_traffic(url):
    try:
        rank = BeautifulSoup(urllib.request.urlopen(f"http://data.alexa.com/data?cli=10&dat=s&{url=}").read(),
                             "html.parser").find("REACH")['RANK']
        rank = int(rank)
        if not (rank < 100000):
            return -1
        return 0
    except HTTPError:
        return -1
    except Exception as e:
        print(e)
        return 1


def has_dns_record(url):
    dns_detail = get_domain_details(url)
    return 0 if dns_detail else 1


def is_sixmonth_old_dns(url):
    dns_details = get_domain_details(url)
    if not dns_details:
        return 1
    created_time = dns_details.creation_date
    expiry_date = dns_details.expiration_date

    if not created_time or not expiry_date:
        return 1

    if not isinstance(created_time, str) or not isinstance(expiry_date, str) \
            or isinstance(created_time, list) or isinstance(expiry_date, list):
        return -1

    created_time = datetime.strptime(created_time, '%Y-%m-%d')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
    age = abs(expiry_date - created_time).days / 30
    return 1 if age < 6 else 0
