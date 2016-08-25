import urllib

def read_text():
    quotes = open("{{text file}}")      #open a text file
    contents_of_file = quotes.read()      #read text from the file
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)     #check profanity

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)     #Google-what do you like service
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("No curse words:)")
    else:
        print("Could not scan the document properly.")

read_text()
