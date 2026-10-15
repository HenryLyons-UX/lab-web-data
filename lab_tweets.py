# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
output = []
for year in range(2009, 2019):
    filename = f'master_{year}.json'
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    output.extend(data)
tweet = output[0]
if 'full_text' in tweet:
    message = tweet['full_text']
else:
    message = tweet['text']
print(message)
totalnum = 0
fakenewnum = 0
russianum = 0
mexiconum = 0

phrases = ["Obama", "Trump", "Fake News", "Russia", "Mexico", "China", "Crypto", "FTX"]
counts = {}
for phrase in phrases:
    counts[phrase] = 0

for tweet in output:
    if 'full_text' in tweet:
        message = tweet['full_text']
    else:
        message = tweet['text']
    message = message.lower()
    for phrase in phrases:
        if phrase.lower() in message:
            counts[phrase] += 1

for phrase in phrases:
    print(phrase, counts[phrase])
labels = []
percent = []
import matplotlib.pyplot as plt
print('| phrase            | percent of tweets |')
print('| ----------------- | ----------------- |')
for phrase in phrases:
    frac = (counts[phrase] / len(output)) * 100
    percent_text = f'{frac:05.2f}'
    print(f'| {phrase.lower():>17} | {percent_text:<17} |')
    labels.append(phrase.lower())
    percent.append(frac)

plt.bar(labels, percent)
plt.xlabel('Phrase')
plt.ylabel('Percent of tweets')
plt.title('Phrases in Trump tweets, 2009–2018')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('tweets.png')

