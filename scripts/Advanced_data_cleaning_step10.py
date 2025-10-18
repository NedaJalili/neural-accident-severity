
import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.columns = [col.strip() for col in df.columns]

    # --- پاکسازی khatkeshi ---
    khatkeshi_map = {
        'ندارد': 'ندارد',
        'منقطع': 'منقطع',
        'مقطع': 'منقطع',
        'ممتد': 'ممتد',
        'دوبل': 'دوبل',
        'نامشخص': 'نامشخص',
        '-': 'نامشخص',
        '': 'نامشخص',
        'nan': 'نامشخص',
        'ممتد و دوبل': 'ممتد و دوبل',
        'ممتد- دوبل': 'ممتد و دوبل',
        'ممتد و منقطع': 'ممتد و منقطع',
        'منقطع و ممتد': 'ممتد و منقطع'
    }
    df['khatkeshi'] = df['khatkeshi'].astype(str).str.strip().replace(khatkeshi_map)

    # --- پاکسازی vaze_roshanaei ---
    vaze_roshanaei_map = {
        'روز': 'روز',
        'شب با روشنایی کافی': 'شب با روشنایی کافی',
        'غروب': 'غروب',
        'شب بدون روشنایی کافی': 'شب بدون روشنایی کافی',
        'نامشخص': 'نامشخص',
        'طلوع': 'طلوع',
        'سایر': 'سایر',
        'شب': 'شب با روشنایی نامشخص',
        '-': 'نامشخص',
        'nan': 'نامشخص',
        '': 'نامشخص'
    }
    df['vaze_roshanaei'] = df['vaze_roshanaei'].astype(str).str.strip().replace(vaze_roshanaei_map)

    # --- پاکسازی sharayet_sathe_rah ---
    sharayet_sathe_rah_map = {
        'خشک و معمولی': 'خشک و معمولی',
        'مرطوب و خیس': 'مرطوب و خیس',
        'یخبندان و برفی': 'یخبندان و برفی',
        'نامشخص': 'نامشخص',
        'سایر': 'سایر',
        'شنی و خاکی': 'شنی و خاکی',
        'گل آلود': 'گل آلود',
        '-': 'نامشخص',
        'nan': 'نامشخص',
        '': 'نامشخص'
    }
    df['sharayet_sathe_rah'] = df['sharayet_sathe_rah'].astype(str).str.strip().replace(sharayet_sathe_rah_map)

    # --- پاکسازی noe_shane ---
    noe_shane_map = {
        'شانه ندارد': 'شانه ندارد',
        'شانه خاکی': 'شانه خاکی',
        'شانه آسفالته': 'شانه آسفالته',
        'نامشخص': 'نامشخص',
        '-': 'نامشخص',
        'nan': 'نامشخص',
        '': 'نامشخص'
    }
    df['noe_shane'] = df['noe_shane'].astype(str).str.strip().replace(noe_shane_map)

    # --- پاکسازی vaze_hava ---
    vaze_hava_map = {
        'صاف': 'صاف',
        'ابری': 'ابری',
        'بارانی': 'بارانی',
        'برفی': 'برفی',
        'نامشخص': 'نامشخص',
        'بارانی و ابری': 'بارانی و ابری',
        'مه آلود': 'مه آلود',
        'غبارآلود': 'غبارآلود',
        'صاف - ابری': 'صاف - ابری',
        '-': 'نامشخص',
        'nan': 'نامشخص',
        '': 'نامشخص'
    }
    df['vaze_hava'] = df['vaze_hava'].astype(str).str.strip().replace(vaze_hava_map)

    # --- پاکسازی noe_tasadof ---
    noe_tasadof_map = {
        'خسارتی': 'خسارتی',
        'جرحی': 'جرحی',
        'فوتی': 'فوتی',
        '-': 'نامشخص',
        'nan': 'نامشخص',
        'درج نشده': 'نامشخص',
        '': 'نامشخص'
    }
    df['noe_tasadof'] = df['noe_tasadof'].astype(str).str.strip().replace(noe_tasadof_map)

    # --- پاکسازی noe_barkhord ---
    noe_barkhord_map = {
    'درج نشده': 'نامشخص',
    '-': 'نامشخص',
    'nan': 'نامشخص',
    '': 'نامشخص',
    14: 'نامشخص',
    24: 'نامشخص',
    30: 'نامشخص',
    44: 'نامشخص',
    'وسیله نقلیه-یک وسیله نقلیه': 'وسیله نقلیه با یک وسیله نقلیه',
    'وسلیه نقلیه': 'وسیله نقلیه با یک وسیله نقلیه',
    'وسیله نفیله - وسیله نقلیه': 'وسیله نقلیه با یک وسیله نقلیه',
    'وسیله نقلیه -ئسیله نقلیه': 'وسیله نقلیه با یک وسیله نقلیه',
    'وسیله نقلیه -موتور سیکلت': 'وسیله نقلیه با موتورسیکلت',
    'وسسیله نقلیه با کموتورسیکلت': 'وسیله نقلیه با موتورسیکلت',
    'موتورسیکلت با یک وسیله نقلیه': 'موتورسیکلت با وسیله نقلیه',
    'موتور سیکلت': 'موتورسیکلت',
    'موتورسیکلت': 'موتورسیکلت',
    'موتور سیکلت با موتور سیکلت': 'موتورسیکلت با موتورسیکلت',  # مورد دوم
    'موتورسیکلت با موتورسیکلت': 'موتورسیکلت با موتورسیکلت',
    'موتورسیکلت - سایر': 'سایر',
    'وسیله نقلیه - سایر': 'سایر',
    'یک وسیله نقلیه با سایر موارد': 'سایر',
    'وسیله نقلیه با-چند وسیله نقلیه و عابر': 'وسیله نقلیه با چند وسیله نقلیه و عابر',
    'وسیله نقلیه با جدول وسط': 'وسیله نقلیه با شیء ثابت',
    'نقلیه با عابر': 'وسیله نقلیه با عابر',
    'وسیله نقلیه-عابر': 'وسیله نقلیه با عابر',
    'موتور سیکلت با چند وسیله دیگر': 'موتورسیکلت با چند وسیله دیگر',
    'موتور سیکلت با عابر': 'موتورسیکلت با عابر',
    'دوچرخه با موتور سیکلت': 'دوچرخه با موتورسیکلت',
    'وسیله نقلیه - پرتاب سرنشین': 'پرتاب سرنشین',
    'وسیله نقلیه - واژگونی و سقوط، خروج از جاده': 'واژگونی و سقوط، خروج از جاده',
    'واژگونی و سقوط': 'واژگونی و سقوط',
    'وسیله نقلیه - چند برخوردی': 'چند برخوردی',
    'وسیله نقلیه با عابر،روسیله نقلیه': 'وسیله نقلیه با عابر'  # مورد اول
    }

    df['noe_barkhord'] = df['noe_barkhord'].astype(str).str.strip().replace(noe_barkhord_map)
    df['noe_barkhord'] = df['noe_barkhord'].replace({14: 'نامشخص', 24: 'نامشخص', 30: 'نامشخص', 44: 'نامشخص'})

    # --- نگاشت مجدد عددی ---
    def make_id_column(col):
        unique_vals = df[col].unique()
        mapping = {val: idx for idx, val in enumerate(unique_vals)}
        df[col + '_id'] = df[col].map(mapping)
        return mapping

    mappings = {}
    for col in [
        'noe_tasadof', 'noe_barkhord', 'vaze_roshanaei',
        'sharayet_sathe_rah', 'noe_shane', 'vaze_hava', 'khatkeshi'
    ]:
        mappings[col] = make_id_column(col)

    # --- ذخیره فایل خروجی ---
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"✅ داده‌ها پاکسازی و نگاشت عددی مجدد شد و فایل در {output_path} ذخیره شد.")

    # --- نمایش نگاشت‌ها ---
    for col, mapping in mappings.items():
        print(f"\nنگاشت عددی برای ستون {col}:")
        for val, idx in mapping.items():
            print(f"  {idx} => {val}")

if __name__ == "__main__":
    input_path = '/content/drive/MyDrive/neural-accident-severity/data/accidents_cleaned_khatkeshi_step8.csv'
    output_path = '/content/drive/MyDrive/neural-accident-severity/data/Advanced_data_cleaning_step10.csv'
    clean_data(input_path, output_path)
