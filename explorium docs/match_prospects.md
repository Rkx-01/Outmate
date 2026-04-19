> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Match prospects

> Match a list of prospects attributes to ids.
Returns a list of the same length and order as the input list, with the matched ids.

### Introduction

The **Match Prospects** endpoint allows users to accurately match individual prospects to unique **Prospect IDs** using multiple fetchers, such as email, phone number, LinkedIn profile, or name and company combination. This ensures accurate lead identification and enhances sales and marketing workflows.

<Icon icon="thumbtack" iconType="solid" color="red" /> **Key Benefits:**

* Match and validate **lead data** across multiple fetchers.
* Enhance **B2B prospecting** by linking leads to business profiles.
* Improve **lead scoring and segmentation** with high-quality matches.
* Reduce **data duplication** and inconsistencies.

### Endpoint: `POST /v1/prospects/match`

<AccordionGroup>
  <Accordion title="How It Works">
    1. **Input:** Provide a list of prospects with at least one fetcher (e.g., email, phone number, LinkedIn URL, or name & company).
    2. **Processing:** The system cross-references internal datasets and returns the best possible matches.
    3. **Output:** A structured response with matched **Prospect IDs**, maintaining the same order as the input list.
  </Accordion>

  <Accordion title="Request Schema">
    | Field                     | Type   | Description                                                      |
    | :------------------------ | :----- | :--------------------------------------------------------------- |
    | **prospects\_to\_match:** | Array  | A list of prospect fetchers to match                             |
    | `email`                   | String | The prospect's email address                                     |
    | `phone_number`            | String | The prospect's phone number                                      |
    | `full_name`               | String | The prospect's full name (must be accompanied by `company_name`) |
    | `company_name`            | String | The prospect's company name (must be accompanied by `full_name`) |
    | `linkedin`                | String | LinkedIn profile URL                                             |
    | `business_id` (optional)  | String | Filters the match to a specific company                          |
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl -X POST "https://api.explorium.ai/v1/prospects/match" \
      -H "API_KEY: your_api_key_here" \
      -H "Content-Type: application/json" \
      -d '{

     "request_context": {},
      "prospects_to_match": [
        {
          "business_id": "19fbe842a2e51db95d4f92333f2cc63a",
          "linkedin": "https://www.linkedin.com/in/russell-lumpkin-07585b128"
        },
        {
          "full_name": "Richard Branson", 
          "company_name": "Virgin"
        },
        {
          "email": "satyan@microsoft.com"
        }
      ]
    }'
    ```
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON theme={null}
    {
      "response_context": {
        "correlation_id": "68d2e054ffa149dab8d09c59f1092091",
        "request_status": "success",
        "time_took_in_seconds": 0
      },
      "total_results": 3,
      "total_matches": 3,
      "matched_prospects": [
        {
          "input": {
            "business_id": "19fbe842a2e51db95d4f92333f2cc63a",
            "full_name": null,
            "company_name": null,
            "email": null,
            "phone_number": null,
            "linkedin": "https://www.linkedin.com/in/russell-lumpkin-07585b128"
          },
          "prospect_id": "6ffd52c681452e2da8aac7ec3efb174f4604734c"
        },
        {
          "input": {
            "business_id": null,
            "full_name": "Richard Branson",
            "company_name": "Virgin",
            "email": null,
            "phone_number": null,
            "linkedin": null
          },
          "prospect_id": "46ab818ec439a76489024b5727abdf194dfa3329"
        },
        {
          "input": {
            "business_id": null,
            "full_name": null,
            "company_name": null,
            "email": "satyan@microsoft.com",
            "phone_number": null,
            "linkedin": null
          },
          "prospect_id": "f80a80fb6b3d55dfefd269bb35c2049e050876ae"
        }
      ]
    }

    ```
  </Accordion>

  <Accordion title="Best Practices">
    * **Use multiple fetchers** whenever possible to increase match accuracy.
    * **Combine with** `business_id` **to refine matches to a specific company.**
    * **Ensure accurate and up-to-date data** for improved results.
    * **Handle** `null` **values** in responses where no match is found.
    * **Use the input field** when sending multiple queries to match your queries with the results.
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> **For more details on request formats and usage, refer to the API documentation.**


## OpenAPI

````yaml post /v1/prospects/match
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/match:
    post:
      tags:
        - Prospects
      summary: Match Prospects
      description: >-
        Match a list of prospects attributes to ids.

        Returns a list of the same length and order as the input list, with the
        matched ids.
      operationId: match_prospects
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
              $ref: '#/components/schemas/ProspectsMatchRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProspectsMatchResponse'
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
    ProspectsMatchRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        prospects_to_match:
          items:
            $ref: '#/components/schemas/ProspectMatchInput'
          type: array
          maxItems: 50
          minItems: 1
          title: Prospects To Match
      additionalProperties: false
      type: object
      required:
        - prospects_to_match
      title: ProspectsMatchRequest
    ProspectsMatchResponse:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        total_results:
          type: integer
          exclusiveMinimum: 0
          title: Total Results
          description: The total_results number matched prospects
        total_matches:
          type: integer
          minimum: 0
          title: Total Matches
          description: The total number of matches.
        matched_prospects:
          items:
            anyOf:
              - $ref: '#/components/schemas/ProspectMatchOutputWithError'
              - $ref: '#/components/schemas/ProspectMatchOutput'
          type: array
          title: Matched Prospects
          description: >-
            A list of matched prospects ids represented by MD5 hashes. May
            contain None for unmatched items.
      type: object
      required:
        - response_context
        - total_results
        - total_matches
      title: ProspectsMatchResponse
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
    ProspectMatchInput:
      properties:
        business_id:
          type: string
          title: Business Id
          description: Explorium business id
          example: null
          nullable: true
        full_name:
          type: string
          title: Full Name
          description: Full name of the person
          example: null
          nullable: true
        company_name:
          type: string
          title: Company Name
          description: Company name
          example: null
          nullable: true
        email:
          type: string
          title: Email
          description: Email address
          example: null
          nullable: true
        phone_number:
          type: string
          title: Phone Number
          description: Phone number
          example: null
          nullable: true
        linkedin:
          type: string
          title: Linkedin
          description: LinkedIn URL
          example: null
          nullable: true
      type: object
      title: ProspectMatchInput
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
    ProspectMatchOutputWithError:
      properties:
        input:
          $ref: '#/components/schemas/ProspectMatchInput'
        prospect_id:
          type: string
          pattern: ^[a-f0-9]{40}$
          title: Prospect Id
        error:
          type: string
          title: Error
        error_type:
          type: string
          title: Error Type
      type: object
      required:
        - input
        - error
        - error_type
      title: ProspectMatchOutputWithError
    ProspectMatchOutput:
      properties:
        input:
          $ref: '#/components/schemas/ProspectMatchInput'
        prospect_id:
          type: string
          pattern: ^[a-f0-9]{40}$
          title: Prospect Id
      type: object
      required:
        - input
      title: ProspectMatchOutput
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