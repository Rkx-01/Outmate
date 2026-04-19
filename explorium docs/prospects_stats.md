> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prospects Statistics

> Fetch stats for businesses.

# Prospects Statistics

### **Introduction**

The **Prospects Statistics** API provides aggregated insights and distributions for prospects based on your search criteria. This powerful analytics endpoint helps you understand the composition of your prospect universe, enabling data-driven decisions for sales territory planning, market analysis, and campaign targeting.

📌 **Key Benefits:**

* Get **instant insights** into prospect distributions without fetching individual records
* Understand **market composition** by department, seniority, location, and more
* Receive **dynamic statistics** that adapt to your filter criteria
* Make **data-driven decisions** for territory planning and resource allocation
* **No credit charges** for statistical analysis

***

<AccordionGroup>
  <Accordion title="How It Works" icon="sparkles">
    **Input:** Provide filters identical to the prospects fetch endpoint to define your target audience
    2\. **Processing:** The system aggregates prospect data based on your filters and calculates distributions
    3\. **Output:** Dynamic statistics showing distributions for the filters you've applied
    4\. **Intelligence:** The response structure adapts based on which filters are used in the request
  </Accordion>

  <Accordion title="Request Schema" icon="sparkles">
    | Field     | Type   | Description                                                                                             | Required |
    | --------- | ------ | ------------------------------------------------------------------------------------------------------- | -------- |
    | `filters` | Object | Filter criteria to define the prospect universe. Supports all filters from the `/v1/prospects` endpoint | No       |

    **Note:** See the "Supported Filters" section below for the complete list of available filters and their usage.
  </Accordion>

  <Accordion title="Supported Filters" icon="sparkles">
    This endpoint supports **ALL filters** available in the `/v1/prospects` fetch endpoint:

    ### **Contact Availability Filters**

    | Filter             | Description                  | Example           |
    | ------------------ | ---------------------------- | ----------------- |
    | `has_email`        | Filter by email availability | `{"value": true}` |
    | `has_phone_number` | Filter by phone availability | `{"value": true}` |

    ### **Professional Filters**

    | Filter                    | Description                    | Example                                             |
    | ------------------------- | ------------------------------ | --------------------------------------------------- |
    | `job_level`               | Filter by seniority level      | `{"values": ["director", "vp", "cxo"]}`             |
    | `job_department`          | Filter by department           | `{"values": ["sales", "marketing", "engineering"]}` |
    | `job_title`               | Filter by job title keywords   | `{"value": "Sales Representative"}`                 |
    | `total_experience_months` | Filter by total experience     | `{"gte": 60, "lte": 120}`                           |
    | `current_role_months`     | Filter by time in current role | `{"gte": 12}`                                       |

    ### **Geographic Filters**

    | Filter                | Description                     | Example                            |
    | --------------------- | ------------------------------- | ---------------------------------- |
    | `country_code`        | Filter by prospect's country    | `{"values": ["us", "gb", "de"]}`   |
    | `region_country_code` | Filter by prospect's region     | `{"values": ["us-ca", "us-ny"]}`   |
    | `city_region_country` | Filter by city, region, country | `{"values": ["New York, NY, US"]}` |

    ### **Company Filters**

    | Filter                        | Description                     | Example                                |
    | ----------------------------- | ------------------------------- | -------------------------------------- |
    | `business_id`                 | Filter by specific business IDs | `{"values": ["exp_id_1", "exp_id_2"]}` |
    | `company_name`                | Filter by company names         | `{"values": ["Meta", "Tesla"]}`        |
    | `company_size`                | Filter by employee count ranges | `{"values": ["51-200", "201-500"]}`    |
    | `company_revenue`             | Filter by revenue ranges        | `{"values": ["10M-50M", "50M-100M"]}`  |
    | `company_country_code`        | Filter by company HQ country    | `{"values": ["us", "ca"]}`             |
    | `company_region_country_code` | Filter by company HQ region     | `{"values": ["us-ca", "us-tx"]}`       |

    ### **Industry Classification Filters**

    | Filter              | Description                          | Example                                                      |
    | ------------------- | ------------------------------------ | ------------------------------------------------------------ |
    | `google_category`   | Filter by Google business category   | `{"values": ["Software Development", "Retail"]}`             |
    | `naics_category`    | Filter by NAICS industry codes       | `{"values": ["5611", "23"]}`                                 |
    | `linkedin_category` | Filter by LinkedIn business category | `{"values": ["software development", "investment banking"]}` |

    **Filter Structure:**

    * Use `{"values": [...]}` for multi-value filters
    * Use `{"value": ...}` for single-value or boolean filters
    * Use `{"gte": ..., "lte": ...}` for numeric range filters
  </Accordion>

  <Accordion title="Dynamic Response Structure" icon="sparkles">
    The response intelligently adapts based on the filters used in your request:

    | Filters Used                             | Statistics Returned                          | Use Case                       |
    | ---------------------------------------- | -------------------------------------------- | ------------------------------ |
    | `job_department` + `region_country_code` | Distribution of departments across regions   | Territory planning by function |
    | `job_department` + `country_code`        | Distribution of departments across countries | Executive targeting analysis   |
    | Single filter only                       | Simple count distribution                    | Quick market sizing            |

    **Always Included:**

    * `total_results`: Total count of matching prospects
    * `response_context`: Request metadata and performance metrics
  </Accordion>

  <Accordion title="Request Examples" icon="sparkles">
    ```json theme={null}
    {
    "filters": {
    "job_department": {
      "values": ["engineering", "sales", "marketing"]
    },
    "region_country_code": {
      "values": ["us-ca", "us-ny", "us-tx"]
    },
    "company_size": {
      "values": ["51-200", "201-500"]
    }
    }
    }
    ```
  </Accordion>

  <Accordion title="Response Examples" icon="sparkles">
    **Department by Region Response:**

    ```json theme={null}
    {
      "response_context": {
        "correlation_id": "812719a515474144a8cac019d7776b14",
        "request_status": "success",
        "time_took_in_seconds": 0.75
      },
      "total_results": 4500,
      "stats": {
        "job_departments_per_location": {
          "engineering": {
            "California, US": 850,
            "New York, US": 620,
            "Texas, US": 480,
            "total": 1950
          },
          "sales": {
            "California, US": 560,
            "New York, US": 410,
            "Texas, US": 380,
            "total": 1350
          },
          "marketing": {
            "California, US": 420,
            "New York, US": 350,
            "Texas, US": 430,
            "total": 1200
          },
          "total_per_location": {
            "California, US": 1830,
            "New York, US": 1380,
            "Texas, US": 1290,
            "total": 4500
          }
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Use Cases" icon="sparkles">
    ### **Sales Territory Planning**

    * Analyze prospect distribution across regions using `region_country_code` and `job_department`
    * Balance territories based on prospect density with `company_size` and `job_level` filters
    * Identify underserved markets by comparing prospect counts across geographic areas

    ### **Account-Based Marketing (ABM)**

    * Target specific companies using `company_name` or `business_id` filters
    * Analyze decision-maker distribution with `job_level` and `job_department`
    * Segment by company characteristics using `company_revenue` and `company_size`

    ### **Campaign Targeting**

    * Size your total addressable market using industry filters (`naics_category`, `linkedin_category`)
    * Validate contact availability with `has_email` and `has_phone_number`
    * Focus on new decision-makers using `current_role_months` filter

    ### **Market Intelligence**

    * Compare prospect density across industries using classification filters
    * Analyze experience levels with `total_experience_months`
    * Track job mobility trends with role duration filters

    ### **Lead Scoring & Qualification**

    * Identify high-value segments combining `job_level`, `company_revenue`, and `job_department`
    * Find prospects in growth companies using company size and revenue filters
    * Target specific buyer personas with precise filter combinations
  </Accordion>

  <Accordion title="Best Practices" icon="sparkles">
    * **Start broad, then narrow:** Begin with 1-2 filters to understand market size, then add filters progressively
    * **Validate before fetching:** Always run stats before expensive fetch operations to ensure sufficient results
    * **Use classification filters:** Leverage `naics_category` or `linkedin_category` for accurate industry targeting
    * **Combine geographic levels:** Use country → region → city filters for precise location targeting
    * **Monitor regularly:** Schedule weekly/monthly stats queries to track market changes
    * **Cross-reference filters:** Combine professional (job\_level) with company (company\_size) filters for better segmentation
    * **Experience targeting:** Use experience filters to identify senior professionals or recent role changes
    * **Industry-specific analysis:** Combine industry classifications with other filters for vertical-specific insights
  </Accordion>

  <Accordion title="Important Notes" icon="sparkles">
    * **No credit charges:** Statistical queries are free and don't consume any credits
    * **Real-time data:** Statistics reflect the current state of the prospect database
    * **Dynamic response:** Response structure automatically adapts to your filter combination
    * **All filters supported:** Every filter from the `/v1/prospects` endpoint works here
  </Accordion>
</AccordionGroup>

**Try Me Example:**

```json theme={null}
  {
    "filters": {
      "job_department": {
        "values": ["engineering", "sales", "marketing"]
      },
      "region_country_code": {
        "values": ["us-ca", "us-ny", "us-tx"]
      },
      "company_size": {
        "values": ["51-200", "201-500"]
      }
    }
  }
