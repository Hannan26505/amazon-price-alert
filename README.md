# 🛒 Amazon Price Alert

A Python-based Amazon price tracking system that automatically checks the price of a product and sends an email notification when the price drops below a predefined target price.

The project uses an Amazon product data API and GitHub Actions to run the price checker automatically every day without requiring the user's computer to be turned on.

---

## 🚀 Features

- 🔍 Fetches Amazon product information using an API
- 💰 Checks the current product price
- 🎯 Compares the price with a predefined target price
- 📧 Sends an email alert when the price reaches the target
- ⏰ Runs automatically every day using GitHub Actions
- 🔐 Uses GitHub Secrets to protect API and email credentials
- ▶️ Supports manual workflow execution through GitHub Actions

---

## 🛠️ Technologies Used

- **Python**
- **Requests** — API requests
- **SMTP** — Email notifications
- **OpenWeb Ninja Amazon Data API** — Amazon product information
- **Git & GitHub**
- **GitHub Actions** — Cloud-based automation

---

## ⚙️ How It Works

```text
                 GitHub Actions
                       │
                       ▼
              api_price_alert.py
                       │
                       ▼
             Amazon Data API
                       │
                       ▼
                Product Price
                       │
                       ▼
              Compare with Target
                    Price
                  /       \
                 /         \
        Price <= Target   Price > Target
              │                 │
              ▼                 ▼
        Send Email          No Email
           Alert

## 📌 Example

    If the target price is:

    ₹1600

    and the API returns:

    Current Price: ₹799

    The program checks:

    799 <= 1600

    Since the condition is true, an email price-drop alert is sent.

## 🔐 Security

    Sensitive credentials are not stored directly in the source code.

    The project uses GitHub Secrets for:

    AMAZON_API_KEY
    EMAIL_ADDRESS
    EMAIL_PASSWORD

    These values are passed to the Python program as environment variables during the GitHub Actions workflow.

## ⏰ Automation

    The GitHub Actions workflow is scheduled to run once every day at 9:00 PM IST.

    The workflow can also be triggered manually using GitHub's Run workflow option.

## 📂 Project Structure

`    Amazon_Price_Alert/
    │
    ├── api_price_alert.py
    ├── main.py
    ├── .gitignore
    ├── README.md
    │
    └── .github/
        └── workflows/
            └── price_tracker.yml`

## Files

    api_price_alert.py

    Main program that retrieves the Amazon product price through the API and sends the email alert.

    main.py

    Original version of the project that used Requests and BeautifulSoup for Amazon price scraping.

    price_tracker.yml

    GitHub Actions workflow responsible for running the price tracker automatically.

## 🔄 Evolution of the Project

    The project was initially developed using:

    Requests → BeautifulSoup → Amazon webpage → Price

    During cloud automation, Amazon's automated-access protection made direct scraping unreliable.

    The project was therefore improved to use:

    Python → Amazon Data API → Product Price

    This API-based approach is used by the GitHub Actions automation.

## 🔮 Future Improvements

    Track multiple products simultaneously
    Store historical prices
    Create price history graphs
    Add Telegram/WhatsApp notifications
    Add a web dashboard
    Allow users to set their own target prices
    Store price history in a database

## 👨‍💻 Author

    Hannan

    GitHub: Hannan26505