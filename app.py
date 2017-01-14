from flask import *
import pdfkit, os, uuid

app = Flask(__name__)

Download_PATH = 'wkhtmltopdf/bin/wkhtmltopdf.exe'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Download_FOLDER = os.path.join(APP_ROOT, Download_PATH)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/api/wkhtmltopdf_url", methods=['POST'])
def wkhtmltopdfurl():
    url = request.form['URL']
    try:
        filename = str(uuid.uuid4()) + '.pdf'
        config = pdfkit.configuration(wkhtmltopdf=Download_FOLDER)
        pdfkit.from_url(url, filename, configuration=config)
        pdfDownload = open(filename, 'rb').read()
        os.remove(filename)
        return Response(
            pdfDownload,
            mimetype="application/pdf",
            headers={
                "Content-disposition": "attachment; filename=" + filename,
                "Content-type": "application/force-download"
            }
        )
    except ValueError:
        print("Oops! ")


@app.route("/api/wkhtmltopdf_template", methods=['POST'])
def wkhtmltopdf_template():
    filename = str(uuid.uuid4()) + '.pdf'
    config = pdfkit.configuration(wkhtmltopdf=Download_FOLDER)
    body = '''
    <p style="text-align:center;font-size:large;">明 細 表</p>
    <hr>
    <p style="margin-top: 15px;margin-bottom: 15px;margin-left: 150px; font-size:large;">訂單編號 :  {} </p>
    <p style="margin-top: 15px;margin-bottom: 15px;margin-left: 150px; font-size:large;">交易方式 :  {}  </p>
    <p style="margin-top: 15px;margin-bottom: 15px;margin-left: 150px; font-size:large;">交易帳號 :  {}  </p>
    <hr>
    <p style="margin-top: 15px;margin-bottom: 15px;margin-left: 150px; font-size:large;">姓名 :  {}  </p>
    <p style="margin-top: 15px;margin-bottom: 15px;margin-left: 150px; font-size:large;">身分證字號 :  {} </p>
    <img style="position: fixed;bottom: 50px;right: 0; height:50%; width:auto;" src="http://i.imgur.com/uLhrB27.jpg" alt="新垣結衣" title="新垣結衣">
            '''.format(
        "123456789",
        "信用卡",
        "xxxxxxx1111111",
        "twtrubiks",
        "A000000000"
    )
    options = {
        'encoding': 'UTF-8'
    }
    pdfkit.from_string(body, filename, configuration=config, options=options)
    pdfDownload = open(filename, 'rb').read()
    os.remove(filename)
    return Response(
        pdfDownload,
        mimetype="application/pdf",
        headers={
            "Content-disposition": "attachment; filename=" + filename,
            "Content-type": "application/force-download"
        }
    )
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug='True')
