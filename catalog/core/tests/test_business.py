import os

import pytest

from config.settings import PROJECT_ROOT, CSV_SEPARATOR
from core.business import import_csv
from core.models import Pants

ERROR_FILE_1 = os.path.join(PROJECT_ROOT, 'contrib/sample_error_1.csv')
ERROR_FILE_2 = os.path.join(PROJECT_ROOT, 'contrib/sample_error_2.csv')
ERROR_FILE_3 = os.path.join(PROJECT_ROOT, 'contrib/sample_error_3.csv')
SUCCESS_FILE_1 = os.path.join(PROJECT_ROOT, 'contrib/sample_success_1.csv')
SUCCESS_FILE_2 = os.path.join(PROJECT_ROOT, 'contrib/sample_success_2.csv')
SUCCESS_FILE_3 = os.path.join(PROJECT_ROOT, 'contrib/sample_success_3.csv')
SUCCESS_FILE_4 = os.path.join(PROJECT_ROOT, 'contrib/sample_success_4.csv')


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


@pytest.mark.django_db
def test_csv_import_with_success():
    with open(SUCCESS_FILE_1, 'r') as success_file:
        result = import_csv(success_file)
        assert Pants.objects.count() > 0
        assert result['successful_imports'] == 1
        assert result['total_errors'] == 0


@pytest.mark.parametrize(('file_name'), [
    (SUCCESS_FILE_2),
    (SUCCESS_FILE_3)
])
@pytest.mark.django_db
def test_csv_import_with_success_when_double_quotes_on_fields():
    with open(SUCCESS_FILE_1, 'r') as success_file:
        result = import_csv(success_file)
        assert Pants.objects.count() > 0
        assert result['successful_imports'] == 1
        assert result['total_errors'] == 0


@pytest.mark.django_db
def test_csv_import_with_multiple_lines_success():
    with open(SUCCESS_FILE_4, 'r') as success_file:
        result = import_csv(success_file)
        assert Pants.objects.count() == 11
        assert result['successful_imports'] == 11
        assert result['total_errors'] == 1
