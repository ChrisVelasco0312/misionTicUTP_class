from developers import devs
import pandas as pd

# ids = [dev['cc'] for dev in devs]
ids = list(map(lambda x: x['cc'], devs))
salarios = list(map(lambda x: x['Salario'], devs))

print(ids)
print(salarios)

devs_data_frame = pd.DataFrame(
    {'document': [doc for doc in ids], 'salary': [sal for sal in salarios]})

print(devs_data_frame)
