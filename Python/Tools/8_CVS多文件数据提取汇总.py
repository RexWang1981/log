import pandas as pd
import os

# 获取CSV文件路径列表
csv_files = ['1 _2024-05-30_17-32-40_screen.CSV', '2 _2024-05-30_17-32-57_screen.CSV', '3 _2024-05-30_17-33-15_screen.CSV']  # 这里填入你的CSV文件名列表在·

# 临时存储所有数据的列表
data_list = []
file_names = []

# 读取每个CSV文件的数据，并存储文件名
for csv_file in csv_files:
    df = pd.read_csv(csv_file, usecols=[0, 1])
    data_list.append(df)
    file_names.append(os.path.basename(csv_file))

# 计算最终的 DataFrame 大小
num_files = len(csv_files)
max_rows = max(df.shape[0] for df in data_list)
total_cols = num_files * 3 - 1  # 每个文件2列数据+1列间隔

# 创建一个空的 DataFrame
summary_df = pd.DataFrame(index=range(max_rows + 1), columns=range(total_cols))

# 添加文件名作为来源
for i, file_name in enumerate(file_names):
    summary_df.iloc[0, i * 3] = file_name

# 添加每个文件的数据到 DataFrame
for i, df in enumerate(data_list):
    start_col = i * 3 + 1
    end_col = start_col + 2
    summary_df.iloc[1:len(df) + 1, start_col:end_col] = df.values

# 创建一个Excel writer对象
excel_writer = pd.ExcelWriter('merged_data.xlsx', engine='openpyxl')

# 将汇总数据写入到Excel文件的一个sheet中
summary_df.to_excel(excel_writer, index=False, header=False, sheet_name='MergedData')

# 保存Excel文件
excel_writer.save()