from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("4. Employee up...")
province_data = {
    "doctype": "DocType",
    "name": "Province",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "province_id", "fieldtype": "Data", "reqd": 1}, # Mã tỉnh thành
        {"fieldname": "province_name", "fieldtype": "Data", "reqd": 1}, # Tên tỉnh thành
    ]
}

create_doctype(province_data)


add_custom_field('Employee', 'birthplace', 'Data') # Nơi sinh
add_custom_field('Employee', 'tax_code', 'Data') # Mã số thuế TNCN
add_custom_field('Employee', 'citizen_identification_number', 'Data') # Số CMND
add_custom_field('Employee', 'issue_date', 'Date') # Ngày cấp
add_custom_field('Employee', 'province', 'Link', link_to='Province') # Nơi cấp
add_custom_field('Employee', 'is_sales_agent', 'Check') # Bán hàng
add_custom_field('Employee', 'is_purchasing_agent', 'Check') # Mua hàng
add_custom_field('Employee', 'is_debt_or_provisional', 'Check') # Công nợ/tạm ứng

# employee: Mã nhân viên
# first_name: Họ và tên
# designation: Chức vụ
# department: Bộ phận
# gender: Giới tính
# date_of_birth: Ngày sinh
# current_address: Địa chỉ thường trú
# cell_number: Điện thoại
# personal_email: Email
# Bank A/C No.: Số thẻ/Ngân hàng
# status: Trạng thái
