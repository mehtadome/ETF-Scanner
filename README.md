# ETF Scanner

Pulls from locally saved CSVs to .

## Lifetime of Pandas Tables

Duration of the python script run. Consider using the following formats to save parsing:

### Pickle

Preserves pandas objects and data types.

```
# Store as pickle file
df_etf.to_pickle('data.pkl')

# Later, load it back:
df = pd.read_pickle('data.pkl')
```

- [More info](https://www.datacamp.com/tutorial/pickle-python-tutorial).

### SQLAlchemy

Object-relational Mapper (ORM) Database which preserves object mapping.

```
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db')
df_etf.to_sql('table_name', engine)
```

- [More info](https://docs.sqlalchemy.org/en/14/orm/tutorial.html).

## Data Encountered

Empty, --, Nan
