import urllib.parse
import urllib.request
import json
import pushover

app_id = APP_ID_HERE
app_key = APP_KEY_HERE
URL = 'https://api.tfl.gov.uk/Line/211/Status?detail=False&app_id=' + app_id + '&app_key=' + app_key

request = urllib.request.Request(URL)
make_request = urllib.request.urlopen(request)
raw_response = make_request.read().decode('utf8')
parsed_response = json.loads(raw_response)

if len(parsed_response) > 0:
    for incidents in parsed_response[0]['lineStatuses']:
        notification = pushover.sendPush('Bus disruption', incidents['disruption']['description'])
