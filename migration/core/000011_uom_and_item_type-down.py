from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger

###################### UOM ######################

logger.info("UOM reverse...")

delete_custom_field("uom_id", "UOM")
delete_custom_field("name_alias", "UOM")
delete_custom_field("uom_2", "UOM")

###################### Item Type ######################

logger.info("Item Type reverse...")
delete_doctype("Item Type")






