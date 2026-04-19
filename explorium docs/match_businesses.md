> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Match Businesses

> Match a list of businesses attributes to ids.
Returns a list of the same length and order as the input list, with the matched ids.

## Description

The **Match Businesses** endpoint is the **first step** in the data enrichment process. It enables users to accurately identify businesses based on their **name or domain**, returning a **unique Business ID** that acts as the **foundation for all subsequent API interactions**.

This endpoint is designed to provide **high-accuracy business matching** by leveraging **multiple data sources, validation layers, and proprietary algorithms** to ensure precise identification.

Once a business is successfully matched, its **Business ID** becomes the **primary key** for retrieving enriched company data, accessing financial insights, monitoring real-time business events, and performing additional analytics through other Explorium APIs.

<AccordionGroup>
  <Accordion title="Coverage">
    | Attribute             | Coverage Details                                               |
    | :-------------------- | :------------------------------------------------------------- |
    | **Total Businesses**  | 80M+ businesses across 150+ countries                          |
    | **Matching Accuracy** | Advanced entity resolution for precise business identification |
    | **Real-Time Updates** | Ensures the latest business records are used for matching      |
  </Accordion>

  <Accordion title="How It Works">
    ### How It Works

    **Input**: A list of business identifiers, which can include `name`, `website (domain)`, and `linkedin_company_url`.\
    **Processing**: The system cross-references multiple internal datasets to determine the best possible match.\
    **Output**: A structured response containing the matched Business IDs, preserving the exact order of the input list.

    ***

    ### Matching Strategy

    When using the **Business Match** endpoint, the system applies a multi-step resolution strategy based on the fields you provide — primarily `name` and `website`.

    #### 1. Primary Matching — Smart Fuzzy Logic (Name + Website)

    We begin by attempting to match the business using both the company name and website domain.\
    The company name is evaluated using a smart fuzzy matching algorithm designed to handle:

    * Common variations and abbreviations
    * Typos and noisy CRM inputs
    * Token normalization, semantic similarity, and industry-aware string processing

    The website (domain) serves as a strong anchoring signal to disambiguate between similarly named companies and to boost confidence.\
    This phase ensures high-precision matching while remaining robust to imperfect input data.

    #### 2. Fallback Matching — Website Only

    If the system fails to find a confident match using both name and domain, it automatically falls back to matching by website alone.\
    Because domains are typically unique and consistent across organizations, this fallback ensures matches can still be returned when the company name is incomplete, inconsistent, or incorrect.

    ***

    ### Important Notes

    * Fallback matching from **name + website → website only** occurs only when both fields are provided.
    * If only the website is supplied, it will be used directly for matching.
    * If only the name is provided, matching relies solely on fuzzy name resolution without domain anchoring.
    * This logic is aligned with the AgentSource model, which emphasizes main site-level resolution (not individual branches).

    ***

    ### Example Scenarios

    | Input                                               | Matching Outcome                             |
    | :-------------------------------------------------- | :------------------------------------------- |
    | `Name: Starbucks EMEA`, `Website: starbucks.com`    | Match using name + website (fuzzy supported) |
    | `Name: abcxyz`, `Website: starbucks.com`            | Fallback — match using website only          |
    | `Name: Starbucks`, `Website: fakeurl.xyz`           | No match — invalid domain                    |
    | `Name: (empty)`, `Website: starbucks.com`           | Match using website only                     |
    | `Name: Starbuks Intl Ltd`, `Website: starbucks.com` | Match using fuzzy logic + website            |

    ### Recommendation

    To get the best possible results:

    * Always include both `name` and `website` when calling the Business Match endpoint.
    * This enables the system to apply smart fuzzy matching **and** fallback recovery for unmatched names — maximizing accuracy, coverage, and confidence.
  </Accordion>

  <Accordion title="Schema Explanation">
    | **Field**             | **Type** | **Description**                                                            |
    | :-------------------- | :------- | :------------------------------------------------------------------------- |
    | `businesses_to_match` | Array    | List of business identifiers to match (can include name, domain, LinkedIn) |
    | `name`                | String   | Business name provided for matching                                        |
    | `domain`              | String   | Business domain provided for matching                                      |
    | `linkedin_url`        | String   | LinkedIn company profile URL (optional, improves matching accuracy)        |
    | `business_id`         | String   | Unique identifier for the matched business (null if not found)             |
  </Accordion>

  <Accordion title="Best Practices">
    * **Always store the Business ID** – It serves as the key for all future enrichment and analytics.
    * **Use multiple identifiers** (e.g., name + domain, or LinkedIn URL) for **higher match accuracy**.
    * **Batch requests efficiently** to optimize API performance.
    * **Handle null values gracefully** to account for unmatched businesses.
    * **Update and validate input data regularly** to ensure the most accurate matches.
  </Accordion>

  <Accordion title="Body Params – Example with LinkedIn URL">
    ```json theme={null}
    {
      "request_context": {
        "seller_id": "sample_seller"
      },
      "businesses_to_match": [
        {
          "name": "microsoft",
          "linkedin_url": "https://linkedin.com/company/microsoft"
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> For detailed endpoint explanations, request examples, and integration tips, explore the documentation sections above.

## Body Params - Try Me Example

```
name: Apple
domain: apple.com

