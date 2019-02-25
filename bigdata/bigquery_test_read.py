from google.cloud import bigquery as bq
from pprint import pprint
# import bigquery
# client = bigquery.get_client(json_key_file='./bigquery.json')
client = bq.Client()
# Perform a query.
def read_table(table):
    QUERY = ('select * from `august-outlet-229402.bqdb.{}`'.format(table))
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()        # Waits for query to finish
    for row in rows:
        pprint(row)

read_table('Song')