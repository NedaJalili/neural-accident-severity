
import pandas as pd

# مسیر فایل ورودی
input_path = "/content/drive/MyDrive/neural-accident-severity/data/Advanced_data_cleaning_step10.csv"

# لیست ستون‌های مورد نیاز به ترتیب دلخواه
columns = [
    "mavane_did_id",
    "naqayes_moaser_rah_id",
    "vaze_hava_id",
    "sharayet_sathe_rah_id",
    "vaze_roshanaei_id",
    "noe_barkhord_id",
    "noe_shane_id",
    "khatkeshi_id",
    "noe_tasadof_id"
]

# خواندن فایل و انتخاب فقط ستون‌های مورد نظر
df = pd.read_csv(input_path)
df_selected = df[columns]

# ذخیره خروجی به صورت فایل CSV جدید
output_path = "/content/drive/MyDrive/neural-accident-severity/data/id_columns_step11.csv"
df_selected.to_csv(output_path, index=False)
print("فایل آماده‌سازی شد و ذخیره گردید:", output_path)
