> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Contact details

### Introduction

The **Contact details enrichments** API provides detailed information about individual prospects, including contact details, professional emails, and phone numbers. This API is crucial for lead enrichment, personalized outreach, and enhancing sales intelligence workflows.

<Icon icon="thumbtack" iconType="solid" color="red" /> **Key Benefits:**

* Access **validated contact information** for prospects.
* Retrieve **multiple email addresses**, including personal and professional.
* Ensure **accurate and up-to-date data** for prospecting and engagement.

### Endpoint: `POST /prospects/contacts_information/enrich`

<AccordionGroup>
  <Accordion title="How It Works">
    1. **Input:** Provide a `prospect_id` (retrieved from the **Match Prospects** endpoint) to retrieve enrichment details.
    2. **Processing:** The system scans and fetches available data from multiple sources.
    3. **Output:** A structured response containing contact details, emails, and phone numbers.
  </Accordion>

  <Accordion title="Request Schema">
    | Field         | Type   | Description                                     |
    | :------------ | :----- | :---------------------------------------------- |
    | `prospect_id` | String | A unique identifier for the prospect (Required) |
  </Accordion>

  <Accordion title="Best Practices">
    * **Use verified prospect IDs** for accurate enrichment.
    * **Cross-check multiple contact points** to reach prospects effectively.
    * **Store enriched data in CRM** for seamless sales workflows.
    * **Update prospect details regularly** to maintain accuracy in outreach campaigns.
  </Accordion>

  <Accordion title="Contacts Information Output Signal">
    | Signal                      | API Name                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              | Data Type Final |
    | :-------------------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
    | professional\_email\_status | Individual's professional email validity status | Recommended validity status for the listed 'Professional email' address. Returns one of the following possible values: 'valid' emails are determined as safe to email, 'invalid' emails are addresses we recommend to erase from mailing lists, 'catch-all' emails are created as a precaution by domain owners. For recommendations on how best to use 'catch all' emails, read more on our resource center page 'Email validation: catch-all domains'. | object          |
    | emails                      | Individual's emails                             | List of all email addresses associated with the individual labeled as a professional or personal email address.                                                                                                                                                                                                                                                                                                                                          | array           |
    | professions\_email          | Individual's professional email                 | Current professional email address associated with the individual                                                                                                                                                                                                                                                                                                                                                                                        | string          |
    | mobile\_phone               | Individual's mobile phone                       | Individual's direct dial mobile phone number.                                                                                                                                                                                                                                                                                                                                                                                                            | string          |
    | phone\_numbers              | Individual's phone numbers                      | List of all phone numbers associated with the individual.                                                                                                                                                                                                                                                                                                                                                                                                | array           |
  </Accordion>
</AccordionGroup>

## Body Params - Try Me Example

```
prospect_id: ee936e451b50c70e068e1b54e106cb89173198c4
```

**Email Only (2 credits):**

```json theme={null}
  {
    "prospect_id": "ee936e451b50c70e068e1b54e106cb89173198c4",
    "parameters": {
      "contact_types": ["email"]
    }
  }
```

**Phone Only (5 credits):**

```json theme={null}
{
    "prospect_id": "ee936e451b50c70e068e1b54e106cb89173198c4",
    "parameters": {
      "contact_types": ["phone"]
    }
  }
```

**Both Email and Phone (5 credits) - Default behavior:**

```json theme={null}
{
    "prospect_id": "ee936e451b50c70e068e1b54e106cb89173198c4",
    "parameters": {
      "contact_types": ["email", "phone"]
    }
  }
```

**Backward Compatible (no parameters = all contact types):**

```
prospect_id: ee936e451b50c70e068e1b54e106cb89173198c4
```


## OpenAPI

````yaml post /v1/prospects/contacts_information/enrich
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/contacts_information/enrich:
    post:
      tags:
        - ProspectsEnrichments
      summary: Contacts Information
      operationId: prospects_contacts_information_enrich
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
              $ref: '#/components/schemas/ProspectsContactsEnrichRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/ProspectsEnrichResponse_ContactsInformationOutputSchema_
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
    ProspectsContactsEnrichRequest:
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
        prospect_id:
          type: string
          pattern: ^[a-f0-9]{40}$
          title: Prospect Id
          description: The prospect_id to enrich.
      additionalProperties: false
      type: object
      required:
        - prospect_id
      title: ProspectsContactsEnrichRequest
    ProspectsEnrichResponse_ContactsInformationOutputSchema_:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        data:
          anyOf:
            - $ref: '#/components/schemas/ContactsInformationOutputSchema'
            - items:
                $ref: '#/components/schemas/ContactsInformationOutputSchema'
              type: array
          title: Data
        entity_id:
          anyOf:
            - type: string
              pattern: ^[a-f0-9]{32}$
            - type: string
              pattern: ^[a-f0-9]{40}$
          title: Entity Id
      type: object
      required:
        - response_context
      title: ProspectsEnrichResponse[ContactsInformationOutputSchema]
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