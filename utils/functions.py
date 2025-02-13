import requests
import json
from migration.config import ADMIN_HEADERS, ERPNEXT_DOMAIN, ERPNEXT_CUSTOM_FIELD_URL
from loguru import logger


def add_custom_field(dt, fieldname, fieldtype, reqd=0, default=None, options=None, link_to=None):
    data = {
        "dt": dt,
        "fieldname": fieldname,
        "fieldtype": fieldtype,
        "reqd": reqd,
        "default": default
    }
    
    if fieldtype == "Select" and options:
        data["options"] = options
    elif fieldtype == "Link" and link_to:
        data["options"] = link_to
    
    response = requests.post(f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_FIELD_URL}", headers=ADMIN_HEADERS, data=json.dumps(data))
    
    if response.status_code == 200:
        logger.success(f"Field {fieldname} created successfully!")
    else:
        logger.error(f"Fail when creating {fieldname} field")



def delete_custom_field(fieldname, doctype):
    delete_url = f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_FIELD_URL}/{doctype}-{fieldname}"

    response = requests.delete(delete_url, headers=ADMIN_HEADERS)

    if response.status_code == 202:
        logger.success(f"Field {fieldname} deleted successfully!")
    else:
        logger.error(f"Fail when deleting {fieldname} field")
