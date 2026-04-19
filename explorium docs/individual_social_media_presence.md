> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Individual’s social media presence

### Introduction

The **Individual’s Social Media Presence Enrichments** API provides insights into a prospect’s social media activity. This endpoint retrieves public posts from professional networks, allowing businesses to analyze engagement trends, content topics, and prospect interests for better outreach and marketing strategies.

<Icon icon="thumbtack" iconType="solid" color="red" /> **Key Benefits:**

* Gain **real-time visibility** into a prospect’s social media activity.
* Understand **professional interests, opinions, and engagement**.
* Improve **personalized outreach** by leveraging recent posts and topics of discussion.
* Track changes in **professional communication patterns** over time.

<AccordionGroup>
  <Accordion title="How It Works">
    1. **Input:** Provide a `prospect_id` (retrieved from the **Match Prospects** endpoint) to fetch their social media data.
    2. **Processing:** The system gathers publicly available social media posts and organizes them into a structured format.
    3. **Output:** A response containing recent posts, links to content, and engagement details.
  </Accordion>

  <Accordion title="Request Schema">
    | Field         | Type   | Description                                     |
    | :------------ | :----- | :---------------------------------------------- |
    | `prospect_id` | String | A unique identifier for the prospect (Required) |
  </Accordion>

  <Accordion title="Best Practices">
    * **Use verified prospect IDs** for accurate enrichment.
    * **Analyze engagement patterns** to tailor marketing efforts.
    * **Store and categorize insights** in your CRM for future reference.
    * **Leverage content analysis** for personalized outreach.
    * **Monitor recent social media activity** to track industry trends and thought leadership.
  </Accordion>

  <Accordion title="Individual’s Social Media Presence Output Signal">
    | Signal               | API Name                | Description                                                           | Data Type Final |
    | :------------------- | :---------------------- | :-------------------------------------------------------------------- | :-------------- |
    | created\_at          | Time of posting         | Timestamp of when the individual's post was published.                | datetime        |
    | number\_of\_likes    | Number of post likes    | Number of likes the individual's post received by time of collection. | integer         |
    | post\_url            | LinkedIn® post URL      | URL to the LinkedIn® post published by individual.                    | url             |
    | number\_of\_comments | Number of post comments | Number of comments on the individual's post by time of collection.    | integer         |
    | days\_since\_posted  | Days since post         | Number of days since the post was published by the individual.        | integer         |
    | post\_text           | Post text content       | Text content of the LinkedIn® post published by individual.           | string          |
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> **Key Consideration:**

* Posts retrieved are from publicly available social media content.
* Engagement data (likes, comments) may not always be available.
* Ensure **valid prospect IDs** (from **Match Prospects**) to retrieve accurate data.
* Use insights for **trend analysis, competitor research, and engagement tracking**.

## Body Params - Try Me Example

```
prospect_id: ee936e451b50c70e068e1b54e106cb89173198c4
```


## OpenAPI

````yaml post /v1/prospects/linkedin_posts/enrich
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/linkedin_posts/enrich:
    post:
      tags:
        - ProspectsEnrichments
      summary: Linkedin Posts
      operationId: prospects_linkedin_posts_enrich
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
              $ref: >-
                #/components/schemas/partner_service__models__prospects__enrich_requests__LinkedInPostsEnrichRequest
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/ProspectsEnrichResponse_LinkedinProspectsPostsOutputSchema_
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
    partner_service__models__prospects__enrich_requests__LinkedInPostsEnrichRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        parameters:
          allOf:
            - $ref: '#/components/schemas/LinkedInPostsEnrichmentParams'
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
      title: LinkedInPostsEnrichRequest
    ProspectsEnrichResponse_LinkedinProspectsPostsOutputSchema_:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        data:
          anyOf:
            - $ref: '#/components/schemas/LinkedinProspectsPostsOutputSchema'
            - items:
                $ref: '#/components/schemas/LinkedinProspectsPostsOutputSchema'
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
      title: ProspectsEnrichResponse[LinkedinProspectsPostsOutputSchema]
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
    LinkedInPostsEnrichmentParams:
      properties: {}
      additionalProperties: false
      type: object
      title: LinkedInPostsEnrichmentParams
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
    LinkedinProspectsPostsOutputSchema:
      properties:
        display_name:
          type: string
          title: Display Name
        post_text:
          type: string
          title: Post Text
        days_since_posted:
          type: integer
          title: Days Since Posted
        post_url:
          type: string
          maxLength: 2048
          pattern: >-
            ^(https?:)?//(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+[a-z\u00a1-\uffff]{2,}\.?(?:[/?#]\S*)?$
          format: uri
          title: Post Url
        number_of_comments:
          type: integer
          title: Number Of Comments
        number_of_likes:
          type: integer
          title: Number Of Likes
        created_at:
          type: string
          format: date-time
          title: Created At
      type: object
      title: LinkedinProspectsPostsOutputSchema
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