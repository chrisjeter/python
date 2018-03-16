import requests, ssl, logging
def email_alart(door_state):
	request_url = "https://api.mailgun.net/v3/mg.kansashunter.org/messages"
	api_key = "key-e7a8070aaf3649a7494f8333edf04e1b"
	fromaddr = "Safe Monitor  <SafeMonitor@kansashunter.org>"
	toaddr = ["cjeter+mailgun@gmail.com", "7856919005@txt.att.net"]
	open_body = "The door to the safe has been OPENED!"
	still_open_body = "The door to the safe has been OPENED \
						for longer than the TIMEOUT!"
	logging.captureWarnings(True)
	if (door_state == "open"):
		return requests.post(
        request_url,
        auth=("api", api_key),
        data={"from": fromaddr,
              "to": toaddr,
              "subject": "SAFE ALART",
              "text": open_body})
	elif (door_state == "still_open"):
		return requests.post(
		request_url,
		auth=("api", api_key),
		data={"from": fromaddr,
			  "to": toaddr,
              "subject": "SAFE ALART",
              "text": still_open_body})

email_alart("still_open")
