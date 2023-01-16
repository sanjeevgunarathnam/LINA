import wolframalpha

client = wolframalpha.Client('EKER4Q-57GXHXEXHE')

while True:
    query = str(input('query: '))
    res = client.query(query)
    output = next(res.results).text
    print(output)