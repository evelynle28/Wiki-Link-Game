import wikipedia as wiki
#The program counts the number of links appeared on a certain wiki page
topic = input("Enter the topic name or -q to quit: ")
while (topic != "-q"):
  try:
    topic_page = wiki.WikipediaPage(topic)
  except wiki.exceptions.PageError:
    print ("Cannot find this topic!")
  else:
    result = topic_page.links
    print ("There are", len(result), "links in total on this page.")
  print()
  #Prompt user to re-enter a new topic
  topic = input("Enter the topic name or -q to quit: ")

print ("Quit Successfully!")
