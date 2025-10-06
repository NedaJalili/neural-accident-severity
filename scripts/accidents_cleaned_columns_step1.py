
import pandas as pd

# خواندن فایل داده
df = pd.read_csv('/content/drive/MyDrive/neural-accident-severity/data/accidents_data_id_first_file.csv')

# حذف فاصله‌های ابتدا و انتهای نام ستون‌ها
df.columns = [col.strip() for col in df.columns]

# لیست دقیق ۱۶ ستونی که باید بمانند (مطابق با نام‌های واقعی در فایل)
final_columns = [
    'noe_barkhord_id', 'noe_barkhord',
    'naqayes_moaser_rah_id',
    'vaze_roshanaei_id', 'vaze_roshanaei',
    'sharayet_sathe_rah_id', 'sharayet_sathe_rah',
    'noe_shane_id', 'noe_shane',
    'mavane_did_id',
    'vaze_hava_id', 'vaze_hava',
    'khatkeshi_id', 'khatkeshi',
    'noe_tasadof_id', 'noe_tasadof'
]

# فقط ستون‌هایی که واقعاً وجود دارند را انتخاب کن
final_columns = [col for col in final_columns if col in df.columns]

# فقط این ستون‌ها را نگه دار و بقیه را حذف کن—even اگر بعضی‌شان خالی باشند
final_df = df[final_columns]

# ذخیره دیتافریم تمیزشده
final_df.to_csv('/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_columns_step1.csv', index=False, encoding='utf-8-sig')

print("فقط ۱۶ ستون اصلی نگه داشته شد—even اگر بعضی‌شان خالی باشند. فایل تمیز ذخیره شد.")
