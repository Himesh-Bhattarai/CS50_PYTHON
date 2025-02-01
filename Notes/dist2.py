students = [
    {"name ": "himesh", "house": "space", "s": "s"},
    {"name ": "himesh1", "house": "spac", "s": "s"},
    {"name ": "himesh2", "house": "spae", "s": "s"},
    {"name ": "himesh3", "house": "spce", "s": "s"},
    {"name ": "himesh4", "house": "pace", "s": "s"},
    {"name ": "himesh5", "house": "sace", "s": None},
    
]

for student in students:
    print(student["name "], student["house"], student["s"], sep=",")