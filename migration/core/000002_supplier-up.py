from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("2. Supplier up...")
add_custom_field('Supplier', 'supplier_code', 'Data') # Mã nhà cung cấp
add_custom_field('Supplier', 'is_customer', 'Check') # Khách hàng
add_custom_field('Supplier', 'is_supplier', 'Check') # Nhà cung cấp
add_custom_field('Supplier', 'name_alias', 'Data') # Tên khác
add_custom_field('Supplier', 'address', 'Data') # Địa chỉ
add_custom_field('Supplier', 'contact_person', 'Data') # Người đại diện
add_custom_field('Supplier', 'employee', 'Link', link_to='Employee') # Nhân viên bán hàng
add_custom_field('Supplier', 'supplier_group_1', 'Link', link_to='Supplier Group') # Nhóm 1
add_custom_field('Supplier', 'supplier_group_2', 'Link', link_to='Supplier Group') # Nhóm 2
add_custom_field('Supplier', 'supplier_group_3', 'Link', link_to='Supplier Group') # Nhóm 3
add_custom_field('Supplier', 'payment_term', 'Link', link_to='Payment Term') # Mã th.toán công nợ
add_custom_field('Supplier', 'credit_limit', 'Float') # Giới hạn tiền nợ
add_custom_field('Supplier', 'mode_of_payment', 'Link', link_to='Mode of Payment') # Phương thức thanh toán
add_custom_field('Supplier', 'region', 'Data') # Khu vực
add_custom_field('Supplier', 'phone_number', 'Data') # Điện thoại
add_custom_field('Supplier', 'fax_number', 'Data') # Fax
add_custom_field('Supplier', 'email', 'Data') # Thư
add_custom_field('Supplier', 'note', 'Data') # Ghi chú
add_custom_field('Supplier', 'date_of_birth', 'Date') # Ngày sinh
add_custom_field('Supplier', 'legal_representative', 'Data') # Người đại diện pháp luật
add_custom_field('Supplier', 'position', 'Data') # Chức vụ
add_custom_field('Supplier', 'bank_account_number', 'Data') # Số tài khoản
add_custom_field('Supplier', 'bank_name', 'Data') # Tên ngân hàng
add_custom_field('Supplier', 'bank_branch', 'Data') # Chi nhánh
add_custom_field('Supplier', 'bank_province_city', 'Data') # Tỉnh thành
add_custom_field('Supplier', 'shipping_address', 'Data') # Địa chỉ giao hàng
add_custom_field('Supplier', 'use_e_invoice', 'Check') # Sử dụng hđ điện tử
add_custom_field('Supplier', 'e_invoice_email', 'Data') # Thư nhận HĐĐT 
add_custom_field('Supplier', 'e_invoice_representative', 'Data') # Người đại diện
add_custom_field('Supplier', 'order_source_table', 'Table', options='Order Source') # Nguồn đơn

# supplier_name: Tên nhà cung cấp
# tax_id: Mã số thuế
# accounts: Tài khoản ngầm định (list: company, default_account)
# website: Trang chủ
# disabled: Trạng thái
# supplier_details: Thông tin thêm
# business_type: Lĩnh vực hoạt dộng