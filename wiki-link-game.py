import wikipedia as wiki
import random

link_set = set() #Set containing the links that have been through
valid = False

#Prompt user to enter the topic until it is valid
while (valid == False):
  page_name = input("Enter the starting page: ")
  try:
    page = wiki.WikipediaPage(page_name)
  except wiki.exceptions.DisambiguationError as e:
    print ("Randomly pick one from the options.")
    page = wiki.WikipediaPage(random.choice(e.options))
    valid = True
  except wiki.exceptions.PageError:
    print ("Page does not exist!")
  else:
    valid = True

count = 0 #Counter for the number of links that the program has run into
final = False
while (not final):
  #Check if there is enough 10 links in the current page
  if (len(page.links) <10):
    print ("There are not enough 10 links in this page")
    final = True
  else:
    #Take the 10th link in the list of links
    link_title = page.links[9]
    print (link_title)
    if (link_title in link_set):
      print ("We have already encountered this")
      final = True
    else:
      count += 1 #update the number of valid link
      link_set.add(link_title) #Add the new link to the link_set
      try:
        page = wiki.WikipediaPage(link_title)
      except wiki.exceptions.PageError:
        print("This page has no content");
        final = True

print ("Total number of points:", count)




