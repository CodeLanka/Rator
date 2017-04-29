import json

semantic_mappings_all = ['', 'user.profile.name', 'id', 'phone', 'company', 'user.linkedin.url', 'twitter'
                     'tshirt', 'food', 'isgithub', 'user.github.url', 'isstack', 'user.stackoverflow.url',
                     'job', 'reason', 'location']
semantic_mappings = ['',
                     'user.profile.name', '', '', '', 'user.linkedin.url',
                     '', '', '', '', 'user.github.url',
                     '', '', '', 'user.stackoverflow.url', '',
                     '', '', '']
outfile = open('data/answers.json', 'w+', encoding='utf-8')
with open('data/responses.json') as data_file:
    items = json.load(data_file)
    answer_array = []

    for entry in items:
        record = {}
        record['user'] = {}
        record['answers'] = []
        record['user']['email'] = entry['email']
        record['user']['score'] = 0
        response = json.loads(entry['response'])
        for qna in response:
            if semantic_mappings[int(qna['name'])] != '':
                semantic_entry = {}
                semantic_entry['id'] = 1
                semantic_entry['value'] = qna['value']
                semantic_entry['semantic'] = semantic_mappings[int(qna['name'])]
                record['answers'].append(semantic_entry)

        answer_array.append(record)
        # github_adapter = GithubAdaptor()
        # github_adapter.rate(entry[])

    print(answer_array)
    outfile.write(json.dumps(answer_array))
    outfile.close()
