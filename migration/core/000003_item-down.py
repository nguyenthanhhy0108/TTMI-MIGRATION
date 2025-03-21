from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("3. Item down...")

delete_custom_field('item_code', 'Item')
delete_custom_field('lastest_export_date', 'Item')
delete_custom_field('lastest_entry_date', 'Item')
delete_custom_field('maximum_inventory', 'Item')
delete_custom_field('minimum_inventory', 'Item')
delete_custom_field('planning_style', 'Item')
delete_custom_field('sub_code', 'Item')
delete_custom_field('selling_prices', 'Item')
delete_custom_field('goods_codes', 'Item')
delete_custom_field('is_finished_goods', 'Item')
delete_custom_field('item_group_1', 'Item')
delete_custom_field('item_group_2', 'Item')
delete_custom_field('item_group_3', 'Item')
delete_custom_field('default_warehouse', 'Item')
delete_custom_field('default_location', 'Item')
delete_custom_field('default_tax_code', 'Item')
delete_custom_field('barcode', 'Item')
delete_custom_field('cost_center', 'Item')
delete_custom_field('warehouse_account', 'Item')
delete_custom_field('income_account', 'Item')
delete_custom_field('expense_account', 'Item')
delete_custom_field('discount_account', 'Item')
delete_custom_field('returns_account', 'Item')
delete_custom_field('work_in_progress_account', 'Item')
delete_custom_field('raw_material_expense_account', 'Item')
delete_custom_field('volume', 'Item')
delete_custom_field('color', 'Item')
delete_custom_field('size', 'Item')
delete_custom_field('specifications', 'Item')
delete_custom_field('promotion_account', 'Item')
delete_custom_field('name_alias', 'Item')
delete_custom_field('note', 'Item')
delete_custom_field('tax_code', 'Tax Category')
delete_custom_field('name_alias', 'Tax Category')

delete_doctype('Item Price Table')
delete_doctype('Goods Code Table')
