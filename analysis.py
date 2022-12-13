import re

def filterListEmpty(finded):
  filtered = []
  for i in range(len(finded)):
    if len(finded[i]) != 0:
      filtered.append(finded[i])
  return filtered

def filterListEmptyPrint(finded, findedName):
  print("Possíveis " + findedName + ":")
  for elementLine in finded:
    if len(elementLine) != 0:
      for element in elementLine:
        print(element)

def main():
  # log = "" 
  data_log = open("log.txt","r")
  resultsCpfs = []
  resultsCnpjs = []
  resultsEmails = []
  resultsUrls = []
  resultsPhoneNumbers = []
  resultsPasswords = []

  for line in data_log:
    removedDataAndTime = re.sub("\d{2}\/\d{2}\/\d{4}\s\d{2}:\d{2}:\d{2}\s-\s","",line)
    cpfs = re.findall("([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})", removedDataAndTime)
    cnpjs = re.findall("([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})", removedDataAndTime)
    emails = re.findall("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", removedDataAndTime)
    urls = re.findall("^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$", removedDataAndTime)
    phoneNumbers = re.findall("^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$", removedDataAndTime)
    passwords = re.findall("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", removedDataAndTime)

    resultsCpfs.append(cpfs)
    resultsCnpjs.append(cnpjs)
    resultsEmails.append(emails)
    resultsUrls.append(urls)
    resultsPhoneNumbers.append(phoneNumbers)
    resultsPasswords.append(passwords)
    # regex = re.sub("\\n","",regex)

  # https://uibakery.io/regex-library/email-regex-python
  # https://pt.stackoverflow.com/questions/11045/express%C3%A3o-regular-para-validar-um-campo-que-aceita-cpf-ou-cnpj

  filterListEmptyPrint(resultsCpfs, "CPFs")
  filterListEmptyPrint(resultsCnpjs, "CNPJs")
  filterListEmptyPrint(resultsEmails, "Emails")
  filterListEmptyPrint(resultsPhoneNumbers, "números de celulares")
  filterListEmptyPrint(resultsUrls, "URLs")
  filterListEmptyPrint(resultsPasswords,"senhas")

if __name__=='__main__':
    main()