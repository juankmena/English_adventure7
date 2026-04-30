# Question bank based only on the uploaded topics/practices and user-provided notebook notes.

UNIT1_WORDS = [
    "about", "however", "summer", "midnight", "lie down", "amazing", "lucky", "winter",
    "look for", "temperature", "wrong", "since", "warm", "travel around", "weather",
    "awful", "everywhere", "campground", "bright", "heating"
]

UNIT2_WORDS = [
    "magazine", "pick up", "newspaper", "ticket", "find out", "brilliant", "free",
    "concert", "bookstore", "go shopping", "festival", "hang out", "movie theater",
    "go out", "fun", "advertisement", "exhibition", "hobby", "weekend", "photographer"
]

IDIOMS = {
    "shoestring budget": {
        "meaning": "doing something with very little money or a very tight budget",
        "spanish": "hacer algo con muy poco dinero o presupuesto ajustado",
        "example": "We traveled through Europe on a shoestring budget."
    },
    "get away from it all": {
        "meaning": "escape routine, stress, or work; usually by going somewhere peaceful",
        "spanish": "desconectarse de todo",
        "example": "I need to go to the beach and get away from it all."
    },
    "walking on air": {
        "meaning": "feeling extremely happy or excited because something good happened",
        "spanish": "estar en las nubes de felicidad",
        "example": "After the good news, she was walking on air."
    },
    "it is up in the air": {
        "meaning": "something is undecided or uncertain",
        "spanish": "estar en el aire; nada está decidido",
        "example": "Our travel plans are still up in the air."
    },
    "to hit the sack": {
        "meaning": "to go to sleep",
        "spanish": "irse a dormir / irse a la cama",
        "example": "I am tired, so I am going to hit the sack early."
    },
}

