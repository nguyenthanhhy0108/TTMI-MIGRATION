from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("3. Item up...")
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

goods_code_table_data = {
    "doctype": "DocType",
    "name": "Goods Code Table",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "good_code", "fieldtype": "Data", "reqd": 1},
    ]
}

create_doctype(goods_code_table_data)

add_custom_field('Tax Category', 'tax_code', 'Data') # Mã thuế
add_custom_field('Tax Category', 'name_alias', 'Data') # Tên khác

add_custom_field('Item', 'name_alias', 'Data') # Tên khác
add_custom_field('Item', 'is_finished_goods', 'Check') # Tạo nhập thành phẩm
add_custom_field('Item', 'item_group_1', 'Link', link_to='Item Group') # Nhóm 1
add_custom_field('Item', 'item_group_2', 'Link', link_to='Item Group') # Nhóm 2
add_custom_field('Item', 'item_group_3', 'Link', link_to='Item Group') # Nhóm 3
add_custom_field('Item', 'default_warehouse', 'Link', link_to='Warehouse') # Mã kho mặc định
add_custom_field('Item', 'default_location', 'Link', link_to='Location') # Mã vị trí mặc định
add_custom_field('Item', 'default_tax_code', 'Link', link_to='Tax Category') # Mã thuế mặc định
add_custom_field('Item', 'barcode', 'Data') # Mã vạch
add_custom_field('Item', 'cost_center', 'Link', link_to='Cost Center') # Mã phí 
add_custom_field('Item', 'warehouse_account', 'Link', link_to='Account') # Tk kho (Tk vật tư)
add_custom_field('Item', 'income_account', 'Link', link_to='Account') # Tk doanh thu
add_custom_field('Item', 'expense_account', 'Link', link_to='Account') # Tk giá vốn
add_custom_field('Item', 'discount_account', 'Link', link_to='Account') # Tk chiết khấu
add_custom_field('Item', 'promotion_account', 'Link', link_to='Account') # Tk khuyến mãi
add_custom_field('Item', 'returns_account', 'Link', link_to='Account') # Tk trả lại
add_custom_field('Item', 'work_in_progress_account', 'Link', link_to='Account') # Tk s/p dở dang
add_custom_field('Item', 'raw_material_expense_account', 'Link', link_to='Account') # Tk chi phí NVL

add_custom_field('Item', 'volume', 'Float') # Thể tích
add_custom_field('Item', 'color', 'Data') # Màu sắc
add_custom_field('Item', 'size', 'Data') # Kích cỡ
add_custom_field('Item', 'specifications', 'Data') # Quy cách

add_custom_field('Item', 'selling_prices', 'Table', options='Item Price Table') # Giá bán
add_custom_field('Item', 'goods_codes', 'Table', options='Goods Code Table') # Mã hàng hoá
add_custom_field('Item', 'sub_code', 'Data') # Mã phụ
add_custom_field('Item', 'planning_style', 'Select', options='Không hoạch định\nHoạch định\nHoạch định theo cỡ lô') # Kiểu tính hoạch định
add_custom_field('Item', 'minimum_inventory', 'Float') # Tồn kho tối thiểu
add_custom_field('Item', 'maximum_inventory', 'Float') # Tồn kho tối đa
add_custom_field('Item', 'lastest_entry_date', 'Date') # Ngày nhập cuối
add_custom_field('Item', 'lastest_export_date', 'Date') # Ngày xuất cuối
add_custom_field('Item', 'note', 'Data') # Ghi chú


# item_code: Mã sản phẩm
# item_name: Tên sản phẩm
# stock_uom: Đơn vị tính
# purchase_uom: ĐVT nhập liệu
# is_stock_item: Theo dõi tồn kho
# has_batch_no: Theo dõi lô
# valuation_method: Cách tính giá tồn kho
# item_group: Loại vật tư
# default_location: Vị trí mặc định
# shelf_life_in_days: Số ngày sử dụng
# barcodes: Mã vạch (Barcode) (table)
# weight_per_unit: Khối lượng
# country_of_origin: Ñước sản xuất
# description: Mô tả
# uoms: Quy đổi đvt (table)
# Mã hàng hoá (Không biết)
# Hình ảnh (Không biết)
# disabled: Trạng thái