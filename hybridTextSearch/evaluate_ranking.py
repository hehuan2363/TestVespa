import requests
import ir_datasets
from ir_measures import calc_aggregate, nDCG, ScoredDoc
from enum import Enum
from typing import List

class RModel(Enum):
    SPARSE = 1
    DENSE = 2
    HYBRID = 3

def parse_vespa_response(response:dict, qid:str) -> List[ScoredDoc]:
    result = []
    hits = response['root'].get('children',[])
    for hit in hits:
      doc_id = hit['fields']['doc_id']
      relevance = hit['relevance']
      result.append(ScoredDoc(qid, doc_id, relevance))
    return result

def search(query:str, qid:str, ranking:str, 
           hits=10, language="en", mode=RModel.SPARSE) -> List[ScoredDoc]:
    yql = "select doc_id from doc where ({targetHits:100}userInput(@user-query))"
    if mode == RModel.DENSE:
        yql = "select doc_id from doc where ({targetHits:10}nearestNeighbor(embedding, e))"
    elif mode == RModel.HYBRID:
        yql = "select doc_id from doc where ({targetHits:100}userInput(@user-query)) OR ({targetHits:10}nearestNeighbor(embedding, e))"
    query_request = {
        'yql': yql,
        'user-query': query, 
        'ranking.profile': ranking,
        'hits' : hits, 
        'language': language
    }
    if mode == RModel.DENSE or mode == RModel.HYBRID:
        query_request['input.query(e)'] = "embed(@user-query)"

    response = requests.post("http://localhost:8080/search/", json=query_request)
    if response.ok:
        return parse_vespa_response(response.json(), qid)
    else:
      print("Search request failed with response " + str(response.json()))
      return []

def main():
  import argparse
  parser = argparse.ArgumentParser(description='Evaluate ranking models')
  parser.add_argument('--ranking', type=str, required=True, help='Vespa ranking profile')
  parser.add_argument('--mode', type=str, default="sparse", help='retrieval mode, valid values are sparse, dense, hybrid')
  args = parser.parse_args()
  mode = RModel.HYBRID
  if args.mode == "sparse":
    mode = RModel.SPARSE
  elif args.mode == "dense":
    mode = RModel.DENSE
     

  dataset = ir_datasets.load("beir/nfcorpus/test")
  results = []
  metrics = [nDCG@10]
  for query in dataset.queries_iter():
    qid = query.query_id
    query_text = query.text
    results.extend(search(query_text, qid, args.ranking, mode=mode))
    
  metrics = calc_aggregate(metrics, dataset.qrels, results)
  print("Ranking metric NDCG@10 for rank profile {}: {:.4f}".format(args.ranking, metrics[nDCG@10]))

if __name__ == "__main__":
    main()