
import pandas as pd

# مسیر فایل ورودی و خروجی
input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_noe_barkhord_step3.csv'
output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_vaze_roshanaei_step4.csv'

# خواندن فایل
df = pd.read_csv(input_path)
df.columns = [col.strip() for col in df.columns]

# حذف فاصله‌های اضافی و تبدیل به رشته
df['vaze_roshanaei'] = df['vaze_roshanaei'].astype(str).str.strip()

# دیکشنری نگاشت دستی
replace_dict = {
    'روز': 'روز', 'روز ': 'روز',
    'غروب': 'غروب', 'غروب ': 'غروب',
    'طلوع': 'طلوع', 'طلوع ': 'طلوع',
    'شب': 'شب', 'شب ': 'شب',
    'شب با روشنایی کافی': 'شب با روشنایی کافی',
    'شب با روشنایی کافی ': 'شب با روشنایی کافی',
    'شب با روشنای کافی': 'شب با روشنایی کافی',
    'شب با نور کافی': 'شب با روشنایی کافی',
    'شب با نور کافی ': 'شب با روشنایی کافی',
    'شب بدون روشنایی کافی': 'شب بدون روشنایی کافی',
    'شب بدون روشنایی کافی ': 'شب بدون روشنایی کافی',
    'شب بدون نور کافی': 'شب بدون روشنایی کافی',
    'سایر': 'سایر', 'سایر ': 'سایر',
    'درج نشده': 'نامشخص', 'درج نشده ': 'نامشخص',
    '_': 'نامشخص', '-': 'نامشخص', 'nan': 'نامشخص',
    'شب با غروب کافی': 'شب با روشنایی کافی',
    'ب با روشنایی کافی': 'شب با روشنایی کافی'
}

# جایگزینی مقادیر با دیکشنری نگاشت
df['vaze_roshanaei'] = df['vaze_roshanaei'].replace(replace_dict)

# حذف ستون vaze_roshanaei_id اگر وجود داشت
if 'vaze_roshanaei_id' in df.columns:
    df.drop(columns=['vaze_roshanaei_id'], inplace=True)

# نگاشت عددی مقادیر تمیز شده
vaze_roshanaei_map = {val: idx for idx, val in enumerate(df['vaze_roshanaei'].unique())}
df['vaze_roshanaei_id'] = df['vaze_roshanaei'].map(vaze_roshanaei_map)

# نمایش نگاشت و نمونه داده‌ها
print("نگاشت vaze_roshanaei:")
print(df[['vaze_roshanaei', 'vaze_roshanaei_id']].drop_duplicates().to_string(index=False))
print("\nنمونه خروجی (۵ سطر اول):")
print(df[['vaze_roshanaei', 'vaze_roshanaei_id']].head())

# ذخیره فایل خروجی
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print("\n✅ تمیزکاری و نگاشت ستون vaze_roshanaei انجام شد و فایل ذخیره شد.")
