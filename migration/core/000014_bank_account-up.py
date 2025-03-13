from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("13. Bank Account up...")

###################### Bank Account ######################

# add custom field
add_custom_field("Bank Account", "cal_account", "Link", link_to="Account") # Tài khoản
add_custom_field("Bank Account", "bank_account", "Data") # Tài khoản ngân hàng
add_custom_field("Bank Account", "alias", "Data") # Tên khác
add_custom_field("Bank Account", "branch", "Data") # Chi nhánh
add_custom_field("Bank Account", "province", "Data") # Tỉnh
add_custom_field("Bank Account", "phone", "Data") # Điện thoại
add_custom_field("Bank Account", "fax", "Data") # Fax
add_custom_field("Bank Account", "account_holder", "Data") # Chủ tài khoản
add_custom_field("Bank Account", "notes", "Data") # Ghi chú