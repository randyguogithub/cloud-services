from __future__ import absolute_import
import sys
import os

from google.cloud import bigquery

try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
except:
    print("Please check if \"key.json\" file exists.")

# https://pydata-google-auth.readthedocs.io/en/latest/cli.html#loading-user-credentials-with-print-token
#  access token associate with the credentials at ~/keys/google-credentials.json.  

projectid = 'local-bastion-154121'
filename = 'master.csv'	# pass csv filename as commandline argument
dataset_id = 'Property_Dataset'
table_id = 'pmDATA'
tablefullname = projectid+"."+dataset_id+"."+table_id

print('Connecting to BigQuery Database.')
client = bigquery.Client(project=projectid)

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True

job_config.schema = [
    bigquery.SchemaField('company_name','STRING'),
    bigquery.SchemaField('contacts','STRING'),
    bigquery.SchemaField('address','STRING'),
    bigquery.SchemaField('city','STRING'),
    bigquery.SchemaField('state','STRING'),
    bigquery.SchemaField('zipcode','STRING'),
    bigquery.SchemaField('designation','STRING'),
    bigquery.SchemaField('first_name','STRING'),
    bigquery.SchemaField('last_name','STRING'),
    bigquery.SchemaField('phone','STRING'),
    bigquery.SchemaField('mobile','STRING'),
    bigquery.SchemaField('email','STRING'),
    bigquery.SchemaField('email_2','STRING'),
    bigquery.SchemaField('website','STRING'),
    bigquery.SchemaField('doors','STRING'),
]

print('Creating Upload Job')
with open(filename, 'rb') as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        location='US',  # Must match the destination dataset location.
        job_config=job_config)  # API request

print('Uploading Data into BigQuery Table')

job.result()  # Waits for table load to complete.

print('Loaded {} rows into {}:{}.'.format(job.output_rows, dataset_id, table_id))