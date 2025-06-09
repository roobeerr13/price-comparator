from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product = request.form['product']
        # Simulación de resultados (luego usaremos APIs reales)
        results = [
            {'store': 'Amazon', 'price': '$29.99', 'link': f'https://amazon.com/s?k={product}&tag=TU_TAG_AFILIADO'},
            {'store': 'eBay', 'price': '$25.00', 'link': f'https://ebay.com/s?k={product}&tag=TU_TAG_EBAY'}
        ]
        return render_template('results.html', product=product, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)