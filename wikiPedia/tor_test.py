import socks
import socket
from urllib.request import urlopen
import requests
socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050)
socket.socket=socks.socksocket
ret=urlopen('http://icanhazip.com')
print(ret.read())