import re

def main():
  log = "" 
  data_log = open("log.txt","r")
  for line in data_log:
    regex = re.sub("\d{2}\/\d{2}\/\d{4}\s\d{2}:\d{2}:\d{2}\s-\s","",line)
    # regex = re.sub("\\n"," ",regex)
    # print(regex)
    log = log + regex
  print(log)

if __name__=='__main__':
    main()