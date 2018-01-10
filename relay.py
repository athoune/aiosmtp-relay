import asyncio
import logging

from aiosmtpd.controller import Controller
from aiosmtplib import SMTP as Client


class RelayHandler:

    async def handle_DATA(self, server, session, envelope):
        print(envelope)
        print(dir(envelope))
        return '250 Message accepted for delivery'


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    controller = Controller(RelayHandler(), loop=loop)
    print('listening')
    server = loop.create_server(controller.factory, host='0.0.0.0', port=8025)
    loop.run_until_complete(server)
    loop.run_forever()
