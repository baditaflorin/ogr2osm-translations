import re


def filterTags(attrs):
    with open("log.txt", "a") as log_file:
        log_file.write("called")
    if not attrs:
        with open("log.txt", "a") as log_file:
            log_file.write("no attributes")
        return
    tags = {}

    # DO NOT DELETE THESE ROWS IF YOU WANT TO REPLACE ABBREVIATIONS
    # PLEASE REPLACE "PRIME_NAME" WITH THE NAME OF THE FIELD CONTAINING THE ROAD NAMES

    name_column = "FULLNAME"  # REPLACE WITH YOUR COLUMN

    # convert names to Title Case
    attrs[name_column] = attrs[name_column].title()

    # replace cardinal direction abbreviations
    attrs[name_column] = re.sub('S$', 'South', attrs[name_column])  # finds S at end of name
    attrs[name_column] = attrs[name_column].replace("S ", "South ", 1)  # finds S at beginning of name
    attrs[name_column] = re.sub('W$', 'West', attrs[name_column])
    attrs[name_column] = attrs[name_column].replace("W ", "West ", 1)
    attrs[name_column] = re.sub('E$', 'East', attrs[name_column])
    attrs[name_column] = attrs[name_column].replace("E ", "East ", 1)
    attrs[name_column] = re.sub('N$', 'North', attrs[name_column])
    attrs[name_column] = attrs[name_column].replace("N ", "North ", 1)

    # replace street type abbreviations
    attrs[name_column] = attrs[name_column].replace(" St ", " Street ")
    attrs[name_column] = attrs[name_column].replace("Rd", "Road")
    attrs[name_column] = attrs[name_column].replace(" Pl ", " Place ")
    attrs[name_column] = attrs[name_column].replace("Ave ", "Avenue ")
    attrs[name_column] = attrs[name_column].replace("Cv", "Cove")
    attrs[name_column] = attrs[name_column].replace(" Dr", " Drive")
    attrs[name_column] = attrs[name_column].replace("Ln", "Lane")
    attrs[name_column] = attrs[name_column].replace("Cir", "Circle")
    attrs[name_column] = attrs[name_column].replace("Ter", "Terrace")
    attrs[name_column] = attrs[name_column].replace("Blvd", "Boulevard")
    attrs[name_column] = attrs[name_column].replace("Bldv", "Boulevard")
    attrs[name_column] = attrs[name_column].replace("Ct", "Court")
    attrs[name_column] = attrs[name_column].replace("Hwy", "Highway")
    attrs[name_column] = attrs[name_column].replace("Fwy", "Freeway")
    attrs[name_column] = attrs[name_column].replace(" Aly ", " Alley ")
    attrs[name_column] = attrs[name_column].replace("Pkwy", "Parkway")
    attrs[name_column] = attrs[name_column].replace("Cres ", "Crescent ")
    attrs[name_column] = attrs[name_column].replace(" S ", " South ")
    attrs[name_column] = attrs[name_column].replace(" N ", " North ")
    attrs[name_column] = attrs[name_column].replace(" E ", " East ")
    attrs[name_column] = attrs[name_column].replace(" W ", " West ")
    attrs[name_column] = attrs[name_column].replace("Rte", "Route")
    attrs[name_column] = attrs[name_column].replace("Crst", "Crest")
    attrs[name_column] = attrs[name_column].replace("Expy", "Expressway")
    attrs[name_column] = attrs[name_column].replace("Mnr", "Manor")
    attrs[name_column] = attrs[name_column].replace("Trl", "Trail")
    attrs[name_column] = attrs[name_column].replace("Hl", "Hill")
    attrs[name_column] = attrs[name_column].replace("Mdws", "Meadows")
    attrs[name_column] = attrs[name_column].replace(" Sq ", " Square ")
    attrs[name_column] = attrs[name_column].replace(" Con ", " Connection ")
    attrs[name_column] = attrs[name_column].replace("Apt", "Apartment")
    attrs[name_column] = attrs[name_column].replace("Apts", "Apartments")
    attrs[name_column] = attrs[name_column].replace("Lndg", "Landing")
    attrs[name_column] = attrs[name_column].replace("Crk", "Creek")
    attrs[name_column] = attrs[name_column].replace("Brg", "Bridge")
    attrs[name_column] = attrs[name_column].replace("Plz", "Plaza")
    attrs[name_column] = attrs[name_column].replace("Clb", "Club")
    attrs[name_column] = attrs[name_column].replace("Tpke", "Turnpike")
    attrs[name_column] = attrs[name_column].replace(" Pt ", " Point ")
    attrs[name_column] = attrs[name_column].replace("Pte", "Pointe")
    attrs[name_column] = attrs[name_column].replace("Hts", "Heights")

    # special cases for replacing some abbreviations at the end of the name
    if attrs[name_column].endswith(" St"):
        attrs[name_column] = attrs[name_column].replace(" St", " Street")
    if attrs[name_column].endswith(" Pl"):
        attrs[name_column] = attrs[name_column].replace(" Pl", " Place")
    if attrs[name_column].endswith(" Ave"):
        attrs[name_column] = attrs[name_column].replace(" Ave", " Avenue")
    if attrs[name_column].endswith(" Sq"):
        attrs[name_column] = attrs[name_column].replace(" Sq", " Square")
    if attrs[name_column].endswith(" Con"):
        attrs[name_column] = attrs[name_column].replace(" Con", " Connection")
    if attrs[name_column].endswith(" Aly"):
        attrs[name_column] = attrs[name_column].replace(" Aly", " Alley")
    if attrs[name_column].endswith(" Pt"):
        attrs[name_column] = attrs[name_column].replace(" Pt", " Point")

        # MODIFY THESE TO SUIT YOUR NEEDS

    tags.update({'highway': highway_class(attrs['MTFCC'])})

    if attrs['MTFCC'] == '0':
            tags.update({'access': 'private'})
    elif attrs['MTFCC'] == '12':
        tags.update({'access': 'no'})
    elif attrs['MTFCC'] == 'S1730':
        tags.update({'service': 'alley'})
    elif attrs['MTFCC'] == 'S1740':
        tags.update({'access': 'private'})
    elif attrs['MTFCC'] == 'S1750' and attrs['FULLNAME'] == 'Driveway':
        del tags['name']
    elif attrs['MTFCC'] == 'S1780':
        tags.update({'service': 'parking_aisle'})

        tags.update({'tiger:linearid': attrs['LINEARID']})
    tags.update({'tiger:source': 'TIGER 2017 shp2cygnus data processing'})

    if "OBJECTID" in attrs:
        tags["highway"] = "road"

    if name_column in attrs:
        tags["name"] = attrs[name_column]

    if "ONEWAY" in attrs:
        if attrs["ONEWAY"].strip() == "TF":
            tags["oneway"] = "-1"
		if attrs["ONEWAY"].strip() == "FT":
			tags["oneway"] = "yes"

    return tags

def highway_class(class_id):

    if class_id == '0':
        return 'service'
    elif class_id == '1':
        return 'trunk'
    elif class_id == '2':
        return 'primary'
    elif class_id == '3':
        return 'secondary'
    elif class_id == '4':
        return 'tertiary'
    elif class_id == '5':
        return 'residential'
    elif class_id == '6':
        return 'service'
    elif class_id == '9':
        return 'residential'
    elif class_id == '10':
        return 'residential'
    elif class_id == '12':
        return 'service'
    elif class_id == '14':
        return 'service'
    elif class_id == '15':
        return 'tertiary'
    else:
        return 'road'
