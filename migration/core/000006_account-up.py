from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

add_custom_field("Account", "account_id", "Data")
add_custom_field("Account", "name_english", "Data")
add_custom_field("Account", "name_alias", "Data")
add_custom_field("Account", "short_name", "Data")
add_custom_field("Account", "shot_name_alias", "Data")
add_custom_field("Account", "debt_tracking_account", "Select", 
                 options="Không theo dõi công nợ\nCông nợ phải thu\nCông nợ phải trả\nCông nợ khác")
add_custom_field("Account", "calc_accounts_debt_recording_period_method", "Select", 
                 options="Không tính chênh lệch\Trung bình tháng\nĐích danh\nTrung bình di động")
add_custom_field("Account", "calc_aging_method", "Select", 
                 options="Không tính chênh lệch\Trung bình tháng\nĐích danh\nTrung bình di động")
add_custom_field("Account", "note", "Data")
