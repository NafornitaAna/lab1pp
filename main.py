import re


def main():
    file = open("input text",'r')
    text = file.read()
    file.close()

    for ch in ".,?!;:":
        text = text.replace(ch,"")

    text=text.lower()


    cuvinte=re.split(" |\n", text)
    cuvinte=list(filter(lambda cuvant: len(cuvant)>6,cuvinte))

    text= " ".join(cuvinte)

    print(text)

if __name__ == '__main__':
    main()

