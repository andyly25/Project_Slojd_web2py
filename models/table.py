db.define_table('npost',
		Field('your_message', 'text')
		)
db.npost.your_message.requires = IS_NOT_EMPTY()