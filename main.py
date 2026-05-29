import csv

def chiqar_csv(fayl_ismi):
    with open(fayl_ismi, 'r') as f:
        csv_reader = csv.reader(f)
        for satr in csv_reader:
            print(satr)

chiqar_csv('ma'lumotlar.csv')
```

```python
import pandas as pd

def chiqar_csv(fayl_ismi):
    df = pd.read_csv(fayl_ismi)
    print(df)

chiqar_csv('ma\'lumotlar.csv')
