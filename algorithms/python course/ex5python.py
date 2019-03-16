str = 'X-DSPAM-Confidence: 0.8475 '

colon_pos = str.find(":")

after_colon = str[colon_pos+1 : ].strip()

result = float(after_colon)

print(result)

