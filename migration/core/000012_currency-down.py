from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Currency reverse...")
###################### CURRENCY ######################

delete_custom_field("currency_alias", "Currency") # Tên khác
delete_custom_field("account_arise_debt", "Currency") # Tk phát sinh nợ
delete_custom_field("account_arise_credit", "Currency") # Tk phát sinh có
delete_custom_field("stt", "Currency") # STT
delete_custom_field("read_alone", "Currency") # Đọc lẻ
delete_custom_field("pronunciation", "Currency") # Cách đọc
delete_custom_field("pronunciation_2", "Currency") # Cách đọc 2








