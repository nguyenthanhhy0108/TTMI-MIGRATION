from migration.utils.functions import delete_custom_field, delete_doctype, delete_permission, delete_data
from loguru import logger


logger.info("Employee reverse...")

delete_custom_field('birthplace', 'Employee')
delete_custom_field('tax_code', 'Employee')
delete_custom_field('citizen_identification_number', 'Employee')
delete_custom_field('issue_date', 'Employee')
delete_custom_field('province', 'Employee')
delete_custom_field('is_sales_agent', 'Employee')
delete_custom_field('is_purchasing_agent', 'Employee')
delete_custom_field('is_debt_or_provisional', 'Employee')

delete_doctype('Province')
