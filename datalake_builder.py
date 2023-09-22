import os


def parse_files():
    for filename in os.listdir('books_datalake'):
        name = filename.split('.txt')[0].split('_')[2]

        with open(os.path.join('books_datalake', filename), encoding="utf-8") as f:
            text = f.read()

            text = text.split('***')

            with open(os.path.join('metadata', name + '.metadata'), 'w', encoding="utf-8") as f:
                f.write(text[0] + '***' + text[1] + '***')
                f.write('\n')
                f.write(text[-1])

            with open(os.path.join('data', name + '.txt'), 'w', encoding="utf-8") as f:
                f.write(text[2].lower())
