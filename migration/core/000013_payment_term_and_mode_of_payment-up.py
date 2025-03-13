from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

logger.info("12. Payment Term up...")

###################### Payment Term ######################

# add custom field
add_custom_field("Payment Term", "term_name", "Data") # Tên thanh toán
add_custom_field("Payment Term", "name_alias", "Data") # Tên khác

###################### Mode of Payment ######################

# add custom field
add_custom_field("Mode of Payment", "method_name", "Data") # Tên thanh toán
add_custom_field("Mode of Payment", "name_alias", "Data") # Tên khác
add_custom_field("Mode of Payment", "invoice_method_code", "Data") # Mã ph.thức HĐĐT
