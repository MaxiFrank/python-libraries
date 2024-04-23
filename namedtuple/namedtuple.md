# namedtuple

collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

- returns a new tuple subclass named typename
- `__repr__()` method lists the tuple contents in name=value format
- field_names are sequence of strings such as ['x', 'y'], 'x y', or 'x, y'

## methods
- `somenamedtuple._make(iterable)`
    * Makes a new instance from an existing sequence or iterable.
- `somenamedtuple._asdict()`
    * Return a new dict which maps field names to their corresponding values:
- `somenamedtuple._replace(**kwargs)`
    * Return a new instance of the named tuple replacing specified fields with new values
- `somenamedtuple._fields`
    * Tuple of strings listing the field names. Useful for introspection and for creating new named tuple types from existing named tuples.
- `somenamedtuple._field_defaults`
    * somenamedtuple._field_defaults
- `getattr()`
    * To retrieve a field whose name is stored in a string