```


## OpenAPI

````yaml post /v1/prospects/stats
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/stats:
    post:
      tags:
        - Prospects
      summary: Prospect Fetch Stats
      description: Fetch stats for businesses.
      operationId: prospect_fetch_stats
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
              $ref: '#/components/schemas/ProspectsStatsRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProspectsStatsResponse'
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
    ProspectsStatsRequest:
      properties:
        request_context:
          type: object
          title: Request Context
          example: null
          nullable: true
        filters:
          $ref: '#/components/schemas/ProspectsFetchFilters'
      additionalProperties: false
      type: object
      required:
        - filters
      title: ProspectsStatsRequest
    ProspectsStatsResponse:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        total_results:
          type: integer
          title: Total Results
        stats:
          $ref: '#/components/schemas/ProspectsStats'
      type: object
      required:
        - response_context
        - total_results
        - stats
      title: ProspectsStatsResponse
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
    ProspectsFetchFilters:
      properties:
        prospect_id:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_ProspectId_'
          title: Prospect ID
          description: Filter prospects by specific Explorium prospect IDs
          example:
            values:
              - edf268ac410ff3ba9ca9cc67b065664f38201984
              - 5b486640efabe6f8bb8cf446e80169ba4a1c5ad8
          nullable: true
        has_email:
          allOf:
            - $ref: '#/components/schemas/ExistsFilter'
          title: Has Email
          description: >-
            Filter prospects by whether they have an email. Categories: [True,
            False]
          example:
            value: true
        has_phone_number:
          allOf:
            - $ref: '#/components/schemas/ExistsFilter'
          title: Has Phone Number
          description: >-
            Filter prospects by whether they have a phone number. Categories:
            [True, False]
          example:
            value: true
        job_level:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_JobSeniorityLevel_'
          title: Job Level
          description: >-
            Filter prospects by their job level. Categories: [director, manager,
            vp, partner, cxo, non-managerial, senior, entry, training, unpaid]
          example:
            values:
              - owner
              - c-suite
              - vice president
              - director
              - senior non-managerial
              - manager
              - partner
              - non-managerial
              - junior
              - president
              - senior manager
              - advisor
              - freelancer
              - board member
              - founder
        job_department:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_JobDepartment_'
          title: Job Department
          description: >-
            Filter prospects by their job department. Categories: [customer
            service, design, education, engineering, finance, general, health,
            sales, ...]
          example:
            values:
              - administration
              - real estate
              - healthcare
              - partnerships
              - c-suite
              - design
              - human resources
              - engineering
              - education
              - strategy
              - product
              - sales
              - r&d
              - retail
              - customer success
              - security
              - public service
              - creative
              - it
              - support
              - marketing
              - trade
              - legal
              - operations
              - procurement
              - data
              - manufacturing
              - logistics
              - finance
        business_id:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_BusinessId_'
          title: Business ID
          description: >-
            Filter prospects by account. Use Explorium entity IDs. Maximum
            10,000 items allowed. Example: [EXP_ENTITY_ID_1, EXP_ENTITY_ID_2]
          example:
            values:
              - 8adce3ca1cef0c986b22310e369a0793
              - 340c8040bd50cbab9c7df718bbe51cc9
        total_experience_months:
          allOf:
            - $ref: '#/components/schemas/RangeFilter_Int_'
          title: Total Experience Months
          description: Filter by total months of experience.
          example:
            gte: 1
            lte: 10
        country_code:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_CountryCodeAlpha2_'
          title: Country Code
          description: 'Filter prospects by country using alpha-2 codes. Example: [us, ca]'
          example:
            values:
              - US
              - CA
        region_country_code:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_RegionCode_'
          title: Region Country Code
          description: >-
            Filter prospects by region using ISO 3166-2 codes. Example: [us-ut,
            us-ca]
          example:
            values:
              - US-CA
              - IL-TA
        current_role_months:
          allOf:
            - $ref: '#/components/schemas/RangeFilter_Int_'
          title: Current Role Months
          description: Filter by number of months in current role.
          example:
            gte: 1
            lte: 10
        company_size:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_NumberOfEmployeesRange_'
          title: Company Size
          description: >-
            Filter by company’s number of employees. Options: [1-10, 11-50, ...,
            10001+]
          example:
            values:
              - 1-10
              - 11-50
              - 51-200
              - 201-500
              - 501-1000
              - 1001-5000
              - 5001-10000
              - 10001+
        company_revenue:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_RevenueRange_'
          title: Company Revenue
          description: >-
            Filter by company’s annual revenue. Options: [0-500K, 500K-1M, ...,
            10B-100B]
          example:
            values:
              - 0-500K
              - 500K-1M
              - 1M-5M
              - 5M-10M
              - 10M-25M
              - 25M-75M
              - 75M-200M
              - 200M-500M
              - 500M-1B
              - 1B-10B
              - 10B-100B
              - 100B-1T
              - 1T-10T
              - 10T+
        google_category:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_StandardizedText_'
          title: Google Category
          description: >-
            Filter by company’s Google business category. Example: [Paving
            contractor, Retail]
          example:
            values:
              - construction
        naics_category:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_NAICS_'
          title: NAICS Category
          description: 'Filter by NAICS code (2, 4, or full). Example: [23, 5611]'
          example:
            values:
              - '541512'
        linkedin_category:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_Text_'
          title: LinkedIn Category
          description: >-
            Filter by company’s LinkedIn business category. Example: [software
            development, investment banking]
          example:
            values:
              - retail
        job_title:
          allOf:
            - $ref: '#/components/schemas/JobTitleFilter'
          title: Job Title
          description: >-
            Filter prospects by their job titles. Supports
            include_related_job_titles parameter. Example: [Sales
            Representative, SEO specialist, Technical Support Engineer]
          example:
            values:
              - Software Engineer
              - Data Scientist
            include_related_job_titles: false
        company_country_code:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_CountryCodeAlpha2_'
          title: Company Country Code
          description: 'Filter by company HQ country using alpha-2 codes. Example: [us, ca]'
          example:
            values:
              - US
              - CA
        company_region_country_code:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_RegionCode_'
          title: Company Region Country Code
          description: >-
            Filter by company HQ region using ISO 3166-2 codes. Example: [us-ut,
            us-ca]
          example:
            values:
              - US-CA
              - IL-TA
        city_region_country:
          allOf:
            - $ref: '#/components/schemas/IncludesFilter_Text_'
          title: City Region Country
          description: Filter by city region country.
          example:
            values:
              - Paris, FR
              - Tel Aviv, IL
              - Miami, FL, US
        company_name:
          allOf:
            - $ref: '#/components/schemas/AnyMatchFilter_OrganizationName_'
          title: Company Name
          description: 'Filter by company name. Example: [Meta, Tesla]'
          example:
            values:
              - Microsoft
              - Google
        has_website:
          allOf:
            - $ref: '#/components/schemas/ExistsFilter'
          title: Has Website
          description: >-
            Filter prospects by whether their company has a website. Categories:
            [True, False]
          example:
            value: true
          nullable: true
      additionalProperties: false
      type: object
      title: ProspectsFetchFilters
      example: {}
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
    ProspectsStats:
      properties:
        job_departments_per_location:
          type: object
          title: Job Departments Per Location
        total_per_location:
          type: object
          title: Total Per Location
      type: object
      title: ProspectsStats
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
    IncludesFilter_ProspectId_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
            pattern: ^[a-f0-9]{40}$
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[ProspectId]
    ExistsFilter:
      properties:
        negate:
          type: boolean
          title: Negate
        value:
          type: boolean
          title: Value
      additionalProperties: false
      type: object
      required:
        - value
      title: ExistsFilter
    IncludesFilter_JobSeniorityLevel_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            $ref: '#/components/schemas/JobSeniorityLevel'
          type: array
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[JobSeniorityLevel]
    IncludesFilter_JobDepartment_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            $ref: '#/components/schemas/JobDepartment'
          type: array
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[JobDepartment]
    IncludesFilter_BusinessId_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
            pattern: ^[a-f0-9]{32}$
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[BusinessId]
    RangeFilter_Int_:
      properties:
        negate:
          type: boolean
          title: Negate
        gte:
          type: integer
          title: Gte
        lte:
          type: integer
          title: Lte
      additionalProperties: false
      type: object
      title: RangeFilter[Int]
    IncludesFilter_CountryCodeAlpha2_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
            pattern: >-
              ^(aw|af|ao|ai|ax|al|ad|ae|ar|am|as|aq|tf|ag|au|at|az|bi|be|bj|bq|bf|bd|bg|bh|bs|ba|bl|by|bz|bm|bo|br|bb|bn|bt|bv|bw|cf|ca|cc|ch|cl|cn|ci|cm|cd|cg|ck|co|km|cv|cr|cu|cw|cx|ky|cy|cz|de|dj|dm|dk|do|dz|ec|eg|er|eh|es|ee|et|fi|fj|fk|fr|fo|fm|ga|gb|ge|gg|gh|gi|gn|gp|gm|gw|gq|gr|gd|gl|gt|gf|gu|gy|hk|hm|hn|hr|ht|hu|id|im|in|io|ie|ir|iq|is|il|it|jm|je|jo|jp|kz|ke|kg|kh|ki|kn|kr|kw|la|lb|lr|ly|lc|li|lk|ls|lt|lu|lv|mo|mf|ma|mc|md|mg|mv|mx|mh|mk|ml|mt|mm|me|mn|mp|mz|mr|ms|mq|mu|mw|my|yt|na|nc|ne|nf|ng|ni|nu|nl|no|np|nr|nz|om|pk|pa|pn|pe|ph|pw|pg|pl|pr|kp|pt|py|ps|pf|qa|re|ro|ru|rw|sa|sd|sn|sg|gs|sh|sj|sb|sl|sv|sm|so|pm|rs|ss|st|sr|sk|si|se|sz|sx|sc|sy|tc|td|tg|th|tj|tk|tm|tl|to|tt|tn|tr|tv|tw|tz|ug|ua|um|uy|us|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|xk|ye|za|zm|zw)$
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[CountryCodeAlpha2]
    IncludesFilter_RegionCode_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
            pattern: >-
              ^(ad-02|ad-03|ad-04|ad-05|ad-06|ad-07|ad-08|ae-aj|ae-az|ae-du|ae-fu|ae-rk|ae-sh|ae-uq|af-bal|af-bam|af-bdg|af-bds|af-bgl|af-day|af-fra|af-fyb|af-gha|af-gho|af-hel|af-her|af-jow|af-kab|af-kan|af-kap|af-kdz|af-kho|af-knr|af-lag|af-log|af-nan|af-nim|af-nur|af-pan|af-par|af-pia|af-pka|af-sam|af-sar|af-tak|af-uru|af-war|af-zab|ag-03|ag-04|ag-05|ag-06|ag-07|ag-08|ag-10|ag-11|al-01|al-02|al-03|al-04|al-05|al-06|al-07|al-08|al-09|al-10|al-11|al-12|al-br|al-bu|al-di|al-dl|al-dr|al-dv|al-el|al-er|al-fr|al-gj|al-gr|al-ha|al-ka|al-kb|al-kc|al-ko|al-kr|al-ku|al-lb|al-le|al-lu|al-mk|al-mm|al-mr|al-mt|al-pg|al-pq|al-pr|al-pu|al-sh|al-sk|al-sr|al-te|al-tp|al-tr|al-vl|am-ag|am-ar|am-av|am-er|am-gr|am-kt|am-lo|am-sh|am-su|am-tv|am-vd|ao-bgo|ao-bgu|ao-bie|ao-cab|ao-ccu|ao-cnn|ao-cno|ao-cus|ao-hua|ao-hui|ao-lno|ao-lsu|ao-lua|ao-mal|ao-mox|ao-nam|ao-uig|ao-zai|ar-a|ar-b|ar-c|ar-d|ar-e|ar-g|ar-h|ar-j|ar-k|ar-l|ar-m|ar-n|ar-p|ar-q|ar-r|ar-s|ar-t|ar-u|ar-v|ar-w|ar-x|ar-y|ar-z|at-1|at-2|at-3|at-4|at-5|at-6|at-7|at-8|at-9|au-act|au-nsw|au-nt|au-qld|au-sa|au-tas|au-vic|au-wa|az-abs|az-aga|az-agc|az-agm|az-ags|az-agu|az-ast|az-ba|az-bab|az-bal|az-bar|az-bey|az-bil|az-cab|az-cal|az-cul|az-das|az-fuz|az-ga|az-gad|az-gor|az-goy|az-gyg|az-hac|az-imi|az-ism|az-kal|az-kan|az-kur|az-la|az-lac|az-lan|az-ler|az-mas|az-mi|az-na|az-nef|az-nv|az-nx|az-ogu|az-ord|az-qab|az-qax|az-qaz|az-qba|az-qbi|az-qob|az-qus|az-sa|az-sab|az-sad|az-sah|az-sak|az-sal|az-sar|az-sat|az-sbn|az-siy|az-skr|az-sm|az-smi|az-smx|az-sr|az-sus|az-tar|az-tov|az-uca|az-xa|az-xac|az-xci|az-xiz|az-xvd|az-yar|az-ye|az-yev|az-zan|az-zaq|az-zar|ba-01|ba-02|ba-03|ba-04|ba-05|ba-06|ba-07|ba-08|ba-09|ba-10|ba-bih|ba-brc|ba-srp|bb-01|bb-02|bb-03|bb-04|bb-05|bb-06|bb-07|bb-08|bb-09|bb-10|bb-11|bd-01|bd-02|bd-03|bd-04|bd-05|bd-06|bd-07|bd-08|bd-09|bd-10|bd-11|bd-12|bd-13|bd-14|bd-15|bd-16|bd-17|bd-18|bd-19|bd-20|bd-21|bd-22|bd-23|bd-24|bd-25|bd-26|bd-27|bd-28|bd-29|bd-30|bd-31|bd-32|bd-33|bd-34|bd-35|bd-36|bd-37|bd-38|bd-39|bd-40|bd-41|bd-42|bd-43|bd-44|bd-45|bd-46|bd-47|bd-48|bd-49|bd-50|bd-51|bd-52|bd-53|bd-54|bd-55|bd-56|bd-57|bd-58|bd-59|bd-60|bd-61|bd-62|bd-63|bd-64|bd-a|bd-b|bd-c|bd-d|bd-e|bd-f|bd-g|be-bru|be-van|be-vbr|be-vlg|be-vli|be-vov|be-vwv|be-wal|be-wbr|be-wht|be-wlg|be-wlx|be-wna|bf-01|bf-02|bf-03|bf-04|bf-05|bf-06|bf-07|bf-08|bf-09|bf-10|bf-11|bf-12|bf-13|bf-bal|bf-bam|bf-ban|bf-baz|bf-bgr|bf-blg|bf-blk|bf-com|bf-gan|bf-gna|bf-gou|bf-hou|bf-iob|bf-kad|bf-ken|bf-kmd|bf-kmp|bf-kop|bf-kos|bf-kot|bf-kow|bf-ler|bf-lor|bf-mou|bf-nam|bf-nao|bf-nay|bf-nou|bf-oub|bf-oud|bf-pas|bf-pon|bf-sen|bf-sis|bf-smt|bf-sng|bf-som|bf-sor|bf-tap|bf-tui|bf-yag|bf-yat|bf-zir|bf-zon|bf-zou|bg-01|bg-02|bg-03|bg-04|bg-05|bg-06|bg-07|bg-08|bg-09|bg-10|bg-11|bg-12|bg-13|bg-14|bg-15|bg-16|bg-17|bg-18|bg-19|bg-20|bg-21|bg-22|bg-23|bg-24|bg-25|bg-26|bg-27|bg-28|bh-13|bh-14|bh-15|bh-16|bh-17|bi-bb|bi-bl|bi-bm|bi-br|bi-ca|bi-ci|bi-gi|bi-ki|bi-kr|bi-ky|bi-ma|bi-mu|bi-mw|bi-ng|bi-rt|bi-ry|bj-ak|bj-al|bj-aq|bj-bo|bj-co|bj-do|bj-ko|bj-li|bj-mo|bj-ou|bj-pl|bj-zo|bn-be|bn-bm|bn-te|bn-tu|bo-b|bo-c|bo-h|bo-l|bo-n|bo-o|bo-p|bo-s|bo-t|bq-bo|bq-sa|bq-se|br-ac|br-al|br-am|br-ap|br-ba|br-ce|br-df|br-es|br-fn|br-go|br-ma|br-mg|br-ms|br-mt|br-pa|br-pb|br-pe|br-pi|br-pr|br-rj|br-rn|br-ro|br-rr|br-rs|br-sc|br-se|br-sp|br-to|bs-ak|bs-bi|bs-bp|bs-by|bs-ce|bs-ci|bs-ck|bs-co|bs-cs|bs-eg|bs-ex|bs-fp|bs-gc|bs-hi|bs-ht|bs-in|bs-li|bs-mc|bs-mg|bs-mi|bs-ne|bs-no|bs-ns|bs-rc|bs-ri|bs-sa|bs-se|bs-so|bs-ss|bs-sw|bs-wg|bt-11|bt-12|bt-13|bt-14|bt-15|bt-21|bt-22|bt-23|bt-24|bt-31|bt-32|bt-33|bt-34|bt-41|bt-42|bt-43|bt-44|bt-45|bt-ga|bt-ty|bw-ce|bw-gh|bw-kg|bw-kl|bw-kw|bw-ne|bw-nw|bw-se|bw-so|by-br|by-hm|by-ho|by-hr|by-ma|by-mi|by-vi|bz-bz|bz-cy|bz-czl|bz-ow|bz-sc|bz-tol|ca-ab|ca-bc|ca-mb|ca-nb|ca-nl|ca-ns|ca-nt|ca-nu|ca-on|ca-pe|ca-qc|ca-sk|ca-yt|cd-bc|cd-bn|cd-eq|cd-ka|cd-ke|cd-kn|cd-kw|cd-ma|cd-nk|cd-or|cd-sk|cf-ac|cf-bb|cf-bgf|cf-bk|cf-hk|cf-hm|cf-hs|cf-kb|cf-kg|cf-lb|cf-mb|cf-mp|cf-nm|cf-op|cf-se|cf-uk|cf-vk|cg-11|cg-12|cg-13|cg-14|cg-15|cg-2|cg-5|cg-7|cg-8|cg-9|cg-bzv|ch-ag|ch-ai|ch-ar|ch-be|ch-bl|ch-bs|ch-fr|ch-ge|ch-gl|ch-gr|ch-ju|ch-lu|ch-ne|ch-nw|ch-ow|ch-sg|ch-sh|ch-so|ch-sz|ch-tg|ch-ti|ch-ur|ch-vd|ch-vs|ch-zg|ch-zh|ci-01|ci-02|ci-03|ci-04|ci-05|ci-06|ci-07|ci-08|ci-09|ci-10|ci-11|ci-12|ci-13|ci-14|ci-15|ci-16|ci-17|ci-18|ci-19|cl-ai|cl-an|cl-ap|cl-ar|cl-at|cl-bi|cl-co|cl-li|cl-ll|cl-lr|cl-ma|cl-ml|cl-rm|cl-ta|cl-vs|cm-ad|cm-ce|cm-en|cm-es|cm-lt|cm-no|cm-nw|cm-ou|cm-su|cm-sw|cn-ah|cn-bj|cn-cq|cn-fj|cn-gd|cn-gs|cn-gx|cn-gz|cn-ha|cn-hb|cn-he|cn-hi|cn-hk|cn-hl|cn-hn|cn-jl|cn-js|cn-jx|cn-ln|cn-mo|cn-nm|cn-nx|cn-qh|cn-sc|cn-sd|cn-sh|cn-sn|cn-sx|cn-tj|cn-tw|cn-xj|cn-xz|cn-yn|cn-zj|co-ama|co-ant|co-ara|co-atl|co-bol|co-boy|co-cal|co-caq|co-cas|co-cau|co-ces|co-cho|co-cor|co-cun|co-dc|co-gua|co-guv|co-hui|co-lag|co-mag|co-met|co-nar|co-nsa|co-put|co-qui|co-ris|co-san|co-sap|co-suc|co-tol|co-vac|co-vau|co-vid|cr-a|cr-c|cr-g|cr-h|cr-l|cr-p|cr-sj|cu-01|cu-02|cu-03|cu-04|cu-05|cu-06|cu-07|cu-08|cu-09|cu-10|cu-11|cu-12|cu-13|cu-14|cu-99|cv-b|cv-br|cv-bv|cv-ca|cv-cf|cv-cr|cv-ma|cv-mo|cv-pa|cv-pn|cv-pr|cv-rb|cv-rg|cv-rs|cv-s|cv-sd|cv-sf|cv-sl|cv-sm|cv-so|cv-ss|cv-sv|cv-ta|cv-ts|cy-01|cy-02|cy-03|cy-04|cy-05|cy-06|cz-10|cz-101|cz-102|cz-103|cz-104|cz-105|cz-106|cz-107|cz-108|cz-109|cz-110|cz-111|cz-112|cz-113|cz-114|cz-115|cz-116|cz-117|cz-118|cz-119|cz-120|cz-121|cz-122|cz-20|cz-201|cz-202|cz-203|cz-204|cz-205|cz-206|cz-207|cz-208|cz-209|cz-20a|cz-20b|cz-20c|cz-31|cz-311|cz-312|cz-313|cz-314|cz-315|cz-316|cz-317|cz-32|cz-321|cz-322|cz-323|cz-324|cz-325|cz-326|cz-327|cz-41|cz-411|cz-412|cz-413|cz-42|cz-421|cz-422|cz-423|cz-424|cz-425|cz-426|cz-427|cz-51|cz-511|cz-512|cz-513|cz-514|cz-52|cz-521|cz-522|cz-523|cz-524|cz-525|cz-53|cz-531|cz-532|cz-533|cz-534|cz-63|cz-631|cz-632|cz-633|cz-634|cz-635|cz-64|cz-641|cz-642|cz-643|cz-644|cz-645|cz-646|cz-647|cz-71|cz-711|cz-712|cz-713|cz-714|cz-715|cz-72|cz-721|cz-722|cz-723|cz-724|cz-80|cz-801|cz-802|cz-803|cz-804|cz-805|cz-806|de-bb|de-be|de-bw|de-by|de-hb|de-he|de-hh|de-mv|de-ni|de-nw|de-rp|de-sh|de-sl|de-sn|de-st|de-th|dj-ar|dj-as|dj-di|dj-dj|dj-ob|dj-ta|dk-81|dk-82|dk-83|dk-84|dk-85|dm-01|dm-02|dm-03|dm-04|dm-05|dm-06|dm-07|dm-08|dm-09|dm-10|do-01|do-02|do-03|do-04|do-05|do-06|do-07|do-08|do-09|do-10|do-11|do-12|do-13|do-14|do-15|do-16|do-17|do-18|do-19|do-20|do-21|do-22|do-23|do-24|do-25|do-26|do-27|do-28|do-29|do-30|dz-01|dz-02|dz-03|dz-04|dz-05|dz-06|dz-07|dz-08|dz-09|dz-10|dz-11|dz-12|dz-13|dz-14|dz-15|dz-16|dz-17|dz-18|dz-19|dz-20|dz-21|dz-22|dz-23|dz-24|dz-25|dz-26|dz-27|dz-28|dz-29|dz-30|dz-31|dz-32|dz-33|dz-34|dz-35|dz-36|dz-37|dz-38|dz-39|dz-40|dz-41|dz-42|dz-43|dz-44|dz-45|dz-46|dz-47|dz-48|ec-a|ec-b|ec-c|ec-d|ec-e|ec-f|ec-g|ec-h|ec-i|ec-l|ec-m|ec-n|ec-o|ec-p|ec-r|ec-s|ec-sd|ec-se|ec-t|ec-u|ec-w|ec-x|ec-y|ec-z|ee-37|ee-39|ee-44|ee-49|ee-51|ee-57|ee-59|ee-65|ee-67|ee-70|ee-74|ee-78|ee-82|ee-84|ee-86|eg-alx|eg-asn|eg-ast|eg-ba|eg-bh|eg-bns|eg-c|eg-dk|eg-dt|eg-fym|eg-gh|eg-gz|eg-hu|eg-is|eg-js|eg-kb|eg-kfs|eg-kn|eg-mn|eg-mnf|eg-mt|eg-pts|eg-shg|eg-shr|eg-sin|eg-su|eg-suz|eg-wad|er-an|er-dk|er-du|er-gb|er-ma|er-sk|es-a|es-ab|es-al|es-an|es-ar|es-as|es-av|es-b|es-ba|es-bi|es-bu|es-c|es-ca|es-cb|es-cc|es-ce|es-cl|es-cm|es-cn|es-co|es-cr|es-cs|es-ct|es-cu|es-ex|es-ga|es-gc|es-gi|es-gr|es-gu|es-h|es-hu|es-ib|es-j|es-l|es-le|es-lo|es-lu|es-m|es-ma|es-mc|es-md|es-ml|es-mu|es-na|es-nc|es-o|es-or|es-p|es-pm|es-po|es-pv|es-ri|es-s|es-sa|es-se|es-sg|es-so|es-ss|es-t|es-te|es-tf|es-to|es-v|es-va|es-vc|es-vi|es-z|es-za|et-aa|et-af|et-am|et-be|et-dd|et-ga|et-ha|et-or|et-sn|et-so|et-ti|fi-01|fi-02|fi-03|fi-04|fi-05|fi-06|fi-07|fi-08|fi-09|fi-10|fi-11|fi-12|fi-13|fi-14|fi-15|fi-16|fi-17|fi-18|fi-19|fj-c|fj-e|fj-n|fj-r|fj-w|fm-ksa|fm-pni|fm-trk|fm-yap|fr-01|fr-02|fr-03|fr-04|fr-05|fr-06|fr-07|fr-08|fr-09|fr-10|fr-11|fr-12|fr-13|fr-14|fr-15|fr-16|fr-17|fr-18|fr-19|fr-21|fr-22|fr-23|fr-24|fr-25|fr-26|fr-27|fr-28|fr-29|fr-2a|fr-2b|fr-30|fr-31|fr-32|fr-33|fr-34|fr-35|fr-36|fr-37|fr-38|fr-39|fr-40|fr-41|fr-42|fr-43|fr-44|fr-45|fr-46|fr-47|fr-48|fr-49|fr-50|fr-51|fr-52|fr-53|fr-54|fr-55|fr-56|fr-57|fr-58|fr-59|fr-60|fr-61|fr-62|fr-63|fr-64|fr-65|fr-66|fr-67|fr-68|fr-69|fr-70|fr-71|fr-72|fr-73|fr-74|fr-75|fr-76|fr-77|fr-78|fr-79|fr-80|fr-81|fr-82|fr-83|fr-84|fr-85|fr-86|fr-87|fr-88|fr-89|fr-90|fr-91|fr-92|fr-93|fr-94|fr-95|fr-ara|fr-bfc|fr-bl|fr-bre|fr-cor|fr-cp|fr-cvl|fr-ges|fr-gf|fr-gp|fr-gua|fr-hdf|fr-idf|fr-lre|fr-may|fr-mf|fr-mq|fr-naq|fr-nc|fr-nor|fr-occ|fr-pac|fr-pdl|fr-pf|fr-pm|fr-re|fr-tf|fr-wf|fr-yt|ga-1|ga-2|ga-3|ga-4|ga-5|ga-6|ga-7|ga-8|ga-9|gb-abc|gb-abd|gb-abe|gb-agb|gb-agy|gb-and|gb-ann|gb-ans|gb-bas|gb-bbd|gb-bdf|gb-bdg|gb-ben|gb-bex|gb-bfs|gb-bge|gb-bgw|gb-bir|gb-bkm|gb-bmh|gb-bne|gb-bnh|gb-bns|gb-bol|gb-bpl|gb-brc|gb-brd|gb-bry|gb-bst|gb-bur|gb-cam|gb-cay|gb-cbf|gb-ccg|gb-cgn|gb-che|gb-chw|gb-cld|gb-clk|gb-cma|gb-cmd|gb-cmn|gb-con|gb-cov|gb-crf|gb-cry|gb-cwy|gb-dal|gb-dby|gb-den|gb-der|gb-dev|gb-dgy|gb-dnc|gb-dnd|gb-dor|gb-drs|gb-dud|gb-dur|gb-eal|gb-eaw|gb-eay|gb-edh|gb-edu|gb-eln|gb-els|gb-enf|gb-eng|gb-erw|gb-ery|gb-ess|gb-esx|gb-fal|gb-fif|gb-fln|gb-fmo|gb-gat|gb-gbn|gb-glg|gb-gls|gb-gre|gb-gwn|gb-hal|gb-ham|gb-hav|gb-hck|gb-hef|gb-hil|gb-hld|gb-hmf|gb-hns|gb-hpl|gb-hrt|gb-hrw|gb-hry|gb-ios|gb-iow|gb-isl|gb-ivc|gb-kec|gb-ken|gb-khl|gb-kir|gb-ktt|gb-kwl|gb-lan|gb-lbc|gb-lbh|gb-lce|gb-lds|gb-lec|gb-lew|gb-lin|gb-liv|gb-lnd|gb-lut|gb-man|gb-mdb|gb-mdw|gb-mea|gb-mik|gb-mln|gb-mon|gb-mrt|gb-mry|gb-mty|gb-mul|gb-nay|gb-nbl|gb-nel|gb-net|gb-nfk|gb-ngm|gb-nir|gb-nlk|gb-nln|gb-nmd|gb-nsm|gb-nth|gb-ntl|gb-ntt|gb-nty|gb-nwm|gb-nwp|gb-nyk|gb-old|gb-ork|gb-oxf|gb-pem|gb-pkn|gb-ply|gb-pol|gb-por|gb-pow|gb-pte|gb-rcc|gb-rch|gb-rct|gb-rdb|gb-rdg|gb-rfw|gb-ric|gb-rot|gb-rut|gb-saw|gb-say|gb-scb|gb-sct|gb-sfk|gb-sft|gb-sgc|gb-shf|gb-shn|gb-shr|gb-skp|gb-slf|gb-slg|gb-slk|gb-snd|gb-sol|gb-som|gb-sos|gb-sry|gb-ste|gb-stg|gb-sth|gb-stn|gb-sts|gb-stt|gb-sty|gb-swa|gb-swd|gb-swk|gb-tam|gb-tfw|gb-thr|gb-tob|gb-tof|gb-trf|gb-twh|gb-ukm|gb-vgl|gb-war|gb-wbk|gb-wdu|gb-wft|gb-wgn|gb-wil|gb-wkf|gb-wll|gb-wln|gb-wls|gb-wlv|gb-wnd|gb-wnm|gb-wok|gb-wor|gb-wrl|gb-wrt|gb-wrx|gb-wsm|gb-wsx|gb-yor|gb-zet|gd-01|gd-02|gd-03|gd-04|gd-05|gd-06|gd-10|ge-ab|ge-aj|ge-gu|ge-im|ge-ka|ge-kk|ge-mm|ge-rl|ge-sj|ge-sk|ge-sz|ge-tb|gh-aa|gh-ah|gh-ba|gh-cp|gh-ep|gh-np|gh-tv|gh-ue|gh-uw|gh-wp|gl-ku|gl-qa|gl-qe|gl-sm|gm-b|gm-l|gm-m|gm-n|gm-u|gm-w|gn-b|gn-be|gn-bf|gn-bk|gn-c|gn-co|gn-d|gn-db|gn-di|gn-dl|gn-du|gn-f|gn-fa|gn-fo|gn-fr|gn-ga|gn-gu|gn-k|gn-ka|gn-kb|gn-kd|gn-ke|gn-kn|gn-ko|gn-ks|gn-l|gn-la|gn-le|gn-lo|gn-m|gn-mc|gn-md|gn-ml|gn-mm|gn-n|gn-nz|gn-pi|gn-si|gn-te|gn-to|gn-yo|gq-an|gq-bn|gq-bs|gq-c|gq-cs|gq-i|gq-kn|gq-li|gq-wn|gr-01|gr-03|gr-04|gr-05|gr-06|gr-07|gr-11|gr-12|gr-13|gr-14|gr-15|gr-16|gr-17|gr-21|gr-22|gr-23|gr-24|gr-31|gr-32|gr-33|gr-34|gr-41|gr-42|gr-43|gr-44|gr-51|gr-52|gr-53|gr-54|gr-55|gr-56|gr-57|gr-58|gr-59|gr-61|gr-62|gr-63|gr-64|gr-69|gr-71|gr-72|gr-73|gr-81|gr-82|gr-83|gr-84|gr-85|gr-91|gr-92|gr-93|gr-94|gr-a|gr-a1|gr-b|gr-c|gr-d|gr-e|gr-f|gr-g|gr-h|gr-i|gr-j|gr-k|gr-l|gr-m|gt-av|gt-bv|gt-cm|gt-cq|gt-es|gt-gu|gt-hu|gt-iz|gt-ja|gt-ju|gt-pe|gt-pr|gt-qc|gt-qz|gt-re|gt-sa|gt-sm|gt-so|gt-sr|gt-su|gt-to|gt-za|gw-ba|gw-bl|gw-bm|gw-bs|gw-ca|gw-ga|gw-l|gw-n|gw-oi|gw-qu|gw-s|gw-to|gy-ba|gy-cu|gy-de|gy-eb|gy-es|gy-ma|gy-pm|gy-pt|gy-ud|gy-ut|hn-at|hn-ch|hn-cl|hn-cm|hn-cp|hn-cr|hn-ep|hn-fm|hn-gd|hn-ib|hn-in|hn-le|hn-lp|hn-oc|hn-ol|hn-sb|hn-va|hn-yo|hr-01|hr-02|hr-03|hr-04|hr-05|hr-06|hr-07|hr-08|hr-09|hr-10|hr-11|hr-12|hr-13|hr-14|hr-15|hr-16|hr-17|hr-18|hr-19|hr-20|hr-21|ht-ar|ht-ce|ht-ga|ht-nd|ht-ne|ht-no|ht-ou|ht-sd|ht-se|hu-ba|hu-bc|hu-be|hu-bk|hu-bu|hu-bz|hu-cs|hu-de|hu-du|hu-eg|hu-er|hu-fe|hu-gs|hu-gy|hu-hb|hu-he|hu-hv|hu-jn|hu-ke|hu-km|hu-kv|hu-mi|hu-nk|hu-no|hu-ny|hu-pe|hu-ps|hu-sd|hu-sf|hu-sh|hu-sk|hu-sn|hu-so|hu-ss|hu-st|hu-sz|hu-tb|hu-to|hu-va|hu-ve|hu-vm|hu-za|hu-ze|id-ac|id-ba|id-bb|id-be|id-bt|id-go|id-ij|id-ja|id-jb|id-ji|id-jk|id-jt|id-jw|id-ka|id-kb|id-ki|id-kr|id-ks|id-kt|id-la|id-ma|id-ml|id-mu|id-nb|id-nt|id-nu|id-pa|id-pb|id-ri|id-sa|id-sb|id-sg|id-sl|id-sm|id-sn|id-sr|id-ss|id-st|id-su|id-yo|ie-c|ie-ce|ie-cn|ie-co|ie-cw|ie-d|ie-dl|ie-g|ie-ke|ie-kk|ie-ky|ie-l|ie-ld|ie-lh|ie-lk|ie-lm|ie-ls|ie-m|ie-mh|ie-mn|ie-mo|ie-oy|ie-rn|ie-so|ie-ta|ie-u|ie-wd|ie-wh|ie-ww|ie-wx|il-d|il-ha|il-jm|il-m|il-ta|il-z|in-an|in-ap|in-ar|in-as|in-br|in-ch|in-ct|in-dd|in-dl|in-dn|in-ga|in-gj|in-hp|in-hr|in-jh|in-jk|in-ka|in-kl|in-ld|in-mh|in-ml|in-mn|in-mp|in-mz|in-nl|in-or|in-pb|in-py|in-rj|in-sk|in-tg|in-tn|in-tr|in-up|in-ut|in-wb|iq-an|iq-ar|iq-ba|iq-bb|iq-bg|iq-da|iq-di|iq-dq|iq-ka|iq-ma|iq-mu|iq-na|iq-ni|iq-qa|iq-sd|iq-sw|iq-ts|iq-wa|ir-01|ir-02|ir-03|ir-04|ir-05|ir-06|ir-07|ir-08|ir-10|ir-11|ir-12|ir-13|ir-14|ir-15|ir-16|ir-17|ir-18|ir-19|ir-20|ir-21|ir-22|ir-23|ir-24|ir-25|ir-26|ir-27|ir-28|ir-29|ir-30|ir-31|is-0|is-1|is-2|is-3|is-4|is-5|is-6|is-7|is-8|it-21|it-23|it-25|it-32|it-34|it-36|it-42|it-45|it-52|it-55|it-57|it-62|it-65|it-67|it-72|it-75|it-77|it-78|it-82|it-88|it-ag|it-al|it-an|it-ao|it-ap|it-aq|it-ar|it-at|it-av|it-ba|it-bg|it-bi|it-bl|it-bn|it-bo|it-br|it-bs|it-bt|it-bz|it-ca|it-cb|it-ce|it-ch|it-ci|it-cl|it-cn|it-co|it-cr|it-cs|it-ct|it-cz|it-en|it-fc|it-fe|it-fg|it-fi|it-fm|it-fr|it-ge|it-go|it-gr|it-im|it-is|it-kr|it-lc|it-le|it-li|it-lo|it-lt|it-lu|it-mb|it-mc|it-me|it-mi|it-mn|it-mo|it-ms|it-mt|it-na|it-no|it-nu|it-og|it-or|it-ot|it-pa|it-pc|it-pd|it-pe|it-pg|it-pi|it-pn|it-po|it-pr|it-pt|it-pu|it-pv|it-pz|it-ra|it-rc|it-re|it-rg|it-ri|it-rm|it-rn|it-ro|it-sa|it-si|it-so|it-sp|it-sr|it-ss|it-sv|it-ta|it-te|it-tn|it-to|it-tp|it-tr|it-ts|it-tv|it-ud|it-va|it-vb|it-vc|it-ve|it-vi|it-vr|it-vs|it-vt|it-vv|jm-01|jm-02|jm-03|jm-04|jm-05|jm-06|jm-07|jm-08|jm-09|jm-10|jm-11|jm-12|jm-13|jm-14|jo-aj|jo-am|jo-aq|jo-at|jo-az|jo-ba|jo-ir|jo-ja|jo-ka|jo-ma|jo-md|jo-mn|jp-01|jp-02|jp-03|jp-04|jp-05|jp-06|jp-07|jp-08|jp-09|jp-10|jp-11|jp-12|jp-13|jp-14|jp-15|jp-16|jp-17|jp-18|jp-19|jp-20|jp-21|jp-22|jp-23|jp-24|jp-25|jp-26|jp-27|jp-28|jp-29|jp-30|jp-31|jp-32|jp-33|jp-34|jp-35|jp-36|jp-37|jp-38|jp-39|jp-40|jp-41|jp-42|jp-43|jp-44|jp-45|jp-46|jp-47|ke-01|ke-02|ke-03|ke-04|ke-05|ke-06|ke-07|ke-08|ke-09|ke-10|ke-11|ke-12|ke-13|ke-14|ke-15|ke-16|ke-17|ke-18|ke-19|ke-20|ke-21|ke-22|ke-23|ke-24|ke-25|ke-26|ke-27|ke-28|ke-29|ke-30|ke-31|ke-32|ke-33|ke-34|ke-35|ke-36|ke-37|ke-38|ke-39|ke-40|ke-41|ke-42|ke-43|ke-44|ke-45|ke-46|ke-47|kg-b|kg-c|kg-gb|kg-j|kg-n|kg-o|kg-t|kg-y|kh-1|kh-10|kh-11|kh-12|kh-13|kh-14|kh-15|kh-16|kh-17|kh-18|kh-19|kh-2|kh-20|kh-21|kh-22|kh-23|kh-24|kh-3|kh-4|kh-5|kh-6|kh-7|kh-8|kh-9|ki-g|ki-l|ki-p|km-a|km-g|km-m|kn-01|kn-02|kn-03|kn-04|kn-05|kn-06|kn-07|kn-08|kn-09|kn-10|kn-11|kn-12|kn-13|kn-15|kn-k|kn-n|kp-01|kp-02|kp-03|kp-04|kp-05|kp-06|kp-07|kp-08|kp-09|kp-10|kp-13|kr-11|kr-26|kr-27|kr-28|kr-29|kr-30|kr-31|kr-41|kr-42|kr-43|kr-44|kr-45|kr-46|kr-47|kr-48|kr-49|kw-ah|kw-fa|kw-ha|kw-ja|kw-ku|kw-mu|kz-akm|kz-akt|kz-ala|kz-alm|kz-ast|kz-aty|kz-kar|kz-kus|kz-kzy|kz-man|kz-pav|kz-sev|kz-vos|kz-yuz|kz-zap|kz-zha|la-at|la-bk|la-bl|la-ch|la-ho|la-kh|la-lm|la-lp|la-ou|la-ph|la-sl|la-sv|la-vi|la-vt|la-xa|la-xe|la-xi|la-xs|lb-ak|lb-as|lb-ba|lb-bh|lb-bi|lb-ja|lb-jl|lb-na|li-01|li-02|li-03|li-04|li-05|li-06|li-07|li-08|li-09|li-10|li-11|lk-1|lk-11|lk-12|lk-13|lk-2|lk-21|lk-22|lk-23|lk-3|lk-31|lk-32|lk-33|lk-4|lk-41|lk-42|lk-43|lk-44|lk-45|lk-5|lk-51|lk-52|lk-53|lk-6|lk-61|lk-62|lk-7|lk-71|lk-72|lk-8|lk-81|lk-82|lk-9|lk-91|lk-92|lr-bg|lr-bm|lr-cm|lr-gb|lr-gg|lr-gk|lr-lo|lr-mg|lr-mo|lr-my|lr-ni|lr-ri|lr-si|ls-a|ls-b|ls-c|ls-d|ls-e|ls-f|ls-g|ls-h|ls-j|ls-k|lt-al|lt-kl|lt-ku|lt-mr|lt-pn|lt-sa|lt-ta|lt-te|lt-ut|lt-vl|lu-d|lu-g|lu-l|lv-001|lv-002|lv-003|lv-004|lv-005|lv-006|lv-007|lv-008|lv-009|lv-010|lv-011|lv-012|lv-013|lv-014|lv-015|lv-016|lv-017|lv-018|lv-019|lv-020|lv-021|lv-022|lv-023|lv-024|lv-025|lv-026|lv-027|lv-028|lv-029|lv-030|lv-031|lv-032|lv-033|lv-034|lv-035|lv-036|lv-037|lv-038|lv-039|lv-040|lv-041|lv-042|lv-043|lv-044|lv-045|lv-046|lv-047|lv-048|lv-049|lv-050|lv-051|lv-052|lv-053|lv-054|lv-055|lv-056|lv-057|lv-058|lv-059|lv-060|lv-061|lv-062|lv-063|lv-064|lv-065|lv-066|lv-067|lv-068|lv-069|lv-070|lv-071|lv-072|lv-073|lv-074|lv-075|lv-076|lv-077|lv-078|lv-079|lv-080|lv-081|lv-082|lv-083|lv-084|lv-085|lv-086|lv-087|lv-088|lv-089|lv-090|lv-091|lv-092|lv-093|lv-094|lv-095|lv-096|lv-097|lv-098|lv-099|lv-100|lv-101|lv-102|lv-103|lv-104|lv-105|lv-106|lv-107|lv-108|lv-109|lv-110|lv-dgv|lv-jel|lv-jkb|lv-jur|lv-lpx|lv-rez|lv-rix|lv-ven|lv-vmr|ly-ba|ly-bu|ly-dr|ly-gt|ly-ja|ly-jb|ly-jg|ly-ji|ly-ju|ly-kf|ly-mb|ly-mi|ly-mj|ly-mq|ly-nl|ly-nq|ly-sb|ly-sr|ly-tb|ly-wa|ly-wd|ly-ws|ly-za|ma-01|ma-02|ma-03|ma-04|ma-05|ma-06|ma-07|ma-08|ma-09|ma-10|ma-11|ma-12|ma-agd|ma-aou|ma-asz|ma-azi|ma-bem|ma-ber|ma-bes|ma-bod|ma-bom|ma-brr|ma-cas|ma-che|ma-chi|ma-cht|ma-dri|ma-err|ma-esi|ma-esm|ma-fah|ma-fes|ma-fig|ma-fqh|ma-gue|ma-guf|ma-haj|ma-hao|ma-hoc|ma-ifr|ma-ine|ma-jdi|ma-jra|ma-ken|ma-kes|ma-khe|ma-khn|ma-kho|ma-laa|ma-lar|ma-mar|ma-mdf|ma-med|ma-mek|ma-mid|ma-moh|ma-mou|ma-nad|ma-nou|ma-oua|ma-oud|ma-ouj|ma-ouz|ma-rab|ma-reh|ma-saf|ma-sal|ma-sef|ma-set|ma-sib|ma-sif|ma-sik|ma-sil|ma-skh|ma-taf|ma-tai|ma-tao|ma-tar|ma-tat|ma-taz|ma-tet|ma-tin|ma-tiz|ma-tng|ma-tnt|ma-yus|ma-zag|mc-cl|mc-co|mc-fo|mc-ga|mc-je|mc-la|mc-ma|mc-mc|mc-mg|mc-mo|mc-mu|mc-ph|mc-sd|mc-so|mc-sp|mc-sr|mc-vr|md-an|md-ba|md-bd|md-br|md-bs|md-ca|md-cl|md-cm|md-cr|md-cs|md-ct|md-cu|md-do|md-dr|md-du|md-ed|md-fa|md-fl|md-ga|md-gl|md-hi|md-ia|md-le|md-ni|md-oc|md-or|md-re|md-ri|md-sd|md-si|md-sn|md-so|md-st|md-sv|md-ta|md-te|md-un|me-01|me-02|me-03|me-04|me-05|me-06|me-07|me-08|me-09|me-10|me-11|me-12|me-13|me-14|me-15|me-16|me-17|me-18|me-19|me-20|me-21|mg-a|mg-d|mg-f|mg-m|mg-t|mg-u|mh-alk|mh-all|mh-arn|mh-aur|mh-ebo|mh-eni|mh-jab|mh-jal|mh-kil|mh-kwa|mh-l|mh-lae|mh-lib|mh-lik|mh-maj|mh-mal|mh-mej|mh-mil|mh-nmk|mh-nmu|mh-ron|mh-t|mh-uja|mh-uti|mh-wtj|mh-wtn|mk-01|mk-02|mk-03|mk-04|mk-05|mk-06|mk-07|mk-08|mk-09|mk-10|mk-11|mk-12|mk-13|mk-14|mk-15|mk-16|mk-17|mk-18|mk-19|mk-20|mk-21|mk-22|mk-23|mk-24|mk-25|mk-26|mk-27|mk-28|mk-29|mk-30|mk-31|mk-32|mk-33|mk-34|mk-35|mk-36|mk-37|mk-38|mk-39|mk-40|mk-41|mk-42|mk-43|mk-44|mk-45|mk-46|mk-47|mk-48|mk-49|mk-50|mk-51|mk-52|mk-53|mk-54|mk-55|mk-56|mk-57|mk-58|mk-59|mk-60|mk-61|mk-62|mk-63|mk-64|mk-65|mk-66|mk-67|mk-68|mk-69|mk-70|mk-71|mk-72|mk-73|mk-74|mk-75|mk-76|mk-77|mk-78|mk-79|mk-80|mk-81|mk-82|mk-83|mk-84|ml-1|ml-2|ml-3|ml-4|ml-5|ml-6|ml-7|ml-8|ml-bk0|mm-01|mm-02|mm-03|mm-04|mm-05|mm-06|mm-07|mm-11|mm-12|mm-13|mm-14|mm-15|mm-16|mm-17|mn-035|mn-037|mn-039|mn-041|mn-043|mn-046|mn-047|mn-049|mn-051|mn-053|mn-055|mn-057|mn-059|mn-061|mn-063|mn-064|mn-065|mn-067|mn-069|mn-071|mn-073|mn-1|mr-01|mr-02|mr-03|mr-04|mr-05|mr-06|mr-07|mr-08|mr-09|mr-10|mr-11|mr-12|mr-nkc|mt-01|mt-02|mt-03|mt-04|mt-05|mt-06|mt-07|mt-08|mt-09|mt-10|mt-11|mt-12|mt-13|mt-14|mt-15|mt-16|mt-17|mt-18|mt-19|mt-20|mt-21|mt-22|mt-23|mt-24|mt-25|mt-26|mt-27|mt-28|mt-29|mt-30|mt-31|mt-32|mt-33|mt-34|mt-35|mt-36|mt-37|mt-38|mt-39|mt-40|mt-41|mt-42|mt-43|mt-44|mt-45|mt-46|mt-47|mt-48|mt-49|mt-50|mt-51|mt-52|mt-53|mt-54|mt-55|mt-56|mt-57|mt-58|mt-59|mt-60|mt-61|mt-62|mt-63|mt-64|mt-65|mt-66|mt-67|mt-68|mu-ag|mu-bl|mu-br|mu-cc|mu-cu|mu-fl|mu-gp|mu-mo|mu-pa|mu-pl|mu-pu|mu-pw|mu-qb|mu-ro|mu-rp|mu-sa|mu-vp|mv-00|mv-01|mv-02|mv-03|mv-04|mv-05|mv-07|mv-08|mv-12|mv-13|mv-14|mv-17|mv-20|mv-23|mv-24|mv-25|mv-26|mv-27|mv-28|mv-29|mv-ce|mv-mle|mv-nc|mv-no|mv-sc|mv-su|mv-un|mv-us|mw-ba|mw-bl|mw-c|mw-ck|mw-cr|mw-ct|mw-de|mw-do|mw-kr|mw-ks|mw-li|mw-lk|mw-mc|mw-mg|mw-mh|mw-mu|mw-mw|mw-mz|mw-n|mw-nb|mw-ne|mw-ni|mw-nk|mw-ns|mw-nu|mw-ph|mw-ru|mw-s|mw-sa|mw-th|mw-zo|mx-agu|mx-bcn|mx-bcs|mx-cam|mx-chh|mx-chp|mx-cmx|mx-coa|mx-col|mx-dur|mx-gro|mx-gua|mx-hid|mx-jal|mx-mex|mx-mic|mx-mor|mx-nay|mx-nle|mx-oax|mx-pue|mx-que|mx-roo|mx-sin|mx-slp|mx-son|mx-tab|mx-tam|mx-tla|mx-ver|mx-yuc|mx-zac|my-01|my-02|my-03|my-04|my-05|my-06|my-07|my-08|my-09|my-10|my-11|my-12|my-13|my-14|my-15|my-16|mz-a|mz-b|mz-g|mz-i|mz-l|mz-mpm|mz-n|mz-p|mz-q|mz-s|mz-t|na-ca|na-er|na-ha|na-ka|na-kh|na-ku|na-od|na-oh|na-ok|na-on|na-os|na-ot|na-ow|ne-1|ne-2|ne-3|ne-4|ne-5|ne-6|ne-7|ne-8|ng-ab|ng-ad|ng-ak|ng-an|ng-ba|ng-be|ng-bo|ng-by|ng-cr|ng-de|ng-eb|ng-ed|ng-ek|ng-en|ng-fc|ng-go|ng-im|ng-ji|ng-kd|ng-ke|ng-kn|ng-ko|ng-kt|ng-kw|ng-la|ng-na|ng-ni|ng-og|ng-on|ng-os|ng-oy|ng-pl|ng-ri|ng-so|ng-ta|ng-yo|ng-za|ni-an|ni-as|ni-bo|ni-ca|ni-ci|ni-co|ni-es|ni-gr|ni-ji|ni-le|ni-md|ni-mn|ni-ms|ni-mt|ni-ns|ni-ri|ni-sj|nl-aw|nl-bq1|nl-bq2|nl-bq3|nl-cw|nl-dr|nl-fl|nl-fr|nl-ge|nl-gr|nl-li|nl-nb|nl-nh|nl-ov|nl-sx|nl-ut|nl-ze|nl-zh|no-01|no-02|no-03|no-04|no-05|no-06|no-07|no-08|no-09|no-10|no-11|no-12|no-14|no-15|no-18|no-19|no-20|no-21|no-22|no-50|np-1|np-2|np-3|np-4|np-5|np-ba|np-bh|np-dh|np-ga|np-ja|np-ka|np-ko|np-lu|np-ma|np-me|np-na|np-ra|np-sa|np-se|nr-01|nr-02|nr-03|nr-04|nr-05|nr-06|nr-07|nr-08|nr-09|nr-10|nr-11|nr-12|nr-13|nr-14|nz-auk|nz-bop|nz-can|nz-cit|nz-gis|nz-hkb|nz-mbh|nz-mwt|nz-n|nz-nsn|nz-ntl|nz-ota|nz-s|nz-stl|nz-tas|nz-tki|nz-wgn|nz-wko|nz-wtc|om-ba|om-bu|om-da|om-ma|om-mu|om-sh|om-wu|om-za|om-zu|pa-1|pa-2|pa-3|pa-4|pa-5|pa-6|pa-7|pa-8|pa-9|pa-em|pa-ky|pa-nb|pe-ama|pe-anc|pe-apu|pe-are|pe-aya|pe-caj|pe-cal|pe-cus|pe-huc|pe-huv|pe-ica|pe-jun|pe-lal|pe-lam|pe-lim|pe-lma|pe-lor|pe-mdd|pe-moq|pe-pas|pe-piu|pe-pun|pe-sam|pe-tac|pe-tum|pe-uca|pg-cpk|pg-cpm|pg-ebr|pg-ehg|pg-epw|pg-esw|pg-gpk|pg-mba|pg-mpl|pg-mpm|pg-mrl|pg-ncd|pg-nik|pg-npp|pg-nsb|pg-san|pg-shm|pg-wbk|pg-whm|pg-wpd|ph-00|ph-01|ph-02|ph-03|ph-05|ph-06|ph-07|ph-08|ph-09|ph-10|ph-11|ph-12|ph-13|ph-14|ph-15|ph-40|ph-41|ph-abr|ph-agn|ph-ags|ph-akl|ph-alb|ph-ant|ph-apa|ph-aur|ph-ban|ph-bas|ph-ben|ph-bil|ph-boh|ph-btg|ph-btn|ph-buk|ph-bul|ph-cag|ph-cam|ph-can|ph-cap|ph-cas|ph-cat|ph-cav|ph-ceb|ph-com|ph-dao|ph-das|ph-dav|ph-din|ph-eas|ph-gui|ph-ifu|ph-ili|ph-iln|ph-ils|ph-isa|ph-kal|ph-lag|ph-lan|ph-las|ph-ley|ph-lun|ph-mad|ph-mag|ph-mas|ph-mdc|ph-mdr|ph-mou|ph-msc|ph-msr|ph-nco|ph-nec|ph-ner|ph-nsa|ph-nue|ph-nuv|ph-pam|ph-pan|ph-plw|ph-que|ph-qui|ph-riz|ph-rom|ph-sar|ph-sco|ph-sig|ph-sle|ph-slu|ph-sor|ph-suk|ph-sun|ph-sur|ph-tar|ph-taw|ph-wsa|ph-zan|ph-zas|ph-zmb|ph-zsi|pk-ba|pk-gb|pk-is|pk-jk|pk-kp|pk-pb|pk-sd|pk-ta|pl-ds|pl-kp|pl-lb|pl-ld|pl-lu|pl-ma|pl-mz|pl-op|pl-pd|pl-pk|pl-pm|pl-sk|pl-sl|pl-wn|pl-wp|pl-zp|ps-bth|ps-deb|ps-gza|ps-hbn|ps-jem|ps-jen|ps-jrh|ps-kys|ps-nbs|ps-ngz|ps-qqa|ps-rbh|ps-rfh|ps-slt|ps-tbs|ps-tkm|pt-01|pt-02|pt-03|pt-04|pt-05|pt-06|pt-07|pt-08|pt-09|pt-10|pt-11|pt-12|pt-13|pt-14|pt-15|pt-16|pt-17|pt-18|pt-20|pt-30|pw-002|pw-004|pw-010|pw-050|pw-100|pw-150|pw-212|pw-214|pw-218|pw-222|pw-224|pw-226|pw-227|pw-228|pw-350|pw-370|py-1|py-10|py-11|py-12|py-13|py-14|py-15|py-16|py-19|py-2|py-3|py-4|py-5|py-6|py-7|py-8|py-9|py-asu|qa-da|qa-kh|qa-ms|qa-ra|qa-us|qa-wa|qa-za|ro-ab|ro-ag|ro-ar|ro-b|ro-bc|ro-bh|ro-bn|ro-br|ro-bt|ro-bv|ro-bz|ro-cj|ro-cl|ro-cs|ro-ct|ro-cv|ro-db|ro-dj|ro-gj|ro-gl|ro-gr|ro-hd|ro-hr|ro-if|ro-il|ro-is|ro-mh|ro-mm|ro-ms|ro-nt|ro-ot|ro-ph|ro-sb|ro-sj|ro-sm|ro-sv|ro-tl|ro-tm|ro-tr|ro-vl|ro-vn|ro-vs|rs-00|rs-01|rs-02|rs-03|rs-04|rs-05|rs-06|rs-07|rs-08|rs-09|rs-10|rs-11|rs-12|rs-13|rs-14|rs-15|rs-16|rs-17|rs-18|rs-19|rs-20|rs-21|rs-22|rs-23|rs-24|rs-25|rs-26|rs-27|rs-28|rs-29|rs-km|rs-vo|ru-ad|ru-al|ru-alt|ru-amu|ru-ark|ru-ast|ru-ba|ru-bel|ru-bry|ru-bu|ru-ce|ru-che|ru-chu|ru-cu|ru-da|ru-in|ru-irk|ru-iva|ru-kam|ru-kb|ru-kc|ru-kda|ru-kem|ru-kgd|ru-kgn|ru-kha|ru-khm|ru-kir|ru-kk|ru-kl|ru-klu|ru-ko|ru-kos|ru-kr|ru-krs|ru-kya|ru-len|ru-lip|ru-mag|ru-me|ru-mo|ru-mos|ru-mow|ru-mur|ru-nen|ru-ngr|ru-niz|ru-nvs|ru-oms|ru-ore|ru-orl|ru-per|ru-pnz|ru-pri|ru-psk|ru-ros|ru-rya|ru-sa|ru-sak|ru-sam|ru-sar|ru-se|ru-smo|ru-spe|ru-sta|ru-sve|ru-ta|ru-tam|ru-tom|ru-tul|ru-tve|ru-ty|ru-tyu|ru-ud|ru-uly|ru-vgg|ru-vla|ru-vlg|ru-vor|ru-yan|ru-yar|ru-yev|ru-zab|rw-01|rw-02|rw-03|rw-04|rw-05|sa-01|sa-02|sa-03|sa-04|sa-05|sa-06|sa-07|sa-08|sa-09|sa-10|sa-11|sa-12|sa-14|sb-ce|sb-ch|sb-ct|sb-gu|sb-is|sb-mk|sb-ml|sb-rb|sb-te|sb-we|sc-01|sc-02|sc-03|sc-04|sc-05|sc-06|sc-07|sc-08|sc-09|sc-10|sc-11|sc-12|sc-13|sc-14|sc-15|sc-16|sc-17|sc-18|sc-19|sc-20|sc-21|sc-22|sc-23|sc-24|sc-25|sd-dc|sd-de|sd-dn|sd-ds|sd-dw|sd-gd|sd-gz|sd-ka|sd-kh|sd-kn|sd-ks|sd-nb|sd-no|sd-nr|sd-nw|sd-rs|sd-si|se-ab|se-ac|se-bd|se-c|se-d|se-e|se-f|se-g|se-h|se-i|se-k|se-m|se-n|se-o|se-s|se-t|se-u|se-w|se-x|se-y|se-z|sg-01|sg-02|sg-03|sg-04|sg-05|sh-ac|sh-hl|sh-ta|si-001|si-002|si-003|si-004|si-005|si-006|si-007|si-008|si-009|si-010|si-011|si-012|si-013|si-014|si-015|si-016|si-017|si-018|si-019|si-020|si-021|si-022|si-023|si-024|si-025|si-026|si-027|si-028|si-029|si-030|si-031|si-032|si-033|si-034|si-035|si-036|si-037|si-038|si-039|si-040|si-041|si-042|si-043|si-044|si-045|si-046|si-047|si-048|si-049|si-050|si-051|si-052|si-053|si-054|si-055|si-056|si-057|si-058|si-059|si-060|si-061|si-062|si-063|si-064|si-065|si-066|si-067|si-068|si-069|si-070|si-071|si-072|si-073|si-074|si-075|si-076|si-077|si-078|si-079|si-080|si-081|si-082|si-083|si-084|si-085|si-086|si-087|si-088|si-089|si-090|si-091|si-092|si-093|si-094|si-095|si-096|si-097|si-098|si-099|si-100|si-101|si-102|si-103|si-104|si-105|si-106|si-107|si-108|si-109|si-110|si-111|si-112|si-113|si-114|si-115|si-116|si-117|si-118|si-119|si-120|si-121|si-122|si-123|si-124|si-125|si-126|si-127|si-128|si-129|si-130|si-131|si-132|si-133|si-134|si-135|si-136|si-137|si-138|si-139|si-140|si-141|si-142|si-143|si-144|si-146|si-147|si-148|si-149|si-150|si-151|si-152|si-153|si-154|si-155|si-156|si-157|si-158|si-159|si-160|si-161|si-162|si-163|si-164|si-165|si-166|si-167|si-168|si-169|si-170|si-171|si-172|si-173|si-174|si-175|si-176|si-177|si-178|si-179|si-180|si-181|si-182|si-183|si-184|si-185|si-186|si-187|si-188|si-189|si-190|si-191|si-192|si-193|si-194|si-195|si-196|si-197|si-198|si-199|si-200|si-201|si-202|si-203|si-204|si-205|si-206|si-207|si-208|si-209|si-210|si-211|sk-bc|sk-bl|sk-ki|sk-ni|sk-pv|sk-ta|sk-tc|sk-zi|sl-e|sl-n|sl-s|sl-w|sm-01|sm-02|sm-03|sm-04|sm-05|sm-06|sm-07|sm-08|sm-09|sn-db|sn-dk|sn-fk|sn-ka|sn-kd|sn-ke|sn-kl|sn-lg|sn-mt|sn-se|sn-sl|sn-tc|sn-th|sn-zg|so-aw|so-bk|so-bn|so-br|so-by|so-ga|so-ge|so-hi|so-jd|so-jh|so-mu|so-nu|so-sa|so-sd|so-sh|so-so|so-to|so-wo|sr-br|sr-cm|sr-cr|sr-ma|sr-ni|sr-pm|sr-pr|sr-sa|sr-si|sr-wa|ss-bn|ss-bw|ss-ec|ss-ee|ss-ew|ss-jg|ss-lk|ss-nu|ss-uy|ss-wr|st-p|st-s|sv-ah|sv-ca|sv-ch|sv-cu|sv-li|sv-mo|sv-pa|sv-sa|sv-sm|sv-so|sv-ss|sv-sv|sv-un|sv-us|sy-di|sy-dr|sy-dy|sy-ha|sy-hi|sy-hl|sy-hm|sy-id|sy-la|sy-qu|sy-ra|sy-rd|sy-su|sy-ta|sz-hh|sz-lu|sz-ma|sz-sh|td-ba|td-bg|td-bo|td-cb|td-en|td-gr|td-hl|td-ka|td-lc|td-lo|td-lr|td-ma|td-mc|td-me|td-mo|td-nd|td-od|td-sa|td-si|td-ta|td-ti|td-wf|tg-c|tg-k|tg-m|tg-p|tg-s|th-10|th-11|th-12|th-13|th-14|th-15|th-16|th-17|th-18|th-19|th-20|th-21|th-22|th-23|th-24|th-25|th-26|th-27|th-30|th-31|th-32|th-33|th-34|th-35|th-36|th-37|th-39|th-40|th-41|th-42|th-43|th-44|th-45|th-46|th-47|th-48|th-49|th-50|th-51|th-52|th-53|th-54|th-55|th-56|th-57|th-58|th-60|th-61|th-62|th-63|th-64|th-65|th-66|th-67|th-70|th-71|th-72|th-73|th-74|th-75|th-76|th-77|th-80|th-81|th-82|th-83|th-84|th-85|th-86|th-90|th-91|th-92|th-93|th-94|th-95|th-96|th-s|tj-gb|tj-kt|tj-su|tl-al|tl-an|tl-ba|tl-bo|tl-co|tl-di|tl-er|tl-la|tl-li|tl-mf|tl-mt|tl-oe|tl-vi|tm-a|tm-b|tm-d|tm-l|tm-m|tm-s|tn-11|tn-12|tn-13|tn-14|tn-21|tn-22|tn-23|tn-31|tn-32|tn-33|tn-34|tn-41|tn-42|tn-43|tn-51|tn-52|tn-53|tn-61|tn-71|tn-72|tn-73|tn-81|tn-82|tn-83|to-01|to-02|to-03|to-04|to-05|tr-01|tr-02|tr-03|tr-04|tr-05|tr-06|tr-07|tr-08|tr-09|tr-10|tr-11|tr-12|tr-13|tr-14|tr-15|tr-16|tr-17|tr-18|tr-19|tr-20|tr-21|tr-22|tr-23|tr-24|tr-25|tr-26|tr-27|tr-28|tr-29|tr-30|tr-31|tr-32|tr-33|tr-34|tr-35|tr-36|tr-37|tr-38|tr-39|tr-40|tr-41|tr-42|tr-43|tr-44|tr-45|tr-46|tr-47|tr-48|tr-49|tr-50|tr-51|tr-52|tr-53|tr-54|tr-55|tr-56|tr-57|tr-58|tr-59|tr-60|tr-61|tr-62|tr-63|tr-64|tr-65|tr-66|tr-67|tr-68|tr-69|tr-70|tr-71|tr-72|tr-73|tr-74|tr-75|tr-76|tr-77|tr-78|tr-79|tr-80|tr-81|tt-ari|tt-cha|tt-ctt|tt-dmn|tt-eto|tt-ped|tt-pos|tt-prt|tt-ptf|tt-rcm|tt-sfo|tt-sge|tt-sip|tt-sjl|tt-tup|tt-wto|tv-fun|tv-nit|tv-nkf|tv-nkl|tv-nma|tv-nmg|tv-nui|tv-vai|tw-cha|tw-cyi|tw-cyq|tw-hsq|tw-hsz|tw-hua|tw-ila|tw-kee|tw-khh|tw-khq|tw-mia|tw-nan|tw-pen|tw-pif|tw-tao|tw-tnn|tw-tnq|tw-tpe|tw-tpq|tw-ttt|tw-txg|tw-txq|tw-yun|tz-01|tz-02|tz-03|tz-04|tz-05|tz-06|tz-07|tz-08|tz-09|tz-10|tz-11|tz-12|tz-13|tz-14|tz-15|tz-16|tz-17|tz-18|tz-19|tz-20|tz-21|tz-22|tz-23|tz-24|tz-25|tz-26|ua-05|ua-07|ua-09|ua-12|ua-14|ua-18|ua-21|ua-23|ua-26|ua-30|ua-32|ua-35|ua-40|ua-43|ua-46|ua-48|ua-51|ua-53|ua-56|ua-59|ua-61|ua-63|ua-65|ua-68|ua-71|ua-74|ua-77|ug-101|ug-102|ug-103|ug-104|ug-105|ug-106|ug-107|ug-108|ug-109|ug-110|ug-111|ug-112|ug-113|ug-114|ug-115|ug-116|ug-201|ug-202|ug-203|ug-204|ug-205|ug-206|ug-207|ug-208|ug-209|ug-210|ug-211|ug-212|ug-213|ug-214|ug-215|ug-216|ug-217|ug-218|ug-219|ug-220|ug-221|ug-222|ug-223|ug-224|ug-301|ug-302|ug-303|ug-304|ug-305|ug-306|ug-307|ug-308|ug-309|ug-310|ug-311|ug-312|ug-313|ug-314|ug-315|ug-316|ug-317|ug-318|ug-319|ug-320|ug-321|ug-401|ug-402|ug-403|ug-404|ug-405|ug-406|ug-407|ug-408|ug-409|ug-410|ug-411|ug-412|ug-413|ug-414|ug-415|ug-416|ug-417|ug-418|ug-419|ug-c|ug-e|ug-n|ug-w|um-67|um-71|um-76|um-79|um-81|um-84|um-86|um-89|um-95|us-ak|us-al|us-ar|us-as|us-az|us-ca|us-co|us-ct|us-dc|us-de|us-fl|us-ga|us-gu|us-hi|us-ia|us-id|us-il|us-in|us-ks|us-ky|us-la|us-ma|us-md|us-me|us-mi|us-mn|us-mo|us-mp|us-ms|us-mt|us-nc|us-nd|us-ne|us-nh|us-nj|us-nm|us-nv|us-ny|us-oh|us-ok|us-or|us-pa|us-pr|us-ri|us-sc|us-sd|us-tn|us-tx|us-um|us-ut|us-va|us-vi|us-vt|us-wa|us-wi|us-wv|us-wy|uy-ar|uy-ca|uy-cl|uy-co|uy-du|uy-fd|uy-fs|uy-la|uy-ma|uy-mo|uy-pa|uy-rn|uy-ro|uy-rv|uy-sa|uy-sj|uy-so|uy-ta|uy-tt|uz-an|uz-bu|uz-fa|uz-ji|uz-ng|uz-nw|uz-qa|uz-qr|uz-sa|uz-si|uz-su|uz-tk|uz-to|uz-xo|vc-01|vc-02|vc-03|vc-04|vc-05|vc-06|ve-a|ve-b|ve-c|ve-d|ve-e|ve-f|ve-g|ve-h|ve-i|ve-j|ve-k|ve-l|ve-m|ve-n|ve-o|ve-p|ve-r|ve-s|ve-t|ve-u|ve-v|ve-w|ve-x|ve-y|ve-z|vn-01|vn-02|vn-03|vn-04|vn-05|vn-06|vn-07|vn-09|vn-13|vn-14|vn-15|vn-18|vn-20|vn-21|vn-22|vn-23|vn-24|vn-25|vn-26|vn-27|vn-28|vn-29|vn-30|vn-31|vn-32|vn-33|vn-34|vn-35|vn-36|vn-37|vn-39|vn-40|vn-41|vn-43|vn-44|vn-45|vn-46|vn-47|vn-49|vn-50|vn-51|vn-52|vn-53|vn-54|vn-55|vn-56|vn-57|vn-58|vn-59|vn-61|vn-63|vn-66|vn-67|vn-68|vn-69|vn-70|vn-71|vn-72|vn-73|vn-ct|vn-dn|vn-hn|vn-hp|vn-sg|vu-map|vu-pam|vu-sam|vu-see|vu-tae|vu-tob|ws-aa|ws-al|ws-at|ws-fa|ws-ge|ws-gi|ws-pa|ws-sa|ws-tu|ws-vf|ws-vs|ye-ab|ye-ad|ye-am|ye-ba|ye-da|ye-dh|ye-hd|ye-hj|ye-ib|ye-ja|ye-la|ye-ma|ye-mr|ye-mu|ye-mw|ye-ra|ye-sd|ye-sh|ye-sn|ye-ta|za-ec|za-fs|za-gt|za-lp|za-mp|za-nc|za-nl|za-nw|za-wc|zm-01|zm-02|zm-03|zm-04|zm-05|zm-06|zm-07|zm-08|zm-09|zw-bu|zw-ha|zw-ma|zw-mc|zw-me|zw-mi|zw-mn|zw-ms|zw-mv|zw-mw)$
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[RegionCode]
    IncludesFilter_NumberOfEmployeesRange_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            $ref: '#/components/schemas/NumberOfEmployeesRange'
          type: array
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[NumberOfEmployeesRange]
    IncludesFilter_RevenueRange_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            $ref: '#/components/schemas/RevenueRange'
          type: array
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[RevenueRange]
    IncludesFilter_StandardizedText_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[StandardizedText]
    IncludesFilter_NAICS_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
            pattern: ^\d{2,6}$
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[NAICS]
    IncludesFilter_Text_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: IncludesFilter[Text]
    JobTitleFilter:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
          type: array
          maxItems: 300
          title: Job Titles
          description: List of job titles to filter by. Maximum 300 items allowed.
          example:
            - Software Engineer
            - Data Scientist
        operator:
          type: string
          enum:
            - or
            - and
          title: Operator
        include_related_job_titles:
          type: boolean
          title: Include Related Job Titles
          description: When set to true, includes related job titles in the search.
          example: false
          nullable: true
      additionalProperties: false
      type: object
      required:
        - values
      title: JobTitleFilter
    AnyMatchFilter_OrganizationName_:
      properties:
        negate:
          type: boolean
          title: Negate
        values:
          items:
            type: string
            maxLength: 256
          type: array
          title: Values
      additionalProperties: false
      type: object
      required:
        - values
      title: AnyMatchFilter[OrganizationName]
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
    JobSeniorityLevel:
      type: string
      enum:
        - owner
        - c-suite
        - vice president
        - director
        - senior non-managerial
        - manager
        - partner
        - non-managerial
        - junior
        - president
        - senior manager
        - advisor
        - freelancer
        - board member
        - founder
      title: JobSeniorityLevel
      description: >-
        The `JobSeniorityLevel` class is an enumeration that represents various
        levels of job seniority.


        This enum is used to categorize jobs based on their seniority levels,
        such as:

        - Entry-level positions

        - Managerial roles

        - Executive roles (e.g., C-Suite, VP)


        These categories ensure consistent filtering and classification of
        job-related data across the application.
    JobDepartment:
      type: string
      enum:
        - administration
        - real estate
        - healthcare
        - partnerships
        - c-suite
        - design
        - human resources
        - engineering
        - education
        - strategy
        - product
        - sales
        - r&d
        - retail
        - customer success
        - security
        - public service
        - creative
        - it
        - support
        - marketing
        - trade
        - legal
        - operations
        - procurement
        - data
        - manufacturing
        - logistics
        - finance
      title: JobDepartment
      description: >-
        The `JobDepartment` class is an enumeration that represents various job
        departments.


        This enum is used to categorize jobs based on their associated
        departments, such as:

        - Engineering

        - Marketing

        - Sales

        - Legal

        - Customer Service


        These categories ensure consistent filtering and classification of
        job-related data across the application.
    NumberOfEmployeesRange:
      type: string
      enum:
        - 1-10
        - 11-50
        - 51-200
        - 201-500
        - 501-1000
        - 1001-5000
        - 5001-10000
        - 10001+
      title: NumberOfEmployeesRange
      description: >-
        The `NumberOfEmployeesRange` class is an enumeration that represents
        predefined ranges

        for the number of employees in a company. These ranges are used for
        filtering and

        categorizing companies based on their workforce size.
    RevenueRange:
      type: string
      enum:
        - 0-500K
        - 500K-1M
        - 1M-5M
        - 5M-10M
        - 10M-25M
        - 25M-75M
        - 75M-200M
        - 200M-500M
        - 500M-1B
        - 1B-10B
        - 10B-100B
        - 100B-1T
        - 1T-10T
        - 10T+
      title: RevenueRange
      description: >-
        The `RevenueRange` class is an enumeration that represents predefined
        ranges for the revenue of a company.
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````