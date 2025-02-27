from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Purchase Invoice reverse...")
delete_custom_field(fieldname='employee_name', doctype='Purchase Invoice')


logger.info("Supplier reverse...")
delete_custom_field(fieldname='link', doctype='Supplier')
delete_custom_field(fieldname='mail', doctype='Supplier')
delete_custom_field(fieldname='fax', doctype='Supplier')
delete_custom_field(fieldname='address', doctype='Supplier')
delete_custom_field(fieldname='phone', doctype='Supplier')
delete_custom_field(fieldname='tax_code', doctype='Supplier')