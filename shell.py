import alpaga

while True:
    text = input('alpaga > ')
    result, error = alpaga.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)

