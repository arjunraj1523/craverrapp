from urllib import urlopen
import re
def getIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    Ip_addr = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
    return Ip_addr


