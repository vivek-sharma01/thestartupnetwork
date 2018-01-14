from django.utils.translation import ugettext_lazy as _

MEMBERSHIPS = (
    ('CR', _('Conference Room')),
    ('DD', _('Dedicated Desks')),
    ('ES', _('Event Space')),
    ('FD', _('Flexible Desks')),
    ('PS', _('Private Studios')),
    ('VO', _('Virtual Office')),
)

MEMBERSHIPS_DICT = {
    'Conference Room': 'CR',
    'Dedicated Desks': 'DD',
    'Event Space': 'ES',
    'Flexible Desks': 'FD',
    'Private Studios': 'PS',
    'Virtual Office': 'VO'
}


MEMBERSHIPS_REVERSE_DICT = {
    'CR': 'Conference Room',
    'DD': 'Dedicated Desks',
    'ES': 'Event Space',
    'FD': 'Flexible Desks',
    'PS': 'Private Studios',
    'VO': 'Virtual Office'}

MEMBERSHIPS_91SPRINGBOARD_MAPPING = {
    9: 'Private Studios',
    10: 'Flexible Desks',
    11: 'Conference Room',
    12: 'Virtual Office',
    13: 'Event Space'
}
