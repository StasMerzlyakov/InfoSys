# -*- coding: utf-8 -*-

#
# api для поиска с использованием sphinxsearch
#

import sphinxsearch

# 
# Метод поиск, реализованный через sphinx
#
def sphinx_search(words):
  c = sphinxsearch.SphinxClient()
  c.SetServer('127.0.0.1', 9312)
  q = c.Query(words)
  matches = q['matches']
  return matches
