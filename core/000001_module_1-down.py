from migration.utils.functions import delete_custom_field


delete_custom_field(fieldname='uom_detail', doctype='UOM')
delete_custom_field(fieldname='uom_alias', doctype='UOM')
delete_custom_field(fieldname='status', doctype='UOM')