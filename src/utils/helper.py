import re
from urllib.parse import urlparse
import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import whois
from datetime import datetime

from src.utils.feature_extraction import has_ip, has_at, has_redirection, has_hypen, shortining_service, \
    has_non_standard_ports, has_suffix_prefix, has_subdomains, is_https, url_length_long, is_active, web_traffic, \
    has_dns_record, is_sixmonth_old_dns


def get_scheme(url):
    return urlparse(url).scheme


def get_domain(url):
    return urlparse(url).netloc


def get_host_name(url):
    return urlparse(url).hostname


def get_port(url):
    return urlparse(url).port


def get_path(url):
    return urlparse(url).path


def get_domain_details(url):
    try:
        return whois.whois(get_domain(url))
    except Exception as e:
        print(e)
        return None


def gen_features(df):
    funcs = [has_ip, has_at, has_hypen, has_redirection, has_non_standard_ports, has_subdomains, has_suffix_prefix,
             is_https, url_length_long, shortining_service,
             is_active, web_traffic, has_dns_record, is_sixmonth_old_dns]
    for func in funcs:
        df[func.__name__] = df.url.apply(func)
    return df
