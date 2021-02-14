#!/usr/bin/env python
"""

Neural SPARQL Machines - Interpreter module.

'SPARQL as a Foreign Language' by Tommaso Soru and Edgard Marx et al., SEMANTiCS 2017
https://arxiv.org/abs/1708.07624

Version 1.0.0

"""
import sys
import re

from generator_utils import decode, fix_URI
import importlib
from SPARQLWrapper import SPARQLWrapper, JSON


PREFIXES = 'PREFIX terms: <http://purl.org/dc/terms/>\n' \
'PREFIX entities: <http://resources.samsung.com/entities/>\n' \
'PREFIX git: <http://resources.samsung.com/git/>\n' \
'PREFIX dcat: <http://www.w3.org/ns/dcat#>\n' \
'PREFIX cve2: <http://resources.samsung.com/cve2/>\n' \
'PREFIX vocabulary: <http://resources.samsung.com/vocabulary/>\n' \
'PREFIX repositories: <http://resources.samsung.com/repositories/>\n' \
'PREFIX projects: <http://resources.samsung.com/projects/>\n' \
'PREFIX contributors: <http://resources.samsung.com/contributors/>\n' \
'PREFIX license: <http://resources.samsung.com/license/>\n' \
'PREFIX foaf: <http://xmlns.com/foaf/0.1/>\n' \
'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n' \
'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n' \
'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'


if __name__ == '__main__':
    importlib.reload(sys)
    encoded_sparql = sys.argv[1]
    decoded_sparql = decode(encoded_sparql)
    decoded_sparql = fix_URI(decoded_sparql)
    sparql = SPARQLWrapper("http://localhost:7200/repositories/iliarkov")
    decoded_sparql = decoded_sparql[:-2]
    decoded_sparql += '. }'
    sparql.setQuery(PREFIXES + decoded_sparql)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print(result["a"]["value"])
