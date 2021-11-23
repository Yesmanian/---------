filename = 'corpus.txt'


def filter_by_text(text):
    # 주어진 규칙에 맞추어 filter_by_text()함수를 구현해주세요.
    # corpus.txt에 있는 텍스트를 읽어와서 corpus라는 리스트에 추가한다.
    corpus = []
    processed_text = import_as_tuple(filename)
    corpus.append(processed_text)
    # print(corpus)
    # corpus에 있는 데이터 중, text로 시작하는 단어만을 추려서 result라는 리스트에 저장한다.
    result = []
    for word,fre in corpus[0]:
        if word.startswith(text):
            result.append((word,int(fre)))

    # 찾은 영어 단어를 빈도수를 기준으로 내림차순으로 정렬하여 20개만 출력한다.
    print(sort_by_frequency(result))

    return result


def import_as_tuple(filename):
    tuples = []
    with open(filename) as file:
        for line in file:
            # 아래 코드를 작성하세요.
            split = line.strip().split('/')
            word = split[0]
            freq = split[1]
            new_tuple = (word, freq)
            tuples.append(new_tuple)

    return tuples


def get_freq(pair):
    return pair[1]


def sort_by_frequency(pairs):
    return sorted(pairs, key=get_freq,reverse=True)[:20]


# 아래 부분은 수정하지 마세요!
# 입력과 출력을 수행하는 코드입니다.
t = input()
filter_by_text(t)

a = [1, 2, 3, 4, 5]

print(list(filter(lambda x:x%2, list(map(lambda x:x**2, a)))))