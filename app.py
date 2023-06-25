from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hesap_makinesi():
    if request.method == 'POST':
        sayi1 = float(request.form['sayi1'])
        sayi2 = float(request.form['sayi2'])
        islem = request.form['islem']
        
        if islem == 'toplama':
            sonuc = sayi1 + sayi2
        elif islem == 'cikarma':
            sonuc = sayi1 - sayi2
        elif islem == 'carpma':
            sonuc = sayi1 * sayi2
            
        # İşlem seçeneklerine göre sonucu hesaplayın ve burada ekleyin
        
        return render_template('index.html', sayi1=sayi1, sayi2=sayi2, islem=islem, sonuc=sonuc)
    
    return render_template('index.html', sayi1=None, sayi2=None, islem=None, sonuc=None)

if __name__ == '__main__':
    app.run(debug=True, port=8090)
