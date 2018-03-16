def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/mg.kansashunter.org/messages",
        auth=("api", "key-e7a8070aaf3649a7494f8333edf04e1b"),
        data={"from": "Safe Monitor <safe@kansashunter.org>",
              "to": "Chris Jeter <cjeter@gmail.com>",
              "subject": "Hello Chris Jeter",
              "text": "Test Message."})
