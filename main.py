import requests
from bs4 import BeautifulSoup  
import smtplib
import os

url = "https://www.amazon.in/GHPC-Striped-Sleeves-Regular-FSH523319_42/dp/B0FNS4VPR3/ref=sl_ob_desktop_dp_0_1_v2?_encoding=UTF8&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

my_email = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]
to_email = os.environ["TO_EMAIL"]

target_price = 1600


response = requests.get(url, headers=headers)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    
    title_element = soup.find(
        name="span",
        class_="a-size-large product-title-word-break"
    )

   
    price_element = soup.find(
        name="span",
        class_="a-price-whole"
    )

    
    if title_element and price_element:

        title = title_element.getText().strip()

        price_whole = price_element.getText().strip()
        price = float(price_whole.replace(",", ""))

        print(title)
        print(price)

       
        if price <= target_price:

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()

                connection.login(
                    user=my_email,
                    password=password
                )

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=to_email,
                    msg=f"Subject: PRICE DROP ALERT!\n\n"
                        f"{title}\n"
                        f"Now available at Price Rs {price}\n\n"
                        f"Buy here: {url}"
                )

                print("Price drop email sent!")

        else:
            print("Price is above target price.")

    else:
        print("Could not find title or price.")

else:
    print("Could not access Amazon.")
    print("Status code:", response.status_code)