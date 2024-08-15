from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import json
import requests

app = Flask(__name__)


headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://www.flipkart.com",
        "Referer": "https://www.flipkart.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
        # "X-User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 FKUA/website/42/website/Desktop"
    }


def get_price(productID):
    url = f"https://www.flipkart.com/swiss-beauty-long-lasting-misty-finish-professional-makeup-fixer-spray-face-primer-70-ml/p/itm2a28f3ec66d53?pid={productID}"

    response = requests.get(url,headers=headers)
    res = BeautifulSoup(response.content, 'html.parser')
    price_ = res.find('div', {'class': 'Nx9bqj CxhGGd'}).text
    return price_.replace('₹', '')


@app.route('/get_prices', methods=['GET'])
def get_prices():
    style_ids = request.args.get('pids').split(',')
    data = []
    for style_id in style_ids:
        price = get_price(style_id)
        data.append({'PID': style_id, 'price': price})
    return jsonify(data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000,debug=True)

# get_price("PRMFBCHJCZJHUEM8")


