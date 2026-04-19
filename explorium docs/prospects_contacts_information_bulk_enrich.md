> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Contact details (Bulk)

## Description

The **Bulk Contact Details Enrichment** API allows users to retrieve verified **data** for multiple prospects in a single request. This endpoint enhances lead intelligence by providing accurate **emails, phone numbers, and mobile numbers** at scale.

<Icon icon="thumbtack" iconType="solid" color="red" /> **Key Benefits:**

* **Bulk retrieval** of enriched contact data for up to 50 prospects per request.
* **Enhance outreach** with validated professional and personal contact details.
* **Optimize lead engagement** by leveraging multiple verified data points.

<AccordionGroup>
  <Accordion title="How It Works">
    1. **Input:** Provide up to 50 `prospect_id` values, obtained from the **Match Prospects** endpoint.
    2. **Processing:** The system retrieves verified contact information, including emails and phone numbers.
    3. **Output:** Returns structured data in the same order as the input, ensuring easy mapping.
  </Accordion>

  <Accordion title="Request Schema">
    | Field          | Type  | Description                                       |
    | :------------- | :---- | :------------------------------------------------ |
    | `prospect_ids` | Array | A list of up to 50 unique prospect IDs (Required) |
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl --request POST \
         --url https://api.explorium.ai/v1/prospects/contacts_information/bulk_enrich \
         --header 'accept: application/json' \
         --header 'api_key: <your_api_key>' \
         --header 'content-type: application/json' \
         --data '{
      "prospect_ids": [
        "ee936e451b50c70e068e1b54e106cb89173198c4",
        "d668424ab4f6aaeeeb74248d56b8335383fd522b"
      ]
    }'
    ```
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON expandable theme={null}
    {
      "response_context": {
        "correlation_id": "f6bf2bf8c0e34f3d9fa000f83398c97b",
        "request_status": "success",
        "time_took_in_seconds": 0.733
      },
      "data": [
        {
          "prospect_id": "ee936e451b50c70e068e1b54e106cb89173198c4",
          "data": {
            "emails": [
              {
                "address": "satyanadella@hotmail.com",
                "type": "personal"
              },
              {
                "address": "satyan@microsoft.com",
                "type": "professional"
              }
            ],
            "phone_numbers": [
              {
                "phone_number": "+14258828080"
              },
              {
                "phone_number": "+14255032236"
              }
            ],
            "mobile_phone": "+14255032236"
          }
        },
        {
          "prospect_id": "57f9e5dac64d31d80e6e9432fe2c500d0bba2c01",
          "data": {
            "emails": [
              {
                "address": "lorihuang@hotmail.com",
                "type": "personal"
              },
              {
                "address": "jensenh@nvidia.com",
                "type": "current_professional"
              }
            ],
            "phone_numbers": [
              {
                "phone_number": "+14156991685"
              },
              {
                "phone_number": "+13172018718"
              }
            ],
            "mobile_phone": "+14156991685"
          }
        }
      ],
      "total_results": 2
    }
    ```
  </Accordion>

  <Accordion title="Best Practices">
    * **Batch process multiple prospect IDs** to improve efficiency and reduce API calls.
    * **Ensure valid prospect IDs** are used to maximize data accuracy.
    * **Leverage enriched contact data** to refine lead scoring and improve outreach.
    * **Regularly update CRM records** with the latest contact details.
  </Accordion>

  <Accordion title="Bulk Contacts Enrichment Output Signals">
    | Signal                      | API Name                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              | Data Type Final |
    | :-------------------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
    | professional\_email\_status | Individual's professional email validity status | Recommended validity status for the listed 'Professional email' address. Returns one of the following possible values: 'valid' emails are determined as safe to email, 'invalid' emails are addresses we recommend to erase from mailing lists, 'catch-all' emails are created as a precaution by domain owners. For recommendations on how best to use 'catch all' emails, read more on our resource center page 'Email validation: catch-all domains'. | object          |
    | emails                      | Individual's emails                             | List of all email addresses associated with the individual labeled as a professional or personal email address.                                                                                                                                                                                                                                                                                                                                          | array           |
    | professions\_email          | Individual's professional email                 | Current professional email address associated with the individual                                                                                                                                                                                                                                                                                                                                                                                        | string          |
    | mobile\_phone               | Individual's mobile phone                       | Individual's direct dial mobile phone number.                                                                                                                                                                                                                                                                                                                                                                                                            | string          |
    | phone\_numbers              | Individual's phone numbers                      | List of all phone numbers associated with the individual.                                                                                                                                                                                                                                                                                                                                                                                                | array           |
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> **For additional enrichment options, explore related API endpoints below.**

