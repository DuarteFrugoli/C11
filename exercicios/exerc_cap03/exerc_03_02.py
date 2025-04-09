loja1 = {'Apple iPhone 15',
         'Samsung Galaxy S23',
         'Samsung Galaxy A15 5G',
         'Oppo Find N2 Flip',
         'Sony Xperia 1 V',
         'Vivo X90 Pro',
         'Asus ROG Phone 7',
         'Motorola Edge 50 Ultra'}
loja2 = {'Apple iPhone 15',
         'Sony Xperia 1 V',
         'Samsung Galaxy S23',
         'Asus ROG Phone 7',
         'Motorola Edge 50 Ultra',
         'Razr 50 Ultra',
         'Galaxy S25 Ultra'}

print(f'Smartphones disponíveis na loja 1: {loja1}')
print(f'Smartphones disponíveis na loja 2: {loja2}')
print(f'Smartphones disponíveis nas 2 lojas no total: {loja1|loja2}')
print(f'Smartphones disponíveis em ambas as lojas: {loja1&loja2}')