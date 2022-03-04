import pandas as pd
import sqlalchemy as sqlalchemy


con = sqlalchemy.create_engine("mysql+pymysql://root:Manicka1983@localhost/puppy_db")

#Cleaning the existing data before loading the data from CSV file
#Also resetting the ID index to 1
con.execute('DELETE FROM OWNERS')
con.execute('DELETE FROM PUPPIES')
con.execute('ALTER TABLE puppies AUTO_INCREMENT=1')
con.execute('ALTER TABLE owners AUTO_INCREMENT=1')

puppy_df = pd.read_csv('c:\\Users\\mppra\\PycharmProjects\\tek-manickapremchand-python2\\manickapremchand_saiprashanthi_python2\\puppy.csv')
print('############ PUPPIES #############')
print(puppy_df)
print('############  #############')
puppy_df.to_sql("puppies", con, if_exists="append", index=False)

owner_df = pd.read_csv('c:\\Users\\mppra\\PycharmProjects\\tek-manickapremchand-python2\\manickapremchand_saiprashanthi_python2\\owner.csv')
print('############ OWNERS #############')
print(owner_df)
print('############  #############')
owner_df.to_sql("owners", con, if_exists="append", index=False)