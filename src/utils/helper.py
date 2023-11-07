from urllib.parse import urlparse

import whois


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
