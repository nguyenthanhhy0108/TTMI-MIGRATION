from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("1. Customer down...")
delete_custom_field(fieldname='customer_code', doctype='Customer')
delete_custom_field(fieldname='is_customer', doctype='Customer')
delete_custom_field(fieldname='is_supplier', doctype='Customer')
delete_custom_field(fieldname='name_alias', doctype='Customer')
delete_custom_field(fieldname='address', doctype='Customer')
delete_custom_field(fieldname='contact_person', doctype='Customer')
delete_custom_field(fieldname='employee', doctype='Customer')
delete_custom_field(fieldname='customer_account', doctype='Account') # Tài khoản ngầm định
delete_custom_field(fieldname='customer_group_1', doctype='Customer')
delete_custom_field(fieldname='customer_group_2', doctype='Customer')
delete_custom_field(fieldname='customer_group_3', doctype='Customer')
delete_custom_field(fieldname='region', doctype='Customer')
delete_custom_field(fieldname='phone_number', doctype='Customer')
delete_custom_field(fieldname='fax_number', doctype='Customer')
delete_custom_field(fieldname='email', doctype='Customer')
delete_custom_field(fieldname='note', doctype='Customer')
delete_custom_field(fieldname='date_of_birth', doctype='Customer')
delete_custom_field(fieldname='legal_representative', doctype='Customer')
delete_custom_field(fieldname='position', doctype='Customer')
delete_custom_field(fieldname='bank_account_number', doctype='Customer')
delete_custom_field(fieldname='bank_name', doctype='Customer')
delete_custom_field(fieldname='bank_branch', doctype='Customer')
delete_custom_field(fieldname='bank_province_city', doctype='Customer')
delete_custom_field(fieldname='shipping_address', doctype='Customer')
delete_custom_field(fieldname='operational_field', doctype='Customer')
delete_custom_field(fieldname='use_e_invoice', doctype='Customer')
delete_custom_field(fieldname='e_invoice_email', doctype='Customer')
delete_custom_field(fieldname='e_invoice_representative', doctype='Customer')
delete_custom_field(fieldname='order_source_table', doctype='Customer')

delete_custom_field(fieldname='group_id', doctype='Customer Group')
delete_custom_field(fieldname='group_alias', doctype='Customer Group')
delete_custom_field(fieldname='status', doctype='Customer Group')

delete_doctype(doctype_name='Order Source')