name: Microsoft
domain: microsoft.com
```


## OpenAPI

````yaml post /v1/businesses/match
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/businesses/match:
    post:
      tags:
        - Businesses
      summary: Match Businesses
      description: >-
        Match a list of businesses attributes to ids.

        Returns a list of the same length and order as the input list, with the
        matched ids.
      operationId: match_businesses
      parameters:
        - required: false
          schema:
            type: string
            title: Tenant
            auto_error: false
            name: tenant
          name: tenant
          in: header
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BusinessesMatchRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BusinessesMatchResponse'
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
    BusinessesMatchRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        businesses_to_match:
          items:
            $ref: '#/components/schemas/BusinessMatchInput'
          type: array
          maxItems: 50
          minItems: 1
          title: Businesses To Match
      additionalProperties: false
      type: object
      required:
        - businesses_to_match
      title: BusinessesMatchRequest
    BusinessesMatchResponse:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        total_results:
          type: integer
          exclusiveMinimum: 0
          title: Total Results
          description: The total_results number matched businesses
        total_matches:
          type: integer
          minimum: 0
          title: Total Matches
          description: The total number of matches.
        matched_businesses:
          items:
            anyOf:
              - $ref: '#/components/schemas/BusinessMatchOutputWithErrors'
              - $ref: '#/components/schemas/BusinessMatchOutput'
          type: array
          title: Matched Businesses
          description: >-
            A list of all businesses. If they not matched `business_id` will
            None.
      type: object
      required:
        - response_context
        - total_results
        - total_matches
      title: BusinessesMatchResponse
      description: 'This is base response model for all responses in partner service. '
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    BusinessMatchInput:
      properties:
        name:
          type: string
          maxLength: 256
          title: Name
        domain:
          type: string
          title: Domain
        url:
          type: string
          title: Url
        linkedin_url:
          type: string
          title: Linkedin Url
      type: object
      title: BusinessMatchInput
    ResponseContext:
      properties:
        correlation_id:
          type: string
          title: Correlation Id
        request_status:
          $ref: '#/components/schemas/RequestStatus'
        time_took_in_seconds:
          type: number
          title: Time Took In Seconds
      type: object
      required:
        - correlation_id
        - request_status
        - time_took_in_seconds
      title: ResponseContext
    BusinessMatchOutputWithErrors:
      properties:
        input:
          $ref: '#/components/schemas/BusinessMatchInput'
        business_id:
          type: string
          pattern: ^[a-f0-9]{32}$
          title: Business Id
        error:
          type: string
          title: Error
        error_type:
          type: string
          title: Error Type
      type: object
      required:
        - error
        - error_type
      title: BusinessMatchOutputWithErrors
    BusinessMatchOutput:
      properties:
        input:
          $ref: '#/components/schemas/BusinessMatchInput'
        business_id:
          type: string
          pattern: ^[a-f0-9]{32}$
          title: Business Id
      type: object
      title: BusinessMatchOutput
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
    RequestStatus:
      type: string
      enum:
        - success
        - miss
        - failure
      title: RequestStatus
      description: >-
        The `RequestStatus` class is an enumeration that defines the possible
        statuses of a request.


        This enum is used to indicate whether a request was successful, missed,
        or failed. It ensures

        consistent handling of request statuses across the application.


        Attributes:
            SUCCESS: Indicates that the request was successfully processed.
            MISS: Indicates that the request did not find any matching data.
            FAILURE: Indicates that the request encountered an error or failure.
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````