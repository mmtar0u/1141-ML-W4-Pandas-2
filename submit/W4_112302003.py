# -*- coding: utf-8 -*-
"""
Pandas 基礎操作課堂練習：學生期中成績分析
"""

import pandas as pd

def load_and_explore_data(file_path):
"""任務一：讀取 CSV 並初步探索資料"""
df = pd.read_csv(file_path, encoding='utf-8-sig')

# TODO 1.1: 顯示前 5 筆資料（指派變數後輸出，避免無效呼叫）
head5 = df.head(5)
print("\n--- 前五筆資料 ---")
print(head5)

# TODO 1.2: 查看資料結構（欄位、型態、缺失值）
print("\n--- 資料結構 ---")
df.info()

nulls = df.isnull().sum() # 指派變數後輸出
print("\n--- 缺失值統計 ---")
print(nulls)

return df

def feature_engineering(df):
"""任務二：計算總分、平均分數與是否及格"""
# TODO 2.1: 計算總分
df['總分'] = df['數學'] + df['英文'] + df['國文'] + df['自然'] + df['社會']

# TODO 2.2: 計算平均分數
df['平均'] = df['總分'] / 5

# TODO 2.3: 新增是否及格欄位（平均 >= 60 為及格）
df['是否及格'] = df['平均'] >= 60

print("\n計算總分、平均分數與是否及格")
print(df)

return df

def filter_and_analyze_data(df):
"""任務三與四：篩選資料與統計"""

# TODO 3.1: 找出數學成績 < 60 的學生
math_failed = df[df['數學'] < 60]
print("\n--- 數學不及格學生 ---")
print(math_failed)

# TODO 3.2: 找出班級為 'A' 且英文 > 90 的學生
high_A = df[(df['班級'] == 'A') & (df['英文'] > 90)]
print("\n--- A班英文 > 90 的學生 ---")
print(high_A)

# TODO 4.1: 統計摘要（移除未使用的 describe(include='all')）
summary = df.describe()
print("\n--- 統計摘要 ---")
print(summary)

# TODO 4.2: 找出總分最高的學生（依建議調整敘事順序）
max_total = df['總分'].max()
top_series = df.loc[df['總分'].idxmax(), ['姓名', '總分']] # 先取出姓名/總分（Series）
top_student = df[df['總分'] == max_total] # 再保留完整列資料（DataFrame）

print("\n--- 總分最高的學生 ---")
print(top_series)

# 回傳 dict，方便 pytest 檢查每個任務
return {
"processed_df": df,
"math_failed": math_failed,
"high_A": high_A,
"summary": summary,
"top_student": top_student
}

def save_results(df, output_file_path):
"""任務五：儲存為 CSV（加入例外處理）"""
try:
df.to_csv(output_file_path, index=False, encoding="utf-8-sig")
except FileNotFoundError as e:
print(f"\n儲存失敗：FileNotFoundError - {e}")
return False
except PermissionError as e:
print(f"\n儲存失敗：PermissionError - {e}")
return False
else:
print(f"\n結果已儲存至 {output_file_path}")
return True

if __name__ == "__main__":
INPUT_CSV = "grades.csv"
OUTPUT_CSV = "grades_analyzed.csv"

df = load_and_explore_data(INPUT_CSV)
df = feature_engineering(df)
result = filter_and_analyze_data(df)
save_results(result["processed_df"], OUTPUT_CSV)

print("完成所有分析任務")
