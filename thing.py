import httplib, urllib

temperature = "90"
humidity = "30"
def update_thing():
    global temperature
    params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'key' : 'WXM1DA1C87VPHTIZ'})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPSConnection("api.thingspeak.com:443")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print temperature
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
