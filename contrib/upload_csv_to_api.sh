#!/bin/bash
URL='http://localhost:8000/core/csv_import'
FILENAME=sample_success_4.csv

curl -X POST -H "Content-Disposition:inline;filename=$FILENAME" $URL -d @$FILENAME
