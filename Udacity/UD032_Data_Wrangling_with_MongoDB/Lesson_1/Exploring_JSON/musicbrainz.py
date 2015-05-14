# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    c = 0
    for each in results["artists"]:
        if each["name"] == "First Aid Kit":
            c += 1
    print "How many bands named 'First Aid Kit'? ", c

    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    print "begin-area name for 'Queen': ", results["artists"][0]["begin-area"]["name"]

    results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
    for each in results["artists"][0]["aliases"]:
        if each["locale"] == "es":
            print "Spanish alias for 'The Beatles': ", each["name"]
            break

    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    print "'Nirvana' disambiguation: ", results["artists"][0]["disambiguation"]

    results = query_by_name(ARTIST_URL, query_type["simple"], "One direction")
    print "When was 'One Direction' formed? ", results["artists"][0]["life-span"]["begin"]

if __name__ == '__main__':
    main()
