#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.factory import create_app
from api.utils.config import DevelopmentConfig, ProductionConfig
import os


use_config = {
    'PROD': ProductionConfig,
    'DEV': DevelopmentConfig,
}
use_reloader = {
    'PROD': True
}

config = use_config.get(
    os.environ.get('WORK_ENV', 'DEV')
)

app = create_app(config)

if __name__ == '__main__':
    use_reloader = use_reloader.get(
        os.environ.get('WORK_ENV', 'DEV')
    )
    app.run(port=5000, host="0.0.0.0", use_reloader=use_reloader)
