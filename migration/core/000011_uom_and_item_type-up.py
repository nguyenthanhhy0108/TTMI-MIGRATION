from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

###################### UOM ######################

add_custom_field("UOM", "uom_id", "Data") # Mã đơn vị
add_custom_field("UOM", "name_alias", "Data") # Tên khác
add_custom_field("UOM", "uom_2", "Data") # Đơn vị tính 2

# uom_id: Mã đơn vị
# uom_name: Tên đvt
# name_alias: Tên khác
# uom_2: Đơn vị tính 2
# enabled: Trạng thái

###################### Item Type ######################

item_type_data = {
    "doctype": "DocType",
    "name": "Item Type",
    "module": "Custom",
    "custom": 1,
    "fields": [
        {"fieldname": "item_type_id", "fieldtype": "Data", "reqd": 1}, # Mã loại vật tư
        {"fieldname": "item_type_name", "fieldtype": "Data", "reqd": 1}, # Tên loại vật tư
        {"fieldname": "name_alias", "fieldtype":"Data", "reqd":0}, # Tên khác
        {"fieldname": "status", "fieldtype": "Select", "options": 'in_use\nnot_in_use'}, # Trạng thái
        {"fieldname": "warehouse_account", "fieldtype": "Link", "options": "Account"}, # Tk kho
        {"fieldname": "revenue_account", "fieldtype": "Link", "options": "Account"}, # Tk doanh thu
        {"fieldname": "cost_account", "fieldtype": "Link", "options": "Account"}, # Tk giá vốn
        {"fieldname": "discount_account", "fieldtype": "Link", "options": "Account"}, # Tk chiết khấu
        {"fieldname": "promotion_account", "fieldtype": "Link", "options": "Account"}, # Tk khuyến mãi
        {"fieldname": "return_account", "fieldtype": "Link", "options": "Account"}, # Tk trả lại
        {"fieldname": "wip_account", "fieldtype": "Link", "options": "Account"}, # Tk sản phẩm dở dang
        {"fieldname": "material_account", "fieldtype": "Link", "options": "Account"}, # Tk chi phí NVL        
    ]
}

create_doctype(item_type_data)

# item_type_id: Mã loại vật tư
# item_type_name: Tên loại vật tư
# name_alias: Tên khác
# status: Trạng thái
# warehouse_account: Tk kho
# revenue_account: Tk doanh thu
# cost_account: Tk giá vốn
# discount_account: Tk chiết khấu
# promotion_account: Tk khuyến mãi
# return_account: Tk trả lại
# wip_account: Tk sản phẩm dở dang
# material_account: Tk chi phí NVL
