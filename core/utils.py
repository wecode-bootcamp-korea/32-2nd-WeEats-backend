import re

from django.core.exceptions import ValidationError

REGEX_CATEGORY = '[1-6]'
REGEX_ORDER    = '^random$'

def validate_category(category_id):
    if not re.match(REGEX_CATEGORY, category_id):
        raise ValidationError('INVALID_CATEGORY', code=400)

def validate_order_random(category_id):
    if not re.match(REGEX_ORDER, category_id):
        raise ValidationError('INVALID_ORDER', code=400)