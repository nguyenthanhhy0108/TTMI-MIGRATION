from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

province_data = {
    "doctype": "DocType",
    "name": "Province",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "province_id", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "province_name", "fieldtype": "Data", "reqd": 1},
    ]
}

create_doctype(province_data)


add_custom_field('Employee', 'birthplace', 'Data')
add_custom_field('Employee', 'tax_code', 'Data')
add_custom_field('Employee', 'citizen_identification_number', 'Data')
add_custom_field('Employee', 'issue_date', 'Date')
add_custom_field('Employee', 'province', 'Link', link_to='Province')
add_custom_field('Employee', 'is_sales_agent', 'Select', options='Yes\nNo')
add_custom_field('Employee', 'is_purchasing_agent', 'Select', options='Yes\nNo')
add_custom_field('Employee', 'is_debt_or_provisional', 'Select', options='Yes\nNo')
