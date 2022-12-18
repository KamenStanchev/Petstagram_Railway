from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_file_max_size(value):
    file_size = value.file.size
    megabyte_limit = 5.0
    if file_size > megabyte_limit*1024*1024:
        raise ValidationError(f'Max file size is {megabyte_limit}MB')
