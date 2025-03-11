from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger


logger.info("1. Customer up...")
order_source_data = {
    "doctype": "DocType",
    "name": "Order Source",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "source_id", "fieldtype": "Data", "reqd": 1}, # Mã nguồn đơn
        {"fieldname": "source_name", "fieldtype": "Data", "reqd": 1}, # Tên nguồn đơn
        {"fieldname": "note", "fieldtype":"Data", "reqd":0}, # Ghi chú
        {"fieldname": "status", "fieldtype": "Select", "options": 'in_use\nnot_in_use'} # Trạng thái
    ]
}

create_doctype(order_source_data)

add_custom_field('Customer Group', 'group_id', 'Data')  # Mã nhóm
add_custom_field('Customer Group', 'group_alias', 'Data') # Tên khác
add_custom_field('Customer Group', 'status', 'Select', options='in_use\nnot_in_use')

add_custom_field('Customer', 'customer_code', 'Data') # Mã khách hàng
add_custom_field('Customer', 'is_customer', 'Check') # Khách hàng
add_custom_field('Customer', 'is_supplier', 'Check') # Nhà cung cấp
add_custom_field('Customer', 'name_alias', 'Data') # Tên khác
add_custom_field('Customer', 'address', 'Data') # Địa chỉ
add_custom_field('Customer', 'contact_person', 'Data') # Người liên hệ
add_custom_field('Customer', 'employee', 'Link', link_to='Employee') # Nhân viên bán hàng
add_custom_field('Customer', 'customer_account', 'Link', link_to='Account') # Tài khoản ngầm định
add_custom_field('Customer', 'customer_group_1', 'Link', link_to='Customer Group') # Nhóm 1
add_custom_field('Customer', 'customer_group_2', 'Link', link_to='Customer Group') # Nhóm 2
add_custom_field('Customer', 'customer_group_3', 'Link', link_to='Customer Group') # Nhóm 3
add_custom_field('Customer', 'region', 'Data') # Khu vực
add_custom_field('Customer', 'phone_number', 'Data') # Điện thoại
add_custom_field('Customer', 'fax_number', 'Data') # Fax
add_custom_field('Customer', 'email', 'Data') # Thư
add_custom_field('Customer', 'note', 'Data') # Ghi chú
add_custom_field('Customer', 'date_of_birth', 'Date') # Ngày sinh
add_custom_field('Customer', 'legal_representative', 'Data') # Người đại diện pháp luật
add_custom_field('Customer', 'position', 'Data') # Chức vụ
add_custom_field('Customer', 'bank_account_number', 'Data') # Số tài khoản
add_custom_field('Customer', 'bank_name', 'Data') # Tên ngân hàng
add_custom_field('Customer', 'bank_branch', 'Data') # Chi nhánh
add_custom_field('Customer', 'bank_province_city', 'Data') # Tỉnh thành
add_custom_field('Customer', 'shipping_address', 'Data') # Địa chỉ giao hàng
add_custom_field('Customer', 'operational_field', 'Data') # Địa chỉ giao hàng
add_custom_field('Customer', 'use_e_invoice', 'Select', options='Yes\nNo') # Sử dụng hđ điện tử
add_custom_field('Customer', 'e_invoice_email', 'Data') # Thư nhận HĐĐT
add_custom_field('Customer', 'e_invoice_representative', 'Data') # Nguời đại diện
add_custom_field('Customer', 'order_source_table', 'Table', options='Order Source') # Nguồn đơn
