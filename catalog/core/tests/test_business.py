import os

import pytest

from config.settings import PROJECT_ROOT, CSV_SEPARATOR
from core.business import import_csv

ERROR_FILE_1 = os.path.join(PROJECT_ROOT, 'contrib/sample_error_1.csv')
ERROR_FILE_2 = os.path.join(PROJECT_ROOT, 'contrib/sample_error_2.csv')
ERROR_FILE_3 = os.path.join(PROJECT_ROOT, 'contrib/sample_error_3.csv')


@pytest.mark.django_db
def test_csv_import_with_errors_when_not_expected_columns():
    with open(ERROR_FILE_1, 'r') as error_file:
        result = import_csv(error_file)
        assert result == {
            'successful_imports': 0,
            'total_errors': 1,
            'imported': [],
            'errors': ["The CSV does not have all expected columns, "
                       "which are: brand model color material "
                       "cost_price sell_price taxes"]}


@pytest.mark.django_db
def test_csv_import_with_errors_when_columns_not_expected_order():
    with open(ERROR_FILE_2, 'r') as error_file:
        result = import_csv(error_file)
        assert result == {
            'successful_imports': 0,
            'total_errors': 1,
            'imported': [],
            'errors': ["The CSV does not have columns "
                       "on expected order, which is: "
                       "brand model color material "
                       "cost_price sell_price taxes"]}


@pytest.mark.django_db
def test_csv_import_with_errors_when_not_all_fields_on_second_line():
    with open(ERROR_FILE_3, 'r') as error_file:
        result = import_csv(error_file)
        assert result == {
            'successful_imports': 0,
            'total_errors': 1,
            'imported': [],
            'errors': [f'Line 2 does not have all expected fields. ' 
                       f'Remember the CSV separator must be '
                       f'"{CSV_SEPARATOR}".']}
