tabby_cat = "\tI'm tabbed in." # embeds tabspace into str
persian_cat = "I'm split\non a line." # embeds new line into str
backslash_cat = "I'm \\ a \\ cat." # embeds \ into str

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ['/','-','|','\\','|']:
        print "%s\r" % i,
    