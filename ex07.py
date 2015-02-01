print 'Mary had a little lamb.'
print "It's fleece was white as %s." % 'snow'
print 'and everywhere that Mary went.'
print '.' * 10 # What does that do?

end01 = 'C'
end02 = 'h'
end03 = 'e'
end04 = 'e'
end05 = 's'
end06 = 'e'
end07 = 'B'
end08 = 'u'
end09 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# Watch that comma at the end. Try removing it to see what happens.
print end01 + end02 + end03 + end04 + end05 + end06,
print end07 + end08 + end09 + end10 + end11 + end12

# I think I prefer this str embedment method
print '{0}{1}{2}{3}{4}{5}' .format (end01, end02, end03, end04, end05, end06)