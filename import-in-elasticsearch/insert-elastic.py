from lawsByRowWithParentAsObject import laws
from datetime import datetime
from elasticsearch import Elasticsearch
import uuid
import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-I", "--index", help="Indicate the index name for elasticsearch")

# read arguments from the command line
args = parser.parse_args()
index_name = args.index

es = Elasticsearch()
# Insert all row from lawsArrayFromJS into elasticsearch
for article in laws:
    res = es.index(index=index_name, doc_type='_doc', id=uuid.uuid4(), body=article)