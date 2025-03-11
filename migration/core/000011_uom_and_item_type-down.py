from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger

###################### UOM ######################

logger.info("11. UOM and Item Type down...")

delete_custom_field("uom_id", "UOM")
delete_custom_field("name_alias", "UOM")
delete_custom_field("uom_2", "UOM")

###################### Item Type ######################

delete_doctype("Item Type")






