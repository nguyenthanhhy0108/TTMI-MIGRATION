from migration.utils.functions import add_custom_field, create_doctype, add_permission, insert_data
from loguru import logger

add_custom_field("Account", "account_id", "Data") # Tài khoản
add_custom_field("Account", "name_english", "Data") # Tên tiếng anh
add_custom_field("Account", "name_alias", "Data") # Tên khác
add_custom_field("Account", "short_name", "Data") # Tên ngắn
add_custom_field("Account", "shot_name_alias", "Data") # Tên ngắn khác
add_custom_field("Account", "debt_tracking_account", "Select", # Tk theo dõi công nợ
                 options="Không theo dõi công nợ\nCông nợ phải thu\nCông nợ phải trả\nCông nợ khác")
add_custom_field("Account", "calc_accounts_debt_recording_period_method", "Select", # Pp tính tggs nợ
                 options="Không tính chênh lệch\Trung bình tháng\nĐích danh\nTrung bình di động")
add_custom_field("Account", "calc_aging_method", "Select", # Pp tính tggs có
                 options="Không tính chênh lệch\Trung bình tháng\nĐích danh\nTrung bình di động")
add_custom_field("Account", "note", "Data") # Ghi chú