QUIZ = {
    "Vocabulary Unit 1": [
        {"type":"mcq", "q":"I was very tired, so I decided to ____.", "options":["look for", "lie down", "travel around"], "answer":"lie down", "explain":"'Lie down' means to rest your body horizontally."},
        {"type":"mcq", "q":"The movie was so good. It was ____.", "options":["awful", "amazing", "wrong"], "answer":"amazing", "explain":"'Amazing' means very surprising or impressive."},
        {"type":"mcq", "q":"We were very ____ to see that animal.", "options":["lucky", "wrong", "awful"], "answer":"lucky", "explain":"'Lucky' means having good fortune."},
        {"type":"mcq", "q":"The ____ in this city is usually hot.", "options":["midnight", "weather", "lie down"], "answer":"weather", "explain":"'Weather' describes conditions such as hot, cold, sunny, or rainy."},
        {"type":"mcq", "q":"I have lived here ____ 2020.", "options":["about", "since", "however"], "answer":"since", "explain":"'Since' means from a time in the past until now."},
        {"type":"fill", "q":"We stayed at a ______ near the lake.", "answer":"campground", "explain":"A campground is a place where people can camp."},
        {"type":"fill", "q":"It was very cold, so the ______ system was necessary.", "answer":"heating", "explain":"A heating system makes a place warm."},
        {"type":"fill", "q":"The day was ______ and beautiful.", "answer":"bright", "explain":"'Bright' can describe a sunny, full-of-light day."},
        {"type":"match", "q":"Match: 'about'", "options":["around / approximately", "extremely bad", "to rest"], "answer":"around / approximately", "explain":"'About' can mean approximately."},
        {"type":"match", "q":"Match: 'awful'", "options":["very surprising", "extremely bad or unpleasant", "having good fortune"], "answer":"extremely bad or unpleasant", "explain":"'Awful' means very bad or unpleasant."},
    ],
    "Vocabulary Unit 2": [
        {"type":"fill", "q":"Last ______, I decided to hang out with my friends in the city.", "answer":"weekend", "explain":"'Weekend' fits the time context."},
        {"type":"fill", "q":"I read a ______ and saw an advertisement about a cultural festival.", "answer":"newspaper", "explain":"The practice text uses 'newspaper' in this sentence."},
        {"type":"fill", "q":"We wanted to ______ more about it.", "answer":"find out", "explain":"'Find out' means discover information."},
        {"type":"fill", "q":"We went to a ______ to look for information.", "answer":"bookstore", "explain":"A bookstore is a place; the practice text uses it for finding information."},
        {"type":"mcq", "q":"One of my friends got a ____ for a live concert.", "options":["ticket", "photographer", "advertisement"], "answer":"ticket", "explain":"You need a ticket for a concert."},
        {"type":"mcq", "q":"At night, we went to the ____ to watch a film.", "options":["movie theater", "festival", "bookstore"], "answer":"movie theater", "explain":"A movie theater is where people watch films."},
        {"type":"classify", "q":"Classify 'go shopping'.", "options":["verb", "place", "noun"], "answer":"verb", "explain":"'Go shopping' is an action."},
        {"type":"classify", "q":"Classify 'movie theater'.", "options":["verb", "place", "noun"], "answer":"place", "explain":"A movie theater is a place."},
        {"type":"classify", "q":"Classify 'ticket'.", "options":["verb", "place", "noun"], "answer":"noun", "explain":"A ticket is a thing, so it is a noun."},
        {"type":"tf", "q":"In the Unit 2 practice text, the friends visited an exhibition.", "options":["True", "False"], "answer":"True", "explain":"The practice text says they went to an art exhibition."},
    ],
    "Past Simple": [
        {"type":"fill", "q":"Yesterday, I ______ (go) to the beach.", "answer":"went", "explain":"'Go' is irregular: go → went."},
        {"type":"fill", "q":"She ______ (study) for the exam last night.", "answer":"studied", "explain":"Regular verb ending in consonant + y: study → studied."},
        {"type":"fill", "q":"We ______ (eat) pizza for dinner.", "answer":"ate", "explain":"'Eat' is irregular: eat → ate."},
        {"type":"fill", "q":"They ______ (play) soccer after school.", "answer":"played", "explain":"Regular verbs in past simple usually add -ed."},
        {"type":"fill", "q":"He ______ (see) a movie last weekend.", "answer":"saw", "explain":"'See' is irregular: see → saw."},
        {"type":"transform", "q":"Change to negative: I visited my grandmother.", "answer":"I did not visit my grandmother.", "alt":["I didn't visit my grandmother."], "explain":"Past simple negative uses did not/didn't + base verb."},
        {"type":"transform", "q":"Change to question: You watched TV.", "answer":"Did you watch TV?", "explain":"Past simple questions use Did + subject + base verb."},
        {"type":"transform", "q":"Change to question: They went to the park.", "answer":"Did they go to the park?", "explain":"After Did, use the base form: go, not went."},
    ],
    "Past Continuous": [
        {"type":"fill", "q":"I ______ (read) a book at 8 p.m.", "answer":"was reading", "explain":"Past continuous: was/were + verb-ing."},
        {"type":"fill", "q":"They ______ (play) video games when I arrived.", "answer":"were playing", "explain":"They → were + playing."},
        {"type":"fill", "q":"She ______ (cook) dinner yesterday evening.", "answer":"was cooking", "explain":"She → was + cooking."},
        {"type":"fill", "q":"We ______ (study) when the teacher called.", "answer":"were studying", "explain":"We → were + studying."},
        {"type":"fill", "q":"He ______ (sleep) at midnight.", "answer":"was sleeping", "explain":"He → was + sleeping."},
    ],
    "Prepositions of Time": [
        {"type":"mcq", "q":"I wake up ___ 6:00 a.m.", "options":["in", "on", "at", "no preposition"], "answer":"at", "explain":"Use AT for clock times."},
        {"type":"mcq", "q":"My birthday is ___ July.", "options":["in", "on", "at", "no preposition"], "answer":"in", "explain":"Use IN for months."},
        {"type":"mcq", "q":"We have English class ___ Monday.", "options":["in", "on", "at", "no preposition"], "answer":"on", "explain":"Use ON for days."},
        {"type":"mcq", "q":"The party is ___ night.", "options":["in", "on", "at", "no preposition"], "answer":"at", "explain":"The notebook uses AT for times such as night and dinnertime."},
        {"type":"mcq", "q":"She was born ___ 2012.", "options":["in", "on", "at", "no preposition"], "answer":"in", "explain":"Use IN for years."},
        {"type":"mcq", "q":"We are traveling ___ tomorrow.", "options":["in", "on", "at", "no preposition"], "answer":"no preposition", "explain":"Notebook exception: today, tomorrow, yesterday, next week, this weekend, last week, every weekend do not need in/on/at."},
        {"type":"mcq", "q":"We go out ___ every weekend.", "options":["in", "on", "at", "no preposition"], "answer":"no preposition", "explain":"Notebook exception: every weekend uses no preposition."},
        {"type":"mcq", "q":"The event is ___ Christmas Day.", "options":["in", "on", "at", "no preposition"], "answer":"on", "explain":"Use ON for holidays/dates in this material."},
    ],
    "Adverbs": [
        {"type":"fill", "q":"She speaks English ______. (good)", "answer":"well", "explain":"Good is an adjective; well is the adverb."},
        {"type":"fill", "q":"They finished the homework ______. (quick)", "answer":"quickly", "explain":"Quick → quickly."},
        {"type":"fill", "q":"I saw him ______. (yesterday)", "answer":"yesterday", "explain":"Yesterday is an adverb of time."},
        {"type":"fill", "q":"He drives ______. (careful)", "answer":"carefully", "explain":"Careful → carefully."},
        {"type":"fill", "q":"We will travel ______. (tomorrow)", "answer":"tomorrow", "explain":"Tomorrow is an adverb of time."},
    ],
    "Infinitives and Gerunds": [
        {"type":"mcq", "q":"I enjoy ______ books.", "options":["reading", "to read"], "answer":"reading", "explain":"Enjoy is followed by a gerund (-ing)."},
        {"type":"mcq", "q":"She wants ______ to the party.", "options":["going", "to go"], "answer":"to go", "explain":"Want is followed by an infinitive."},
        {"type":"mcq", "q":"They like ______ basketball.", "options":["playing", "to play", "both are correct"], "answer":"both are correct", "explain":"Like can be followed by gerund or infinitive in the practice material."},
        {"type":"mcq", "q":"He decided ______ Spanish before his trip.", "options":["to study", "studying"], "answer":"to study", "explain":"Decide is followed by infinitive."},
        {"type":"mcq", "q":"We love ______ movies together.", "options":["watching", "to watch", "both are correct"], "answer":"both are correct", "explain":"Love can be followed by gerund or infinitive in the practice material."},
    ],
    "Present Continuous as Future": [
        {"type":"fill", "q":"I ______ (meet) my friends tomorrow.", "answer":"am meeting", "explain":"Present continuous as future: am/is/are + verb-ing."},
        {"type":"fill", "q":"She ______ (travel) next week.", "answer":"is traveling", "alt":["is travelling"], "explain":"She → is + traveling/travelling."},
        {"type":"fill", "q":"We ______ (have) a test on Friday.", "answer":"are having", "explain":"We → are + having."},
        {"type":"fill", "q":"They ______ (visit) their grandparents tonight.", "answer":"are visiting", "explain":"They → are + visiting."},
        {"type":"fill", "q":"He ______ (play) basketball this afternoon.", "answer":"is playing", "explain":"He → is + playing."},
    ],
    "Prepositions": [
        {"type":"fill", "q":"The bank is just ______ the supermarket. (next to / in front of / behind / at / near)", "answer":"next to", "explain":"'Just next to' means very close beside something."},
        {"type":"fill", "q":"The park is just ______ the school. (next to / in front of / behind / at / near)", "answer":"in front of", "explain":"'In front of' is one of the listed prepositions."},
        {"type":"fill", "q":"I sat just ______ my best friend in class. (next to / in front of / behind / at / near)", "answer":"next to", "explain":"Sitting next to someone means beside that person."},
        {"type":"fill", "q":"The bus stop is just ______ the corner. (next to / in front of / behind / at / near)", "answer":"at", "explain":"'At the corner' is the expected phrase."},
        {"type":"fill", "q":"Who are you talking ______? (to / for / with / about / at)", "answer":"to", "alt":["with"], "explain":"The practice focuses on stranding prepositions in WH-questions."},
        {"type":"fill", "q":"What are you looking ______? (to / for / with / about / at)", "answer":"for", "explain":"Look for = try to find something."},
    ],
    "Adjectives Fact and Opinion": [
        {"type":"classify", "q":"Classify 'big'.", "options":["fact", "opinion"], "answer":"fact", "explain":"Size adjectives are fact adjectives."},
        {"type":"classify", "q":"Classify 'beautiful'.", "options":["fact", "opinion"], "answer":"opinion", "explain":"Beautiful describes what someone thinks."},
        {"type":"classify", "q":"Classify 'wooden'.", "options":["fact", "opinion"], "answer":"fact", "explain":"Material adjectives are fact adjectives."},
        {"type":"classify", "q":"Classify 'amazing'.", "options":["fact", "opinion"], "answer":"opinion", "explain":"Amazing expresses an opinion."},
        {"type":"classify", "q":"Classify 'round'.", "options":["fact", "opinion"], "answer":"fact", "explain":"Shape adjectives are fact adjectives."},
        {"type":"classify", "q":"Classify 'awful'.", "options":["fact", "opinion"], "answer":"opinion", "explain":"Awful expresses what someone thinks or feels about something."},
    ],
    "Idioms": [
        {"type":"mcq", "q":"I have very little money for the trip. I am traveling on a ____.", "options":["shoestring budget", "walking on air", "hit the sack"], "answer":"shoestring budget", "explain":"Shoestring budget = very little money / tight budget."},
        {"type":"mcq", "q":"I am so stressed. I need to go to the beach and ____.", "options":["get away from it all", "hit the sack", "up in the air"], "answer":"get away from it all", "explain":"Get away from it all = escape routine or stress."},
        {"type":"mcq", "q":"She passed the exam. She is ____ today.", "options":["walking on air", "up in the air", "on a shoestring budget"], "answer":"walking on air", "explain":"Walking on air = extremely happy."},
        {"type":"mcq", "q":"Our plans are not decided yet. They are ____.", "options":["up in the air", "walking on air", "hit the sack"], "answer":"up in the air", "explain":"Up in the air = undecided or uncertain."},
        {"type":"mcq", "q":"I am tired. I am going to ____ early tonight.", "options":["hit the sack", "get away from it all", "walk on air"], "answer":"hit the sack", "explain":"Hit the sack = go to sleep."},
    ],
}

