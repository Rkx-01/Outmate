> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Businesses Enrollments

> Update enrollments for businesses

## Description

Update an existing enrollment.

<AccordionGroup>
  <Accordion title="How It Works">
    * **Input**: Define parameters including enrollment\_key and enrollment\_id to update, and updated business\_ids, and event\_types.
    * **Processing**: The system will update your your enrollment and update the monitoring for events.
    * **Output**: A confirmation response containing your enrollment\_key and enrollment\_id for future reference.
  </Accordion>

  <Accordion title="Query Parameters">
    | Field           | Type   | Description                                                               |
    | :-------------- | :----- | :------------------------------------------------------------------------ |
    | enrollment\_key | String | A unique identifier for this enrollment                                   |
    | enrollment\_id  | String | A unique identifier for this enrollment                                   |
    | business\_ids   | Array  | List of Business IDs to monitor for events                                |
    | event\_types    | Array  | Types of events to monitor (e.g., ipo\_announcement, new\_funding\_round) |
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl -X PATCH \
      "https://api.explorium.ai/v1/businesses/events/enrollments" \
      -H "API_KEY: your_api_key_here" \
      -H "Content-Type: application/json" \
      -d '{
      "enrollment_key": "my_b2b_saas_monitor",
      "enrollment_id": "en_7b429a01",
      "business_ids": [
        "8adce3ca1cef0c986b22310e369a0793",
        "665595bbb4e724de6f8bc705a5b84753"
      ],
      "event_types": [
        "ipo_announcement",
        "new_funding_round",
        "new_product"
      ]
    }'
    ```
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON theme={null}
    {
      "request_context": {
        "correlation_id": "1234",
        "request_status": "success",
        "time_took_in_seconds": 0.515
      },
      "enrollment_key": "my_b2b_saas_monitor",
      "enrollment_id": "en_7b429a01"
    }
    ```
  </Accordion>
</AccordionGroup>


## OpenAPI

````yaml patch /v1/businesses/events/enrollments
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/businesses/events/enrollments:
    patch:
      tags:
        - Businesses
      summary: Update Businesses Enrollments
      description: Update enrollments for businesses
      operationId: update_businesses_enrollments
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
              $ref: '#/components/schemas/BusinessesEnrollmentsUpdateRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BusinessesEnrollmentsUpdateResponse'
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
    BusinessesEnrollmentsUpdateRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        enrollment_key:
          type: string
          minLength: 4
          title: Enrollment Key
        event_types:
          items:
            $ref: '#/components/schemas/BusinessesEventIdentifier'
          type: array
          minItems: 1
        enrollment_id:
          type: string
          title: Enrollment Id
        business_ids:
          items:
            type: string
            pattern: ^[a-f0-9]{32}$
          type: array
          maxItems: 20
          minItems: 1
          title: Business Ids
      additionalProperties: false
      type: object
      required:
        - enrollment_key
        - event_types
        - enrollment_id
        - business_ids
      title: BusinessesEnrollmentsUpdateRequest
    BusinessesEnrollmentsUpdateResponse:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        enrollment_key:
          type: string
          minLength: 4
          title: Enrollment Key
        enrollment_id:
          type: string
          title: Enrollment Id
      type: object
      required:
        - response_context
        - enrollment_key
        - enrollment_id
      title: BusinessesEnrollmentsUpdateResponse
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