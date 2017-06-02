from truthmeas.request import make_request

if __name__ == "__main__":
    data = {"pokemon": "bulbasaur"}
    json = make_request(data)
    print(json)