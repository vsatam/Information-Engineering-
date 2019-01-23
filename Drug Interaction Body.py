
import urllib.request
import bs4 as bs
import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Api Project.html')


proc = subprocess.Popen("name of file.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()

link_1 = 'https://rxnav.nlm.nih.gov/REST/rxcui?name=Zocor%2040%20mg%20oral%20tablet'
html1 = urllib.request.urlopen(link_1).read().decode('utf-8')
soup1 = bs.BeautifulSoup(html1, 'html5lib')
x = str(soup1.find_all('rxnormid')[0])
start=x.find('>')
remaining = x[start:]
e = remaining.find('<')
middle=remaining[1:e]
Drug_1 = middle


link_2 = 'https://rxnav.nlm.nih.gov/REST/rxcui?name=bosentan%20125%20mg%20oral%20tablet'
html2 = urllib.request.urlopen(link_2).read().decode('utf-8')
soup2 = bs.BeautifulSoup(html2, 'html5lib')
y = str(soup2.find_all('rxnormid')[0])
start=y.find('>')
remaining = y[start:]
e = remaining.find('<')
middle=remaining[1:e]
Drug_2 = middle




link_3 = 'https://rxnav.nlm.nih.gov/REST/rxcui?name=Diflucan%2050%20mg%20oral%20tablet'
html3 = urllib.request.urlopen(link_3).read().decode('utf-8')
soup3 = bs.BeautifulSoup(html3, 'html5lib')
z = str(soup3.find_all('rxnormid')[0])
start=z.find('>')
remaining = z[start:]
e = remaining.find('<')
middle=remaining[1:e]
Drug_3 = middle



for i in range (0,3):
    try:
        link_int = 'https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis=' + str(Drug_1) + '+' + str(Drug_2) + '+' + str(Drug_3)
        response = requests.get(link_int)
        t=json.loads(response.text)
        Interaction = t['fullInteractionTypeGroup'][0]['fullInteractionType'][i]['interactionPair'][0]['description']
        print(Interaction)
    except:
        print('No interaction')


