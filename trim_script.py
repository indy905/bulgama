import re

with open('/Users/joseph/Documents/personal/bulgama/chatpers/008.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Title
text = text.replace('제8화. 마기(때)를 벗겨내는 의식', '마기를 벗겨내는 의식')

# Fix Economy
text = text.replace('식혜 백 잔이 훌쩍 넘는 거금이다!', '식혜 열두 잔이 훌쩍 넘는 거금이다!')

# Fix VIP
text = text.replace('VIP 고객님들', '귀빈들')

# Remove some fluff to reduce length if needed, but manual trim might be better.
# Let's save the basic fixes first.
with open('/Users/joseph/Documents/personal/bulgama/chatpers/008.md', 'w', encoding='utf-8') as f:
    f.write(text)

