import asyncio
import logging

from aiosmtpd.controller import Controller
from aiosmtplib import SMTP as Client


class RelayHandler:


    def __init__(self, hostname="127.0.0.1", port=1025):
        self.output_hostname = hostname
        self.output_port = port

    async def handle_DATA(self, server, session, envelope):
        print(envelope)
        print(dir(envelope))
        print(envelope.mail_options)
        print(envelope.rcpt_options)
        print(envelope.rcpt_tos)
        c = Client()
        await c.connect(hostname=self.output_hostname,
                        port=self.output_port)
        print(type(envelope.content))
        await c.sendmail(envelope.mail_from, envelope.rcpt_tos, envelope.content )
        return '250 Message accepted for delivery'


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    controller = Controller(RelayHandler(), loop=loop)
    print('listening')
    server = loop.create_server(controller.factory, host='0.0.0.0', port=2025)
    loop.run_until_complete(server)
    loop.run_forever()
