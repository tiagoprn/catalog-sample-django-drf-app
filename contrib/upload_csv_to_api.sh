#!/bin/bash
URL='http://localhost:8000/core/csv_import'
FILENAME=sample_success_4.csv

# --data-binary below is needed to keep the line breaks when uploading,
# using just -d will remove them
curl -X POST  -H "Content-Disposition:inline;filename=$FILENAME" $URL --data-binary @$FILENAME
