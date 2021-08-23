from sqlalchemy.exc import ArgumentError
from  sqlalchemy.schema import Column
from six import string_types

class I18IdColumn(Column):

    def __init__(self, *args, **kwargs):
        if 'name' not in kwargs and isinstance(args[0], string_types) is False:
            raise ArgumentError("You must pass a `name` when create a I18IdColumn")

        self.rn_parent_col = kwargs.pop('parent_column')
        super().__init__(*args, **kwargs)