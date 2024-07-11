## Defining Relationships

- OR <br>
- AND

=== "OR" 

    The syntax given below allows access for either `tag1` OR `tag2`.<br>
                
    ```yaml
    tags: 
      -- tag1
      -- tag2
    ```
    The outermost list contains two inner lists, each representing a tag. In this case, it means that both "tag1" and "tag2" are considered separately which is how you define the OR relationships between tags.

    **Example of OR Relationship** <br>

    === "Example 1"
    
        In this example policy, an object MUST have the resource path of `/metis/api/v2/workspaces/public` **OR** `/metis/api/v2/workspaces/sandbox` to qualify for this policy to apply.
                
        ```yaml hl_lines="16-17"
        name: object-example1
        version: v1
        type: policy
        layer: user
        description: example policy
        policy:
          access:
            subjects:
              tags:
                - - roles:id:developer
                  - roles:id:testuser
            predicates:
              - read
            objects:
              paths:
                - /metis/api/v2/workspaces/public
                - /metis/api/v2/workspaces/sandbox
            allow: true
        ```

    === "Example 2" 

        In this example policy, an object MUST have the `PII.Email` **OR** `PII.Sensitive` tags to qualify for this policy to apply.
                
        ```yaml hl_lines="16-17"
        name: object-example2
        version: v1
        type: policy
        layer: user
        description: example policy
        policy:
          access:
            subjects:
              tags:
                - - roles:id:developer
                  - roles:id:testuser
            predicates:
              - read
            objects:
              tags:
                - - PII.Email
                - - PII.Sensitive
            allow: true
        ```
            
=== "AND"

    - Defining Complex Relationships Using AND, OR
        
        This section represents an expression where either "tag1" or both "tag2" and "tag3" should be true. The outermost list contains three elements. The first and second elements represent "tag1" and "tag2" separately. The third element, "tag3," is indented to indicate that it is a child of "tag2," implying that both "tag2" and "tag3" should be true.
        
    ```yaml
    # tag1 OR (tag2 AND tag3)
    tags: 
    - - tag1
    - - tag2
      - tag3
    ```
    
    - Example of Complex AND, OR Relationship
        
        For example, to qualify for the following example policy, a subject must have either both tags (`roles:id:pii-reader` AND `roles:id:testuser`) OR the tag `roles:id:marketing-manager`.
        
    ```yaml
    name: subject-example2
    version: v1
    type: policy
    layer: user
    description: example policy
    policy:
      access:
        subjects:
          tags:
            - - roles:id:pii-reader
              - roles:id:testuser
            - - roles:id:marketing-manager
        predicates:
          - read
        objects:
          tags:
            - - PII.Sensitive
              - dataos:type:column
        allow: true
    ```
    
2.  **Evaluating List Attributes using Wildcard**

The symbol`:` is a delimiter in the tags field and paths field, and predicates field; additional syntax includes:
         
| Wildcard | Wildcard Name | Example | Description |
| --- | --- | --- | --- |
| ? | Single Character Wildcard - Matches exactly one occurrence of any character | ?at | Matches cat and bat but not at |
| * | Glob/Asterisk - Matches any number of characters, including none, within the same level of a hierarchy. Can be used to evaluate all items in a list; if any item in the list matches the condition, then the condition passes. | foo:*:bar | Matches foo:baz:bar and foo:zab:bar but not foo:bar nor foo:baz:baz:bar |
| ** | Super Glob/Double Asterisk - Matches any number of characters across multiple levels of a hierarchy. Can be used to evaluate all items in a list; if any item in the list matches the condition, then the condition passes. |  foo:**:bar | Matches foo:baz:baz:bar, foo:baz:bar, and foo:bar, but not foobar or foo:baz |
| [] | Character List - Matches exactly one character that is contained within the brackets.  | [cb]at | matches cat and bat but not mat nor at
(It’s worthing noting that the order of characters within the brackets doesn’t matter, [cb]at and [bc]at function the same way) |
| [!] | Negated Character List - Matches any single character that is not listed between the brackets. | [!cb]at | matches tat and mat but not cat nor bat |
| [-] | Ranged Character List - Match a specific character within a certain range. | [a-c]at | cat and bat but not mat nor at |
| [!-] | Negated Ranged Character List | [!a-c]at  | matches mat and tat but not cat nor bat |
| {[]} | Alternatives List | {cat,bat,[mt]at}  | matches cat, bat, mat, tat and nothing else |
| \ | Backslash (escape) | foo\\bar
foo\bar 
foo\*bar | matches foo\bar and nothing else
matches foobar and nothing else
matches foo*bar and nothing else |

**Example Usage:**

```yaml
# single tag
tags:
	-- "roles:id:testuser"
# group of tags
tags:
	-- "roles:id:test1"
	-- "roles:id:test2"
```
