import base64

MESSAGE = '''
Encoded
Message
HERE
'''

KEY = 'Username'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print (''.join(result))

