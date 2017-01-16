import urllib.request
import urllib.parse

token = PUSHOVER_TOKEN_HERE
user = PUSHOVER_USER_ID_HERE
device = PUSHOVER_DEVICE_HERE

def sendPush(title, message):
    data = urllib.parse.urlencode({'token': token, 'user': user, 'device': device,
                                   'title': title, 'message': message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.pushover.net/1/messages.json")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return fr
