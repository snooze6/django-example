from Flickr import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'CopyRight'),
    (COPYLEFT, 'CopyLeft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)
BADWORDS = getattr(settings, 'PROJECT_BADWORDS', [])