import requests
from bs4 import BeautifulSoup
import json
#################################
def view():
    print('_'*44)
#################################
def get_citations_number(url) :  
    res = requests.get(url)
    soup = BeautifulSoup(res.content , 'html.parser')
    data = soup.find_all('a' , title="Wikipedia:Citation needed")
    return len(data)

def get_citations_passage(url): 
    res = requests.get(url)
    soup = BeautifulSoup(res.content , 'html.parser')
    text = soup.find_all( 'p') 
    
    output=[]
    for passege in text :
        citations_passage = {'passage':''} 
        result = passege.find_all('a' , title="Wikipedia:Citation needed")
        if result : 
            citations_passage['passage'] =  passege.text.strip()
            output.append(citations_passage)
    return output

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    
if __name__ == "__main__" : 
    view()
    print (get_citations_number(URL))
    view()
    print (get_citations_passage(URL))
    view()

with open('citations_passage.json', 'w') as f :
    content = json.dumps(get_citations_passage(URL))
    f.write(content)
