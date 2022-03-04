import pandas as pd

puppy_df = pd.read_csv('c:\\Users\\mppra\\PycharmProjects\\tek-manickapremchand-python2\\manickapremchand_saiprashanthi_python2\\puppy.csv')

owner_df = pd.read_csv('c:\\Users\\mppra\\PycharmProjects\\tek-manickapremchand-python2\\manickapremchand_saiprashanthi_python2\\owner.csv')

print("Puppy Table Count using len: ", len(puppy_df))
print("Owner Table Count using len: ", len(owner_df))

print("Puppy Table Columns Count: ", len(puppy_df.columns))
print("Owner Table Columns Count: ", len(owner_df.columns))

print("Group-by Eye Color")
by_eyecolor = puppy_df.groupby('Eye_Color')
print(by_eyecolor.size().reset_index(name='counts'))