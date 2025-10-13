
import pandas as pd

def clean_noe_shane():
    input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_sharayet_sathe_rah_step5.csv'
    output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_noe_shane_step6.csv'

    df = pd.read_csv(input_path)
    df.columns = [col.strip() for col in df.columns]

    df['noe_shane'] = df['noe_shane'].astype(str).str.strip()

    replace_dict = {
        'شانه ندارد': 'شانه ندارد',
        'شانه ندارد ': 'شانه ندارد',
        'شانه خاکی': 'شانه خاکی',
        'شانه خاکی ': 'شانه خاکی',
        'شانه آسفالته': 'شانه آسفالته',
        'شانه اسفالته': 'شانه آسفالته',
        'اسفالته': 'شانه آسفالته',
        'درج نشده': 'نامشخص',
        'درج نشده ': 'نامشخص',
        'nan': 'نامشخص',
        '-': 'نامشخص'
    }

    df['noe_shane'] = df['noe_shane'].replace(replace_dict)

    noe_shane_map = {val: idx for idx, val in enumerate(df['noe_shane'].unique())}

    df['noe_shane_id'] = df['noe_shane'].map(noe_shane_map)

    print("نگاشت noe_shane:")
    print(df[['noe_shane', 'noe_shane_id']].drop_duplicates().to_string(index=False))

    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print("✅ پاکسازی و نگاشت ستون noe_shane انجام شد و فایل ذخیره شد.")

if __name__ == "__main__":
    clean_noe_shane()
