
graph = dict()
seen = []
toSearch = []

def crawlGraph(url, levels):
	if url in seen:
		return
	seen.append(url)
	
	process(url, levels)
	urls = parseUrls(url)
	toSearch = filter(urls, seen)

	if (levels != 0):
		for i in urls:
			crawlGraph(i, levels-1)


def process(url, levels):
	print(f"processing {url}")
	
def parseUrls(url):
	if url not in graph.keys():
		return []
	return sorted(list(graph[url]))

def filter(source, destination):
	result = []
	for i in source:
		if i not in destination:
			result.append(i)
	return result

def loadGraph(urlRelations):
	for relation in urlRelations:
		(k,v) = relation
		if k in graph.keys():
			siblings = graph[k]
			siblings.add(v)
			graph[k] = siblings
		else:
			graph[k] = {v}


if __name__ == "__main__":
	urls = [
		("url","a"),
		("url","b"),
		("url","c"),
		("a","b"),
		("b","a"),
		("b","c"),
		("c","a"),
		("c","d"),
		("d","e"),
		("e","f")
	]

	loadGraph(urls)
	print(graph)

	crawlGraph("url",3)
	print(seen)
