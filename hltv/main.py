import update_stats
import pandas as pd

data = update_stats.get_stats()

df = pd.DataFrame(data)

print(df)