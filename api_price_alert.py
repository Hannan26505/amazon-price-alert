import os
import requests
import smtplib

url = "https://www.amazon.in/dp/B0FNS4VPR3"

api_key = os.environ["AMAZON_API_KEY"].strip()

target_price = 1600

headers = {
    "x-api-key": api_key
}

params = {
    "asin": "B0FNS4VPR3",
    "country": "IN"
}

response = requests.get(
    "https://api.openwebninja.com/realtime-amazon-data/product-details",
    headers=headers,
    params=params
)

print("Status code:", response.status_code)

data = response.json()["data"]

title = data["product_title"]
price = float(data["product_price"])
product_link = data["product_url"]

print(title)
print(price)
print(product_link)

if price <= target_price:

    my_email = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(
            user=my_email,
            password=password
        )

        connection.sendmail(
            from_addr=my_email,
            to_addrs="maazsidpython@gmail.com",
            msg=f"Subject: PRICE DROP ALERT!\n\n"
                f"{title}\n"
                f"Now available at Price Rs {price}\n\n"
                f"Buy here: {product_link}"
        )

    print("Price drop email sent successfully!")

else:
    print("Price is above target price.")