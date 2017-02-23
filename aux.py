start_msg = '''
<b>Bem-vindo ao Coinversor Bot!</b>

Use esse bot para ver a atual taxa de conversão de moedas.
Esse bot funciona apenas no <i>modo inline</i>.

<code>@CoinversorBot</code> digite uma moeda (<b>BRL</b> or <b>50eur</b>) e clique em uma opção para enviar uma resposta.
'''

help_msg = '''
Digite uma moeda para saber as cotações em diversas moedas.

<b>Exemplo de uso: </b>@coinversorbot <b>brl or 50BRL</b>

/list para listar todas as moedas disponíveis nesse bot.
'''

list_msg = '''
<b>Moedas Disponíveis</b>
<code>
AUD - Dólar Australiano
BRL - Real
EUR - Euro
GBP - Libra Esterlina
JPY - Yen
PYG - Guaraní Paraguaio
USD - Dólar Americano
</code>
'''

e_amount = str(u' \n\U0001F4B0 ')
e_check = str(u' \U0001F5F8 ')
e_calendar = str(u' \n\U0001F4C5 ')
e_clock = str(u' \n\U0001F550 ')
e_currency = str(u' \U0001F4B1 ')

def get_texts():
    return start_msg, help_msg, list_msg

def get_emojis():
    return e_amount, e_check, e_calendar, e_clock, e_currency

