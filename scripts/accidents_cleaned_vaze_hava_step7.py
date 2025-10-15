
import pandas as pd

def clean_vaze_hava():
    input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_noe_shane_step6.csv'
    output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_vaze_hava_step7.csv'

    df = pd.read_csv(input_path)
    df.columns = [col.strip() for col in df.columns]

    df['vaze_hava'] = df['vaze_hava'].astype(str).str.strip()

    replace_dict = {
        'صاف': 'صاف',
        'صاف ': 'صاف',
        'ابری': 'ابری',
        'بارانی': 'بارانی',
        'برفی': 'برفی',
        'برفی ': 'برفی',
        'بارانی و ابری': 'بارانی و ابری',
        'مه آلود': 'مه آلود',
        'مه آلود ': 'مه آلود',
        'غبارآلود': 'غبارآلود',
        'غبارآلود ': 'غبارآلود',
        'صاف - ابری': 'صاف - ابری',
        '-': 'نامشخص',
        '----': 'نامشخص',
        'درج نشده': 'نامشخص',
        'nan': 'نامشخص',
        'nan ': 'نامشخص',
        '': 'نامشخص',
        'None': 'نامشخص',
        'none': 'نامشخص',
        'NaN': 'نامشخص'
    }

    df['vaze_hava'] = df['vaze_hava'].replace(replace_dict)

    vaze_hava_map = {val: idx for idx, val in enumerate(df['vaze_hava'].unique())}

    df['vaze_hava_id'] = df['vaze_hava'].map(vaze_hava_map)

    print("نگاشت vaze_hava:")
    print(df[['vaze_hava', 'vaze_hava_id']].drop_duplicates().to_string(index=False))

    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print("✅ پاکسازی و نگاشت ستون vaze_hava انجام شد و فایل ذخیره شد.")

if __name__ == "__main__":
    clean_vaze_hava()
