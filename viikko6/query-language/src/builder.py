from matchers import All, And, Not, Or, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
  def __init__(self, 
      matchers = [],
      filter_matcher = None, 
      default_matcher = And
    ) -> None:

    self._matchers = matchers
    self._default_matcher = default_matcher

    if filter_matcher: self._matchers.append(filter_matcher)

  def build(self):
    args = self._matchers.copy()
    self._matchers.clear()

    return self._default_matcher(*args)

  def playsIn(self, team):
    return QueryBuilder(
      self._matchers,
      PlaysIn(team),
      self._default_matcher
    )

  def hasAtLeast(self, value, attr):
    return QueryBuilder(
      self._matchers,
      HasAtLeast(value, attr),
      self._default_matcher
    )

  def hasFewerThan(self, value, attr):
    return QueryBuilder(
      self._matchers,
      HasFewerThan(value, attr),
      self._default_matcher
    )

  def oneOf(self, *args):
    return QueryBuilder(
      list(args),
      default_matcher = Or
    )
