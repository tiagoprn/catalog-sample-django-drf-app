#!/bin/bash
URL='http://localhost:8000/core/csv_import'
FILENAME=sample_error_1.csv

curl -X POST -H "Content-Disposition:inline;filename=$FILENAME" $URL -d @$FILENAME
