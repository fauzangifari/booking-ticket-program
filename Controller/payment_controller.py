import midtransclient
import qrcode
from PIL import Image

# Pengaturan akun Midtrans
midtransclient.api_host = 'https://api.sandbox.midtrans.com'
midtransclient.client_key = 'SB-Mid-client-G4gQEFMym2g_A6Dr'
midtransclient.server_key = 'SB-Mid-server-yEZ9NloAmgHRbNtp0cVEELnR'

# Data pembayaran
transaction_details = {
    'order_id': 'ORDER-12345',
    'gross_amount': 100000
}

# Buat transaksi baru
api_client = midtransclient.CoreApi()
transaction = api_client.charge(transaction_details)

# Tampilkan informasi pembayaran
print('Silakan lakukan pembayaran dengan menggunakan QRCode berikut:')
print('ID Transaksi: {}'.format(transaction['transaction_id']))
print('Total Pembayaran: Rp{}'.format(transaction['gross_amount']))

# Buat QRCode dari informasi pembayaran
qrcode_data = 'midtrans://qr?type=0&id={}'.format(transaction['transaction_id'])
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qrcode_data)
qr.make(fit=True)

# Tampilkan QRCode
img = qr.make_image(fill_color="black", back_color="white")
img.show()
