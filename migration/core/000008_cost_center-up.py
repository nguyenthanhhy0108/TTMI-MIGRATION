from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

cost_category_data = {
    "doctype": "DocType",
    "name": "Cost Category",
    "module": "Custom",
    "custom": 1,
    "fields": [
        {"fieldname": "group", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "cost_category_id", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "cost_category_name", "fieldtype": "Data", "reqd": 0},
        {"fieldname": "name_alias", "fieldtype": "Data", "reqd": 0},
        {"fieldname": "status", "fieldtype": "Select", "options": 'in_use\nnot_in_use'}
    ]
}

create_doctype(cost_category_data)

add_custom_field("Cost Center", "cost_center_id", "Data")
add_custom_field("Cost Center", "name_alias", "Data")
add_custom_field("Cost Center", "cost_category_1", "Link", link_to="Cost Category")
add_custom_field("Cost Center", "cost_category_2", "Link", link_to="Cost Category")
add_custom_field("Cost Center", "cost_category_3", "Link", link_to="Cost Category")
add_custom_field("Cost Center", "department", "Link", link_to="Department")

