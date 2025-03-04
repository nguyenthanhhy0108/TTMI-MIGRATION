from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

add_custom_field("Department", "department_id", "Data")
add_custom_field("Department", "name_alias", "Data")
add_custom_field("Department", "note", "Data")
add_custom_field("Department", "department_type", "Select", 
                 options="Express\nKiosk\nKiosk Plus\nKhông phân loại")
