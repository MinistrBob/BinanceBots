#!/usr/bin/env python

import logging
import os
import pprint
import time
from binance.spot import Spot
# from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError



# datefmt="%Y-%m-%d %H:%M:%S UTC %s"
# s = time.strftime(datefmt, ct)

# logging.Formatter.converter = time.gmtime  # date time in GMT/UTC
logging.basicConfig(
    level=logging.DEBUG,
#    filename=log_file,
    format="%(asctime)s|%(msecs)03d|%(levelname)5s|%(module)16s| %(message)s",
    datefmt="%Y-%m-%d|%H:%M:%S",
)

# config_logging(logging, logging.DEBUG, format="%(asctime)s|%(msecs)03d|%(levelname)8s|%(module)16s| %(message)s",
#                datefmt="%Y-%m-%d|%H:%M:%S", utc=False)
# Get environment variables
BAK = os.getenv('bak')
BSK = os.environ.get('bsk')
logging.info(BAK)
logging.info(BSK)
# logging.info('test')
# logging.info(BAK)
# exit()

client = Spot()
logging.info(f"time={client.time()}")

client = Spot(key=BAK, secret=BSK)
# Get account information
account = pprint.pformat(client.account())
logging.info(f"account=\n{account}")

try:
    response = pprint.pformat(client.fiat_order_history(0))
    logging.info(f"response=\n{response}")
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
