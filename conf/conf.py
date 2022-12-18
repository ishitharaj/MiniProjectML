# for logging and dynaconf
import logging
from dynaconf import Dynaconf

logger = logging
logging.basicConfig(level=logging.INFO)

settings = Dynaconf(settings_file=["conf/configs.toml"],
                    environments=True,
                    load_dotenv=True,
                    )
