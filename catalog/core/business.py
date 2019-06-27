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

    for index, line in enumerate(file_obj.readlines()):
        line_number = index + 1
        line_fields = line.replace('\n', '').replace(
            '"', '').split(CSV_SEPARATOR)

        if line_number == 1:
            if not set(header) == set(line_fields):
                errors.append(f'The CSV does not have all expected columns, '
                              f'which are: {" ".join(header)}')
                return {
                    'successful_imports': len(imported),
                    'total_errors': len(errors),
                    'imported': imported,
                    'errors': errors
                }

            if not (' '.join(header) == ' '.join(line_fields)):
                errors.append(f'The CSV does not have columns '
                              f'on expected order, '
                              f'which is: {" ".join(header)}')
                return {
                    'successful_imports': len(imported),
                    'total_errors': len(errors),
                    'imported': imported,
                    'errors': errors
                }
            continue

        if not len(line_fields) == len(header):
            message = (f'Line {line_number} does not have '
                       f'all expected fields. Remember the '
                       f'CSV separator must be "{CSV_SEPARATOR}".')
            errors.append(message)
            continue

        pants_dict = {
            'brand': line_fields[0].strip(),
            'model': line_fields[1].strip(),
            'color': line_fields[2].strip(),
            'material': line_fields[3].strip(),
            'cost_price': float(line_fields[4].strip()),
            'sell_price': float(line_fields[5].strip()),
            'taxes': float(line_fields[6].strip())
        }
        serializer = PantsSerializer(data=pants_dict)

        if not serializer.is_valid():
            message = (f'Line number {line_number} could not be imported, '
                       f'it has errors.')
            errors.append(message)
            continue

        try:
            pants = Pants(**pants_dict)
            pants.save()
            message = (f'Line number {line_number} was succesfully '
                       f'imported with pants.id={pants.id}')
            imported.append(message)
        except Exception as ex:
            message = (f'Line number {line_number} could not be '
                       f'imported as a pants record. Exception: {ex}')
            errors.append(message)

    return {
        'successful_imports': len(imported),
        'total_errors': len(errors),
        'imported': imported,
        'errors': errors
    }
