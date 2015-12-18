# 12/18/15
# Directly from Udacity Intro to Computer Science

# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=') + 9 #finds the start of URL, by skipping to
# directly after <a href="

end_link = page.find('">', start_link) #finds the end of the URL
url = page[start_link:end_link] #assigns URL to the link, as defined by the variables

print url #prints http://udacity.com
