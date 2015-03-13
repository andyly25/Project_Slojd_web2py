db.define_table('post', Field('your_message', 'text'))
db.post.your_message.requires = IS_NOT_EMPTY()