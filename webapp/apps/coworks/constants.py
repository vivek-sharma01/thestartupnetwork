from django.utils.translation import ugettext_lazy as _

MEMBERSHIPS = (
    ('CR', _('Conference Room')),
    ('DD', _('Dedicated Desks')),
    ('ES', _('Event Space')),
    ('FD', _('Flexible Desks')),
    ('PS', _('Private Office')),
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
    'PS': 'Private Office',
    'VO': 'Virtual Office',
    'BL': 'Business Lounge'}


MEMBERSHIPS_ORDERING = {
    'CR': 6,
    'DD': 2,
    'ES': 7,
    'FD': 1,
    'PS': 3,
    'VO': 4,
    'BL': 5}

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

AMENITY_FILTER_GROUP = {
    'Work': [],
    'Facilities & Support': [],
    'Events & Activities': [],
    'Food & Kitchen': [],
    'Payable Amenties': [],
    'Other Amenities': []
}

AMENITY_FILTER_REVERSE_MAPPING = {
     'EA': 'Events & Activities',
     'FK': 'Food & Kitchen',
     'FS': 'Facilities & Support',
     'OA': 'Other Amenities',
     'PA': 'Payable Amenties',
     'W': 'Work'
}


ENQUIRY_REASON = {
    'day pass': 'Day Pass Request for {}',
    'membership enquiry': 'Membership Request',
    'message': 'Message'
}

MEMBERSHIP_ENQUIRY_MAIL_TEXT = """
Hi,<br><br>

    Greeting from <a href="https://www.thestartupnetwork.in/">The Startup Network!</a><br><br>

    <b>You have received a customer enquiry.</b><br><br>

    Venue:- {}<br><br>

    Enquiry Details<br><br>

    Enquiry Type:- {}<br>
    Customer Name:- {}<br>
    Contact Number:- {}<br>
    Email id:- {}<br><br>

    In case of any query, reply to the same mail."""

MEMBERSHIP_ENQUIRY_MAIL_SUBJECT = "{} | Customer Enquiry | The Startup Network"

