from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Supplier reverse...")
delete_custom_field(fieldname='supplier_code', doctype='Supplier')
delete_custom_field(fieldname='is_customer', doctype='Supplier')
delete_custom_field(fieldname='is_supplier', doctype='Supplier')
delete_custom_field(fieldname='name_alias', doctype='Supplier')
delete_custom_field(fieldname='address', doctype='Supplier')
delete_custom_field(fieldname='contact_person', doctype='Supplier')
delete_custom_field(fieldname='employee', doctype='Supplier')
delete_custom_field(fieldname='supplier_group_1', doctype='Supplier')
delete_custom_field(fieldname='supplier_group_2', doctype='Supplier')
delete_custom_field(fieldname='supplier_group_3', doctype='Supplier')
delete_custom_field(fieldname='region', doctype='Supplier')
delete_custom_field(fieldname='phone_number', doctype='Supplier')
delete_custom_field(fieldname='fax_number', doctype='Supplier')
delete_custom_field(fieldname='email', doctype='Supplier')
delete_custom_field(fieldname='note', doctype='Supplier')
delete_custom_field(fieldname='date_of_birth', doctype='Supplier')
delete_custom_field(fieldname='legal_representative', doctype='Supplier')
delete_custom_field(fieldname='position', doctype='Supplier')
delete_custom_field(fieldname='bank_account_number', doctype='Supplier')
delete_custom_field(fieldname='bank_name', doctype='Supplier')
delete_custom_field(fieldname='bank_branch', doctype='Supplier')
delete_custom_field(fieldname='bank_province_city', doctype='Supplier')
delete_custom_field(fieldname='shipping_address', doctype='Supplier')
delete_custom_field(fieldname='use_e_invoice', doctype='Supplier')
delete_custom_field(fieldname='e_invoice_email', doctype='Supplier')
delete_custom_field(fieldname='e_invoice_representative', doctype='Supplier')
delete_custom_field(fieldname='order_source_table', doctype='Supplier')
delete_custom_field(fieldname='payment_term', doctype='Supplier')
delete_custom_field(fieldname='credit_limit', doctype='Supplier')
delete_custom_field(fieldname='mode_of_payment', doctype='Supplier')





