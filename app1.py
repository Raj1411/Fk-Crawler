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
        "X-User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 FKUA/website/42/website/Desktop"
    }


def get_price(productID):
    url = f"https://www.flipkart.com/swiss-beauty-long-lasting-misty-finish-professional-makeup-fixer-spray-face-primer-70-ml/p/itm2a28f3ec66d53?pid={productID}"
    session = requests.Session()
    session.headers.update(headers)
    cookies = {
    'T': 'clw5wksvz14n62bftz2na6juq-BR1715661529920',
    'SN': 'VIF8EC90F1AF514015AB97157CA93993D1.TOKA6D8ED18965648468AE9BA7B94556A13.1723725739.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MjU0NTM3MDcsImlhdCI6MTcyMzcyNTcwNywiaXNzIjoia2V2bGFyIiwianRpIjoiMTZhODQ3ZjMtYmIxZi00YzY1LWI4ZWYtZmJkMDk1YjU3M2Q1IiwidHlwZSI6IkFUIiwiZElkIjoiY2x3NXdrc3Z6MTRuNjJiZnR6Mm5hNmp1cS1CUjE3MTU2NjE1Mjk5MjAiLCJrZXZJZCI6IlZJRjhFQzkwRjFBRjUxNDAxNUFCOTcxNTdDQTkzOTkzRDEiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.ubd6HFdWHbUmkKtkCgOoh8disR1YGx8kSAKpa20R35c'
}

    # Update session cookies
    session.cookies.update(cookies)

    response = session.get(url)
    res = BeautifulSoup(response.text, 'html.parser')
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
    app.run('0.0.0.0',debug=True)

# get_price("PRMFBCHJCZJHUEM8")


