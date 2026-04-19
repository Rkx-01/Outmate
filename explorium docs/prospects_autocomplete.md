> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Autocomplete prospects

> Autocomplete prospects fields values by field name.

## Description

The **Prospects Autocomplete** endpoint provides **real-time suggestions** for prospects-related fields, helping users quickly find relevant categories, locations, and industries based on partial text input. This is useful for creating dynamic search fields and enhancing user experience in filtering interfaces.

<AccordionGroup>
  <Accordion title="How It Works">
    * **Input:** Specify a field type (`country`, `region_country_code`, etc.) and provide a partial query string.
    * **Processing:** The system searches through indexed datasets to return the most relevant suggestions.
    * **Output:** A structured response containing suggested values for the given input.
  </Accordion>

  <Accordion title="Query Parameters">
    | Parameter | Type   | Description                                                                        |
    | --------- | ------ | ---------------------------------------------------------------------------------- |
    | `field`   | String | The field for which autocomplete is requested (e.g., `country`, `job_department`). |
    | `query`   | String | Partial text input to generate suggestions.                                        |
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl -X GET \
      "https://api.explorium.ai/v1//prospects/autocomplete?field=country&query=unit" \
      -H "API_KEY: your_api_key_here"
    ```
  </Accordion>

  <Accordion title="Supported Autocomplete Fields & Example Inputs" icon="thumbtack" iconType="solid">
    | **Filter**            | **Description**                                                          | **Example Input**                                |
    | --------------------- | ------------------------------------------------------------------------ | ------------------------------------------------ |
    | `country`             | Autocomplete for country names                                           | `"Uni"` → United States, United Kingdom          |
    | `country_code`        | Autocomplete for country codes (ISO 2-letter)                            | `"US"` → United States                           |
    | `region_country_code` | Autocomplete for region-based country codes                              | `"EU"` → European Union countries                |
    | `city_region_country` | Free-text location input that includes city, region, or country          | `"berlin, germany"` or `"california, us"`        |
    | `google_category`     | Google's business category classification                                | `"E-com"` → E-commerce                           |
    | `naics_category`      | Industry classification based on NAICS codes                             | `"541512"` → Computer Systems Design Services    |
    | `linkedin_category`   | Industry classification from LinkedIn data                               | `"Retail"` → Retail Industry                     |
    | `company_name`        | Free-text match or partial match on company name                         | `"micros"` → Microsoft, MicroStrategy            |
    | `company_size`        | Autocomplete for company sizes (by number of employees)                  | `"500"` → Companies with \~500 employees         |
    | `company_revenue`     | Revenue-based classification (**K, M, B, T** for thousands to trillions) | `"100M"` → \$100 Million+                        |
    | `job_title`           | Autocomplete for job titles                                              | `"Soft"` → Software Engineer, Software Developer |
    | `job_department`      | Autocomplete for job departments                                         | `"Eng"` → Engineering, Product Engineering       |
    | `job_level`           | Job seniority levels                                                     | `"Senior"` → Senior Manager, Senior Engineer     |
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON expandable theme={null}
    [
      {
        "query": "unit",
        "label": "United States",
        "value": "us"
      },
      {
        "query": "unit",
        "label": "United Kingdom",
        "value": "gb"
      },
      {
        "query": "unit",
        "label": "United Arab Emirates",
        "value": "ae"
      },
      {
        "query": "unit",
        "label": "Tanzania, United Republic Of",
        "value": "tz"
      },
      {
        "query": "unit",
        "label": "United States Minor Outlying Islands",
        "value": "um"
      }
    ]
    ```
  </Accordion>

  <Accordion title="Best Practices">
    * **Use precise queries** to get the most relevant autocomplete results.
    * **Optimize search fields** by implementing real-time feedback mechanisms.
    * **Restrict field selection** to avoid unnecessary queries and improve API efficiency.
    * **Combine with filtering APIs** to refine user selections dynamically.
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> **Explore the sections above for additional query examples and integration guidelines.**

## Body Params - Try Me Example

```
field: country
query: unit
```


## OpenAPI

````yaml get /v1/prospects/autocomplete
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/autocomplete:
    get:
      tags:
        - Prospects
      summary: Autocomplete Prospects
      description: Autocomplete prospects fields values by field name.
      operationId: prospects_autocomplete
      parameters:
        - required: true
          schema:
            $ref: '#/components/schemas/AutocompleteType'
          name: field
          in: query
        - required: false
          schema:
            type: string
            title: Query
          name: query
          in: query
        - required: false
          schema:
            type: boolean
            title: Semantic Search
          name: semantic_search
          in: query
        - required: false
          schema:
            type: string
            title: Tenant
            auto_error: false
            name: tenant
          name: tenant
          in: header
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/AutoCompleteItem'
                type: array
                title: Response Prospects Autocomplete
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
        - APIKeyHeader: []
components:
  schemas:
    AutocompleteType:
      enum:
        - country
        - country_code
        - region_country_code
        - google_category
        - naics_category
        - linkedin_category
        - company_tech_stack_tech
        - company_tech_stack_categories
        - job_title
        - company_size
        - company_revenue
        - number_of_locations
        - company_age
        - job_department
        - job_level
        - city_region_country
        - company_name
        - business_intent_topics
        - city_region
      title: AutocompleteType
      description: Enum for autocomplete types.
    AutoCompleteItem:
      properties:
        query:
          type: string
          title: Query
        label:
          type: string
          title: Label
        value:
          type: string
          title: Value
      type: object
      required:
        - query
        - label
        - value
      title: AutoCompleteItem
      example:
        query: united
        label: United States
        value: us
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````