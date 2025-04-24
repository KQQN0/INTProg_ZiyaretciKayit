from flask import Flask, render_template, request, redirect, url_for

uygulama = Flask(__name__)

@uygulama.route('/', methods=['GET', 'POST'])
def ana_sayfa():
    if request.method == 'POST':
        kullanici_adi = request.form['kullanici_adi']
        sifre = request.form['sifre']
        print(f"Giriş denemesi: Kullanıcı Adı: {kullanici_adi}, Şifre: {sifre}")
        return "Giriş Başarılı"
    return render_template('index.html')

if __name__ == '__main__':
    uygulama.run(debug=True)
    #hocam bazı arakdaşlara sordum bu olmicak dedi sizin attığınızda yazıyodu bilemedim : konsola giriş başarılı yazıyo sadece