READING_TEXT = """Last weekend, I decided to hang out with my friends in the city. First, I read a newspaper and saw an advertisement about a cultural festival downtown. We wanted to find out more about it, so we went to a bookstore to look for information. After that, we decided to go shopping and bought some clothes. In the afternoon, we went to an art exhibition. The paintings were brilliant! I especially liked the work of a famous photographer. Later, one of my friends got a ticket for a live concert, so we all went together. It was a fun experience! At night, we went to the movie theater to watch a film. After that, my parents came to pick me up. It was an amazing day. My favorite hobby is spending time with my friends and having fun."""

READING_QUESTIONS = [
    {"type":"tf", "q":"The friends stayed at home all day.", "options":["True", "False"], "answer":"False", "explain":"They went to different places in the city."},
    {"type":"tf", "q":"They visited an exhibition.", "options":["True", "False"], "answer":"True", "explain":"The text says they went to an art exhibition."},
    {"type":"tf", "q":"They went to the movie theater.", "options":["True", "False"], "answer":"True", "explain":"At night, they went to the movie theater."},
    {"type":"fill", "q":"Where did they find information about the festival?", "answer":"bookstore", "alt":["in a bookstore", "at a bookstore", "they found information in a bookstore"], "explain":"They went to a bookstore to look for information."},
    {"type":"fill", "q":"Who picked the writer up?", "answer":"parents", "alt":["my parents", "their parents", "the parents"], "explain":"The text says: my parents came to pick me up."},
]
