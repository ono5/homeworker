# ログの設定ファイル

import os
import logging.config

from .common import LOG_PATH


def setup_logging(sub_folder: str, filename: str) -> None:
    """Setting Logging"""

    full_log_path = LOG_PATH + sub_folder

    if os.path.isdir(full_log_path):
        pass
    else:
        os.mkdir(full_log_path)

    full_file_path = full_log_path + '/' + filename

    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'customFormat': {
                'format': '%(asctime)s %(levelname)s [%(funcName)s] %(message)s'
            },
        },
        'handlers': {
            'fileStreamHandler': {
                'class': 'logging.FileHandler',
                'formatter': 'customFormat',
                'level': logging.DEBUG,
                'filename': f'{full_file_path}',
            },
        },

        'loggers': {
            'writeLogging': {
                'handlers': ['fileStreamHandler'],
                'level': logging.DEBUG,
                'propagate': 0
            },
        }
    })
