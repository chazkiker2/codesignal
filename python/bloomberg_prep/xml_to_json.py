import re

# used to hold the JSON-shaped data after parsing the XML
dom = {}


def parse_stream(stream):
    global dom

    current_book = None
    current_key = None
    for entry in stream:
        # if the entry ENDS an existing token
        if entry[0:2] == "</":
            split_entry = entry[2:-1].split()
            if split_entry[0] == "book":
                current_book = None
            else:
                current_key = None
        # else if the entry STARTS a new token
        elif entry[0] == "<":
            split_entry = entry[1:-1].split()
            # if the token is a book, we need to make a new entry for it in our
            # dictionary, and we need to set it as the book we are currently parsing
            if split_entry[0] == "book":
                book_id = split_entry[1].split("=")[1][1:-1]
                dom[book_id] = {}
                current_book = book_id
            # otherwise, we have run across a new key to input for our current book
            else:
                current_key = split_entry[0]
        # else, the entry is not a token (just data)
        else:
            if current_key and current_book:
                if current_key not in dom[current_book]:
                    dom[current_book][current_key] = ""
                dom[current_book][current_key] += entry


def xml_to_json(filename):
    global dom
    token_stream = []
    with open(filename) as f:
        for line in f:
            token_stream += [
                entry for entry in re.split('(<[^>]*>)', line.strip()) if entry
            ]

    parse_stream(token_stream)

    return dom


def xml_to_json_no_rgx(filename):
    global dom
    token_stream = []
    with open(filename) as f:
        for line in f:
            d1 = "<"
            d2 = ">"

            for entry in line.strip().split(d1):
                if entry:
                    entry2 = entry.split(d2)
                    str_entry2 = f"{entry2}{d2}" if entry2 else ""
                    print(f"{entry2=}")

                    print(f"{d1}{entry}")

    print(token_stream)
    parse_stream(token_stream)
    return dom


if __name__ == '__main__':
    print(xml_to_json_no_rgx("books.xml"))
