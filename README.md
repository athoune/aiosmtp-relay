AIO SMTP Relay
==============

AsyncIO SMTP relay.

    client -> relay -> Postfix -> target

Relay will handle middlewares to do things with with email, like DKIM signing.


Test it
-------

Launch [MailHog](https://github.com/mailhog/MailHog), from the binary or [docker image](https://hub.docker.com/r/mailhog/mailhog/).

Install stuff in a venv

    python3 -m venv .

Launch the relay

    ./bin/python relay.py

Launch the client

    ./bin/python client.py

Watch stuff happening in the MailHog web UI : http://localhost:8025

Hack.

Licence
-------

3 terms BSD licence, ©2018 Mathieu Lecarme
