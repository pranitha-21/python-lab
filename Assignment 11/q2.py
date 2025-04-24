import pandas as pd
s=pd.Series(['X','Y','Y','Aaba','Baca','CABA','None','bird','horse','dog'])
print("original series:")
print(s)


upper_case_s=s.str.upper()
print("Upper case serie:")
print(upper_case_s)

print("Lower case series")
print(s.str.lower())

print("Length of string values")
print(s.str.len())
