import wikipedia as wiki
import random
link_set = set()

flag = False
while (flag == False):
  page_name = input("Enter the starting page: ")
  try:
    page = wiki.WikipediaPage(page_name)
  except wiki.exceptions.DisambiguationError as e:
    page = wiki.WikipediaPage(random.choice(e.options))
    flag = True
  except wiki.exceptions.PageError:
    print ("Page does not exist!")
  else:
    flag = True

links_on_page = page.links
count = 0

valid = True
while (valid):
  if (len(links_on_page) <10):
    print ("There are not enough 10 links in this page")
    valid = False
  else:
    link_title = page.links[9]
    print (link_title)
    if (link_title in link_set):
      print ("We have already encountered this")
      valid = False
    else:
      count += 1
      link_set.add(link_title)
      try:
        page = wiki.WikipediaPage(link_title)
      except wiki.exceptions.PageError:
        print("This page has no content");
        valid = False
      else:
        links_on_page = page.links

print ("Total number of points:", count)