## Body Params - Try Me Example

```
prospect_ids: ee936e451b50c70e068e1b54e106cb89173198c4,
57f9e5dac64d31d80e6e9432fe2c500d0bba2c01
```


## OpenAPI

````yaml post /v1/prospects/contacts_information/bulk_enrich
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/contacts_information/bulk_enrich:
    post:
      tags:
        - ProspectsBulkEnrichments
      summary: Contacts Information
      operationId: prospects_contacts_information_bulk_enrich
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
              $ref: '#/components/schemas/ProspectsBulkContactsEnrichRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/ProspectsBulkEnrichResponse_ContactsInformationOutputSchema_
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
    ProspectsBulkContactsEnrichRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        parameters:
          type: object
          title: Parameters
          nullable: true
        prospect_ids:
          items:
            type: string
            pattern: ^[a-f0-9]{40}$
          type: array
          maxItems: 50
          minItems: 1
          title: Prospect Ids
      additionalProperties: false
      type: object
      required:
        - prospect_ids
      title: ProspectsBulkContactsEnrichRequest
    ProspectsBulkEnrichResponse_ContactsInformationOutputSchema_:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        data:
          items:
            $ref: >-
              #/components/schemas/ProspectsBulkEnrichRow_ContactsInformationOutputSchema_
          type: array
          title: Data
        entity_id:
          anyOf:
            - type: string
              pattern: ^[a-f0-9]{32}$
            - type: string
              pattern: ^[a-f0-9]{40}$
          title: Entity Id
        total_results:
          type: integer
          title: Total Results
      type: object
      required:
        - response_context
        - total_results
      title: ProspectsBulkEnrichResponse[ContactsInformationOutputSchema]
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
    ProspectsBulkEnrichRow_ContactsInformationOutputSchema_:
      properties:
        prospect_id:
          type: string
          pattern: ^[a-f0-9]{40}$
          title: Prospect Id
        data:
          $ref: '#/components/schemas/ContactsInformationOutputSchema'
      type: object
      required:
        - prospect_id
      title: ProspectsBulkEnrichRow[ContactsInformationOutputSchema]
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
    ContactsInformationOutputSchema:
      properties:
        emails:
          items:
            additionalProperties:
              type: string
            type: object
          type: array
          title: Emails
        professions_email:
          type: string
          format: email
          title: Professions Email
        professional_email_status:
          $ref: '#/components/schemas/EmailValidationStatus'
        phone_numbers:
          items:
            additionalProperties:
              type: string
              pattern: >-
                ^\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,12}$
            type: object
          type: array
          title: Phone Numbers
        mobile_phone:
          type: string
          pattern: >-
            ^\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,12}$
          title: Mobile Phone
      type: object
      title: ContactsInformationOutputSchema
    EmailValidationStatus:
      enum:
        - valid
        - catch-all
        - invalid
      title: EmailValidationStatus
      description: >-
        The `EmailValidationStatus` class is an enumeration that represents the
        validation status of an email address.


        This enum is used to categorize email addresses based on their
        validation results, such as:

        - `VALID`: The email address is valid and deliverable.

        - `CATCH_ALL`: The email address is part of a catch-all domain, meaning
        it may or may not be deliverable.

        - `INVALID`: The email address is invalid and undeliverable.


        These statuses are used to ensure consistent handling of email
        validation results across the application.
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````