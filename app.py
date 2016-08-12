from bs4 import BeautifulSoup
import ipdb
from os import path
from wordcloud import WordCloud
from colorama import init, Fore, Back, Style
init()
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
#import matplotlib.pyplot as plt
import re
import operator

raw_messages = open('messages.htm', 'r')
soup = BeautifulSoup(raw_messages, 'html.parser')

#ipdb.set_trace()

threads = soup.find_all("div", class_="thread")
#print(Fore.BLUE + "# of threads: \n" + str(len(threads)))

messages = soup.findAll('p')
#print(Fore.BLUE + "# of messages: \n" + str(len(messages)));

random_var = []

for message in messages:
    val = ' '.join(message.stripped_strings)
    random_var.append(val)

filtered_words = [word for word in random_var if word not in stopwords.words('english')]

final_str = " ".join(filtered_words).encode('utf-8').strip()

#people = []
people = {}
for thread in soup.find_all("div", class_="thread"):
    soup = BeautifulSoup(str(thread), 'html.parser')
    message_count = len(soup.find_all("p"))
    p = re.compile('.*"thread">(.*)')
    #print("Thread: ")
    #print(p.match(str(thread)).group(1))
    #print("# of messages:")
    #print(message_count)
    #print("% of all messages:")
    #print(str(float(message_count)/len(messages) * 100))
    thread_name = {}
    #wordz = thread.encode('utf-8')
    val = p.match(str(thread)).group(1)
    print(val)
    #thread_name["participants"] = val.decode('utf8')
    thread_name["messages"] = message_count
    thread_name["message_percent"] = str(float(message_count)/len(messages) * 100)
    #people.append(thread_name)
    #if hasattr(people, val.decode('utf8')):
    #    thread_name["messages"] = message_count + people[val.decode('utf8')].messages

    people[val.decode('utf8')] = thread_name

print(people)
new_dict = people.sort(key=operator.itemgetter('messages'))
print(new_dict)

ftwo = open('out.txt', 'w')
ftwo.write(final_str)
ftwo.close()
#print('successfully outputted')

d = path.dirname(__file__)
#
# Read the whole text.
text = open(path.join(d, 'out.txt')).read()





# Generate a word cloud image
#wordcloud = WordCloud(width=1600, height=800).generate(text)

# Display the generated image:
# the matplotlib way:
#plt.imshow(wordcloud)
#plt.axis("off")

# take relative word frequencies into account, lower max_font_size
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
#plt.figure( figsize=(20,10), facecolor='k' )
#plt.imshow(wordcloud)
#plt.tight_layout(pad=0)
#plt.axis("off")
#plt.show()
