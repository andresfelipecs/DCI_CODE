dictionary = {
    "next": "a link",
    "results": [
        {"name": "A", "items": ["Shaban"]},
        {"name": "B", "items": ["Peer"]},
        {"name": "C", "items": ["Jacques"]},
        {"name": "D", "items": ["Muhannad"]},
    ]
}

for r in dictionary['results']:
    print(r['items'][0])