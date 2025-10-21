

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# --- تنظیمات ---
DATA_PATH = "/content/drive/MyDrive/neural-accident-severity/data/id_columns_step11.csv"
TARGET_COL = "noe_tasadof_id"
OUTPUT_DIR = "/content/drive/MyDrive/neural-accident-severity/data/preprocessed_dataset_step12/"

# --- 1. بارگذاری و بررسی اولیه داده ---
df = pd.read_csv(DATA_PATH)
print("ابعاد اولیه داده:", df.shape)

# حذف سطرهای تکراری
df = df.drop_duplicates()
print("پس از حذف تکراری‌ها:", df.shape)

# حذف ستون‌های اضافی (مثلاً ایندکس‌های ذخیره‌شده)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# --- 2. بررسی و مدیریت مقادیر گم‌شده و نامعتبر ---
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].replace(['nan', 'NaN', '', ' '], np.nan)
    df[col] = df[col].replace([np.inf, -np.inf], np.nan)
print("تعداد کل NaN پس از پاک‌سازی:", df.isna().sum().sum())

# حذف ردیف‌هایی که مقدار هدفشان گم‌شده است
df = df[df[TARGET_COL].notna()]

# --- 3. تقسیم داده ---
X = df.drop(TARGET_COL, axis=1)
y = df[TARGET_COL]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("ابعاد X_train:", X_train.shape, "ابعاد y_train:", y_train.shape)

# --- 4. تعیین نوع ستون‌ها ---
ordinal_cols = []  # khatkeshi_id دیگر ordinal نیست

nominal_cols = [
    c for c in [
        'khatkeshi_id',
        'noe_barkhord_id', 'vaze_roshanaei_id', 'sharayet_sathe_rah_id',
        'noe_shane_id', 'vaze_hava_id', 'mavane_did_id', 'naqayes_moaser_rah_id'
    ] if c in X.columns
]

numeric_cols = [col for col in X.columns if col not in ordinal_cols + nominal_cols]

# --- 5. ساخت pipeline پیش‌پردازش ---
nominal_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

preprocessor = ColumnTransformer(transformers=[
    ('nom', nominal_transformer, nominal_cols),
    ('num', numeric_transformer, numeric_cols)
])

# --- 6. اجرای پیش‌پردازش ---
print("در حال پیش‌پردازش داده‌ها...")
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# --- 7. بررسی نهایی ابعاد و NaN ---
print("ابعاد نهایی X_train:", X_train_processed.shape)
print("NaN در X_train:", np.isnan(X_train_processed).sum())
print("ابعاد نهایی X_test:", X_test_processed.shape)
print("NaN در X_test:", np.isnan(X_test_processed).sum())

# --- 8. ذخیره‌سازی نتایج ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

new_nominal_cols = []
if nominal_cols:
    ohe = preprocessor.named_transformers_['nom']['onehot']
    new_nominal_cols = list(ohe.get_feature_names_out(nominal_cols))
new_columns = new_nominal_cols + numeric_cols  # چون ordinal_cols خالی است

pd.DataFrame(X_train_processed, columns=new_columns).to_csv(
    os.path.join(OUTPUT_DIR, "X_train_processed.csv"), index=False)
pd.DataFrame(X_test_processed, columns=new_columns).to_csv(
    os.path.join(OUTPUT_DIR, "X_test_processed.csv"), index=False)
y_train.reset_index(drop=True).to_frame(TARGET_COL).to_csv(
    os.path.join(OUTPUT_DIR, "y_train.csv"), index=False)
y_test.reset_index(drop=True).to_frame(TARGET_COL).to_csv(
    os.path.join(OUTPUT_DIR, "y_test.csv"), index=False)

print("پیش‌پردازش و ذخیره‌سازی با موفقیت انجام شد.")


