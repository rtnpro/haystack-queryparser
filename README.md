haystack-queryparser
====================

Converts arbitrarily complicated user entered query strings to a haystack query object.

###Input
  Input should be a string.This the query.
###Output
  Output is a `SQ(haystack.query.SQ)` object.
  This can be passed to `SearchQuerySet.filter` and the	query will be applied

Test
