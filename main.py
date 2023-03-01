def main():
    file = open("input text",'r')
    text = file.read()
    file.close()

    for ch in ".,?!;:":
        text = text.replace(ch,"")

    print(text)


if __name__ == '__main__':
    main()

