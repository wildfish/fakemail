#!/bin/env python

import smtpd
import asyncore


class DebuggyServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from: {}'.format(peer))
        print('Message addressed from: {}'.format(mailfrom))
        print('Message addressed to  : {}'.format(rcpttos))
        print('Message length        : {}'.format(len(data)))
        print('---- BODY ----')
        try:
            print(data.split('Content-Transfer-Encoding: 7bit')[-1])
        except:
            print(data)
        print('-' * 20)
        print('')
        return


if __name__ == '__main__':
    server = DebuggyServer(('127.0.0.1', 2525), None)
    asyncore.loop()
