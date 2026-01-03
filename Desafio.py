import pandas as pd
from pathlib import Path
import os
import datetime

def __apagarTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

source_file_path = Path("Survey.csv")
source_file = pd.read_csv(source_file_path, sep = ";")

print(source_file_path.parent.absolute())

df = pd.DataFrame(source_file)
print(df)

moreThan30 = df["Age"] > 30
lessThan45 = df["Age"] < 45

print(df[moreThan30 & lessThan45])

df2 = df[moreThan30 & lessThan45]

print(df2)


final_file_path = Path("Result.csv")
df2.to_csv(final_file_path, sep = ";")