
db.define_table('child',
     Field('name'),
     Field('weight', 'double'),
     Field('birth_date', 'date'),
     Field('time_of_birth', 'time'))

db.child.name.requires=IS_NOT_EMPTY()
db.child.weight.requires=IS_FLOAT_IN_RANGE(0,100)
db.child.birth_date.requires=IS_DATE()
db.child.time_of_birth.requires=IS_TIME()