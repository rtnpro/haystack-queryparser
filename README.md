haystack-queryparser
====================

Converts arbitrarily complicated user entered query strings to a haystack query object.

###Input
  Input should be a string.This the query.
###Output
  Output is a `SQ(haystack.query.SQ)` object.
  This can be passed to `SearchQuerySet.filter` and the	query will be applied

###Test
  To run the test you need to be in the django environment.So you can do something like this:
```
$ python manage.py shell
>>> import haystack_queryparser.tests as test
>>> test.main()
test_parse (haystack_queryparser.tests.SimpleTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
```