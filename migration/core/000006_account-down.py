from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Account reverse...")

delete_custom_field("account_id", "Account")
delete_custom_field("name_english", "Account")
delete_custom_field("name_alias", "Account")
delete_custom_field("short_name", "Account")
delete_custom_field("shot_name_alias", "Account")
delete_custom_field("debt_tracking_account", "Account")
delete_custom_field("calc_accounts_debt_recording_period_method", "Account")
delete_custom_field("calc_aging_method", "Account")
delete_custom_field("note", "Account")
