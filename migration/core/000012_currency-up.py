from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger


logger.info("Currency setting up...")
###################### CURRENCY ######################

add_custom_field("Currency", "currency_alias", "Data") # Tên khác
add_custom_field("Currency", "account_arise_debt", "Link", link_to="Account") # Tk phát sinh nợ
add_custom_field("Currency", "account_arise_credit", "Link", link_to="Account") # Tk phát sinh có
add_custom_field("Currency", "stt", "Data") # STT
add_custom_field("Currency", "read_alone", "Data") # Đọc lẻ
add_custom_field("Currency", "pronunciation", "Data") # Cách đọc
add_custom_field("Currency", "pronunciation_2", "Data") # Cách đọc 2
#enable: Trạng thái








