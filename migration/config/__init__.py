import os
from dotenv import load_dotenv

load_dotenv()

ERPNEXT_DOMAIN = os.getenv("ERPNEXT_DOMAIN")
ERPNEXT_CUSTOM_FIELD_URL = os.getenv("ERPNEXT_CUSTOM_FIELD_URL")
ERPNEXT_CUSTOM_DOCTYPE_URL = os.getenv("ERPNEXT_CUSTOM_DOCTYPE_URL")
ERPNEXT_CUSTOM_PERMISSION_URL = os.getenv("ERPNEXT_CUSTOM_PERMISSION_URL")

from migration.utils.auth import get_sid

def get_admin_headers():
    return {
        "Cookie": f"full_name=Administrator; sid={get_sid()}; system_user=yes; user_id=Administrator; user_image="
    }

ADMIN_HEADERS = get_admin_headers()