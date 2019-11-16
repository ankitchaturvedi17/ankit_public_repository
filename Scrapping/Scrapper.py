from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re



driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
driver.maximize_window()

#url = 'https://www.amazon.com/Apple-Unlocked-Smartphone-Certified-Refurbished/product-reviews/B00YD545CC/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'
#url = 'https://www.amazon.com/ESR-Tempered-Scratch-Resistant-Silicone-Absorption/product-reviews/B079HMTYYL/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'
#url = 'https://www.amazon.com/Spigen-Hybrid-Cushion-Technology-Protection/product-reviews/B074CMHQW5/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'

URLS = ["https://www.amazon.com/Optimum-Nutrition-Standard-Protein-Chocolate/dp/B000QSNYGI/ref=zg_bs_6973706011_2?_encoding=UTF8&refRID=Z3Q73J5SZVJNT9N2E01G&th=1","https://www.amazon.com/BSN-SYNTHA-6-Replacement-Chocolate-Milkshake/dp/B002DYJ1EC/ref=sr_1_3_s_it?s=grocery&ie=UTF8&qid=1524485023&sr=1-3&keywords=Syntha-6%2B5lbs&dpID=51kbLsRd1rL&preST=_SY300_QL70_&dpSrc=srch&th=1","https://www.amazon.com/Isopure-Protein-Powder-Isolate-Flavor/dp/B000E95HP0/ref=zg_bs_6973706011_9?_encoding=UTF8&refRID=Z3Q73J5SZVJNT9N2E01G&th=1","https://www.amazon.com/dp/B002DUD6QU?aaxitk=dZlMqARGrNthd.XhoRTq9g&pd_rd_i=B002DUD6QU&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3534726502&pd_rd_wg=VXJa6&pf_rd_r=M2H7J4EYJ52WA92R4J6T&pf_rd_s=desktop-sx-top-slot&pf_rd_t=301&pd_rd_w=5wPty&pf_rd_i=Muscle%2Bmilk&pd_rd_r=c2c88bfc-29f5-43eb-b3e5-b48cfcdf9454&hsa_cr_id=9413824230201&th=1","https://www.amazon.com/Orgain-Organic-Protein-Chocolate-Packaging/dp/B00J074W94/ref=zg_bs_6973706011_1?_encoding=UTF8&refRID=Z3Q73J5SZVJNT9N2E01G&th=1","https://www.amazon.com/Garden-Life-Meal-Replacement-Gluten-Free/dp/B007S6Y74O/ref=zg_bs_6973706011_5?_encoding=UTF8&refRID=Z3Q73J5SZVJNT9N2E01G&th=1","https://www.amazon.com/MusclePharm-Combat-Protein-Powder-Essential/dp/B003BVI5FW/ref=zg_bs_6973706011_10?_encoding=UTF8&psc=1&refRID=Z3Q73J5SZVJNT9N2E01G","https://www.amazon.com/Dymatize-Protein-Isolate-Gourmet-Vanilla/dp/B00HJR6SNK/ref=sr_1_1_sspa?s=hpc&ie=UTF8&qid=1524485778&sr=1-1-spons&keywords=Dymatize&th=1","https://www.amazon.com/MuscleTech-NitroTech-Protein-Isolate-Cappuccino/dp/B00M8ZFGEK/ref=sr_1_2_sspa?s=hpc&ie=UTF8&qid=1524485308&sr=1-2-spons&keywords=muscle%2Btech&th=1","https://www.amazon.com/JYM-Supplement-Science-Proteins-Chocolate/dp/B01HGQZZZU/ref=sr_1_cc_1_a_it?s=aps&ie=UTF8&qid=1524485137&sr=1-1-catcorr&keywords=Pro%2BJYM%2C%2B4%2BLbs&th=1"," https://www.amazon.com/Vega-Protein-Greens-Vanilla-servings/dp/B00MYRXIIS/ref=zg_bs_6973706011_4?_encoding=UTF8&refRID=Z3Q73J5SZVJNT9N2E01G&th=1"]
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


startscraping = []
for URL in URLS:
    loc = find_nth(URL, "/", 4)
    start_skucode = find_nth(URL, "/", 5)
    end_skucode = find_nth(URL, "/", 6)
    page1_url = (URL[:loc + 1] + 'product-reviews' + URL[
                                                     start_skucode:end_skucode] + '/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews')
    startscraping.append(page1_url)


waittime=10
AppendFile = open('ReviewsNEW.csv','a')




def reviews(elements):
    for element in elements:
        AppendFile.write('\n')
        #elem1 = element.find_elements_by_class_name('a-row')

        elem1 = element.find_element_by_xpath(".//*[@class='a-link-normal']")

        Rating = elem1.get_attribute("title").split('.')
        Rating = Rating[0]
        reviewtext = element.text.split('\n')
        if reviewtext[0] == "The manufacturer commented on the review below":
            del reviewtext[0]
        customer= reviewtext[1].split(' ')
        customerlength = len(customer)
        customername = ''
        for i in range(0,customerlength-3):
            customername = customername +customer[i]
        date = customer[customerlength-3] +' '+ customer[customerlength-2]+' '+ customer[customerlength-1]
        date = date.replace(',',' ')
        customername =customername[2:-2].replace(',',' ')
        MainReview = reviewtext[0].replace(',',' ')
        completereview = reviewtext[4].replace(',',' ')
        try:
            AppendFile.write(Rating+','+MainReview+','+customername+','+date +','+MainReview+','+completereview)
        except:
            AppendFile.write(Rating + ',' + re.sub('[^a-zA-Z]',' ',MainReview) + ',' + re.sub('[^a-zA-Z]',' ',customername) + ',' + date + ',' + re.sub('[^a-zA-Z]',' ',MainReview) + ',' + re.sub('[^a-zA-Z]',' ',completereview))


for URL in startscraping:
    AppendFile.write('\n')
    url = URL
    driver.get(url)
    #elements = driver.find_elements_by_xpath('//*[@id="cm_cr-review_list"]/[[ancestor::*] And [contains(@id,"customer_review")]]')

    try:
        while driver.find_element_by_class_name('a-last').is_displayed() == True:

            print('try')
            elements = driver.find_elements_by_xpath('//*[contains(@id,"customer_review")]')
            reviews(elements)
            #nextbutton = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[5]/a')
            time.sleep(1)
            nextbutton = driver.find_element_by_class_name('a-last')
            nextbutton.click()
            time.sleep(4)
            '''
            try:
                WebDriverWait(driver, waittime).until(EC.elementToBeClickable((By.CLASS_NAME, 'a-last')))
            except:
                print('Why')
            '''
    except:
        print('Exception')
        elements = driver.find_elements_by_xpath('//*[contains(@id,"customer_review")]')
        reviews(elements)

print('Last Step')
