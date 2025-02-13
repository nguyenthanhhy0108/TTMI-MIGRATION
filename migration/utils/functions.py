import requests
import json
from migration.config import ADMIN_HEADERS, ERPNEXT_DOMAIN, ERPNEXT_CUSTOM_FIELD_URL, ERPNEXT_CUSTOM_DOCTYPE_URL, ERPNEXT_CUSTOM_PERMISSION_URL
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
        logger.error(f"Fail when creating {fieldname} field. Detail: \n {response.text}")



def delete_custom_field(fieldname, doctype):
    delete_url = f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_FIELD_URL}/{doctype}-{fieldname}"

    response = requests.delete(delete_url, headers=ADMIN_HEADERS)

    if response.status_code == 202:
        logger.success(f"Field {fieldname} deleted successfully!")
    else:
        logger.error(f"Fail when deleting {fieldname} field. Detail: \n {response.text}")


def create_doctype(doctype_data):
    response = requests.post(f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_DOCTYPE_URL}", json=doctype_data, headers=ADMIN_HEADERS)

    if response.status_code == 200:
        logger.success(f"Doctype {doctype_data['name']} created successfully!")
    else:
        logger.error(f"Fail when creating {doctype_data['name']} field. Detail: \n {response.text}")


def add_permission(doctype, role, permissions):
    data = {
        "doctype": "Custom DocPerm",
        "parent": doctype,
        "parenttype": "DocType",
        "parentfield": "permissions",
        "role": role,
        **permissions
    }
    response = requests.post(f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_PERMISSION_URL}", json=data, headers=ADMIN_HEADERS)
    if response.status_code == 200:
        logger.success(f"Permissions added to {doctype} for role {role}!")
    else:
        logger.error(f"Failed to add permissions: {permissions} for {role}. Detail: \n {response.text}")


def delete_permission(doctype, role):
    try:
        response = requests.get(
            f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_PERMISSION_URL}?filters=[[\"parent\",\"=\",\"{doctype}\"],[\"role\",\"=\",\"{role}\"]]",
            headers=ADMIN_HEADERS
        )
        response.raise_for_status()
        permissions = response.json().get('data', [])

        if not permissions:
            logger.error(f"No permissions found for this role and doctype. Detail: \n {response.text}")
            return

        for perm in permissions:
            perm_name = perm.get('name')
            del_response = requests.delete(f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_PERMISSION_URL}/{perm_name}", headers=ADMIN_HEADERS)
            if del_response.status_code == 202:
                logger.success(f"Deleted permission {perm_name} for role {role} on {doctype}.")
            else:
                logger.error(f"Failed to delete permission {perm_name}. Detail: \n {response.text}")

    except requests.exceptions.RequestException as e:
        logger.error(f"An unexpected error occurred. Details: \n {e}")
    except ValueError as ve:
        print(f"❌ JSON decode error: {ve}")
        logger.error(f"JSON decode error. Details: \n {ve}")


def delete_doctype(doctype_name):
    response = requests.delete(f"{ERPNEXT_DOMAIN}{ERPNEXT_CUSTOM_DOCTYPE_URL}/{doctype_name}", headers=ADMIN_HEADERS)

    if response.status_code == 202:
        logger.success(f"Doctype {doctype_name} deleted successfully!")
    else:
        logger.error(f"Fail when deleting {doctype_name} doctype. Detail: \n {response.text}")
        print(response.text)