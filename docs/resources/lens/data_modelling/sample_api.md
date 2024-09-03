---
search:
  exclude: true
---

| `api_scopes` | A list of API scopes that the user group members are allowed to access. Each scope represents specific endpoints or functionality. The following `api_scopes` are currently supported:

- `meta`: Provides access to metadata-related endpoints. This scope allows users to view metadata, which typically includes information about sources, authors, timezones, security context, user groups, etc. Providing access to the `meta` API scope grants a user access to the Model and Explore Tab of the Lens Studio Interface. But to fetch insights using the Explore interface, a user also requires the `data` API scope.
- `data`: Allows access to data endpoints. This scope enables users to retrieve, and analyze data.
- `graphql`: Grants access to GraphQL endpoints. GraphQL is a query language for APIs that allows clients to request only the data they need. This scope enables users to perform GraphQL queries and mutations. Granting access to the `graphql` API scope provides access to the GraphQL tab of the Lens studio interface, but to run queries over data you will also require the `data` API scope.
- `jobs`: Provides access to job-related endpoints. 
- `source`: Grants access to source-related endpoints.  | optional (by default all `api_scopes` are included if not explicitly specified) | Follow the principle of least privilege and grant users the minimum level of access required to perform their job functions |