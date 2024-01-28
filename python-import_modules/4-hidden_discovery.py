#!/usr/bin/python3
# prints the names in a compiled module
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    count = len(content)
    for i in range(count):
        if "__" in content[i]:
            continue
        print(content[i])
