import pickle
from datetime import datetime
import os
import networkx

logged_person = ''
friends_list = []
status_data = {}
current_datetime = datetime.now()
graph = networkx.DiGraph()

'''
Funkcija koja prolazi kroz neki od csv fajlova i pregleda da li je ulogovani korisnik taj koji je
vrsio interakciju sa korisnikom objave
Ukoliko jeste, toj objavi se dodaju poeni u zavisnosti od jacine interakcije
Kao parametri prosledjuju se naziv csv fajla i indeks autora objave u nizu (redu)
'''
def give_points_for_my_likes(path: str, position: int):

    file_path = os.path.join('dataset', path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number, row in enumerate(lines[1:], start=2):

            items = row.split(",")
            if items[position] == logged_person:
                date_obj = datetime.strptime(items[position + 1].strip(), "%Y-%m-%d %H:%M:%S")
                # datum reagovanja nalazi se odmah na sledecoj poziciji u odnosu na poziciju autora
                days_difference = current_datetime - date_obj
                days_difference = days_difference.total_seconds() / 3600 / 24
                extra_points = 0
                status_id = items[0]

                if days_difference < 30:

                    if 'reactions' in path:
                        if items[1] == 'likes':
                            extra_points = 1000
                        elif items[1] == 'loves':
                            extra_points = 1300
                        elif items[1] == 'hahas':
                            extra_points = 1200
                        elif items[1] == 'wows' or items[1] == 'special':
                            extra_points = 1100
                        elif items[1] == 'angrys':
                            extra_points = 800
                        elif items[1] == 'sads':
                            extra_points = 900
                    elif 'comments' in path:
                        extra_points = 2000
                        status_id = items[1]
                    elif 'shares' in path:
                        extra_points = 3000

                    extra_points = extra_points * (30 - days_difference) / 30
                    status_data[status_id]['score'] += extra_points

def login():

    global logged_person, friends_list, status_data, graph
    user_name = input('Write your user name to log in: ')

    file_path = os.path.join('dataset', 'friends.csv')
    with open(file_path, 'r') as file:

        for row in file:
            items=row.split(",")
            current_name = items[0]

            if user_name == current_name:
                print('Dear ' + user_name + ', you logged in successfully.')
                logged_person = user_name
                for i in range(2, int(items[1]) + 2):
                    friends_list.append(items[i].strip())
                break

    # evaluating users and their posts
    file_path = os.path.join('dataset', 'original_statuses.csv')
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line_number, row in enumerate(lines[1:], start=2):
            items = row.split(",")

            date_obj = datetime.strptime(items[4], "%Y-%m-%d %H:%M:%S")
            days_difference = current_datetime - date_obj
            days_difference = days_difference.total_seconds() / 3600 / 24
            score = 0

            if days_difference < 10:
                # 7 - comm, 8 - shares, 9 - likes, 10 - loves, 11 - wows, 12 - hahas, 13 - sads, 14 - angrys, 15 - special
                score = 1 * int(items[7]) + 2 * int(items[8]) + 0.5 * int(items[9]) + 0.8 * int(items[10]) + 0.7 * (
                        int(items[11]) + int(items[15])) \
                        + 0.6 * int(items[12]) + 0.4 * int(items[13]) + 0.3 * int(items[14])
                score = (10 - days_difference) * 0.1 * score

            if items[5] in friends_list:
                score += 4000

            date_str = items[4].split(' ')[0]
            status_data[items[0]] = {'message': items[1], 'author': items[5], 'reactions': items[6],
                                     'comments': items[7],
                                     'shares': items[8],
                                     'date': date_str, 'score': score}

        give_points_for_my_likes('original_shares.csv', 1)
        give_points_for_my_likes('original_comments.csv', 4)
        give_points_for_my_likes('original_reactions.csv', 2)

        status_data = sorted(status_data.items(), key=lambda x: x[1]['score'], reverse=True)

        # creating graph users (nodes) and their affinities (oriented edges)
        for _, post in status_data:

            if post['score'] < 4000:
                break
            else:
                graph.add_edges_from([(logged_person, post['author'])])

        with open('graph.pickle', 'wb') as f:
            pickle.dump(graph, f)

        with open('graph.pickle', 'rb') as f:
            graph = pickle.load(f)

    # return values for main
    if not logged_person:
        print("There isn't this user name.")

    return logged_person

def view_menu():
    print('\n****** Welcome to the menu *****')
    print('1. View posts')
    print('2. Search')
    print('X. Log out')

def view_posts():
    prefered_posts_dict = {}

    for key, post in status_data:

        for edge in graph.edges():
            if edge[1] == post['author']:
                prefered_posts_dict[key] = {'message': post['message'], 'author': post['author'], 'reactions': post['reactions'], 'comments': post['comments'],
                                            'shares': post['shares'], 'date': post['date']}
                break

    max_post_number = 10
    current_post_number = 0
    for post in prefered_posts_dict:
        post = prefered_posts_dict[post]
        print('\n' + post['author'] + ', ' + post['date'])
        print(post['message'])
        print('Reactions: ' + post['reactions'] + ', Comments: ' + post['comments'] + ', Shares: ' + post['shares'])
        current_post_number += 1
        if current_post_number >= max_post_number:
            break


def search():
    input_text = input('Please enter the text: ')

    if '"' in input_text:
        input_text = input_text[1:-1]
        for _, post in status_data:
            appearance_num = post['message'].count(input_text)
            appearance_num += post['author'].count(input_text)
            post['appearance_num'] = appearance_num

    elif input_text[-1] == '*':
        input_text = input_text[0:-1]
        for _, post in status_data:
            appearance_num = post['message'].lower().count(input_text.lower())
            appearance_num += post['author'].lower().count(input_text.lower())
            post['appearance_num'] = appearance_num

    else:
        input_text = ' ' + input_text + ' '
        for _, post in status_data:
            appearance_num = post['message'].lower().count(input_text.lower())
            appearance_num += post['author'].lower().count(input_text.lower())
            post['appearance_num'] = appearance_num

        words = input_text.strip().split(' ')
        if len(words) > 1:

            for _, post in status_data:
                for word in words:
                    post['appearance_num'] += post['message'].lower().count(word.lower())
                    post['appearance_num'] += post['author'].lower().count(word.lower())

    sorted_dict = sorted(status_data, key=lambda x: (-x[1]['appearance_num'], -x[1]['score']))

    max_post_number = 10
    current_post_number = 0

    for _, post in sorted_dict:
        if post['appearance_num'] != 0:
            print('\n' + post['author'] + ', ' + post['date'])
            print(post['message'])
            # print(post['appearance_num'], post['score'])
            current_post_number += 1
            if current_post_number >= max_post_number:
                break

    if current_post_number == 0:
        print("There aren't any posts.")

