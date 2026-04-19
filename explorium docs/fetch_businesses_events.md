> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch Businesses Events

> Create events and fetch for businesses.

## Description

The **Business Events** endpoint delivers timely insights into key business activities, such as **funding rounds, IPOs, product launches, hiring trends, office openings and more**. This enables users to monitor industry shifts, analyze market dynamics, and make informed decisions based on recent developments.

Each event provides a snapshot of **real-time changes** occurring within businesses, offering valuable intelligence on company growth, strategic moves, and workforce fluctuations.

### Important Considerations for Event

* Events are **limited to recent occurrences** and are available **`only within the timeframe defined intimestamp_from`** , which should be set to **the last quarter (past 3 months)**.
* If no qualifying events took place in the specified period, the response will be empty.
* This API does not provide historical records. To access past data, refer to the appropriate **Enrichment API** endpoints.

<AccordionGroup>
  <Accordion title="Coverage">
    | Attribute              | Coverage Details                                                                |
    | :--------------------- | :------------------------------------------------------------------------------ |
    | **Total Events**       | Covers thousands of business-related events monthly                             |
    | **Event Categories**   | Includes funding, IPOs, product launches, partnerships, hiring trends, and more |
    | **Geographical Scope** | Global coverage across 150+ countries                                           |
    | **Data Refresh Rate**  | Updated in near real-time                                                       |
  </Accordion>

  <Accordion title="How It Works">
    * **Input:** Define filter parameters such as `event_types`, `business_ids`, and `timestamp_from`.
    * **Processing:** The system retrieves relevant business events from its real-time data sources.
    * **Output:** A structured response containing event details, including timestamps, descriptions, and business associations.
  </Accordion>

  <Accordion title="Query Parameters">
    | Parameter        | Type   | Description                                                                                                          |
    | :--------------- | :----- | :------------------------------------------------------------------------------------------------------------------- |
    | `event_types`    | Array  | Filters events by type (e.g. `ipo_announcement`, `new_funding_round`, `new_investment`, `new_product`, `new_office`) |
    | `business_ids`   | Array  | Returns events related to specific businesses using their Business IDs                                               |
    | `timestamp_from` | String | Filters results to show only events after a specific timestamp (ISO format)                                          |
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl -X POST \
      "https://api.explorium.ai/v1/businesses/events" \
      -H "API_KEY: your_api_key_here" \
      -H "Content-Type: application/json" \
      -d '{
      "event_types": [
        "ipo_announcement",
        "new_investment"
      ],
      "business_ids": [
        "8adce3ca1cef0c986b22310e369a0793"
      ]
    }'
    ```
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON theme={null}
    {
      "response_context": {
        "correlation_id": "e96ef2125e0d45568f370cee53428106",
        "request_status": "success",
        "time_took_in_seconds": 4.299
      },
      "output_events": [
        {
          "event_name": "new_investment",
          "event_time": "2025-01-20T00:00:00+00:00",
          "event_id": "60392c31a409901d75d071565d09dda4",
          "data": {
            "event_name": "new_investment",
            "investment_date": "2025-01-20T00:00:00+00:00",
            "investment_amount": 430000013312,
            "investment_target": "United States",
            "investment_type": "Strategic Investment",
            "link": "https://www.businesstimes.com.sg/international/trump-says-apple-ceo-make-large-investment-us"
          },
          "business_id": "8adce3ca1cef0c986b22310e369a0793"
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Best Practices">
    * **Use targeted queries** by specifying `event_types` to reduce unnecessary data retrieval.
    * **`Combinebusiness_ids withtimestamp_from`** for precise event tracking.
    * **Monitor new event types** as the dataset is continually updated.
    * **Leverage analytics tools** to extract actionable insights and refine business strategies.
  </Accordion>

  <Accordion title="Event Categories">
    ## Funding & Investment

    * [IPO Announcement](/reference/businesses/events/types/ipo-announcement) - Initial Public Offering announcement
    * [New Funding Round](/reference/businesses/events/types/new-funding-round) - Announcement of a new funding round
    * [New Investment](/reference/businesses/events/types/new-investment) - Announcement of a new investment

    ## Product & Business Growth

    * [New Product Launch](/reference/businesses/events/types/new-product-launch) - Launch of a new product
    * [New Office Opening](/reference/businesses/events/types/new-office-opening) - Opening of a new office
    * [Office Closing](/reference/businesses/events/types/office-closing) - Closing of a company's office
    * [Company's Award](/reference/businesses/events/types/companys-award-event) - Recognition of a company's achievements and accolades

    ## Partnerships & Mergers

    * [New Partnership](/reference/businesses/events/types/new-partnership) - Announcement of a new partnership
    * [Merger and Acquisitions](/reference/businesses/events/types/merger-and-acquisitions) - Tracks major M\&A activity

    ## Hiring & Workforce Trends

    * [Hiring (per department)](/reference/businesses/events/types/hiring-by-department) - Hiring by Department
    * [Department trend (per department)](/reference/businesses/events/types/department-trend) - Workforce Changes by Department
    * **New executive level hires** - Announcement of a new employee joining the company

    ## Legal & Security Issues

    * [Lawsuits and Legal Issues](/reference/businesses/events/types/lawsuits-and-legal-issues) - Tracks legal challenges and regulatory issues
    * [Outages and Security Breaches](/reference/businesses/events/types/outages-and-security-breaches) - Identifies major disruptions and cybersecurity incidents

    ## Financial Adjustments

    * [Cost Cutting](/reference/businesses/events/types/cost-cutting) - Tracks significant cost reduction measures
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> For detailed endpoint explanations, request examples, and integration tips, explore the documentation sections above.

## Body Params - Try Me Example

```
event_types: ipo_announcement, new_investment
business_ids: 8adce3ca1cef0c986b22310e369a0793
```


## OpenAPI

````yaml post /v1/businesses/events
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/businesses/events:
    post:
      tags:
        - Businesses
      summary: Fetch Businesses Events
      description: Create events and fetch for businesses.
      operationId: fetch_businesses_events
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
              $ref: '#/components/schemas/BusinessesEventsRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
    BusinessesEventsRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        entity_type:
          allOf:
            - $ref: '#/components/schemas/EntityType'
        event_types:
          items:
            $ref: '#/components/schemas/BusinessesEventIdentifier'
          type: array
          minItems: 1
        timestamp_to:
          anyOf:
            - type: string
              format: date-time
            - type: string
          title: Timestamp To
          description: ISO format datetime string or date in format YYYY-MM-DD
          example: null
          nullable: true
        timestamp_from:
          anyOf:
            - type: string
              format: date-time
            - type: string
          title: Timestamp From
          description: ISO format datetime string or date in format YYYY-MM-DD
          example: null
          nullable: true
        business_ids:
          items:
            type: string
            pattern: ^[a-f0-9]{32}$
          type: array
          maxItems: 40
          minItems: 1
          uniqueItems: true
          title: Business Ids
      additionalProperties: false
      type: object
      required:
        - event_types
        - business_ids
      title: BusinessesEventsRequest
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    EntityType:
      type: string
      enum:
        - business
        - prospect
      title: EntityType
      description: >-
        The `EntityType` class is an enumeration that defines the types of
        entities.


        This enum is used to specify whether the entity is a business or a
        prospect.

        It ensures consistent handling of entity types across the application.


        Attributes:
            BUSINESS: Represents a business entity.
            PROSPECT: Represents a prospect entity.
    BusinessesEventIdentifier:
      type: string
      enum:
        - ipo_announcement
        - new_funding_round
        - new_investment
        - new_product
        - new_office
        - closing_office
        - new_partnership
        - increase_in_engineering_department
        - increase_in_sales_department
        - increase_in_marketing_department
        - increase_in_operations_department
        - increase_in_customer_service_department
        - increase_in_all_departments
        - decrease_in_engineering_department
        - decrease_in_sales_department
        - decrease_in_marketing_department
        - decrease_in_operations_department
        - decrease_in_customer_service_department
        - decrease_in_all_departments
        - employee_joined_company
        - hiring_in_creative_department
        - hiring_in_education_department
        - hiring_in_engineering_department
        - hiring_in_finance_department
        - hiring_in_health_department
        - hiring_in_human_resources_department
        - hiring_in_legal_department
        - hiring_in_marketing_department
        - hiring_in_operations_department
        - hiring_in_professional_service_department
        - hiring_in_sales_department
        - hiring_in_support_department
        - hiring_in_trade_department
        - hiring_in_unknown_department
        - company_award
        - outages_and_security_breaches
        - cost_cutting
        - merger_and_acquisitions
        - lawsuits_and_legal_issues
      title: BusinessesEventIdentifier
      description: >-
        Enumeration of business-related event identifiers.


        This enum defines various types of events associated with businesses,
        such as:

        - Financial activities (e.g., IPO announcements, new funding rounds, new
        investments)

        - Organizational changes (e.g., new offices, closing offices, mergers
        and acquisitions)

        - Workforce trends (e.g., hiring in specific departments, increases or
        decreases in department sizes)

        - Product and partnership updates (e.g., new products, new partnerships)

        - Other significant events (e.g., company awards, outages, cost-cutting
        measures, legal issues)


        These identifiers are used to categorize and track business events
        within the application.
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