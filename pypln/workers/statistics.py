# coding: utf-8

from collections import Counter


__meta__ = {'from': 'document',
            'requires': ['freqdist', 'sentences'],
            'to': 'document',
            'provides': ['momentum-1', 'momentum-2', 'momentum-3',
                         'momentum-4', 'repertoire', 'average-sentence-length',
                         'average-sentence-repertoire'],
}

def _get_momenta(distribution):
    total = 0
    momentum_1 = 0
    momentum_2 = 0
    momentum_3 = 0
    momentum_4 = 0
    for x, y in distribution:
        momentum_1 += y * x
        momentum_2 += y * x * x
        momentum_3 += y * x * x * x
        momentum_4 += y * x * x * x * x
        total += y
    total = float(total)
    return (momentum_1 / total, momentum_2 / total, momentum_3 / total,
            momentum_4 / total)

def _histogram(freqdist):
    counter = Counter()
    for x, y in freqdist:
        counter[y] += 1
    return sorted(counter.most_common())


def main(document):
    freqdist = document['freqdist'] # eg: [('word', 100), ('other', 97)]
    sentences = document['sentences'] # eg: [['1st', 'sentence.'], ['2nd!']]
    momenta = _get_momenta(_histogram(freqdist))
    total_tokens = float(sum(dict(freqdist).values()))
    repertoire = len(freqdist) / total_tokens
    sentence_repertoire_sum = 0
    for sentence in sentences:
        sentence_repertoire_sum += len(set(sentence)) / float(len(sentence))
    number_of_sentences = len(sentences)
    average_sentence_length = total_tokens / number_of_sentences
    sentence_repertoire = sentence_repertoire_sum / number_of_sentences
    return {'momentum-1': momenta[0],
            'momentum-2': momenta[1],
            'momentum-3': momenta[2],
            'momentum-4': momenta[3],
            'repertoire': repertoire,
            'average-sentence-length': average_sentence_length,
            'average-sentence-repertoire': sentence_repertoire,}
