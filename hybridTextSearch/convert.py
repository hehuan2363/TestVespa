import sys
import json

for line in sys.stdin:
  doc = json.loads(line)
  del doc['url']
  vespa_doc = {
    "put": "id:hybrid-search:doc::%s" % doc['doc_id'],
    "fields": {
      **doc
    }
  }
  print(json.dumps(vespa_doc))