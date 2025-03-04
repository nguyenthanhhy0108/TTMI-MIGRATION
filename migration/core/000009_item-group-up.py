from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

add_custom_field("Item Group", "group_type", "Data") # Loại nhóm
add_custom_field("Item Group", "item_group_id", "Data") # Mã nhóm
add_custom_field("Item Group", "name_alias", "Data") # Tên 2
add_custom_field("Item Group", "status", "Select", options="in_use\nnot_in_use") # Trạng thái

# group_type: Loại nhóm
# item_group_id: Mã nhóm
# item_group_name: Tên phân nhóm
# name_alias: Tên 2
# status: Trạng thái

