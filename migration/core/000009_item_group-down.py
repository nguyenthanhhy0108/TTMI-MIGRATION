from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("9. Item Group down...")

delete_custom_field("group_type", "Item Group")
delete_custom_field("item_group_id", "Item Group")
delete_custom_field("name_alias", "Item Group")
delete_custom_field("status", "Item Group")
