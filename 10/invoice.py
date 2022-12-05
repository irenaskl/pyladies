import json
import requests
import os
from datetime import date, datetime
import qrcode


DATA_FILE = 'rates.json'
URL_KURZY_CZ_API = "https://data.kurzy.cz/json/meny/b[6].json"
INVOICE = 'template.txt'
ACCOUNT = 'CZ2806000000000168540115'


class CurrencyError(Exception):
    '''Vlastni vyjimka - chyba zadane meny'''
    pass


class Invoice:

    def save_file(self, data, filename) -> None:
        '''Ulozeni url adresy do formatu .text'''
        with open(filename, 'w') as f:
            f.write(data.text)

    def download_file(self, url=URL_KURZY_CZ_API, filename=DATA_FILE):
        '''Stazeni url adresy'''
        page = requests.get(url)
        page.raise_for_status()
        self.save_file(page, filename)

    def actual_data(self):
        '''Kontrola aktualnosti stazene url'''
        today = date.today()
        # Prepsani datumu do potrebneho formatu
        today = today.strftime('%Y%m%d')
        return self.rates['den'] == today

    def file_exists(self):
        '''Kontrola existence souboru, do ktereho
           se ulozi data z url'''
        file_exists = os.path.exists(DATA_FILE)
        return file_exists

    def load_data(self, filename=DATA_FILE):
        '''Ulozeni stazenych dat do promenne'''
        with open(filename) as f:
            self.rates = json.loads(f.read())

    def count(self, amount, currency):
        '''Vypocet konecne castky'''
        czk_currency = ['KC', 'KČ', 'CZK']
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f'Wrong amount: {amount}')

        if amount < 0:
            raise ValueError(f'Wrong amount: {amount}')

        if currency in czk_currency:
            self.final_amount = str(amount)
        elif currency in self.rates['kurzy']:
            amount = amount * self.rates['kurzy'][currency]['dev_stred']
            self.final_amount = str(amount)
        else:
            raise CurrencyError(f'Invalid currency: {currency}')

    def variable_symbol(self):
        '''Vygenerovani unikatniho variabilniho symbolu'''
        symbol = datetime.now()
        self.symbol = symbol.strftime('%f')

    def create_invoice(self, text, file=INVOICE):
        '''Vytvoreni faktury v html'''
        img = qrcode.make(f'SPD*1.0*ACC:{ACCOUNT}*AM:{self.final_amount}*CC:CZK*MSG:{text}*X-VS:{self.symbol}')
        image_qr = 'invoice' + self.symbol +'.png'
        img.save(image_qr)

        # Vymena znaku ve fakture za znaky zadane uzivatelem
        with open(file, 'r') as f:
            template = (f.read())
            template = template.replace('AMOUNT', self.final_amount)
            template = template.replace('SYMBOL', self.symbol)
            template = template.replace('TEXT', text)
            template = template.replace('INV', self.symbol)
            template = template.replace('ACCOUNT', ACCOUNT)
            template = template.replace('QRCODE', image_qr)

        file2 = 'invoice' + self.symbol + '.html'

        # Vytvoreni nove faktury v html
        with open(file2, 'w') as fp:
            fp.write(template)


if __name__ == '__main__':
    faktura = Invoice()
    if faktura.file_exists() is False:
        faktura.download_file()
    faktura.load_data()
    if faktura.actual_data() is False:
        faktura.download_file
    amount = (input('Fill in the amount: '))
    currency = input('Fill in the currency: ').upper()
    text = input('Payment for: ')
    faktura.count(amount, currency)
    faktura.variable_symbol()
    faktura.create_invoice(text)
