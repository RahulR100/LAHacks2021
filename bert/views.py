from django.shortcuts import render
import article_query
import article_to_point
import json
# Create your views here.

def view_raw_results(request, *args, **kwargs):
	query = "deep AND learning"
	articles_per_page = 50 # 10 to 100
	pages = 2
	
	params = {
   		'apiKey':'neHjg153Yp6UPxMulymbAs7f4QdzrtIJ',
		'page':1,
   		'pageSize':articles_per_page,
   		'metadata':'true',
   		'fulltext':'false',
   		'citations':'false',
   		'similar':'false',
   		'duplicate':'false',
   		'urls':'true',
   		'faithfulMetadata':'false',
	}
	results = article_query.get_queries(query, pages, params)
	a2p = article_to_point.Articles2Points()
	articles = article_to_point.Data2Articles(results)

	context = {
		"points": a2p(articles)
	}

	nodes = list(map(lambda a: a.dict, articles))

	links = []

	graph = {"nodes":nodes, "links":links}
	graph_json = json.dumps(graph) #### data for the 3d-visual

	""" with open("graph.json", 'w+') as file:
		file.write(graph_json) """
	
	return render(request, "raw_results.html", context)

