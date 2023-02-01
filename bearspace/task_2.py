import pandas as pd
import re


def fix_number(number, unit='cm'):
    if number:
        number = float(number.strip().replace(',', '.'))
        if unit == 'in':
            number = number * 2.54
        return number


items = []
dim_df = pd.read_csv("candidateEvalData/dim_df_correct.csv")
for row in dim_df["rawDim"]:
    regex = r"((?<![\/])(?:\d+(?:[.,]\d+)?(?:\s|by|×|x)*)+?)(?=cm|in)"
    if 'Image:' in row:
        row = row.split('Image:')[1].strip()
    unit = 'cm'
    if 'in' in row and 'cm' not in row:
        unit = 'in'
    founds = re.findall(regex, row)
    if founds and len(founds) == 1:
        found = re.split('×|x|by', founds[0])
        height = found[0] if found else None
        width = found[1] if len(found) > 1 else None
        depth = found[2] if len(found) > 2 else None
        item = {
            'rawDim': row,
            'height': fix_number(height, unit),
            'width': fix_number(width, unit),
            'depth': fix_number(depth, unit)
        }
        items.append(item)

df = pd.DataFrame.from_records(items)
print(df)
df.to_csv('task_2.csv', index=False)
