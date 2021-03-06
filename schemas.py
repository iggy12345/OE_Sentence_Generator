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
word text not null,
origin integer not null,
person text,
plurality text,
mood text,
tense text,
participle bool not null,
is_infinitive bool not null,
foreign key (origin) references old_english_words(id)
);
'''

declensions_schemas = '''declensions (
id integer primary key,
word text not null,
origin integer not null,
plurality text,
noun_case text not null,
foreign key (origin) references old_english_words(id)
);
'''

verb_schemas = '''verbs (
id integer primary key,
word integer not null,
strength bool not null,
verb_class integer not null,
transitivity bool not null,
foreign key (word) references old_english_words(id)
);'''

adjective_schemas = '''adjectives (
id integer primary key,
origin integer not null,
word text not null,
strength bool not null,
gender text not null,
noun_case text not null,
plurality text not null,
foreign key (origin) references old_english_words(id)
);'''

adverb_schemas = '''adverbs (
id integer primary key,
word integer not null,
comparative bool not null,
superlative bool not null,
foreign key (word) references old_english_words(id)
);'''


schemas = [
    old_english_schemas,
    conjugations_schemas,
    declensions_schemas,
    verb_schemas,
    adjective_schemas,
    adverb_schemas
]

triggers = [
]

views = [
]

record_typing = {
    'old_english_words': '(name, pos, definition, is_affix)',
    'conjugations': '(word, origin, person, plurality, mood, tense, participle, is_infinitive)',
    'declensions': '(word, origin, plurality, noun_case)',
    'verbs': '(word, strength, verb_class, transitivity)',
    'adjectives': '(origin, word, strength, gender, noun_case, plurality)',
    'adverbs': '(word, comparative, superlative)'
}
