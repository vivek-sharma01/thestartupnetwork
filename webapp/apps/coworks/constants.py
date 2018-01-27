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
    'Virtual Office': 'VO',
    'Business Lounge': 'BL',
    'Hot Desk': 'DD',
    'Meeting Room': 'CR',
    'Dedicated Desk': 'DD',
    'Private Office': 'PS',
    'Virtual Office/Mail box': 'VO',
    'Meeting Rooms for small durations': 'CR',
    'Conference Rooms': 'CR'
}


MEMBERSHIPS_REVERSE_DICT = {
    'CR': 'Conference Room',
    'DD': 'Dedicated Desks',
    'ES': 'Event Space',
    'FD': 'Flexible Desks',
    'PS': 'Private Studios',
    'VO': 'Virtual Office',
    'BL': 'Business Lounge'}

MEMBERSHIPS_91SPRINGBOARD_MAPPING = {
    9: 'Private Studios',
    10: 'Flexible Desks',
    11: 'Conference Room',
    12: 'Virtual Office',
    13: 'Event Space'
}

AMENITIES_FILTER_MAPPING = {
    'Work': 'W',
    'Facilities & Support': 'FS',
    'Events & Activities': 'EA',
    'Food & Kitchen': 'FK',
    'Payable Amenties': 'PA',
    'Other Amenities': 'OA'
}

AMENITIES_FILTER = (
    ('W', _('Work')),
    ('FS', _('Facilities & Support')),
    ('EA', _('Events & Activities')),
    ('FK', _('Food & Kitchen')),
    ('PA', _('Payable Amenties')),
    ('OA', _('Other Amenities')),
)


AMENITIES_FILTER_INDEX = {
    1: 'W',
    2: 'FS',
    3: 'EA',
    4: 'FK',
    5: 'PA',
    6: 'OA'
}


AMENITY_FILTER_CSS = {
    'Work': 'work-ammenties',
    'Facilities & Support': 'support-ammenties',
    'Events & Activities': 'events-ammenties',
    'Food & Kitchen': 'kitchen-ammenties',
    'Payable Amenties': 'unique-ammenties',
    'Other Amenities': 'extra-ammenties'
}

AMENITY_FILTER_REVERSE_MAPPING = {
     'EA': 'Events & Activities',
     'FK': 'Food & Kitchen',
     'FS': 'Facilities & Support',
     'OA': 'Other Amenities',
     'PA': 'Payable Amenties',
     'W': 'Work'
}