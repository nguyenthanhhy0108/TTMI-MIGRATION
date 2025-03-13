from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger

logger.info("12. Payment Term down...")

###################### Payment Term ######################

delete_custom_field("term_name", "Payment Term")
delete_custom_field("name_alias", "Payment Term")

###################### Mode of Payment ######################

delete_custom_field("method_name", "Mode of Payment")
delete_custom_field("name_alias", "Mode of Payment")
delete_custom_field("invoice_method_code", "Mode of Payment")







