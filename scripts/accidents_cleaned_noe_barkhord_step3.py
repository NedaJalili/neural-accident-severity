
import pandas as pd
from rapidfuzz import process, fuzz

# مسیر فایل ورودی و خروجی
input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_noe_tasadof_step2.csv'
output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_noe_barkhord_step3.csv'

# خواندن فایل
df = pd.read_csv(input_path)
df.columns = [col.strip() for col in df.columns]

# حذف فاصله‌های اضافی و تبدیل به رشته
df['noe_barkhord'] = df['noe_barkhord'].astype(str).str.strip()

# گرفتن مقادیر منحصربه‌فرد
unique_values = df['noe_barkhord'].unique()

# لیست مقادیر استاندارد خالی
standard_values = []

# تابع fuzzy برای نگاشت مقادیر مشابه به مقدار استاندارد
def fuzzy_map(value, choices, threshold=85):
    match, score, _ = process.extractOne(value, choices, scorer=fuzz.token_sort_ratio)
    if score >= threshold:
        return match
    else:
        return value

# ساخت لیست مقادیر استاندارد با گروه‌بندی fuzzy
for val in unique_values:
    if not standard_values:
        standard_values.append(val)
    else:
        mapped_val = fuzzy_map(val, standard_values)
        if mapped_val == val:
            standard_values.append(val)

# نگاشت هر مقدار به مقدار استاندارد
mapping_dict = {}
for val in unique_values:
    mapped_val = fuzzy_map(val, standard_values)
    mapping_dict[val] = mapped_val

# جایگزینی مقادیر ستون noe_barkhord با مقادیر تمیز شده
df['noe_barkhord'] = df['noe_barkhord'].map(mapping_dict)

# نگاشت عددی و ذخیره در ستون جدید noe_barkhord_id
barkhord_id_map = {v: i for i, v in enumerate(df['noe_barkhord'].unique())}
df['noe_barkhord_id'] = df['noe_barkhord'].map(barkhord_id_map)

# نمایش مقادیر تمیز شده و نگاشت عددی
print("مقادیر منحصربه‌فرد تمیز شده:")
print(df['noe_barkhord'].unique())
print("\nنگاشت عددی:")
print(df[['noe_barkhord', 'noe_barkhord_id']].drop_duplicates().to_string(index=False))

# ذخیره فایل نهایی
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print("✅ تمیزکاری fuzzy و نگاشت عددی انجام شد و فایل ذخیره شد.")
