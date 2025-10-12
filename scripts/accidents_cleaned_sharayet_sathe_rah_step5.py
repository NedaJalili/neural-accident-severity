
import pandas as pd

def clean_sharayet_sathe_rah():
    input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_vaze_roshanaei_step4.csv'
    output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_sharayet_sathe_rah_step5.csv'

    # خواندن داده‌ها
    df = pd.read_csv(input_path)
    df.columns = [col.strip() for col in df.columns]

    # حذف فاصله‌های اضافی و تبدیل به رشته
    df['sharayet_sathe_rah'] = df['sharayet_sathe_rah'].astype(str).str.strip()

    # دیکشنری نگاشت برای اصلاح مقادیر
    replace_dict = {
        'خشک و معمولی': 'خشک و معمولی',
        'خشک و معولی': 'خشک و معمولی',
        'خشک ومعمولی': 'خشک و معمولی',
        'مرطوب و خیس': 'مرطوب و خیس',
        'مرطوب و خیس ': 'مرطوب و خیس',
        'یخبندان و برفی': 'یخبندان و برفی',
        'یخبندان و برفی ': 'یخبندان و برفی',
        'شنی و خاکی': 'شنی و خاکی',
        'گل آلود': 'گل آلود',
        'درج نشده': 'نامشخص',
        'درج نشده ': 'نامشخص',
        '-': 'نامشخص',
        'nan': 'نامشخص',
        'سایر': 'سایر',
        'سایر ': 'سایر'
    }

    # جایگزینی مقادیر با نگاشت
    df['sharayet_sathe_rah'] = df['sharayet_sathe_rah'].replace(replace_dict)

    # نگاشت عددی مقادیر تمیز شده
    sharayet_sathe_rah_map = {val: idx for idx, val in enumerate(df['sharayet_sathe_rah'].unique())}

    # بازنویسی ستون sharayet_sathe_rah_id (اگر وجود داشته باشد مقدارش بازنویسی می‌شود)
    df['sharayet_sathe_rah_id'] = df['sharayet_sathe_rah'].map(sharayet_sathe_rah_map)

    # نمایش نگاشت‌ها
    print("نگاشت sharayet_sathe_rah:")
    print(df[['sharayet_sathe_rah', 'sharayet_sathe_rah_id']].drop_duplicates().to_string(index=False))

    # ذخیره فایل خروجی
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print("✅ پاکسازی و نگاشت ستون sharayet_sathe_rah انجام شد و فایل ذخیره شد.")

if __name__ == "__main__":
    clean_sharayet_sathe_rah()
