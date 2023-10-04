import logging

import config

logger = logging.getLogger(config.settings.logger_name_prefix + __name__)


# Introduce a db client here
# db_client =

async def check_db_connection():
    # global db_client
    # try:
    #     logger.info(db_client.ready().status)
    # except ReadTimeoutError as e:
    #     logger.error(e)
    pass


async def close_db_connection():
    # global db_client
    # logger.info("Closing database connection")
    # db_client.close()

    pass
