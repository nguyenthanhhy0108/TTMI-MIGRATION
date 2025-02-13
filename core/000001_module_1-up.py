from migration.utils.functions import add_custom_field


add_custom_field('UOM', 'uom_detail', 'Data')
add_custom_field('UOM', 'uom_alias', 'Data')
add_custom_field('UOM', 'status', 'Select', options='in_use\nnot_in_use')