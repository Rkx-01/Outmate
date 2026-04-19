> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Businesses Enrollments

> Delete events enrollments records

## Description

The Delete Business Events Enrollment endpoint allows you to cancel an active event monitoring configuration. This is useful when you no longer need to track certain businesses or when a monitoring strategy needs to be reconfigured.

<AccordionGroup>
  <Accordion title="How It Works">
    * **Input**: Specify the enrollment\_id you wish to cancel.
    * **Processing**: The system removes the enrollment configuration.
    * **Output**: A confirmation of successful deletion.
  </Accordion>

  <Accordion title="Query Parameters">
    | Field          | Type   | Description                                       |
    | :------------- | :----- | :------------------------------------------------ |
    | enrollment\_id | String | The unique identifier of the enrollment to delete |
  </Accordion>

  <Accordion title="Example Request (cURL)">
    ```shell Bash theme={null}
    curl -X DELETE \
      "https://api.explorium.ai/v1/businesses/events/enrollments" \
      -H "API_KEY: your_api_key_here" \
      -H "Content-Type: application/json" \
      -d '{
      "enrollment_id": "en_7b429a01"
    }'
    ```
  </Accordion>

  <Accordion title="Example Response">
    ```json JSON theme={null}
    {
      "status": "success"
    }
    ```
  </Accordion>
</AccordionGroup>


## OpenAPI

````yaml delete /v1/businesses/events/enrollments
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
    delete:
      tags:
        - Businesses
      summary: Delete Businesses Enrollments
      description: Delete events enrollments records
      operationId: delete_businesses_enrollments
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
              $ref: '#/components/schemas/BusinessesEnrollmentsDeleteRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BusinessesEnrollmentsDeleteResponse'
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
    BusinessesEnrollmentsDeleteRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        enrollment_id:
          type: string
          title: Enrollment Id
      additionalProperties: false
      type: object
      required:
        - enrollment_id
      title: BusinessesEnrollmentsDeleteRequest
    BusinessesEnrollmentsDeleteResponse:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        status:
          allOf:
            - $ref: '#/components/schemas/RequestStatus'
      type: object
      required:
        - response_context
      title: BusinessesEnrollmentsDeleteResponse
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