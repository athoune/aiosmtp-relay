from smtplib import SMTP as Client


client = Client('127.0.0.1', 2025)
client.ehlo_or_helo_if_needed()
client.login('bob', 'sponge')
r = client.sendmail('a@example.com', ['b@example.com'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>

Hi Bart, this is Anne.
""")
