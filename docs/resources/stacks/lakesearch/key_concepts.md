# Key concepts of Lakesearch

This section involves key concepts that helps to understand LakeSearch better.

## full-text search

Full-text search, also known as lexical search, is a technique for fast, efficient searching through text fields in documents. Documents and search queries are transformed to enable returning relevant results instead of simply exact term matches. Fields of type text are analyzed and indexed for full-text search.

## Index

An index is a collection of documents uniquely identified by a name or an alias. This unique name is important because it’s used to target the index in search queries and other operations.

## Documents

LakeSearch serializes and stores data in the form of JSON documents. A document is a set of fields, which are key-value pairs that contain your data. Each document has a unique ID, which you can create or have LakeSearch auto-generate.

A simple LakeSearch document might look like this:

```json
{
    "name": "newcustomer",
    "description": "index for customers",
    "tags": [
        "customers"
    ],
    "columns": [
        {
            "name": "id",
            "type": "bigint",
            "description": "mapped to customer_id",
            "tags": [
                "identifier"
            ]
        },
        {
            "name": "education",
            "type": "text"
        },
        {
            "name": "country",
            "type": "text"
        },
        {
            "name": "@timestamp",
            "type": "timestamp"
        },
        {
            "name": "customer_id",
            "type": "bigint"
        },
        {
            "name": "birth_year",
            "type": "bigint"
        },
        {
            "name": "created_at",
            "type": "timestamp"
        }
    ]
}
```

## Mappings and data types

Each index has a mapping or schema for how the fields in your documents are indexed. A mapping defines the data type for each field, how the field should be indexed, and how it should be stored.

## Indexer

The Indexer is responsible for reading data from the source table and loading it into an object storage location, such as an S3 bucket. This process involves an initial data load followed by ongoing synchronization based on a user-defined schedule. The Indexer monitors changes in the source table and ensures that these changes are replicated in the object storage. Each Indexer is dedicated to a single source table and can be vertically scaled to improve performance as needed.


## Search API

A search consists of one or more queries that are combined and sent to LakeSearch. Documents that match a search’s queries are returned in the hits, or search results, of the response. A search may also contain additional information used to better process its queries. For example, a search may be limited to a specific index or only return a specific number of results. You can use the search API to search and aggregate data stored in LakeSearch indices. 






