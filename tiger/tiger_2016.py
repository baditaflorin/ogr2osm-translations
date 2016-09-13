'''
A translation function for Tiger 2016 roads data.

'''

def translateName(rawname):
    '''
    A general purpose name expander.
    '''
    suffixlookup = {
    'Ave':'Avenue',
    'Rd':'Road',
    'Co':'County',
    'St':'Street',
    'Pl':'Place',
    'Cres':'Crescent',
    'Blvd':'Boulevard',
    'Dr':'Drive',
    'Lane':'Lane',
    'Crt':'Court',
    'Ter':'Terrace',
    'Gr':'Grove',
    'Cl':'Close',
    'Rwy':'Railway',
    'Div':'Diversion',
    'Hwy':'Highway',
    'Hwy':'Highway',
    'Conn': 'Connector',
    'E':'East',
    'S':'South',
    'Sw':'Southwest',
    'Se':'Southeast',
    'N':'North',
    'Nw':'Northwest',
    'Ne':'Northeast',
    'W':'West'}

    '''TOFIX St sometimes means Saint, we shoudl fix this '''

    newName = ''
    for partName in rawname.split():
        newName = newName + ' ' + suffixlookup.get(partName,partName)

    return newName.strip()


def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    if 'FULLNAME' in attrs:
        translated = translateName(attrs['FULLNAME'].title())
        if translated != '(Lane)' and translated != '(Ramp)':
            tags['name'] = translated

    if 'MTFCC' in attrs:
        if attrs['MTFCC'].strip() == 'S1100':
            tags['highway'] = 'motorway'
        elif attrs['MTFCC'].strip() == 'S1200':
            tags['highway'] = 'secondary'
        elif attrs['MTFCC'].strip() == 'S1400':
            tags['highway'] = 'unclassified'
        elif attrs['MTFCC'].strip() == 'S1500':
            tags['highway'] = 'track'
            tags['surface'] = 'unpaved'
        elif attrs['MTFCC'].strip() == 'S1630':
            tags['highway'] = 'motorway_link'
            tags['fixme'] = 'some inconsistency can be with this tag, manual check needed'
        elif attrs['MTFCC'].strip() == 'S1640':
            tags['highway'] = 'service'
        elif attrs['MTFCC'].strip() == 'S1710':
            tags['highway'] = 'pedestrian'
        elif attrs['MTFCC'].strip() == 'S1720':
            tags['highway'] = 'steps'
        elif attrs['MTFCC'].strip() == 'S1730':
            tags['highway'] = 'service'
            tags['service'] = 'alley'
        elif attrs['MTFCC'].strip() == 'S1740':
            tags['highway'] = 'service'
            tags['access'] = 'private'
        elif attrs['MTFCC'].strip() == 'S1750':
            tags['highway'] = 'service'
            tags['access'] = 'private'
        elif attrs['MTFCC'].strip() == 'S1780':
            tags['highway'] = 'service'
            tags['service'] = 'parking_aisle'
        elif attrs['MTFCC'].strip() == 'S1820':
            tags['highway'] = 'cycleway'
        elif attrs['MTFCC'].strip() == 'S1830':
            tags['highway'] = 'bridleway'
        elif attrs['MTFCC'].strip() == 'S2000':
            tags['highway'] = 'test'
            tags['surface'] = 'gravel'
        else:
            tags['highway'] = 'unsure'
            tags['fixme'] = attrs['what type of road i am ?']

        tags['source'] = 'Tiger 2016 GIS dataset'

    return tags
