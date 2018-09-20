import re
content = 'Hello 123 4567 World_This a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
test = 'sangfor.test'
tests = re.match('sangfor.(.*)',test)
print(tests.group(1))
