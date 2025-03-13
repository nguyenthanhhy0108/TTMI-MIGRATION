from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger

logger.info("13. Bank Account down...")

###################### Bank Account ######################

delete_custom_field("cal_account", "Bank Account")  # Tài khoản
delete_custom_field("bank_account", "Bank Account")  # Tài khoản ngân hàng
delete_custom_field("alias", "Bank Account")  # Tên khác
delete_custom_field("branch", "Bank Account")  # Chi nhánh
delete_custom_field("province", "Bank Account")  # Tỉnh
delete_custom_field("phone", "Bank Account")  # Điện thoại
delete_custom_field("fax", "Bank Account")  # Fax
delete_custom_field("account_holder", "Bank Account")  # Chủ tài khoản
delete_custom_field("notes", "Bank Account")  # Ghi chú
