from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

item_price_table_data = {
    "doctype": "DocType",
    "name": "Item Price Table",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "item_price", "fieldtype": "Link", "reqd": 1, "options": "Item Price"},
    ]
}

create_doctype(item_price_table_data)
add_custom_field('Tax Category', 'tax_code', 'Data')
add_custom_field('Tax Category', 'name_alias', 'Data')

add_custom_field('Item', 'name_alias', 'Data')
add_custom_field('Item', 'is_finished_goods', 'Select', options='Yes\nNo')
add_custom_field('Item', 'item_group_1', 'Link', link_to='Item Group')
add_custom_field('Item', 'item_group_2', 'Link', link_to='Item Group')
add_custom_field('Item', 'item_group_3', 'Link', link_to='Item Group')
add_custom_field('Item', 'default_warehouse', 'Link', link_to='Warehouse')
add_custom_field('Item', 'default_tax_code', 'Link', link_to='Tax Category')
add_custom_field('Item', 'cost_center', 'Link', link_to='Cost Center')
add_custom_field('Item', 'warehouse_account', 'Link', link_to='Account')
add_custom_field('Item', 'income_account', 'Link', link_to='Account')
add_custom_field('Item', 'expense_account', 'Link', link_to='Account')
add_custom_field('Item', 'discount_account', 'Link', link_to='Account')
add_custom_field('Item', 'promotion_account', 'Link', link_to='Account')
add_custom_field('Item', 'returns_account', 'Link', link_to='Account')
add_custom_field('Item', 'work_in_progress_account', 'Link', link_to='Account')
add_custom_field('Item', 'raw_material_expense_account', 'Link', link_to='Account')
add_custom_field('Item', 'volume', 'Float')
add_custom_field('Item', 'color', 'Data')
add_custom_field('Item', 'size', 'Data')
add_custom_field('Item', 'specifications', 'Data')
add_custom_field('Item', 'selling_price', 'Table', options='Item Price Table')
add_custom_field('Item', 'sub_code', 'Data')
add_custom_field('Item', 'planning_style', 'Select', options='Không hoạch định\nHoạch định\nHoạch định theo cỡ lô')
add_custom_field('Item', 'minimum_inventory', 'Float')
add_custom_field('Item', 'maximum_inventory', 'Float')
add_custom_field('Item', 'lastest_entry_date', 'Date')
add_custom_field('Item', 'lastest_export_date', 'Date')