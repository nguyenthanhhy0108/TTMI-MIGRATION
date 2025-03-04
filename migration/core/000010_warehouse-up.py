from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

add_custom_field("Warehouse", "warehouse_id", "Data") # Mã kho
add_custom_field("Warehouse", "name_alias", "Data") # Tên 2
add_custom_field("Warehouse", "have_location", "Check") # Vị trí
add_custom_field("Warehouse", "is_agent", "Check") # Đại lý
add_custom_field("Warehouse", "note", "Text") # Ghi chú

# company: Đơn vị
# warehouse_id: Mã kho
# warehouse_name: Tên kho
# name_alias: Tên khác
# have_location: Vị trí
# is_agent: Đại lý
# address_line_1: Địa chỉ
# phone_no: Điện thoại
# note: Ghi chú
# disabled: Trạng thái