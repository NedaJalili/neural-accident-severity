
import pandas as pd

def clean_khatkeshi():
    input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_vaze_hava_step7.csv'
    output_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_khatkeshi_step8.csv'

    df = pd.read_csv(input_path)
    df.columns = [col.strip() for col in df.columns]

    df['khatkeshi'] = df['khatkeshi'].astype(str).str.strip()

    replace_dict = {
        'ندارد': 'ندارد',
        'منقطع': 'منقطع',
        'ممتد': 'ممتد',
        'دوبل': 'دوبل',
        'درج نشده': 'نامشخص',
        '-': 'نامشخص',
        'مقطع': 'مقطع',
        'ممتد- دوبل': 'ممتد و دوبل',
        'منقطع وممتد': 'منقطع و ممتد',
        'ممتد و دوبل': 'ممتد و دوبل',
        'ممتد - منقطع': 'ممتد و منقطع',
        'nan': 'نامشخص'
    }

    df['khatkeshi'] = df['khatkeshi'].replace(replace_dict)

    khatkeshi_map = {val: idx for idx, val in enumerate(df['khatkeshi'].unique())}

    df['khatkeshi_id'] = df['khatkeshi'].map(khatkeshi_map)

    print("نگاشت khatkeshi:")
    print(df[['khatkeshi', 'khatkeshi_id']].drop_duplicates().to_string(index=False))

    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print("✅ پاکسازی و نگاشت ستون khatkeshi انجام شد و فایل ذخیره شد.")

if __name__ == "__main__":
    clean_khatkeshi()
