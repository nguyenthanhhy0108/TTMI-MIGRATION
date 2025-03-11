from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("10. Warehouse down...")

delete_custom_field("warehouse_id", "Warehouse")
delete_custom_field("name_alias", "Warehouse")
delete_custom_field("have_location", "Warehouse")
delete_custom_field("is_agent", "Warehouse")
delete_custom_field("note", "Warehouse")
