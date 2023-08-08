#!/usr/bin/python3
"""getting the subs"""
from requests import get
from sys import argv

toplist = []
after = None


def counting_all(toplist, word_list):
    counting_dict = {word.lower(): 0 for word in word_list}
    for title in toplist:
        words = title.split(' ')
        for word in words:
            if counting_dict.get(word) is not None:
                counting_dict[word] += 1

    for key in sorted(counting_dict, key=counting_dict.get, reverse=True):
        if counting_dict.get(key):
            for thing in word_list:
                if key == thing.lower():
                    print("{}: {}".format(thing, counting_dict[key]))


def count_words(subreddit, word_list):
    global toplist
    global after
    """get subs"""
    head = {'User-Agent': 'alx:lin.api.adv:v1.0.0 (by /u/gena)'}
    if after:
        response = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=head).json().get('data')
    else:
        response = get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=head).json().get('data')
    toplist += [dic.get('data').get('title').lower()
                for dic in response.get('children')]
    after = response.get('after')
    if after:
        return count_words(subreddit, word_list)
    return counting_all(toplist, word_list)


if __name__ == "__main__":
    count_words(argv[1], argv[2].split(' '))
