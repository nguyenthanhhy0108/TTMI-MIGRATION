from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger


order_source_data = {
    "doctype": "DocType",
    "name": "Order Source",
    "module": "Custom",
    "custom": 1,
    "istable": 1,
    "fields": [
        {"fieldname": "source_id", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "source_name", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "status", "fieldtype": "Select", "options": 'in_use\nnot_in_use'}
    ]
}

create_doctype(order_source_data)

add_custom_field('Customer Group', 'group_id', 'Data')
add_custom_field('Customer Group', 'group_alias', 'Data')
add_custom_field('Customer Group', 'status', 'Select', options='in_use\nnot_in_use')
add_custom_field('Customer', 'customer_code', 'Data')
add_custom_field('Customer', 'is_customer', 'Check')
add_custom_field('Customer', 'is_supplier', 'Check')
add_custom_field('Customer', 'name_alias', 'Data')
add_custom_field('Customer', 'address', 'Data')
add_custom_field('Customer', 'contact_person', 'Data')
add_custom_field('Customer', 'employee', 'Link', link_to='Employee')
add_custom_field('Customer', 'customer_group_1', 'Link', link_to='Customer Group')
add_custom_field('Customer', 'customer_group_2', 'Link', link_to='Customer Group')
add_custom_field('Customer', 'customer_group_3', 'Link', link_to='Customer Group')
add_custom_field('Customer', 'region', 'Data')
add_custom_field('Customer', 'phone_number', 'Data')
add_custom_field('Customer', 'fax_number', 'Data')
add_custom_field('Customer', 'email', 'Data')
add_custom_field('Customer', 'note', 'Data')
add_custom_field('Customer', 'date_of_birth', 'Date')
add_custom_field('Customer', 'legal_representative', 'Data')
add_custom_field('Customer', 'position', 'Data')
add_custom_field('Customer', 'bank_account_number', 'Data')
add_custom_field('Customer', 'bank_name', 'Data')
add_custom_field('Customer', 'bank_branch', 'Data')
add_custom_field('Customer', 'bank_province_city', 'Data')
add_custom_field('Customer', 'shipping_address', 'Data')
add_custom_field('Customer', 'use_e_invoice', 'Select', options='Yes\nNo')
add_custom_field('Customer', 'e_invoice_email', 'Data')
add_custom_field('Customer', 'e_invoice_representative', 'Data')
add_custom_field('Customer', 'order_source_table', 'Table', options='Order Source')
