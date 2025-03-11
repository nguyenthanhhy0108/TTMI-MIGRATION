from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("8. Cost Center up...")
cost_category_data = {
    "doctype": "DocType",
    "name": "Cost Category",
    "module": "Custom",
    "custom": 1,
    "fields": [
        {"fieldname": "group", "fieldtype": "Data", "reqd": 1}, # Nhóm phí 1, Nhóm phí 2, Nhóm phí 3
        {"fieldname": "cost_category_id", "fieldtype": "Data", "reqd": 1}, # Mã nhóm
        {"fieldname": "cost_category_name", "fieldtype": "Data", "reqd": 0}, # Tên nhóm
        {"fieldname": "name_alias", "fieldtype": "Data", "reqd": 0}, # Tên khác
        {"fieldname": "status", "fieldtype": "Select", "options": 'in_use\nnot_in_use'} # Trạng thái
    ]
}

create_doctype(cost_category_data) # Nhóm phí

add_custom_field("Cost Center", "cost_center_id", "Data") # Mã phí
add_custom_field("Cost Center", "name_alias", "Data") # Tên khác
add_custom_field("Cost Center", "cost_category_1", "Link", link_to="Cost Category") # Nhóm phí 1
add_custom_field("Cost Center", "cost_category_2", "Link", link_to="Cost Category") # Nhóm phí 2
add_custom_field("Cost Center", "cost_category_3", "Link", link_to="Cost Category") # Nhóm phí 3
add_custom_field("Cost Center", "department", "Link", link_to="Department") # Bộ phận

# cost_center_name: Tên phí
# disabled: Trạng thái

