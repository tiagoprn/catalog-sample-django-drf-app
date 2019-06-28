import csv
import io
import os

from config.settings import CSV_SEPARATOR
from core.models import Pants
from core.serializers import PantsSerializer

header = [
    'brand',
    'model',
    'color',
    'material',
    'cost_price',
    'sell_price',
    'taxes',
]


def import_csv(file_obj):
    errors = []
    imported = []

    try:
        _ = file_obj.encoding == 'UTF-8'
    except AttributeError:
        wrapper = io.TextIOWrapper(
            io.BytesIO(),
            encoding='utf-8',
            line_buffering=True
        )
        for line in file_obj:
            line_str = line.decode()
            wrapper.write(line_str)
        wrapper.seek(0, 0)
        file_obj = wrapper

    reader = csv.DictReader(file_obj, delimiter=CSV_SEPARATOR)

    if not set(header) == set(reader.fieldnames):
        errors.append(f'The CSV does not have all expected columns, '
                      f'which are: {" ".join(header)}')
        return {
            'successful_imports': len(imported),
            'total_errors': len(errors),
            'imported': imported,
            'errors': errors
        }

    if ' '.join(header) != ' '.join(reader.fieldnames):
        errors.append(f'The CSV does not have columns '
                      f'on expected order, '
                      f'which is: {" ".join(header)}')
        return {
            'successful_imports': len(imported),
            'total_errors': len(errors),
            'imported': imported,
            'errors': errors
        }

    for line in enumerate(reader):

        # if isinstance(line, bytes):
        #     line = line.decode()
        #
        # line = line.replace('\n', '').replace('"', '').strip()
        # if line == '':
        #     continue

        filled_fields = []
        col_values = line[1]
        for key in col_values.keys():
            if col_values[key] is not None:
                filled_fields.append(col_values[key])

        if not len(set(filled_fields)) == len(set(header)):
            message = (f'Line {reader.line_num} does not have '
                       f'all expected fields. Remember the '
                       f'CSV separator must be "{CSV_SEPARATOR}".')
            errors.append(message)
            continue

        pants_dict = {
            'brand': line[1]["brand"].strip(),
            'model': line[1]["model"].strip(),
            'color': line[1]["color"].strip(),
            'material': line[1]["material"].strip(),
            'cost_price': float(line[1]["cost_price"].strip()),
            'sell_price': float(line[1]["sell_price"].strip()),
            'taxes': float(line[1]["taxes"].strip())
        }
        serializer = PantsSerializer(data=pants_dict)

        if not serializer.is_valid():
            message = (f'Line number {reader.line_num} could not be imported, '
                       f'it has errors: {serializer.errors}')
            errors.append(message)
            continue

        try:
            pants = Pants(**pants_dict)
            pants.save()
            message = (f'Line number {reader.line_num} was succesfully '
                       f'imported with pants.id={pants.id}')
            imported.append(message)
        except Exception as ex:  # pylint: disable=broad-except
            message = (f'Line number {reader.line_num} could not be '
                       f'imported as a pants record. Exception: {ex}')
            errors.append(message)

    return {
        'successful_imports': len(imported),
        'total_errors': len(errors),
        'imported': imported,
        'errors': errors
    }
