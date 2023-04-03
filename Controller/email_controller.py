from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

def kirimEmail(email, receipt_id, flight_id, name, from_location, to_location, plane, ticket_code):
    message = Mail(
        from_email='fauzan@janjianaja.com',
        to_emails=email)

    message.dynamic_template_data = {
        'subject': 'TRAVELOKA: Receipt #' + receipt_id,
        'nomor_pesanan': receipt_id,
        'nomor_penerbangan': flight_id,
        'nama': name,
        'email': email,
        'asal_penerbangan': from_location,
        'tujuan_penerbangan': to_location,
        'pesawat': plane,
        'kode_tiket': ticket_code,
        'jam': '10:51',
        'hari': 'Senin',
        'tanggal': '10',
        'bulan': 'Januari',
        'tahun': '2023',
    }
    message.template_id = 'd-df19ec40d75b465c8f4ca6e7f29a4e61'

    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        print(f"Response code: {code}")
        print(f"Response headers: {headers}")
        print(f"Response body: {body}")
        print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))


kirimEmail('fauzan.gifari30@gmail.com', '67088001', 'GA201',
           'Muhammad Fauzan Gifari', 'Samarinda', 'Surabaya',
           'Garuda Indonesia', 'B10D8ZAA1')
