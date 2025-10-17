
import pandas as pd
import os

def extract_id_meanings(file_path, output_txt_path):
    df = pd.read_csv(file_path)
    df.columns = [col.strip() for col in df.columns]
    id_text_pairs = {
        'noe_tasadof_id': 'noe_tasadof',
        'noe_barkhord_id': 'noe_barkhord',
        'vaze_roshanaei_id': 'vaze_roshanaei',
        'sharayet_sathe_rah_id': 'sharayet_sathe_rah',
        'noe_shane_id': 'noe_shane',
        'vaze_hava_id': 'vaze_hava',
        'khatkeshi_id': 'khatkeshi'
    }
    mappings = {}
    output_lines = []
    for id_col, text_col in id_text_pairs.items():
        if id_col in df.columns and text_col in df.columns:
            unique_pairs = df[[id_col, text_col]].drop_duplicates().sort_values(by=id_col)
            mapping_dict = dict(zip(unique_pairs[id_col], unique_pairs[text_col]))
            mappings[id_col] = mapping_dict
            output_lines.append(f"\nمعانی ستون '{id_col}':")
            print(f"\nمعانی ستون '{id_col}':")
            for num, text in sorted(mapping_dict.items()):
                line = f"  {num} => {text}"
                print(line)
                output_lines.append(line)
        else:
            warning = f"⚠️ ستون '{id_col}' یا '{text_col}' در داده‌ها یافت نشد."
            print(warning)
            output_lines.append(warning)
    # ذخیره در فایل متنی
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))
    print(f"\n✅ نگاشت‌ها در فایل ذخیره شد: {output_txt_path}")
    return mappings

if __name__ == "__main__":
    file_path = '/content/drive/MyDrive/neural-accident-severity/data/Advanced_data_cleaning_step10.csv'
    output_txt_path = '/content/drive/MyDrive/neural-accident-severity/data/extract_id_meanings_step9_2.txt'
    extract_id_meanings(file_path, output_txt_path)
