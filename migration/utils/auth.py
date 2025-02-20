import requests
from migration.config import ERPNEXT_DOMAIN
from loguru import logger


def get_sid() -> str:
    USERNAME = "Administrator"
    PASSWORD = "admin"

    login_url = f"{ERPNEXT_DOMAIN}/api/method/login"
    session = requests.Session()

    payload = {
        "usr": USERNAME,
        "pwd": PASSWORD
    }

    response = session.post(login_url, data=payload)

    if response.status_code == 200:
        sid = session.cookies.get("sid")
        logger.success(f"Creating SID successfully!")
        return sid
    else:
        logger.error(f"Creating SID fail!")
        return ""
