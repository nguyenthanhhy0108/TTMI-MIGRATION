from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("7. Department up...")
add_custom_field("Department", "department_id", "Data") # Mã bộ phận
add_custom_field("Department", "name_alias", "Data") # Tên khác
add_custom_field("Department", "note", "Data") # Ghi chú
add_custom_field("Department", "department_type", "Select", # Loại cửa hàng 
                 options="Express\nKiosk\nKiosk Plus\nKhông phân loại")
