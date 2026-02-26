import requests
import io
import pandas as pd

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
query = """
SELECT
pl_name,
discoverymethod,
pl_masse,
pl_masseerr1,
pl_masseerr2,
pl_rade,
pl_radeerr1,
pl_radeerr2,
pl_orbeccen,
st_mass
FROM
pscomppars
WHERE
pl_masse IS NULL OR pl_rade IS NULL
"""

params = {"query": query, "format": "csv"}

try:
    res = requests.get(url, params=params)
    df = pd.read_csv(io.StringIO(res.text))
    print(df)
except:
    print("Error")
