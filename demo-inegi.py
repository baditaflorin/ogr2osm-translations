# -*- coding: utf-8 -*-
'''
A simplified translation function for INEGI 'Información Vectorial de Localidades Amanzanadas y Números Exteriores' data

DO NOT USE. This is only to demonstrate the capabilities of Cygnus with a simple example.
'''

def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    if 'TIPOVIAL'in attrs:
        source_type = attrs.get('TIPOVIAL')
        if source_type == 'CALLE':
            tags['highway'] = 'residential'
        if source_type == 'PRIVADA':
            tags['highway'] = 'service'
            tags['access'] = 'private'

    if 'NOMVIAL' in attrs:
        source_name = attrs.get('NOMVIAL')
        if source_name != 'NINGUNO':
            tags['name'] = u'{} {}'.format(
                attrs.get('TIPOVIAL'),
                source_name).title()

    tags['source'] = 'INEGI'

    return tags