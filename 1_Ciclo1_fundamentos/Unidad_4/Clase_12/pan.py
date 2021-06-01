import pandas as pd

serie1 = pd.Series([6, 12, 3], index=['dia', 'mes', 'año'])
print(serie1)

serie2 = pd.Series({'dia': 26, 'mes': 5, 'año': 2021})
print(serie2)

frame1 = pd.DataFrame({'dia': [25, 26], 'mes': [5, 5], 'año': [2021, 2021]})
print(frame1)

frame2 = pd.DataFrame([[65, 25, 87], [45, 67, 57], [
                      29, 45, 98]], columns=['dias', 'meses', 'años'])
print(frame2)
