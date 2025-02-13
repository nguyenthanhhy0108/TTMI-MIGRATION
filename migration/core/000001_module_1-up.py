from migration.utils.functions import add_custom_field, create_doctype, add_permission
from loguru import logger

logger.info("UOM set up...")
add_custom_field('UOM', 'uom_detail', 'Data')
add_custom_field('UOM', 'uom_alias', 'Data')
add_custom_field('UOM', 'status', 'Select', options='in_use\nnot_in_use')


logger.info("Item set up...")
add_custom_field('Item', 'item_alias', 'Data')
data = {
    "doctype": "DocType",
    "name": "Material Type",
    "module": "Custom",
    "custom": 1,
    "fields": [
        {"fieldname": "material_type_code", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "material_type_name", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "material_type_alias", "fieldtype": "Data", "reqd": 0},
        {"fieldname": "status", "fieldtype": "Select", "options": 'in_use\nnot_in_use'}
    ]
}
create_doctype(data)
add_permission("Material Type", "Stock User", {"read": 1, "write": 1, "create": 1})
add_custom_field('Item', 'material_type', 'Link', link_to='Material Type')
add_custom_field('Item', 'warehouse_id', 'Link', link_to='Warehouse')
add_custom_field('Item', 'location_id', 'Data')
add_custom_field('Item', 'sub_code', 'Data')
add_custom_field('Item', 'color', 'Data')
add_custom_field('Item', 'size', 'Data')
add_custom_field('Item', 'model', 'Data')
add_custom_field('Item', 'min_inventory', 'Int')
add_custom_field('Item', 'max_inventory', 'Int')


logger.info("Material request set up...")
add_custom_field('Material Request', 'department_id', 'Link', link_to='Department')
add_custom_field('Material Request', 'requested_by', 'Data')
add_custom_field('Material Request', 'priority', 'Data')
add_custom_field('Material Request', 'description', 'Data')
add_custom_field('Material Request', 'no', 'Data')