# neural-accident-severity
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Neural Accident Severity Classification

Multi-class accident severity prediction using a Neural Network model

Project Overview

This repository contains the implementation, analysis, and preprocessing pipeline for a neural-network–based model aimed at predicting road traffic accident severity.

The project uses a real accident dataset collected from traffic police sources and applies statistical tests and machine learning preprocessing techniques to prepare the final dataset for training.

The target variable has three severity levels:

Property damage

Injury

Fatal

Dataset

The initial dataset consists of 697 accident samples. All features are categorical, representing road, weather, and environmental conditions.

Main input features

Collision Type

Road Surface Condition

Lighting Condition

Weather Condition

Road Defects

Road Shoulder Type

Visibility Obstacles

Road Markings

Target variable

Accident Severity
Three classes:

Property Damage (37 percent, 258 samples)

Injury (55.4 percent, 386 samples)

Fatal (7.6 percent, 53 samples)

Class Imbalance

The original dataset shows an imbalanced distribution, especially for fatal crashes. This was considered in preprocessing and modeling steps.

Statistical Analysis Summary

A Chi-square statistical test was conducted to assess the significance of each feature relative to accident severity.

Key findings show significant effects (p-value < 0.05) for:

Collision Type

Road Surface Condition

Weather Condition

Lighting Condition

Non-significant features:

Shoulder Type

Road Defects

Visibility Obstruction

Road Marking Type

These insights were used during feature selection and designing improvement policies.

Preprocessing

Cleaning missing values

Encoding categorical variables 

Class balancing considerations

Feature selection based on p-values and importance metrics

Model

A supervised multi-class classification neural network:

Input: encoded categorical features

Output activation: Softmax

Loss function: Categorical Cross-Entropy

The final processed dataset is ready for model training, evaluation, and benchmarking.

Applications

The model and statistical findings support:

traffic safety decision-making

risk factor identification

injury and fatality reduction policy design

Future Work

Benchmarking with external datasets

Using class balancing techniques

Hyperparameter optimization

Model comparison with tree-based ML models


Contact

Author: Neda Jalili
Project title: Neural Accident Severity

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#پروژه پیش‌بینی شدت تصادفات جاده‌ای با شبکه عصبی
معرفی پروژه

در این مخزن، پیاده‌سازی و تحلیل یک مدل شبکه عصبی برای پیش‌بینی شدت تصادف جاده‌ای ارائه شده است.
دیتاست اولیه از داده‌های واقعی پلیس راهنمایی و رانندگی تهیه شده و پس از پردازش، برای آموزش مدل آماده گردید.

متغیر هدف دارای سه سطح شدت است:

خسارتی

جرحی

فوتی

مشخصات دیتاست

تعداد نمونه‌ها: ۶۹۷ تصادف
تمام ویژگی‌ها کیفی بوده و شرایط محیطی، جاده‌ای و حادثه را توصیف می‌کنند.

ویژگی‌های اصلی

نوع برخورد

شرایط سطح راه

شرایط روشنایی

شرایط آب و هوا

نقایص موثر راه

نوع شانه

موانع دید

خط‌کشی

توزیع شدت تصادفات

جرحی: ۵۵.۴ درصد (۳۸۶ نمونه)

خسارتی: ۳۷ درصد (۲۵۸ نمونه)

فوتی: ۷.۶ درصد (۵۳ نمونه)

این توزیع نشان‌دهنده عدم توازن کلاس‌ها در داده است.

نتایج تحلیل آماری

طبق آزمون آماری کای-اسکوئر (p-value < 0.05):

ویژگی‌های موثر بر شدت تصادف:

نوع برخورد

شرایط سطح راه

شرایط آب و هوا

شرایط روشنایی

ویژگی‌های بدون تأثیر معنادار:

خط‌کشی

نوع شانه

نقایص موثر راه

موانع دید

این نتایج در طراحی مدل و استخراج سیاست‌های ایمنی استفاده شده است.

پردازش داده

پاک‌سازی داده

تبدیل مقادیر کیفی به عددی

انتخاب ویژگی‌های موثر

توجه به عدم توازن کلاس‌ها

مدل شبکه عصبی

مدل از نوع طبقه‌بندی چندکلاسه بوده و خروجی آن احتمال هر شدت تصادف است.
توابع مورد استفاده:

Softmax در لایه خروجی

Loss: Cross-Entropy

کاربردها

تحلیل ریسک تصادف

طراحی مداخلات کاهش جراحات و فوتی

ارائه پیشنهادهای سیاستی‌ برای راهنمایی و رانندگی


اطلاعات تماس

تهیه‌کننده پروژه: ندا جلیلی
عنوان پروژه: پیش‌بینی شدت تصادفات (Neural Accident Severity)
