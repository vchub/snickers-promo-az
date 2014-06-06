#!/usr/bin/python

import os


if __name__ == '__main__':
    # path to SDK
    DEV_SERVER_PATH = "../../lib/google_appengine_1.9.3/dev_appserver.py"
    PRJ_PATH = "."

    # PORT = "8084"
    # # HOST = "snickers.local-re-set.com"
    # HOST = "localhost"
    # cmnd_str = " ".join([DEV_SERVER_PATH, PRJ_PATH, '--host', HOST, '--port', PORT])
    # os.system(cmnd_str)

    cmnd_str = " ".join( [DEV_SERVER_PATH, PRJ_PATH, "--host localhost --port 8085 \
        --admin_host localhost --admin_port 8084"] )
    os.system(cmnd_str)
