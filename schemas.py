old_english_schemas = '''old_english_words (
id integer primary key,
name text not null,
pos text not null,
definition text not null,
is_affix bool not null
);
'''

conjugations_schemas = '''conjugations (
id integer primary key,
word integer not null,
origin integer not null,
person text,
plurality text,
mood text,
tense text,
participle bool not null,
preterite bool not null,
foreign key (word) references old_english_words(id),
foreign key (origin) references old_english_words(id)
);
'''

declensions_schemas = '''declensions (
id integer primary key,
word text not null,
origin integer not null,
plurality text,
declension text not null,
foreign key (origin) references old_english_words(id)
);
'''


schemas = [
    old_english_schemas,
    conjugations_schemas,
    declensions_schemas
]

triggers = [
]

views = [
]

record_typing = {
    'old_english_words': '(name, pos, definition, is_affix)',
    'conjugations': '(word, origin, person, plurality, mood, tense, participle, preterite)',
    'declensions': '(word, origin, plurality, declension)'
}
