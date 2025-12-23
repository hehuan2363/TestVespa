# TestVespa

A collection of examples and experiments exploring [Vespa.ai](https://vespa.ai) - a powerful open-source search engine and vector database.

## Why Vespa.ai is Underrated?

Vespa.ai offers several compelling features that make it a great choice for search and retrieval applications:

- **Hybrid search support** - Combines keyword and semantic search capabilities
- **Open-source** - Self-hosting and cloud hosting options available
- **Multi-vector support** - Handle multiple vector representations efficiently
- **High performance** - Optimized for production workloads
- **Re-ranking** - Built-in support for advanced ranking models

## Project Structure

This repository contains various examples and tutorials:

- `hybridTextSearch/` - Hybrid search implementation combining keyword and semantic search
- `text-search/` - Text search examples
- `imdbquickstart/` - Quickstart tutorial using IMDB data
- `myapp/` - Custom application examples
- `TextSearch.ipynb` - Jupyter notebook for text search experiments
- `tuturial.ipynb` - Tutorial notebook
- `IMDB_top_100.json` - Sample IMDB dataset

## Setup

### Prerequisites

- Python 3.x
- [UV](https://github.com/astral-sh/uv) package manager

### Installation

1. Create and activate a virtual environment using UV:

```bash
uv venv vespa
source vespa/bin/activate  # On Windows: vespa\Scripts\activate
```

2. Install required packages:

```bash
pip install pyvespa
pip install vespacli
```

## Resources

- **Vespa CLI Documentation**: https://docs.vespa.ai/en/reference/vespa-cli/vespa_clone.html
- **Hybrid Search Tutorial**: https://docs.vespa.ai/en/tutorials/hybrid-search.html
- **Vespa.ai Official Docs**: https://docs.vespa.ai/

## Notes

Last updated: October 2, 2025
