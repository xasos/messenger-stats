from bs4 import BeautifulSoup
import ipdb
from os import path
from wordcloud import WordCloud
from colorama import init
init()

f = open('messages.htm', 'r')
soup = BeautifulSoup(f, 'html.parser')

thing = soup.find_all("div", class_="thread")

#print(thing[4])
print("# of threads:")
print(len(thing))


thing2 = soup.findAll('p')
print("# of messages:")
print(len(thing2))

random_var = []

for ps in thing2:
    val = ' '.join(ps.stripped_strings)
    random_var.append(val)

final_str = " ".join(random_var).encode('utf-8').strip()
#print(final_str)

ftwo = open('out.txt', 'w')
ftwo.write(final_str)
ftwo.close()
print('successfully outputted')

#print colored('hello', 'red'), colored('world', 'green')

d = path.dirname(__file__)
#
# Read the whole text.
text = open(path.join(d, 'out.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(width=800, height=400).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
plt.figure( figsize=(20,10), facecolor='k' )
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis("off")
plt.show()
