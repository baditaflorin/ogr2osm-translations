# -*- coding: utf-8 -*-
'''
A simplified translation function for INEGI 'Información Vectorial de Localidades Amanzanadas y Números Exteriores' data

DO NOT USE. This is only to demonstrate the capabilities of Cygnus with a simple example.
'''

def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    source_type = attrs.get('TIPOVIAL')
    source_name = attrs.get('NOMVIAL')

    if source_type:
        tags['inegi:tipovial'] = source_type.lower()
        if source_type == 'CALLE':
            tags['highway'] = 'residential'
        if source_type == 'OTRO':
            tags['highway'] = 'unclassified'
        if source_type == 'PRIVADA':
            tags['highway'] = 'service'
            tags['access'] = 'private'

    if source_name:
        tags['inegi:nomvial'] = source_name.lower()
        if source_name != 'NINGUNO':
            tags['name'] = u'{}{}'.format(
                source_type + ' ' if source_type != 'OTRO' else '',
                source_name).title()


    if 'SENTIDO' in attrs:
        source_oneway = attrs.get('SENTIDO')
        tags['inegi:sentido'] = source_oneway.lower()
        if source_oneway == 'DOS SENTIDOS':
            tags['oneway'] = 'no'
        if source_oneway == 'UN SENTIDO':
            tags['oneway'] = 'yes'

    tags['source'] = 'INEGI'

    return tags