import pandas as pd
df = pd.read_csv('data_files\winequality-red.csv', sep=';')
# df.head()

## OLD CODE

# labels = list(df.columns)
# labels[0] = labels[0].replace(' ', '_')
# labels[1] = labels[1].replace(' ', '_')
# labels[2] = labels[2].replace(' ', '_')
# labels[3] = labels[3].replace(' ', '_')
# labels[5] = labels[5].replace(' ', '_')
# labels[6] = labels[6].replace(' ', '_')
# df.columns = labels
# df.head()


df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

# Alcohol
# a = 'alcohol'
# median_alcohol = df[a].median()
# for i, alcohol in enumerate(df[a]):
#     if alcohol >= median_alcohol:
#         df.loc[i, a] = 'high'
#         # if i < 200:
#         #   print(i, alcohol, median_alcohol)
#     else:
#         df.loc[i, 'alcohol'] = 'low'
# print(df.groupby('alcohol').quality.mean())
# text = df.groupby('alcohol').quality.mean()
# print(text)

# pH
# median_pH = df.pH.median()
# for i, pH in enumerate(df.pH):
#     if pH >= median_pH:
#         df.loc[i, 'pH'] = 'high'
#     else:
#         df.loc[i, 'pH'] = 'low'
# df.groupby('pH').quality.mean()

# Sugar
# median_sugar = df.residual_sugar.median()
# for i, sugar in enumerate(df.residual_sugar):
#     if sugar >= median_sugar:
#         df.loc[i, 'residual_sugar'] = 'high'
#     else:
#         df.loc[i, 'residual_sugar'] = 'low'
# df.groupby('residual_sugar').quality.mean()

# Citric Acid
# median_citric_acid = df.citric_acid.median()
# for i, citric_acid in enumerate(df.citric_acid):
#     if citric_acid >= median_citric_acid:
#         df.loc[i, 'citric_acid'] = 'high'
#     else:
#         df.loc[i, 'citric_acid'] = 'low'
# df.groupby('citric_acid').quality.mean()

def summarize_column(df, column_name):
  median_value = df[column_name].median()
  for i, val in enumerate(df[column_name]):
    if val >= median_value:
      df.loc[i, column_name] = 'high'
    else: 
      df.loc[i, column_name] = 'low'
  return df.groupby(column_name).quality.mean()

# cm_alcohol = summarize_column(df, 'alcohol')
# print(cm_alcohol)

for feature in df.columns[:-1]:
    summarize_column(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')
