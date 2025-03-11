from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("7. Department down...")

delete_custom_field("department_id", "Department")
delete_custom_field("name_alias", "Department")
delete_custom_field("note", "Department")
delete_custom_field("department_type", "Department")
