import json
import requests
import os
from datetime import date, datetime
import qrcode
from requests.exceptions import RequestException


DATA_FILE = 'rates.json'
URL_KURZY_CZ_API = "https://data.kurzy.cz/json/meny/b[1].json"
INVOICE = 'template.txt'
ACCOUNT = 'CZ2806000000000168540115'


class CurrencyError(Exception):
    '''Vlastni vyjimka - chyba zadane meny'''
    pass


class Invoice:

    CZK_CURRENCY = ('KC', 'KČ', 'CZK', 'CZ')

    def save_file(self, data, filename) -> None:
        '''Ulozeni url adresy do formatu .text'''
        with open(filename, 'w') as f:
            f.write(data)

    def download_file(self, url=URL_KURZY_CZ_API, filename=DATA_FILE) -> None:
        '''Stazeni url adresy'''
        page = requests.get(url)
        page.raise_for_status()
        data = page.json()
        self.save_file(data, filename)

    def actual_data(self) -> bool:
        '''Kontrola aktualnosti stazene url'''
        today = date.today()
        # Prepsani datumu do potrebneho formatu
        today = today.strftime('%Y%m%d')
        return self.rates['den'] == today

    def file_exists(self) -> bool:
        '''Kontrola existence souboru, do ktereho
        se ulozi data z url'''
        file_exists = os.path.exists(DATA_FILE)
        return file_exists

    def load_data(self, filename=DATA_FILE) -> None:
        '''Ulozeni stazenych dat do promenne'''
        with open(filename) as f:
            self.rates = json.loads(f.read())

    def count(self, amount, currency) -> None:
        '''Vypocet konecne castky'''
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f'Wrong amount: {amount}')

        if amount < 0:
            raise ValueError(f'Wrong amount: {amount}')

        if currency in self.CZK_CURRENCY:
            self.final_amount = str(amount)
        elif currency in self.rates['kurzy']:
            amount = amount * self.rates['kurzy'][currency]['dev_stred']
            self.final_amount = str(amount)
        else:
            raise CurrencyError(f'Invalid currency: {currency}')

    def variable_symbol(self) -> None:
        '''Vygenerovani unikatniho variabilniho symbolu'''
        symbol = datetime.now()
        self.symbol = symbol.strftime('%f')

    def create_qr(self, text, file=INVOICE) -> None:
        '''Vytvoreni qr kodu'''
        img = qrcode.make(f'SPD*1.0*ACC:{ACCOUNT}*AM:{self.final_amount}*CC:CZK*MSG:{text}*X-VS:{self.symbol}')
        self.image_qr = (f'invoice{self.symbol}.png')
        img.save(self.image_qr)

    def create_invoice(self, file=INVOICE) -> None:
        '''Vytvoreni faktury v html'''
        with open(file, 'r') as f:
            template = self.render_template(f.read())

        file2 = (f' invoice{self.symbol}.html')
        # Vytvoreni nove faktury v html
        with open(file2, 'w') as fp:
            fp.write(template)

    def render_template(self, file_content) -> str:
        '''Vyplneni html faktury dle zadani uzivatele'''
        template_dict = {
            'AMOUNT' : self.final_amount,
            'SYMBOL' : self.symbol,
            'TEXT' : text,
            'INV' : self.symbol,
            'ACCOUNT' : ACCOUNT,
            'QRCODE' : self.image_qr,
        }

        for name, value in template_dict.items():
            file_content = file_content.replace(name, str(value))
        return file_content


if __name__ == '__main__':
    faktura = Invoice()
    if faktura.file_exists() is False:
        try:
            faktura.download_file()
        except RequestException:
            print('Request error - chyba pri nacitani kurzovniho listku')
            exit(1)
        except Exception:
            print('Unknown error - chyba pri nacitani kurzovniho listku')
    faktura.load_data()
    if faktura.actual_data() is False:
        faktura.download_file
    amount = input('Fill in the amount: ')
    currency = input('Fill in the currency: ').upper()
    text = input('Payment for: ')
    faktura.count(amount, currency)
    faktura.variable_symbol()
    faktura.create_qr(text)
    faktura.create_invoice()
