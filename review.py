from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('/home/shreyash/Downloads/chromedriver_linux64 (1)/chromedriver')

print("Current session is {}".format(driver.session_id))
reviews = pd.DataFrame(columns=['Date', 'Name', 'Reviews', 'Stars'])


def getDATA(x):
    try:
        driver.get(
            "https://www.amazon.in/Samsung-Galaxy-Midnight-128GB-Storage/product-reviews/B07HGJKDRR/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=" + str(
                x))

    except Exception as e:
        print(e.message)

    ids = driver.find_elements_by_xpath("//*[contains(@id,'customer_review-')]")
    review_id = []
    for i in ids:
        review_id.append(i.get_attribute('id'))
    for x in review_id:
        # extracts dates from page
        user_date = driver.find_elements_by_xpath('//*[@id="' + x + '"]/span')[0]
        date = user_date.text

        # extracts name from page

        username_element = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div[1]/a/div[2]/span')[0]
        username = username_element.text

        # extracts reviews from page
        user_message = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div[4]')[0]
        message = user_message.text

        star_rating = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div[2]/a[1]')[0]
        print(star_rating)
        star = star_rating.get_attribute('title')
        print(star)

        # appending to dataframe
        reviews.loc[len(reviews)] = [date, username, message, star]

        print(reviews)
    pass


for x in range(0, 2):
    getDATA(x)

reviews.to_csv('test.csv')
driver.close()
