from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

service_data = {
    "doctype": "DocType",
    "name": "Service",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "service_code", "fieldtype": "Data", "reqd": 1}, # Mã dịch vụ
        {"fieldname": "service_name", "fieldtype": "Data", "reqd": 1}, # Tên dịch vụ
        {"fieldname": "name_alias", "fieldtype": "Data", "reqd": 1}, # Tên khác
        {"fieldname": "uom", "fieldtype": "Link", "options": "UOM"}, # Đvt
        {"fieldname": "revenue_account", "fieldtype": "Link", "options": "Account"}, # Tk doanh thu
        {"fieldname": "expense_account", "fieldtype": "Link", "options": "Account"}, # Tk chi phí
        {"fieldname": "tax_category", "fieldtype": "Link", "options": "Tax Category"}, # Mã thuế
        {"fieldname": "cost_center", "fieldtype": "Link", "options": "Cost Center"}, # Mã phí
        {"fieldname": "purchase_price", "fieldtype": "Float"}, # Giá mua
        {"fieldname": "selling_price", "fieldtype": "Float"}, # Giá bán
        {"fieldname": "status", "fieldtype": "Select", "options": "Active\nInactive"}, # Trạng thái
    ]
}

create_doctype(service_data)