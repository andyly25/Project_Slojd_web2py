db.define_table('npost',
		Field('entry1', 'text'),
		Field('entry2', 'text'),
		Field('entry3', 'text')
		)
db.npost.entry1.requires = IS_NOT_EMPTY()
db.npost.entry2.requires = IS_NOT_EMPTY()
db.npost.entry3.requires = IS_NOT_EMPTY()