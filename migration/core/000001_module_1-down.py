from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Supplier reverse...")
delete_custom_field(fieldname='link', doctype='Supplier')
delete_custom_field(fieldname='mail', doctype='Supplier')
delete_custom_field(fieldname='fax', doctype='Supplier')
delete_custom_field(fieldname='address', doctype='Supplier')
delete_custom_field(fieldname='phone', doctype='Supplier')
delete_custom_field(fieldname='tax_code', doctype='Supplier')


logger.info("Warehouse reverse...")
delete_custom_field(fieldname='description', doctype='Department')


logger.info("Warehouse reverse...")
delete_custom_field(fieldname='department_id', doctype='Warehouse')
delete_custom_field(fieldname='description', doctype='Warehouse')


logger.info("Material request reverse...")
delete_custom_field(fieldname='no', doctype='Material Request')
delete_custom_field(fieldname='description', doctype='Material Request')
delete_custom_field(fieldname='priority', doctype='Material Request')
delete_custom_field(fieldname='requested_by', doctype='Material Request')
delete_custom_field(fieldname='department_id', doctype='Material Request')


logger.info("Item reverse...")
delete_custom_field(fieldname='max_inventory', doctype='Item')
delete_custom_field(fieldname='min_inventory', doctype='Item')
delete_custom_field(fieldname='model', doctype='Item')
delete_custom_field(fieldname='size', doctype='Item')
delete_custom_field(fieldname='color', doctype='Item')
delete_custom_field(fieldname='sub_code', doctype='Item')
delete_custom_field(fieldname='location_id', doctype='Item')
delete_custom_field(fieldname='warehouse_id', doctype='Item')
delete_custom_field(fieldname='material_type', doctype='Item')
delete_permission(doctype='Material Type', role='Stock User')
delete_doctype(doctype_name='Material Type')
delete_custom_field(fieldname='item_alias', doctype='Item')


logger.info("UOM reverse...")
delete_custom_field(fieldname='uom_detail', doctype='UOM')
delete_custom_field(fieldname='uom_alias', doctype='UOM')
delete_custom_field(fieldname='status', doctype='UOM')


logger.info("Account reverse...")
delete_data('Account', '3331 - VAT Output - TTMI')
delete_data('Account', '1331 - Thuế GTGT Đầu Vào - TTMI')









