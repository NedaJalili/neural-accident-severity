
import pandas as pd

# مسیر فایل ورودی و خروجی
input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_columns_step1.csv'
output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_noe_tasadof_step2.csv'

# خواندن فایل
df = pd.read_csv(input_path)
df.columns = [col.strip() for col in df.columns]

# اگر ستون noe_tasadof_id قبلاً وجود دارد، حذفش کن
if 'noe_tasadof_id' in df.columns:
    df.drop(columns=['noe_tasadof_id'], inplace=True)

# حذف فاصله‌های اضافی و تبدیل به رشته
df['noe_tasadof'] = df['noe_tasadof'].astype(str).str.strip()

# دیکشنری نگاشت مستقیم همه حالت‌های ممکن به مقدار استاندارد
replace_dict = {
    'خسارتی': 'خسارتی',
    'خسارتی ': 'خسارتی',
    'خسا': 'خسارتی',
    'جرحی': 'جرحی',
    'جرحی ': 'جرحی',
    'فوتی': 'فوتی',
    'فوتی ': 'فوتی',
    'فوتی پزشکی قانونی': 'فوتی',
    'فوتی پزشکی قانونی ': 'فوتی'
}

# جایگزینی مقادیر با replace به صورت دیکشنری
df['noe_tasadof'] = df['noe_tasadof'].replace(replace_dict)

# نگاشت دستی مقادیر به عدد
tasadof_map = {'خسارتی': 0, 'جرحی': 1, 'فوتی': 2}
df['noe_tasadof_id'] = df['noe_tasadof'].map(tasadof_map)

# نمایش نگاشت نهایی و نمونه خروجی
print("نگاشت نهایی noe_tasadof:")
print(df[['noe_tasadof', 'noe_tasadof_id']].drop_duplicates().to_string(index=False))
print("\nنمونه خروجی (۵ سطر اول):")
print(df[['noe_tasadof', 'noe_tasadof_id']].head())

# ذخیره فایل نهایی
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print("\n نگاشت مقادیر با موفقیت انجام شد و فایل جدید ذخیره گردید.")
