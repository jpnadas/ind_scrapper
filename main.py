import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import subprocess

url = 'https://ind.nl/en/Pages/Making-an-appointment-online.aspx'

response = requests.get(url)

if response.status_code == 200:
    print("ok")
    # subprocess.Popen(["/usr/bin/notify-send", "-u", "critical", "IND site online"])
    soup = BeautifulSoup(response.text, "html.parser")

    st = soup.find_all("strong")

    notify_str = st[1].contents[0]

    if "The IND desks can be visited for urgent matters by appointment only up to and including\xa028 April. You\xa0can only make an appointment at an IND desk to collect\xa0your first regular residence document. The condition for this is that you have travelled to the Netherlands with a Provisional Residence Permit (mvv). And that you need a residence document for example to apply for health insurance, or to register in the Personal Records Database (BRP) at your town hall (gemeente). Does this apply to you? Make an appointment to visit an IND desk by calling the IND's information line at 088 043 0430 (standard charges apply). From abroad, please call +31 88 043 0430. You cannot make this appointment" not in notify_str:
        subprocess.Popen(["/usr/bin/notify-send", "-u", "critical", notify_str])
    else:
        subprocess.Popen(["/usr/bin/notify-send", "-u", "critical", "No change to the IND message."])
else:
    subprocess.Popen(["/usr/bin/notify-send", "-u", "critical", "IND site offline"])


