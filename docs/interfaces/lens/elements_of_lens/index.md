---
search:
  exclude: true
---

# Elements of Lens

The Lens is composed of elements such as fields, entities, dimensions, and measures. The objective of these elements is to define the structure and logic of data models. They introduce opinionated simplicity in explaining the reasoning for business concepts.

## Entities

Entities are logical representations of an organization’s widely referred to and analyzed business concepts. They describe business objects such as customers, products, and users or business-specific activities such as web and app events, downloads, and purchases. 

Apart from the `name` and `description` of an entity, entity declaration within a Lens defines the following properties. 

| Properties | Description | Requirement |
| --- | --- | --- |
| `sql` | A query that runs against your data source to extract the entity table | Mandatory |
| `field` | Unique identifiers for an entity | Optional |
| `dimension` | Categorical or time-based data that helps in adding context to the measures | Optional |
| `measures` | Aggregated columns are calculated using SQL expressions. Measures are the foundation for defining metrics. | Optional |
| `relationship` | Defines the relationship of entities with other entities. An entity can be joined to other entities and have one-to-one, one-to-many, or many-to-one relationships. | Optional |
| `extend` | This allows you to extend an existing entity to use all declared elements of the entity. | Optional |

To learn more about entities, refer to
[Entity](/interfaces/lens/elements_of_lens/entity/)

## Field

> Field, Dimensions, Measures, and Relationships are integral to the schema of all entities you define.
> 

Fields are columns that uniquely identify an entity. The fields contain direct mapping to the underlying data source columns. Mention all the columns in the field that directly map to your underlying table. 

Supported properties by fields

| Properties | Description | Requirement |
| --- | --- | --- |
| `name` | Name of the field | Optional |
| `type` | Type of the field | Mandatory |
| `description` | Description of the field | Optional |
| `column` | Maps your field to the column in the physical table | Optional |
| `primary` | Use this property to explicitly state whether the field needs to be considered a primary key. | Optional |

To know more about fields, refer to
[Fields](/interfaces/lens/elements_of_lens/fields/).

## Dimensions

The Lens dimensions are columns containing qualitative data; they are groupable and can be used to query measures to varying levels of granularity. 

Dimensions can be - 

- An attribute that can directly reference a column of the underlying table, or
- A derived value calculated using a SQL expression

For instance, dimensions for a *Customer entity* might include first name, last name, email, phone, location, and age. 

Supported properties for dimensions

| Properties | Description | Mandatory/Optional |
| --- | --- | --- |
| `name` | Name of the dimension. | Optional |
| `description` | Description of the dimension. | Optional |
| `type` | Type of the dimension.| Mandatory |
| `sql_snippet` | A query to extract dimensions from the physical table. It can either be a one-to-one mapping to a column of your physical table, or you can define a custom query. | Optional |
| `sub_query` | Allows referencing measures from other entities. It’s of boolean type. | Optional |
| `hidden` | It will hide the dimension from the user interface if set to true. | Optional |

To know more about dimensions, refer to
[Dimensions](/interfaces/lens/elements_of_lens/dimensions/).

## Measures

Measures are aggregated numerical values derived from quantitative columns. You can also define complex expressions in the SQL snippet besides using the supported aggregation types. A measure can be referenced within a measure to achieve the desired aggregation.

For instance, Orders Entity might include measures such as quantities sold (count), total order amount(sum), and average order amount (avg).

Supported properties for measures

| Properties | Description | Requirement |
| --- | --- | --- |
| `name` | Name of the measure | Optional |
| `description` | Description of the measure | Optional |
| `type` | Type of the measure.  | Yes |
| `sql_snippet` | Based on the measure(aggregation) type, you can specify the aggregated column or define a custom query. | Optional |
| `rolling_window` | You can aggregate column values within a defined window, just like the SQL window function. | Optional |
| `hidden` | It will hide the dimension from the user interface if set to true. | Optional |

To know more about measures, refer to
[Measures](/interfaces/lens/elements_of_lens/measures/).

## Relationships

It defines the relationship between two entities; it can be - one-to-one, one-to-many, or many-to-one. A defined relationship simplifies querying dimensions and measures from multiple entities. Entities would be joined based on the defined keys and relationships. Once the relationship and fields are declared in the model, Lens will automatically generate join logic to render columns correctly. 

Supported properties for relationships

| Properties | Sub-Property | Description | Requirement |
| --- | --- | --- | --- |
| `field` |  | The field on which the join will be defined. Its ‘primary’ property is set to true (Primary Key) | Mandatory |
| `target` |  |  | Mandatory |
|  | `name` | The entity you need to join. |  |
|  | `field` | Join will be performed using this field of the entity |  |
| `description` |  |  | Optional |
| `type` |  | Type of the relationship - 1:1,1:N,N:1 | Mandatory |
| `sql_snippet` |  | If you have more than one clause in your join statement, you can add a query for it. | Optional |

To learn more about relationships, refer to
[Relationships](/interfaces/lens/elements_of_lens/relationships/).