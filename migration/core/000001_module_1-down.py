from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission
from loguru import logger


logger.info("Purchase invoice item set up...")
delete_custom_field(fieldname='give_back_qty', doctype='Purchase Invoice Item')


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








