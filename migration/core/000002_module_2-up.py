from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger


logger.info("Supplier set up...")
add_custom_field('Supplier', 'tax_code', 'Data')
add_custom_field('Supplier', 'phone', 'Data')
add_custom_field('Supplier', 'address', 'Long Text')
add_custom_field('Supplier', 'fax', 'Data')
add_custom_field('Supplier', 'mail', 'Data')
add_custom_field('Supplier', 'link', 'Data')


# logger.info("Account set up...")
# data = {
#         "account_name": "Thuế GTGT Đầu Vào",
#         "name": "1331 - VAT Input - TTMI",
#         "account_number": "1331",
#         "parent_account": "2300 - Duties and Taxes - TTMI",
#         "company": "TTMI",
#         "account_type": "Tax",
#         "root_type": "Liability",
#         "is_group": 0
#     }
# insert_data('Account', data)

# data = {
#         "account_name": "Thuế GTGT Đầu Ra",
#         "name": "3331 - VAT Output - TTMI",
#         "account_number": "3331",
#         "parent_account": "2300 - Duties and Taxes - TTMI",
#         "company": "TTMI",
#         "account_type": "Tax",
#         "root_type": "Liability",
#         "is_group": 0
#     }
# insert_data('Account', data)


logger.info("Purchase Invoice set up...")
add_custom_field('Purchase Invoice', 'employee_name', 'Link', link_to='Employee')