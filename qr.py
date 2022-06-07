import qrcode

def qr_make(url='https://www.mrc.ru', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created - {name}.png'


def main():
    print(qr_make())

if __name__ == '__main__':
    main()

