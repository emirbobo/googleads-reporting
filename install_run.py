import os

# os.getcwd() #get current work direction.
# val2 = os.chdir('D:\\workProgram\\py\\scrapy\\web_spider\\')
val = os.system('pip freeze > requirements.txt')
val = os.system('pip install -r requirements.txt')
