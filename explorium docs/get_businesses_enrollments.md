> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Businesses Enrollments

> Show businesses events enrollments records for user.

## Description

The Get Business Events Enrollments endpoint retrieves all your active event monitoring configurations. This allows you to review which businesses and event types you're currently tracking, along with enrollment details.

<AccordionGroup>
  <Accordion title="How It Works">
    * **Input**: Either pass `partner_id` in the header; otherwise, your key will be used to infer you partner id.
    * **Processing**: The system retrieves all active enrollments associated with your partner\_id.
    * **Output**: A structured response containing all enrollment configurations.
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl -X GET \
      "https://api.explorium.ai/v1/businesses/events/enrollments" \
      -H "API_KEY: your_api_key_here" \
      -H "partner_id: your_partner_id"
    ```
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON theme={null}
    {
      "response_context": {
        "correlation_id": "1234",
        "request_status": "success",
        "time_took_in_seconds": 0.515
      },
      "enrollments": [
        {
          "enrollment_id": "en_7b429a01",
          "enrollment_key": "my_b2b_saas_monitor",
          "business_ids": ["8adce3ca1cef0c986b22310e369a0793", "665595bbb4e724de6f8bc705a5b84753"],
          "event_types": ["ipo_announcement", "new_funding_round", "new_product"]
        },
        {
          "enrollment_id": "en_9c31b8d2",
          "enrollment_key": "fintech_competitors",
          "business_ids": ["2222", "3333"],
          "event_types": ["new_partnership", "new_investment"]
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>


## OpenAPI

````yaml get /v1/businesses/events/enrollments
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
    get:
      tags:
        - Businesses
      summary: Get Businesses Enrollments
      description: Show businesses events enrollments records for user.
      operationId: get_businesses_enrollments
      parameters:
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
                $ref: '#/components/schemas/BusinessesEnrollmentsGetResponse'
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
    BusinessesEnrollmentsGetResponse:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        enrollments:
          items:
            $ref: '#/components/schemas/BusinessesEnrollment'
          type: array
          title: Enrollments
      type: object
      required:
        - response_context
        - enrollments
      title: BusinessesEnrollmentsGetResponse
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
    BusinessesEnrollment:
      properties:
        enrollment_id:
          type: string
          title: Enrollment Id
        enrollment_key:
          type: string
          minLength: 4
          title: Enrollment Key
        event_types:
          items:
            anyOf:
              - $ref: '#/components/schemas/EventName'
              - $ref: '#/components/schemas/InternalEventIdentifier'
          type: array
          title: Event Types
        business_ids:
          items:
            type: string
            pattern: ^[a-f0-9]{32}$
          type: array
          title: Business Ids
      type: object
      required:
        - enrollment_id
        - enrollment_key
        - event_types
        - business_ids
      title: BusinessesEnrollment
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
    EventName:
      type: string
      enum:
        - prospect_changed_role
        - prospect_changed_company
        - prospect_job_start_anniversary
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
      title: EventName
      description: An enumeration.
    InternalEventIdentifier:
      type: string
      enum:
        - prospect_changed_role
        - prospect_changed_company
        - prospect_job_start_anniversary
        - ipo_announcement
        - new_funding_round
        - new_investment
        - new_product
        - new_office
        - closing_office
        - new_partnership
        - merger_and_acquisitions
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
        - company_award
        - outages_and_security_breaches
        - cost_cutting
        - lawsuits_and_legal_issues
      title: InternalEventIdentifier
      description: >-
        The `InternalEventIdentifier` class is an enumeration that defines
        internal event identifiers.


        This enum is used to categorize and track internal events related to
        businesses and prospects.

        All events are now handled internally through the event service.
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````