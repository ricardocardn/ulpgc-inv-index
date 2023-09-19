from InvertedIndexHandler import InvertedIndexHandler


def main():
    iih = InvertedIndexHandler()
    iih.insert_word_document("word", "001")
    iih.insert_word_document("word", "001")
    iih.insert_word_document("word", "002")


if __name__ == "__main__":
    main()
