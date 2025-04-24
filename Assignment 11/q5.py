import pandas as pd
import itertools

data={'artist':['A','B','A','C','B','A','C'], 'venue':['X','Y','Y','X','X','X','Y'], 'date': pd.to_datetime(['2023-01-15','2023-01-20','2023-02-10','2023-02-25','2024-02-05','2024-01-18','2024-02-22'])}
concerts_df=pd.DataFrame(data)

artists=concerts_df['artist'].unique()
venues=concerts_df['venue'].unique()

artist_venue_pairs=pd.MultiIndex.from_product([artists,venues],names=['artist','venue'])
artist_venue_series=pd.Series(index=artist_venue_pairs)

print("All possible pairs:")
print(artist_venue_series.index.tolist())

concerts_df['year_month']=concerts_df['date'].dt.to_period('M')

concert_counts=concerts_df.groupby(['year_month','artist','venue']).size().reset_index(name='count')

wide_table=concert_counts.pivot_table(index='year_month',columns=['artist','venue'],values='count',fill_value=0)

wide_table=wide_table.reindex(columns=artist_venue_series.index,fill_value=0)
print("\n wide table of concert counts per pair per year_month:")
print(wide_table)
