from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("5. Service down...")

delete_doctype('Service')
