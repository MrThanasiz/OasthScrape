import sys


def getData(stopid):

    import bs4 as bs
    from selenium import webdriver


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(chrome_options=chrome_options) 
    driver.get('http://oasth.gr/#el/stopinfo/screen/'+stopid+'/')
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    

    soup = bs.BeautifulSoup(res,'lxml')

    
    p_tag = soup.find("h2", text="Άφιξη Λεωφορείων στη στάση")
    print("Σταση: ",stopid)  ##TODO: ADD STOP NAME HERE...
    if p_tag is None:
        print("Η Στάση δεν υπάρχει ή υπάρχει κάποιο πρόβλημα δικτύου")
    else:
        if len(p_tag.find_next_siblings("ul")) == 0:
            print("Δεν υπάρχουν διερχόμενα λεωφορεία")
        else:
            list1=[]
            print("Έρχονται τα παρακάτω: ")
            for li in p_tag.find_next_siblings("ul")[0].find_all("li"):
                #print(li.text)
                list1.append(li.text)
            list2=[]
            for i in range(len(list1)):
                list2.append(list1[i].replace("\n"," "))
                #list3.append(list2[i].replace("άφιξη","  άφιξη"))##TODO: FIX THIS SO IT LOOKS BETTER...
                #print("i=",i,"list=", end="")
                print(list2[i])
