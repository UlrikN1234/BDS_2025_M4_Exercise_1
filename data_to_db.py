import pandas as pd
import seaborn as sns
import sqlite3

# Loading the Penguins dataset
penguins = sns.load_dataset("penguins").dropna()

# Prepare DataFrames for Tables
islands_df = pd.DataFrame({'island_id': range(1, penguins['island'].nunique() + 1),
                           'name': penguins['island'].unique()})

# Assign each penguin an animal_id
penguins['animal_id'] = range(1, len(penguins) + 1)

# Merge penguins dataset with island_id mapping
penguins_df = penguins.merge(islands_df, left_on='island', right_on='name', how='left')[
    ['species', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex', 'island_id', 'animal_id']
]

# Create SQLite Database
conn = sqlite3.connect('penguins.db')
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON;")

# Create ISLANDS table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ISLANDS (
    island_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
)
''')

# Create PENGUINS table WITHOUT a primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS PENGUINS (
    species TEXT,
    bill_length_mm REAL,
    bill_depth_mm REAL,
    flipper_length_mm REAL,
    body_mass_g REAL,
    sex TEXT,
    island_id INTEGER,
    animal_id INTEGER,
    FOREIGN KEY (island_id) REFERENCES ISLANDS(island_id)
)
''')
# Insert Data into Tables
islands_df.to_sql('ISLANDS', conn, if_exists='append', index=False)
penguins_df.to_sql('PENGUINS', conn, if_exists='append', index=False)

# Close Connection
conn.close()

print("Database created successfully!")