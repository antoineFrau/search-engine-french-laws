stop_words = [
  ".",
  ",",
  "!",
  ":",
  ";",
  "(",
  ")",
  "=",
  "+",
  "-",
  "*",
  "%",
  "/",
  "&",
  "_",
  "<",
  ">",
  "#",
  "@",
  "a",
  "abord",
  "afin",
  "ah",
  "ai",
  "aie",
  "aient",
  "aies",
  "ainsi",
  "ait",
  "allaient",
  "allo",
  "allons",
  "allô",
  "alors",
  "après",
  "as",
  "assez",
  "attendu",
  "au",
  "aucun",
  "aucune",
  "aucuns",
  "aujourd",
  "aujourd'hui",
  "auquel",
  "aura",
  "aurai",
  "auraient",
  "aurais",
  "aurait",
  "auras",
  "aurez",
  "auriez",
  "aurions",
  "aurons",
  "auront",
  "aussi",
  "autre",
  "autres",
  "aux",
  "auxquelles",
  "auxquels",
  "avaient",
  "avais",
  "avait",
  "avant",
  "avec",
  "avez",
  "aviez",
  "avions",
  "avoir",
  "avons",
  "ayant",
  "ayante",
  "ayantes",
  "ayants",
  "ayez",
  "ayons",
  "b",
  "bah",
  "beaucoup",
  "bien",
  "bigre",
  "bon",
  "bonjour",
  "boum",
  "bravo",
  "brrr",
  "c",
  "car",
  "ce",
  "ceci",
  "cela",
  "celle",
  "celle-ci",
  "celle-là",
  "celles",
  "celles-ci",
  "celles-là",
  "celui",
  "celui-ci",
  "celui-là",
  "celà",
  "cent",
  "cependant",
  "certain",
  "certaine",
  "certaines",
  "certains",
  "certes",
  "ces",
  "cet",
  "cette",
  "ceux",
  "ceux-ci",
  "ceux-là",
  "chacun",
  "chaque",
  "cher",
  "chers",
  "chez",
  "chiche",
  "chut",
  "chère",
  "chères",
  "ci",
  "cinq",
  "cinquantaine",
  "cinquante",
  "cinquantième",
  "cinquième",
  "clac",
  "clic",
  "combien",
  "comme",
  "comment",
  "compris",
  "concernant",
  "contre",
  "couic",
  "crac",
  "d",
  "da",
  "dans",
  "de",
  "debout",
  "dedans",
  "dehors",
  "delà",
  "depuis",
  "derrière",
  "des",
  "desquelles",
  "desquels",
  "dessous",
  "dessus",
  "deux",
  "deuxième",
  "deuxièmement",
  "devant",
  "devers",
  "devra",
  "devrait",
  "différent",
  "différente",
  "différentes",
  "différents",
  "dire",
  "dit",
  "divers",
  "diverse",
  "diverses",
  "dix",
  "dix-huit",
  "dix-neuf",
  "dix-sept",
  "dixième",
  "doit",
  "doivent",
  "donc",
  "dont",
  "dos",
  "douze",
  "douzième",
  "dring",
  "droite",
  "du",
  "duquel",
  "durant",
  "dès",
  "début",
  "désormais",
  "e",
  "effet",
  "eh",
  "elle",
  "elle-même",
  "elles",
  "elles-mêmes",
  "en",
  "encore",
  "entre",
  "envers",
  "environ",
  "es",
  "essai",
  "est",
  "et",
  "etant",
  "etc",
  "etre",
  "eu",
  "eue",
  "eues",
  "euh",
  "eurent",
  "eus",
  "eusse",
  "eussent",
  "eussent ",
  "eusses",
  "eussiez",
  "eussions",
  "eut",
  "eux",
  "eux-mêmes",
  "excepté",
  "eûmes",
  "eût",
  "eûtes",
  "f",
  "fais",
  "faisaient",
  "faisant",
  "fait",
  "faites",
  "façon",
  "feront",
  "fi",
  "flac",
  "floc",
  "fois",
  "font",
  "force",
  "furent",
  "fus",
  "fusse",
  "fussent",
  "fussent ",
  "fusses",
  "fussiez",
  "fussions",
  "fut",
  "fûmes",
  "fût",
  "fûtes",
  "g",
  "gens",
  "h",
  "ha",
  "haut",
  "hein",
  "hem",
  "hep",
  "hi",
  "ho",
  "holà",
  "hop",
  "hormis",
  "hors",
  "hou",
  "houp",
  "hue",
  "hui",
  "huit",
  "huitième",
  "hum",
  "hurrah",
  "hé",
  "hélas",
  "i",
  "ici",
  "il",
  "ils",
  "importe",
  "j",
  "je",
  "jusqu",
  "jusque",
  "juste",
  "k",
  "l",
  "la",
  "laquelle",
  "las",
  "le",
  "lequel",
  "les",
  "lesquelles",
  "lesquels",
  "leur",
  "leurs",
  "longtemps",
  "lorsque",
  "lui",
  "lui-même",
  "là",
  "lès",
  "m",
  "ma",
  "maint",
  "maintenant",
  "mais",
  "malgré",
  "me",
  "merci",
  "mes",
  "mien",
  "mienne",
  "miennes",
  "miens",
  "mille",
  "mince",
  "mine",
  "moi",
  "moi-même",
  "moins",
  "mon",
  "mot",
  "moyennant",
  "même",
  "mêmes",
  "n",
  "na",
  "ne",
  "neuf",
  "neuvième",
  "ni",
  "nombreuses",
  "nombreux",
  "nommés",
  "non",
  "nos",
  "notre",
  "nous",
  "nous-mêmes",
  "nouveaux",
  "nul",
  "néanmoins",
  "nôtre",
  "nôtres",
  "o",
  "oh",
  "ohé",
  "ollé",
  "olé",
  "on",
  "ont",
  "onze",
  "onzième",
  "ore",
  "ou",
  "ouf",
  "ouias",
  "oust",
  "ouste",
  "outre",
  "o|",
  "où",
  "p",
  "paf",
  "pan",
  "par",
  "parce",
  "parmi",
  "parole",
  "partant",
  "particulier",
  "particulière",
  "particulièrement",
  "pas",
  "passé",
  "pendant",
  "personne",
  "personnes",
  "peu",
  "peut",
  "peuvent",
  "peux",
  "pff",
  "pfft",
  "pfut",
  "pif",
  "pièce",
  "plein",
  "plouf",
  "plupart",
  "plus",
  "plusieurs",
  "plutôt",
  "pouah",
  "pour",
  "pourquoi",
  "premier",
  "première",
  "premièrement",
  "proche",
  "près",
  "psitt",
  "puisque",
  "q",
  "qu",
  "quand",
  "quant",
  "quant-à-soi",
  "quanta",
  "quarante",
  "quatorze",
  "quatre",
  "quatre-vingt",
  "quatrième",
  "quatrièmement",
  "que",
  "quel",
  "quelconque",
  "quelle",
  "quelles",
  "quelqu'un",
  "quelque",
  "quelques",
  "quels",
  "qui",
  "quiconque",
  "quinze",
  "quoi",
  "quoique",
  "r",
  "revoici",
  "revoilà",
  "rien",
  "s",
  "sa",
  "sacrebleu",
  "sans",
  "sapristi",
  "sauf",
  "se",
  "seize",
  "selon",
  "sept",
  "septième",
  "sera",
  "serai",
  "seraient",
  "serais",
  "serait",
  "seras",
  "serez",
  "seriez",
  "serions",
  "serons",
  "seront",
  "ses",
  "seulement",
  "si",
  "sien",
  "sienne",
  "siennes",
  "siens",
  "sinon",
  "six",
  "sixième",
  "soi",
  "soi-même",
  "soient",
  "sois",
  "soit",
  "soixante",
  "sommes",
  "son",
  "sont",
  "sous",
  "soyez",
  "soyons",
  "stop",
  "suis",
  "suivant",
  "sujet",
  "sur",
  "surtout",
  "t",
  "ta",
  "tac",
  "tandis",
  "tant",
  "te",
  "tel",
  "telle",
  "tellement",
  "telles",
  "tels",
  "tenant",
  "tes",
  "tic",
  "tien",
  "tienne",
  "tiennes",
  "tiens",
  "toc",
  "toi",
  "toi-même",
  "ton",
  "touchant",
  "toujours",
  "tous",
  "tout",
  "toute",
  "toutes",
  "treize",
  "trente",
  "trois",
  "troisième",
  "troisièmement",
  "trop",
  "très",
  "tsoin",
  "tsouin",
  "tu",
  "té",
  "u",
  "un",
  "une",
  "unes",
  "uns",
  "v",
  "va",
  "vais",
  "valeur",
  "vas",
  "vers",
  "via",
  "vif",
  "vifs",
  "vingt",
  "vivat",
  "vive",
  "vives",
  "vlan",
  "voici",
  "voie",
  "voient",
  "voilà",
  "vont",
  "vos",
  "votre",
  "vous",
  "vous ",
  "vous-mêmes",
  "vu",
  "vé",
  "vôtre",
  "vôtres",
  "w",
  "x",
  "y",
  "y ",
  "z",
  "zut",
  "à",
  "â",
  "ça",
  "ès",
  "étaient",
  "étais",
  "était",
  "étant",
  "étante",
  "étantes",
  "étants",
  "état",
  "étiez",
  "étions",
  "été",
  "étée",
  "étées",
  "étés",
  "êtes",
  "être",
  "ô"
]