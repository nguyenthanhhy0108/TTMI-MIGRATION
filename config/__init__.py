import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

ADMIN_HEADERS = {
    "Authorization": f"token {API_KEY}:{API_SECRET}",
    "Content-Type": "application/json"
}

ERPNEXT_DOMAIN = os.getenv("ERPNEXT_DOMAIN")
ERPNEXT_CUSTOM_FIELD_URL = os.getenv("ERPNEXT_CUSTOM_FIELD_URL")