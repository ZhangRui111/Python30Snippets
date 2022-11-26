"""
Converts a string to camelcase.
"""
from re import sub


def camel(s):
    # re.sub(): replace any - or _ with a space;
    # str.title(): capitalize the first letter of each word and convert
    #              the rest to lowercase;
    # str.replace(): remove spaces between words
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    # convert the first letter of the string to lowercase
    s = ''.join([s[0].lower(), s[1:]])
    return s


print(camel('some_database_field_name'))
# >>> 'someDatabaseFieldName'
print(camel('Some label that needs to be camelized'))
# >>> 'someLabelThatNeedsToBeCamelized'
print(camel('some-javascript-property'))
# >>> 'someJavascriptProperty'
print(camel('some-mixed_string with spaces_underscores-and-hyphens'))
# >>> 'someMixedStringWithSpacesUnderscoresAndHyphens'
