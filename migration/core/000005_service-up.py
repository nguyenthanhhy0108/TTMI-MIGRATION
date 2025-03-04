from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

service_data = {
    "doctype": "DocType",
    "name": "Service",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "service_code", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "service_name", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "name_alias", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "uom", "fieldtype": "Link", "options": "UOM"},
        {"fieldname": "revenue_account", "fieldtype": "Link", "options": "Account"},
        {"fieldname": "expense_account", "fieldtype": "Link", "options": "Account"},
        {"fieldname": "tax_category", "fieldtype": "Link", "options": "Tax Category"},
        {"fieldname": "cost_center", "fieldtype": "Link", "options": "Cost Center"},
        {"fieldname": "purchase_price", "fieldtype": "Float"},
        {"fieldname": "selling_price", "fieldtype": "Float"},
        {"fieldname": "status", "fieldtype": "Select", "options": "Active\nInactive"},
    ]
}

create_doctype(service_data)