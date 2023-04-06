from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests


def sessionid_get(url = "https://oficinajudicialvirtual.pjud.cl"):
    session = requests.Session()
    response = session.get(url)
    cookies = session.cookies.get_dict()

    sessionid = cookies['PHPSESSID']
    return sessionid
