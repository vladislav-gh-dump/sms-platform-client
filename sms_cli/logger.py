import logging


logging.basicConfig(
    filename="sms_cli.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

logger = logging.getLogger(__name__)
