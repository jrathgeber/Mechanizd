import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_stock_gainers():
    # URL for TradingView pre-market gainers
    url = "https://www.tradingview.com/markets/stocks-usa/market-movers-pre-market-gainers/"

    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Make the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the stock data
        table = soup.find('table', class_='table-Ngq2xrcG')

        if table:
            # Lists to store our data
            stocks = []

            # Process each row
            for row in table.find_all('tr')[1:]:  # Skip header row
                cells = row.find_all('td')
                if len(cells) >= 2:
                    # Extract ticker and company name
                    ticker_cell = cells[0].find('a', class_='tickerName-GrtoTeat')
                    company_cell = cells[0].find('sup', class_='tickerDescription-GrtoTeat')

                    # Extract percentage gain
                    gain_cell = cells[1].text.strip()

                    if ticker_cell and gain_cell:
                        ticker = ticker_cell.text.strip()
                        company = company_cell.text.strip() if company_cell else "N/A"
                        gain = gain_cell

                        stocks.append({
                            'Ticker': ticker,
                            'Company': company,
                            'Gain': gain
                        })

            # Convert to pandas DataFrame for nice display
            df = pd.DataFrame(stocks)
            print("\nTop Stock Gainers:")
            print("==================")
            for _, row in df.iterrows():
                print(f"{row['Ticker']} ({row['Company']}): {row['Gain']}")

        else:
            print("Could not find the stock table in the page")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    get_stock_gainers()