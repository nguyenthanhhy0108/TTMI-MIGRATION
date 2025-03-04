from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Cost Center reverse...")

delete_custom_field("cost_center_id", "Cost Center")
delete_custom_field("name_alias", "Cost Center")
delete_custom_field("department", "Cost Center")
delete_custom_field("cost_category_1", "Cost Center")
delete_custom_field("cost_category_2", "Cost Center")
delete_custom_field("cost_category_3", "Cost Center")

delete_doctype("Cost Category")
