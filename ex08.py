
formatter = "%s %s %s %s"
# This example demonstrates the various ways that the str may be formatted
print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
print "{0}" .format (formatter)
    