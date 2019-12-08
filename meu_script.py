import json


def main():
    with open('data.json', mode='r') as fp:
        raw_data = json.load(fp)
        count = len(raw_data)
        sorted_data = sorted(raw_data)
        max_entry = max(raw_data)
        min_entry = min(raw_data)
        sum_entries = sum(raw_data)

        print(f"a lista contem: {count} elementos")
        print(f"a lista ordenada fica: {sorted_data}")
        print(f"o maior elemento da lista é: {max_entry}")
        print(f"o menor elemento da lista é: {min_entry}")
        print(f"a soma dos elementos da lista é: {sum_entries}")

if __name__ == '__main__':
    main()
