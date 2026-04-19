> ## Documentation Index
> Fetch the complete documentation index at: https://developers.explorium.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Professional profile: contact and workplace

### Introduction

The **Professional Profile Contact and Workplace Enrichments** API provides comprehensive professional details about a prospect, including job history, company affiliations, skills, education, and workplace details. This endpoint is designed to enhance prospect intelligence, streamline recruitment efforts, and improve sales and marketing strategies.

<Icon icon="thumbtack" iconType="solid" color="red" /> **Key Benefits:**

* Access **detailed career history**, including past and present job roles.
* Retrieve **company affiliations** and workplace insights.
* Analyze **skills and expertise** for targeted outreach.
* Gain **educational background** to understand professional qualifications.
* Improve **lead scoring and personalization** in sales and marketing campaigns.

### Endpoint: `POST /prospects/profiles/enrich`

<AccordionGroup>
  <Accordion title="How It Works">
    1. **Input:** Provide a `prospect_id` (retrieved from the **Match Prospects** endpoint) to fetch professional details.
    2. **Processing:** The system gathers professional data from multiple sources and structures it.
    3. **Output:** A response containing job history, workplace affiliations, skills, and education details.
  </Accordion>

  <Accordion title="Request Schema">
    | Field         | Type   | Description                                     |
    | :------------ | :----- | :---------------------------------------------- |
    | `prospect_id` | String | A unique identifier for the prospect (Required) |
  </Accordion>

  <Accordion title="Best Practices">
    * **Use verified prospect IDs** to ensure accurate data enrichment.
    * **Leverage job history and expertise** for recruitment and lead scoring.
    * **Incorporate workplace insights** into sales and marketing automation.
    * **Analyze skills and education** to personalize communication and engagement.
    * **Cross-check company affiliations** for networking and partnership opportunities.
  </Accordion>

  <Accordion title="Professional Profile Contact and Workplace Output Signal">
    | Signal                 | API Name                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data Type Final |
    | :--------------------- | :-------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
    | gender                 | Individual's gender                           | Gender reported by the individual on their profile. If gender is not reported on profile, returned value is 'null'.                                                                                                                                                                                                                                                                                                                                 | string          |
    | city                   | Individual's city of residence                | Individual's city of residence reported on profile.                                                                                                                                                                                                                                                                                                                                                                                                 | string          |
    | country\_name          | Individual's country of residence             | Individual's country of residence reported on profile.                                                                                                                                                                                                                                                                                                                                                                                              | string          |
    | region\_name           | Individual's State / Region of residence      | Individual's state or region of residence reported on profile.                                                                                                                                                                                                                                                                                                                                                                                      | string          |
    | company\_website       | Individual's workplace: company website       | URL to the company website belonging to the individual's workplace.                                                                                                                                                                                                                                                                                                                                                                                 | string          |
    | company\_linkedin      | Individual's workplace: company LinkedIn® url | URL to the company LinkedIn® page belonging to the individual's workplace.                                                                                                                                                                                                                                                                                                                                                                          | string          |
    | linkedin               | Individual's LinkedIn® URL                    | URN of the individual's LinkedIn® profile.                                                                                                                                                                                                                                                                                                                                                                                                          | url             |
    | linkedin\_url\_array   | LinkedIn®  Identifier Array                   | A list of LinkedIn® profile URLs associated with the prospect. Each entry may include a standard public URL and/or a URN-based URL.                                                                                                                                                                                                                                                                                                                 | array\[string]  |
    | age\_group             | Individual's age group                        | Individual's estimated age group.                                                                                                                                                                                                                                                                                                                                                                                                                   | string          |
    | experience             | Individual's work experience background       | List of work experience background entries on the individual's profile. May include: company name, company website, job title, seniority level, role, start date, end date, and more. Includes current work experience activities if listed.                                                                                                                                                                                                        | array           |
    | education              | Individual's educational background           | List of educational background entries on the individual's profile. May include: institutions name, institutions website, degree category, major, start date, end date, and more. Includes current educational activities if listed.                                                                                                                                                                                                                | array           |
    | interests              | Individual's interests                        | List of all interests reported by the individual on their profile.                                                                                                                                                                                                                                                                                                                                                                                  | array           |
    | skills                 | Individual's skills                           | List of all skills reported by the individual on their profile.                                                                                                                                                                                                                                                                                                                                                                                     | array           |
    | job\_title             | Individual's job title                        | Individual's current job title listed on their professional profile.                                                                                                                                                                                                                                                                                                                                                                                | string          |
    | job\_department        | Individual's job department                   | Individual's job department, derived from their current job title.                                                                                                                                                                                                                                                                                                                                                                                  | object          |
    | job\_department\_array | Job Department (Array)                        | All detected normalized job departments for the individual. Examples: retail, engineering, customer success, administration, education, security, healthcare, public service, partnerships, creative, strategy, real estate, procurement, IT, data, c-suite, manufacturing, support, logistics, product, sales, design, marketing, finance, R\&D, trade, human resources, legal, operations.                                                        | array\<string>  |
    | job\_department\_main  | Job Department (Main)                         | Primary normalized job department selected from the detected departments (e.g., “engineering”). Examples of possible values: retail, engineering, customer success, administration, education, security, healthcare, public service, partnerships, creative, strategy, real estate, procurement, IT, data, c-suite, manufacturing, support, logistics, product, sales, design, marketing, finance, R\&D, trade, human resources, legal, operations. | string          |
    | job\_seniority\_level  | Individual's seniority level                  | Individual's top seniority level, derived from their current job title.                                                                                                                                                                                                                                                                                                                                                                             | object          |
    | job\_level\_array      | Job Level (Array)                             | All detected normalized job levels for the individual. Examples: manager, president, senior manager, owner, advisor, freelancer, junior, director, c-suite, board member, senior non-managerial, non-managerial, partner, vice president, founder.                                                                                                                                                                                                  | array\<string>  |
    | job\_level\_main       | Job Level (Main)                              | Primary normalized job level selected from the detected levels (e.g., “senior non-managerial”). Examples of possible values: manager, president, senior manager, owner, advisor, freelancer, junior, director, c-suite, board member, senior non-managerial, non-managerial, partner, vice president, founder.                                                                                                                                      | string          |
    | company\_name          | Individual's workplace: company name          | Name of the company the individual listed as their workplace.                                                                                                                                                                                                                                                                                                                                                                                       | string          |
    | full\_name             | Individual's full name                        | First and last names associated with the individual, appended with a space.                                                                                                                                                                                                                                                                                                                                                                         | string          |
  </Accordion>
</AccordionGroup>

<Icon icon="thumbtack" iconType="solid" color="red" /> **For additional enrichment options, explore related API endpoints below.**

## Body Params - Try Me Example

```
prospect_id: ee936e451b50c70e068e1b54e106cb89173198c4
```


## OpenAPI

````yaml post /v1/prospects/profiles/enrich
openapi: 3.1.0
info:
  title: Partner Service
  version: 0.2.330
servers:
  - url: https://api.explorium.ai
    description: AgentSource Server
security: []
paths:
  /v1/prospects/profiles/enrich:
    post:
      tags:
        - ProspectsEnrichments
      summary: Profiles
      operationId: prospects_profiles_enrich
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
              $ref: '#/components/schemas/ProspectsEnrichRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/ProspectsEnrichResponse_ProfilesOutputSchema_
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
    ProspectsEnrichRequest:
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
      title: ProspectsEnrichRequest
    ProspectsEnrichResponse_ProfilesOutputSchema_:
      properties:
        response_context:
          $ref: '#/components/schemas/ResponseContext'
        data:
          anyOf:
            - $ref: '#/components/schemas/ProfilesOutputSchema'
            - items:
                $ref: '#/components/schemas/ProfilesOutputSchema'
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
      title: ProspectsEnrichResponse[ProfilesOutputSchema]
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
    ProfilesOutputSchema:
      properties:
        full_name:
          type: string
          title: Full Name
        first_name:
          type: string
          title: First Name
        last_name:
          type: string
          title: Last Name
        country_name:
          type: string
          pattern: >-
            ^(aruba|afghanistan|angola|anguilla|åland\
            islands|albania|andorra|united\ arab\
            emirates|argentina|armenia|american\ samoa|antarctica|french\
            southern\ territories|antigua\ and\
            barbuda|australia|austria|azerbaijan|burundi|belgium|benin|bonaire,\
            sint\ eustatius\ and\ saba|burkina\
            faso|bangladesh|bulgaria|bahrain|bahamas|bosnia\ and\
            herzegovina|saint\ barthélemy|belarus|belize|bermuda|bolivia,\
            plurinational\ state\ of|brazil|barbados|brunei\
            darussalam|bhutan|bouvet\ island|botswana|central\ african\
            republic|canada|cocos\ \(keeling\)\
            islands|switzerland|chile|china|côte\ d'ivoire|cameroon|congo,\ the\
            democratic\ republic\ of\ the|congo|cook\
            islands|colombia|comoros|cabo\ verde|costa\
            rica|cuba|curaçao|christmas\ island|cayman\
            islands|cyprus|czechia|germany|djibouti|dominica|denmark|dominican\
            republic|algeria|ecuador|egypt|eritrea|western\
            sahara|spain|estonia|ethiopia|finland|fiji|falkland\ islands\
            \(malvinas\)|france|faroe\ islands|micronesia,\ federated\ states\
            of|gabon|united\
            kingdom|georgia|guernsey|ghana|gibraltar|guinea|guadeloupe|gambia|guinea\-bissau|equatorial\
            guinea|greece|grenada|greenland|guatemala|french\
            guiana|guam|guyana|hong\ kong|heard\ island\ and\ mcdonald\
            islands|honduras|croatia|haiti|hungary|indonesia|isle\ of\
            man|india|british\ indian\ ocean\ territory|ireland|iran,\ islamic\
            republic\
            of|iraq|iceland|israel|italy|jamaica|jersey|jordan|japan|kazakhstan|kenya|kyrgyzstan|cambodia|kiribati|saint\
            kitts\ and\ nevis|korea,\ republic\ of|kuwait|lao\ people's\
            democratic\ republic|lebanon|liberia|libya|saint\
            lucia|liechtenstein|sri\
            lanka|lesotho|lithuania|luxembourg|latvia|macao|saint\ martin\
            \(french\ part\)|morocco|monaco|moldova,\ republic\
            of|madagascar|maldives|mexico|marshall\ islands|north\
            macedonia|mali|malta|myanmar|montenegro|mongolia|northern\ mariana\
            islands|mozambique|mauritania|montserrat|martinique|mauritius|malawi|malaysia|mayotte|namibia|new\
            caledonia|niger|norfolk\
            island|nigeria|nicaragua|niue|netherlands|norway|nepal|nauru|new\
            zealand|oman|pakistan|panama|pitcairn|peru|philippines|palau|papua\
            new\ guinea|poland|puerto\ rico|korea,\ democratic\ people's\
            republic\ of|portugal|paraguay|palestine,\ state\ of|french\
            polynesia|qatar|réunion|romania|russian\ federation|rwanda|saudi\
            arabia|sudan|senegal|singapore|south\ georgia\ and\ the\ south\
            sandwich\ islands|saint\ helena,\ ascension\ and\ tristan\ da\
            cunha|svalbard\ and\ jan\ mayen|solomon\ islands|sierra\ leone|el\
            salvador|san\ marino|somalia|saint\ pierre\ and\
            miquelon|serbia|south\ sudan|sao\ tome\ and\
            principe|suriname|slovakia|slovenia|sweden|eswatini|sint\ maarten\
            \(dutch\ part\)|seychelles|syrian\ arab\ republic|turks\ and\
            caicos\
            islands|chad|togo|thailand|tajikistan|tokelau|turkmenistan|timor\-leste|tonga|trinidad\
            and\ tobago|tunisia|turkey|tuvalu|taiwan,\ province\ of\
            china|tanzania,\ united\ republic\ of|uganda|ukraine|united\ states\
            minor\ outlying\ islands|uruguay|united\ states|uzbekistan|holy\
            see\ \(vatican\ city\ state\)|saint\ vincent\ and\ the\
            grenadines|venezuela,\ bolivarian\ republic\ of|virgin\ islands,\
            british|virgin\ islands,\ u\.s\.|viet\ nam|vanuatu|wallis\ and\
            futuna|samoa|kosovo|yemen|south\ africa|zambia|zimbabwe)$
          title: Country Name
        region_name:
          type: string
          pattern: >-
            ^(canillo|encamp|la\ massana|ordino|sant\ julià\ de\ lòria|andorra\
            la\ vella|escaldes\-engordany|'ajmān|abū\ ȥaby\ \[abu\
            dhabi\]|dubayy|al\ fujayrah|ra’s\ al\ khaymah|ash\ shāriqah|umm\ al\
            qaywayn|balkh|bāmyān|bādghīs|badakhshān|baghlān|dāykundī|farāh|fāryāb|ghaznī|ghōr|helmand|herāt|jowzjān|kābul|kandahār|kāpīsā|kunduz|khōst|kunar|laghmān|lōgar|nangarhār|nīmrōz|nūristān|panjshayr|parwān|paktiyā|paktīkā|samangān|sar\-e\
            pul|takhār|uruzgān|wardak|zābul|saint\ george|saint\ john|saint\
            mary|saint\ paul|saint\ peter|saint\
            philip|barbuda|redonda|berat|durrës|elbasan|fier|gjirokastër|korçë|kukës|lezhë|dibër|shkodër|tiranë|vlorë|berat|bulqizë|dibër|delvinë|durrës|devoll|elbasan|kolonjë|fier|gjirokastër|gramsh|has|kavajë|kurbin|kuçovë|korçë|krujë|kukës|librazhd|lezhë|lushnjë|mallakastër|malësi\
            e\
            madhe|mirditë|mat|pogradec|peqin|përmet|pukë|shkodër|skrapar|sarandë|tepelenë|tropojë|tiranë|vlorë|aragacotn|ararat|armavir|erevan|gegarkunik'|kotayk'|lory|sirak|syunik'|tavus|vayoc\
            jor|bengo|benguela|bié|cabinda|cuando\-cubango|cunene|cuanza\
            norte|cuanza\ sul|huambo|huíla|lunda\ norte|lunda\
            sul|luanda|malange|moxico|namibe|uíge|zaire|salta|buenos\
            aires|ciudad\ autónoma\ de\ buenos\ aires|san\ luis|entre\
            rios|santiago\ del\ estero|chaco|san\ juan|catamarca|la\
            pampa|mendoza|misiones|formosa|neuquen|rio\ negro|santa\
            fe|tucuman|chubut|tierra\ del\ fuego|corrientes|cordoba|jujuy|santa\
            cruz|burgenland|kärnten|niederösterreich|oberösterreich|salzburg|steiermark|tirol|vorarlberg|wien|australian\
            capital\ territory|new\ south\ wales|northern\
            territory|queensland|south\ australia|tasmania|victoria|western\
            australia|abşeron|ağstafa|ağcabədi|ağdam|ağdaş|ağsu|astara|bakı|babək|balakən|bərdə|beyləqan|biləsuvar|cəbrayıl|cəlilabab|culfa|daşkəsən|füzuli|gəncə|gədəbəy|goranboy|göyçay|göygöl|hacıqabul|i̇mişli|i̇smayıllı|kəlbəcər|kǝngǝrli|kürdəmir|lənkəran|laçın|lənkəran|lerik|masallı|mingəçevir|naftalan|neftçala|naxçıvan|naxçıvan|oğuz|ordubad|qəbələ|qax|qazax|quba|qubadlı|qobustan|qusar|şəki|sabirabad|sədərək|şahbuz|şəki|salyan|şərur|saatlı|şabran|siyəzən|şəmkir|sumqayıt|şamaxı|samux|şirvan|şuşa|tərtər|tovuz|ucar|xankəndi|xaçmaz|xocalı|xızı|xocavənd|yardımlı|yevlax|yevlax|zəngilan|zaqatala|zərdab|unsko\-sanski\
            kanton|posavski\ kanton|tuzlanski\ kanton|zeničko\-dobojski\
            kanton|bosansko\-podrinjski\ kanton|srednjobosanski\
            kanton|hercegovačko\-neretvanski\ kanton|zapadnohercegovački\
            kanton|kanton\ sarajevo|kanton\ br\.\ 10\ \(livanjski\
            kanton\)|federacija\ bosne\ i\ hercegovine|brčko\
            distrikt|republika\ srpska|christ\ church|saint\ andrew|saint\
            george|saint\ james|saint\ john|saint\ joseph|saint\ lucy|saint\
            michael|saint\ peter|saint\ philip|saint\
            thomas|bandarban|barguna|bogra|brahmanbaria|bagerhat|barisal|bhola|comilla|chandpur|chittagong|cox's\
            bazar|chuadanga|dhaka|dinajpur|faridpur|feni|gopalganj|gazipur|gaibandha|habiganj|jamalpur|jessore|jhenaidah|jaipurhat|jhalakati|kishorganj|khulna|kurigram|khagrachari|kushtia|lakshmipur|lalmonirhat|manikganj|mymensingh|munshiganj|madaripur|magura|moulvibazar|meherpur|narayanganj|netrakona|narsingdi|narail|natore|nawabganj|nilphamari|noakhali|naogaon|pabna|pirojpur|patuakhali|panchagarh|rajbari|rajshahi|rangpur|rangamati|sherpur|satkhira|sirajganj|sylhet|sunamganj|shariatpur|tangail|thakurgaon|barisal|chittagong|dhaka|khulna|rajshahi|rangpur|sylhet|bruxelles\-capitale,\
            région\ de;brussels\ hoofdstedelijk\
            gewest|antwerpen|vlaams\-brabant|vlaams\
            gewest|limburg|oost\-vlaanderen|west\-vlaanderen|wallonne,\
            région|brabant\ wallon|hainaut|liège|luxembourg|namur|boucle\ du\
            mouhoun|cascades|centre|centre\-est|centre\-nord|centre\-ouest|centre\-sud|est|hauts\-bassins|nord|plateau\-central|sahel|sud\-ouest|balé|bam|banwa|bazèga|bougouriba|boulgou|boulkiemdé|comoé|ganzourgou|gnagna|gourma|houet|ioba|kadiogo|kénédougou|komondjari|kompienga|koulpélogo|kossi|kouritenga|kourwéogo|léraba|loroum|mouhoun|namentenga|naouri|nayala|noumbiel|oubritenga|oudalan|passoré|poni|séno|sissili|sanmatenga|sanguié|soum|sourou|tapoa|tui|yagha|yatenga|ziro|zondoma|zoundwéogo|blagoevgrad|burgas|varna|veliko\
            tarnovo|vidin|vratsa|gabrovo|dobrich|kardzhali|kyustendil|lovech|montana|pazardzhik|pernik|pleven|plovdiv|razgrad|ruse|silistra|sliven|smolyan|sofia\-grad|sofia|stara\
            zagora|targovishte|haskovo|shumen|yambol|al\ manāmah\ \(al\
            ‘āşimah\)|al\ janūbīyah|al\ muḩarraq|al\ wusţá|ash\
            shamālīyah|bubanza|bujumbura\ rural|bujumbura\
            mairie|bururi|cankuzo|cibitoke|gitega|kirundo|karuzi|kayanza|makamba|muramvya|mwaro|ngozi|rutana|ruyigi|atakora|alibori|atlantique|borgou|collines|donga|kouffo|littoral|mono|ouémé|plateau|zou|belait|brunei\-muara|temburong|tutong|el\
            beni|cochabamba|chuquisaca|la\ paz|pando|oruro|potosí|santa\
            cruz|tarija|bonaire|saba|sint\
            eustatius|acre|alagoas|amazonas|amapá|bahia|ceará|distrito\
            federal|espírito\ santo|fernando\ de\ noronha|goiás|maranhão|minas\
            gerais|mato\ grosso\ do\ sul|mato\
            grosso|pará|paraíba|pernambuco|piauí|paraná|rio\ de\ janeiro|rio\
            grande\ do\ norte|rondônia|roraima|rio\ grande\ do\ sul|santa\
            catarina|sergipe|são\ paulo|tocantins|acklins|bimini|black\
            point|berry\ islands|central\ eleuthera|cat\ island|crooked\ island\
            and\ long\ cay|central\ abaco|central\ andros|east\ grand\
            bahama|exuma|city\ of\ freeport|grand\ cay|harbour\ island|hope\
            town|inagua|long\ island|mangrove\ cay|mayaguana|moore's\
            island|north\ eleuthera|north\ abaco|north\ andros|rum\ cay|ragged\
            island|south\ andros|south\ eleuthera|south\ abaco|san\
            salvador|spanish\ wells|west\ grand\
            bahama|paro|chhukha|ha|samtee|thimphu|tsirang|dagana|punakha|wangdue\
            phodrang|sarpang|trongsa|bumthang|zhemgang|trashigang|monggar|pemagatshel|lhuentse|samdrup\
            jongkha|gasa|trashi\
            yangtse|central|ghanzi|kgalagadi|kgatleng|kweneng|north\-east|north\-west|south\-east|southern|bresckaja\
            voblasć|horad\ minsk|homieĺskaja\ voblasć|hrodzienskaja\
            voblasć|mahilioŭskaja\ voblasć|minskaja\ voblasć|viciebskaja\
            voblasć|belize|cayo|corozal|orange\ walk|stann\
            creek|toledo|alberta|british\ columbia|manitoba|new\
            brunswick|newfoundland\ and\ labrador|nova\ scotia|northwest\
            territories|nunavut|ontario|prince\ edward\
            island|quebec|saskatchewan|yukon\
            territory|bas\-congo|bandundu|équateur|katanga|kasai\-oriental|kinshasa|kasai\-occidental|maniema|nord\-kivu|orientale|sud\-kivu|ouham|bamingui\-bangoran|bangui|basse\-kotto|haute\-kotto|haut\-mbomou|haute\-sangha\
            /\
            mambéré\-kadéï|gribingui|kémo\-gribingui|lobaye|mbomou|ombella\-m'poko|nana\-mambéré|ouham\-pendé|sangha|ouaka|vakaga|bouenza|pool|sangha|plateaux|cuvette\-ouest|lékoumou|kouilou|likouala|cuvette|niari|brazzaville|aargau|appenzell\
            innerrhoden|appenzell\
            ausserrhoden|bern|basel\-landschaft|basel\-stadt|fribourg|genève|glarus|graubünden|jura|luzern|neuchâtel|nidwalden|obwalden|sankt\
            gallen|schaffhausen|solothurn|schwyz|thurgau|ticino|uri|vaud|valais|zug|zürich|lagunes\
            \(région\ des\)|haut\-sassandra\ \(région\ du\)|savanes\ \(région\
            des\)|vallée\ du\ bandama\ \(région\ de\ la\)|moyen\-comoé\
            \(région\ du\)|18\ montagnes\ \(région\ des\)|lacs\ \(région\
            des\)|zanzan\ \(région\ du\)|bas\-sassandra\ \(région\
            du\)|denguélé\ \(région\ du\)|nzi\-comoé\ \(région\)|marahoué\
            \(région\ de\ la\)|sud\-comoé\ \(région\ du\)|worodouqou\ \(région\
            du\)|sud\-bandama\ \(région\ du\)|agnébi\ \(région\ de\ l'\)|bafing\
            \(région\ du\)|fromager\ \(région\ du\)|moyen\-cavally\ \(région\
            du\)|aisén\ del\ general\ carlos\ ibáñez\ del\
            campo|antofagasta|arica\ y\
            parinacota|araucanía|atacama|bío\-bío|coquimbo|libertador\ general\
            bernardo\ o'higgins|los\ lagos|los\ ríos|magallanes\ y\ antártica\
            chilena|maule|región\ metropolitana\ de\
            santiago|tarapacá|valparaíso|adamaoua|centre|far\
            north|east|littoral|north|north\-west\
            \(cameroon\)|west|south|south\-west|anhui\ sheng|beijing\
            shi|chongqing\ shi|fujian\ sheng|guangdong\ sheng|gansu\
            sheng|guangxi\ zhuangzu\ zizhiqu|guizhou\ sheng|henan\ sheng|hubei\
            sheng|hebei\ sheng|hainan\ sheng|hong\ kong\ sar\ \(see\ also\
            separate\ country\ code\ entry\ under\ hk\)|heilongjiang\
            sheng|hunan\ sheng|jilin\ sheng|jiangsu\ sheng|jiangxi\
            sheng|liaoning\ sheng|macao\ sar\ \(see\ also\ separate\ country\
            code\ entry\ under\ mo\)|nei\ mongol\ zizhiqu|ningxia\ huizi\
            zizhiqu|qinghai\ sheng|sichuan\ sheng|shandong\ sheng|shanghai\
            shi|shaanxi\ sheng|shanxi\ sheng|tianjin\ shi|taiwan\ sheng\ \(see\
            also\ separate\ country\ code\ entry\ under\ tw\)|xinjiang\ uygur\
            zizhiqu|xizang\ zizhiqu|yunnan\ sheng|zhejiang\
            sheng|amazonas|antioquia|arauca|atlántico|bolívar|boyacá|caldas|caquetá|casanare|cauca|cesar|chocó|córdoba|cundinamarca|distrito\
            capital\ de\ bogotá|guainía|guaviare|huila|la\
            guajira|magdalena|meta|nariño|norte\ de\
            santander|putumayo|quindío|risaralda|santander|san\ andrés,\
            providencia\ y\ santa\ catalina|sucre|tolima|valle\ del\
            cauca|vaupés|vichada|alajuela|cartago|guanacaste|heredia|limón|puntarenas|san\
            josé|pinar\ del\ rio|la\ habana|ciudad\ de\ la\
            habana|matanzas|villa\ clara|cienfuegos|sancti\ spíritus|ciego\ de\
            ávila|camagüey|las\ tunas|holguín|granma|santiago\ de\
            cuba|guantánamo|isla\ de\ la\ juventud|ilhas\ de\
            barlavento|brava|boa\ vista|santa\ catarina|santa\ catarina\ de\
            fogo|santa\ cruz|maio|mosteiros|paul|porto\ novo|praia|ribeira\
            brava|ribeira\ grande|ribeira\ grande\ de\ santiago|ilhas\ de\
            sotavento|são\ domingos|são\ filipe|sal|são\ miguel|são\ lourenço\
            dos\ órgãos|são\ salvador\ do\ mundo|são\ vicente|tarrafal|tarrafal\
            de\ são\
            nicolau|lefkosía|lemesós|lárnaka|ammóchostos|páfos|kerýneia|praha,\
            hlavní\ mešto|praha\ 1|praha\ 2|praha\ 3|praha\ 4|praha\ 5|praha\
            6|praha\ 7|praha\ 8|praha\ 9|praha\ 10|praha\ 11|praha\ 12|praha\
            13|praha\ 14|praha\ 15|praha\ 16|praha\ 17|praha\ 18|praha\
            19|praha\ 20|praha\ 21|praha\ 22|středočeský\
            kraj|benešov|beroun|kladno|kolín|kutná\ hora|mělník|mladá\
            boleslav|nymburk|praha\-východ|praha\-západ|příbram|rakovník|jihočeský\
            kraj|české\ budějovice|český\ krumlov|jindřichův\
            hradec|písek|prachatice|strakonice|tábor|plzeňský\
            kraj|domažlice|klatovy|plzeň\-město|plzeň\-jih|plzeň\-sever|rokycany|tachov|karlovarský\
            kraj|cheb|karlovy\ vary|sokolov|ústecký\
            kraj|děčín|chomutov|litoměřice|louny|most|teplice|ústí\ nad\
            labem|liberecký\ kraj|česká\ lípa|jablonec\ nad\
            nisou|liberec|semily|královéhradecký\ kraj|hradec\
            králové|jičín|náchod|rychnov\ nad\ kněžnou|trutnov|pardubický\
            kraj|chrudim|pardubice|svitavy|ústí\ nad\ orlicí|kraj\
            vysočina|havlíčkův\ brod|jihlava|pelhřimov|třebíč|žďár\ nad\
            sázavou|jihomoravský\
            kraj|blansko|brno\-město|brno\-venkov|břeclav|hodonín|vyškov|znojmo|olomoucký\
            kraj|jeseník|olomouc|prostějov|přerov|šumperk|zlínský\
            kraj|kroměříž|uherské\ hradiště|vsetín|zlín|moravskoslezský\
            kraj|bruntál|frýdek\ místek|karviná|nový\
            jičín|opava|ostrava\-město|brandenburg|berlin|baden\-württemberg|bayern|bremen|hessen|hamburg|mecklenburg\-vorpommern|niedersachsen|nordrhein\-westfalen|rheinland\-pfalz|schleswig\-holstein|saarland|sachsen|sachsen\-anhalt|thüringen|arta|ali\
            sabieh|dikhil|djibouti|obock|tadjourah|nordjylland|midtjylland|syddanmark|hovedstaden|sjælland|saint\
            peter|saint\ andrew|saint\ david|saint\ george|saint\ john|saint\
            joseph|saint\ luke|saint\ mark|saint\ patrick|saint\ paul|distrito\
            nacional\ \(santo\
            domingo\)|azua|bahoruco|barahona|dajabón|duarte|la\ estrelleta\
            \[elías\ piña\]|el\ seybo\ \[el\ seibo\]|espaillat|independencia|la\
            altagracia|la\ romana|la\ vega|maría\ trinidad\ sánchez|monte\
            cristi|pedernales|peravia|puerto\ plata|salcedo|samaná|san\
            cristóbal|san\ juan|san\ pedro\ de\ macorís|sánchez\
            ramírez|santiago|santiago\ rodríguez|valverde|monseñor\ nouel|monte\
            plata|hato\ mayor|adrar|chlef|laghouat|oum\ el\
            bouaghi|batna|béjaïa|biskra|béchar|blida|bouira|tamanghasset|tébessa|tlemcen|tiaret|tizi\
            ouzou|alger|djelfa|jijel|sétif|saïda|skikda|sidi\ bel\
            abbès|annaba|guelma|constantine|médéa|mostaganem|msila|mascara|ouargla|oran|el\
            bayadh|illizi|bordj\ bou\ arréridj|boumerdès|el\
            tarf|tindouf|tissemsilt|el\ oued|khenchela|souk\
            ahras|tipaza|mila|aïn\ defla|naama|aïn\
            témouchent|ghardaïa|relizane|azuay|bolívar|carchi|orellana|esmeraldas|cañar|guayas|chimborazo|imbabura|loja|manabí|napo|el\
            oro|pichincha|los\ ríos|morona\-santiago|santo\ domingo\ de\ los\
            tsáchilas|santa\
            elena|tungurahua|sucumbíos|galápagos|cotopaxi|pastaza|zamora\-chinchipe|harjumaa|hiiumaa|ida\-virumaa|jõgevamaa|järvamaa|läänemaa|lääne\-virumaa|põlvamaa|pärnumaa|raplamaa|saaremaa|tartumaa|valgamaa|viljandimaa|võrumaa|al\
            iskandarīyah|aswān|asyūt|al\ bahr\ al\ ahmar|al\ buhayrah|banī\
            suwayf|al\ qāhirah|ad\ daqahlīyah|dumyāt|al\ fayyūm|al\
            gharbīyah|al\ jīzah|ḩulwān|al\ ismā`īlīyah|janūb\ sīnā'|al\
            qalyūbīyah|kafr\ ash\ shaykh|qinā|al\ minyā|al\
            minūfīyah|matrūh|būr\ sa`īd|sūhāj|ash\ sharqīyah|shamal\ sīnā'|as\
            sādis\ min\ uktūbar|as\ suways|al\ wādī\ al\ jadīd|ansabā|janūbī\
            al\ baḩrī\ al\ aḩmar|al\ janūbī|qāsh\-barkah|al\ awsaţ|shimālī\ al\
            baḩrī\ al\
            aḩmar|alicante|albacete|almería|andalucía|aragón|asturias,\
            principado\ de|ávila|barcelona|badajoz|bizkaia|burgos|a\
            coruña|cádiz|cantabria|cáceres|ceuta|castilla\ y\ león|castilla\-la\
            mancha|canarias|córdoba|ciudad\
            real|castellón|catalunya|cuenca|extremadura|galicia|las\
            palmas|girona|granada|guadalajara|huelva|huesca|illes\
            balears|jaén|lleida|león|la\ rioja|lugo|madrid|málaga|murcia,\
            región\ de|madrid,\ comunidad\ de|melilla|murcia|navarra\ /\
            nafarroa|navarra,\ comunidad\ foral\ de\ /\ nafarroako\ foru\
            komunitatea|asturias|ourense|palencia|balears|pontevedra|país\
            vasco\ /\ euskal\ herria|la\
            rioja|cantabria|salamanca|sevilla|segovia|soria|gipuzkoa|tarragona|teruel|santa\
            cruz\ de\ tenerife|toledo|valencia\ /\
            valència|valladolid|valenciana,\ comunidad\ /\ valenciana,\
            comunitat|álava|zaragoza|zamora|ādīs\ ābeba|āfar|āmara|bīnshangul\
            gumuz|dirē\ dawa|gambēla\ hizboch|hārerī\ hizb|oromīya|yedebub\
            bihēroch\ bihēreseboch\ na\ hizboch|sumalē|tigray|ahvenanmaan\
            maakunta|etelä\-karjala|etelä\-pohjanmaa|etelä\-savo|kainuu|kanta\-häme|keski\-pohjanmaa|keski\-suomi|kymenlaakso|lappi|pirkanmaa|pohjanmaa|pohjois\-karjala|pohjois\-pohjanmaa|pohjois\-savo|päijät\-häme|satakunta|uusimaa|varsinais\-suomi|central|eastern|northern|rotuma|western|kosrae|pohnpei|chuuk|yap|ain|aisne|allier|alpes\-de\-haute\-provence|hautes\-alpes|alpes\-maritimes|ardèche|ardennes|ariège|aube|aude|aveyron|bouches\-du\-rhône|calvados|cantal|charente|charente\-maritime|cher|corrèze|côte\-d'or|côtes\-d'armor|creuse|dordogne|doubs|drôme|eure|eure\-et\-loir|finistère|corse\-du\-sud|haute\-corse|gard|haute\-garonne|gers|gironde|hérault|ille\-et\-vilaine|indre|indre\-et\-loire|isère|jura|landes|loir\-et\-cher|loire|haute\-loire|loire\-atlantique|loiret|lot|lot\-et\-garonne|lozère|maine\-et\-loire|manche|marne|haute\-marne|mayenne|meurthe\-et\-moselle|meuse|morbihan|moselle|nièvre|nord|oise|orne|pas\-de\-calais|puy\-de\-dôme|pyrénées\-atlantiques|hautes\-pyrénées|pyrénées\-orientales|bas\-rhin|haut\-rhin|rhône|haute\-saône|saône\-et\-loire|sarthe|savoie|haute\-savoie|paris|seine\-maritime|seine\-et\-marne|yvelines|deux\-sèvres|somme|tarn|tarn\-et\-garonne|var|vaucluse|vendée|vienne|haute\-vienne|vosges|yonne|territoire\
            de\
            belfort|essonne|hauts\-de\-seine|seine\-saint\-denis|val\-de\-marne|val\-d'oise|auvergne\-rhône\-alpes|bourgogne\-franche\-comté|saint\-barthélemy|bretagne|corse|clipperton|centre\-val\
            de\ loire|grand\-est|guyane\
            \(française\)|guadeloupe|guadeloupe|hauts\-de\-france|île\-de\-france|la\
            réunion|mayotte|saint\-martin|martinique|nouvelle\-aquitaine|nouvelle\-calédonie|normandie|occitanie|provence\-alpes\-côte\-d’azur|pays\-de\-la\-loire|polynésie\
            française|saint\-pierre\-et\-miquelon|la\ réunion|terres\ australes\
            françaises|wallis\-et\-futuna|mayotte|estuaire|haut\-ogooué|moyen\-ogooué|ngounié|nyanga|ogooué\-ivindo|ogooué\-lolo|ogooué\-maritime|woleu\-ntem|armagh,\
            banbridge\ and\ craigavon|aberdeenshire|aberdeen\ city|argyll\ and\
            bute|isle\ of\ anglesey;\ sir\ ynys\ môn|ards\ and\ north\
            down|antrim\ and\ newtownabbey|angus|bath\ and\ north\ east\
            somerset|blackburn\ with\ darwen|bedford|barking\ and\
            dagenham|brent|bexley|belfast|bridgend;\ pen\-y\-bont\ ar\
            ogwr|blaenau\
            gwent|birmingham|buckinghamshire|bournemouth|barnet|brighton\ and\
            hove|barnsley|bolton|blackpool|bracknell\
            forest|bradford|bromley|bristol,\ city\
            of|bury|cambridgeshire|caerphilly;\ caerffili|central\
            bedfordshire|causeway\ coast\ and\ glens|ceredigion;\ sir\
            ceredigion|cheshire\ east|cheshire\ west\ and\
            chester|calderdale|clackmannanshire|cumbria|camden|carmarthenshire;\
            sir\ gaerfyrddin|cornwall|coventry|cardiff;\
            caerdydd|croydon|conwy|darlington|derbyshire|denbighshire;\ sir\
            ddinbych|derby|devon|dumfries\ and\ galloway|doncaster|dundee\
            city|dorset|derry\ and\ strabane|dudley|durham\
            county|ealing|england\ and\ wales|east\ ayrshire|edinburgh,\ city\
            of|east\ dunbartonshire|east\ lothian|eilean\
            siar|enfield|england|east\ renfrewshire|east\ riding\ of\
            yorkshire|essex|east\ sussex|falkirk|fife|flintshire;\ sir\ y\
            fflint|fermanagh\ and\ omagh|gateshead|great\ britain|glasgow\
            city|gloucestershire|greenwich|gwynedd|halton|hampshire|havering|hackney|herefordshire|hillingdon|highland|hammersmith\
            and\ fulham|hounslow|hartlepool|hertfordshire|harrow|haringey|isles\
            of\ scilly|isle\ of\ wight|islington|inverclyde|kensington\ and\
            chelsea|kent|kingston\ upon\ hull|kirklees|kingston\ upon\
            thames|knowsley|lancashire|lisburn\ and\
            castlereagh|lambeth|leicester|leeds|leicestershire|lewisham|lincolnshire|liverpool|london,\
            city\ of|luton|manchester|middlesbrough|medway|mid\ and\ east\
            antrim|milton\ keynes|midlothian|monmouthshire;\ sir\
            fynwy|merton|moray|merthyr\ tydfil;\ merthyr\ tudful|mid\
            ulster|north\ ayrshire|northumberland|north\ east\
            lincolnshire|newcastle\ upon\ tyne|norfolk|nottingham|northern\
            ireland|north\ lanarkshire|north\ lincolnshire|newry,\ mourne\ and\
            down|north\ somerset|northamptonshire|neath\ port\ talbot;\
            castell\-nedd\ port\ talbot|nottinghamshire|north\
            tyneside|newham|newport;\ casnewydd|north\ yorkshire|oldham|orkney\
            islands|oxfordshire|pembrokeshire;\ sir\ benfro|perth\ and\
            kinross|plymouth|poole|portsmouth|powys|peterborough|redcar\ and\
            cleveland|rochdale|rhondda,\ cynon,\ taff;\ rhondda,\ cynon,\
            taf|redbridge|reading|renfrewshire|richmond\ upon\
            thames|rotherham|rutland|sandwell|south\ ayrshire|scottish\
            borders,\ the|scotland|suffolk|sefton|south\
            gloucestershire|sheffield|st\.\
            helens|shropshire|stockport|salford|slough|south\
            lanarkshire|sunderland|solihull|somerset|southend\-on\-sea|surrey|stoke\-on\-trent|stirling|southampton|sutton|staffordshire|stockton\-on\-tees|south\
            tyneside|swansea;\ abertawe|swindon|southwark|tameside|telford\ and\
            wrekin|thurrock|torbay|torfaen;\ tor\-faen|trafford|tower\
            hamlets|united\ kingdom|vale\ of\ glamorgan,\ the;\ bro\
            morgannwg|warwickshire|west\ berkshire|west\ dunbartonshire|waltham\
            forest|wigan|wiltshire|wakefield|walsall|west\ lothian|wales;\
            cymru|wolverhampton|wandsworth|windsor\ and\
            maidenhead|wokingham|worcestershire|wirral|warrington|wrexham;\
            wrecsam|westminster|west\ sussex|york|shetland\ islands|saint\
            andrew|saint\ david|saint\ george|saint\ john|saint\ mark|saint\
            patrick|southern\ grenadine\
            islands|abkhazia|ajaria|guria|imeret’i|kakhet’i|k’vemo\
            k’art’li|mts’khet’a\-mt’ianet’i|racha\-lech’khumi\-k’vemo\
            svanet’i|samts’khe\-javakhet’i|shida\ k’art’li|samegrelo\-zemo\
            svanet’i|t’bilisi|greater\
            accra|ashanti|brong\-ahafo|central|eastern|northern|volta|upper\
            east|upper\ west|western|kommune\ kujalleq|qaasuitsup\
            kommunia|qeqqata\ kommunia|kommuneqarfik\ sermersooq|banjul|lower\
            river|central\ river|north\ bank|upper\
            river|western|boké|beyla|boffa|boké|conakry|coyah|kindia|dabola|dinguiraye|dalaba|dubréka|faranah|faranah|forécariah|fria|gaoual|guékédou|kankan|kankan|koubia|kindia|kérouané|koundara|kouroussa|kissidougou|labé|labé|lélouma|lola|mamou|macenta|mandiana|mali|mamou|nzérékoré|nzérékoré|pita|siguiri|télimélé|tougué|yomou|annobón|bioko\
            norte|bioko\ sur|región\ continental|centro\ sur|región\
            insular|kié\-ntem|litoral|wele\-nzas|aitolia\ kai\
            akarnania|voiotia|evvoias|evrytania|fthiotida|fokida|argolida|arkadia|achaïa|ileia|korinthia|lakonia|messinia|zakynthos|kerkyra|kefallonia|lefkada|arta|thesprotia|ioannina|preveza|karditsa|larisa|magnisia|trikala|grevena|drama|imathia|thessaloniki|kavala|kastoria|kilkis|kozani|pella|pieria|serres|florina|chalkidiki|agio\
            oros|evros|xanthi|rodopi|dodekanisos|kyklades|lesvos|samos|chios|irakleio|lasithi|rethymno|chania|anatoliki\
            makedonia\ kai\ thraki|attiki|kentriki\ makedonia|dytiki\
            makedonia|ipeiros|thessalia|ionia\ nisia|dytiki\ ellada|sterea\
            ellada|attiki|peloponnisos|voreio\ aigaio|notio\ aigaio|kriti|alta\
            verapaz|baja\
            verapaz|chimaltenango|chiquimula|escuintla|guatemala|huehuetenango|izabal|jalapa|jutiapa|petén|el\
            progreso|quiché|quetzaltenango|retalhuleu|sacatepéquez|san\
            marcos|sololá|santa\
            rosa|suchitepéquez|totonicapán|zacapa|bafatá|bolama|biombo|bissau|cacheu|gabú|leste|norte|oio|quinara|sul|tombali|barima\-waini|cuyuni\-mazaruni|demerara\-mahaica|east\
            berbice\-corentyne|essequibo\ islands\-west\
            demerara|mahaica\-berbice|pomeroon\-supenaam|potaro\-siparuni|upper\
            demerara\-berbice|upper\ takutu\-upper\
            essequibo|atlántida|choluteca|colón|comayagua|copán|cortés|el\
            paraíso|francisco\ morazán|gracias\ a\ dios|islas\ de\ la\
            bahía|intibucá|lempira|la\ paz|ocotepeque|olancho|santa\
            bárbara|valle|yoro|zagrebačka\ županija|krapinsko\-zagorska\
            županija|sisačko\-moslavačka\ županija|karlovačka\
            županija|varaždinska\ županija|koprivničko\-križevačka\
            županija|bjelovarsko\-bilogorska\ županija|primorsko\-goranska\
            županija|ličko\-senjska\ županija|virovitičko\-podravska\
            županija|požeško\-slavonska\ županija|brodsko\-posavska\
            županija|zadarska\ županija|osječko\-baranjska\
            županija|šibensko\-kninska\ županija|vukovarsko\-srijemska\
            županija|splitsko\-dalmatinska\ županija|istarska\
            županija|dubrovačko\-neretvanska\ županija|međimurska\
            županija|grad\
            zagreb|artibonite|centre|grande\-anse|nord|nord\-est|nord\-ouest|ouest|sud|sud\-est|baranya|békéscsaba|békés|bács\-kiskun|budapest|borsod\-abaúj\-zemplén|csongrád|debrecen|dunaújváros|eger|érd|fejér|győr\-moson\-sopron|győr|hajdú\-bihar|heves|hódmezővásárhely|jász\-nagykun\-szolnok|komárom\-esztergom|kecskemét|kaposvár|miskolc|nagykanizsa|nógrád|nyíregyháza|pest|pécs|szeged|székesfehérvár|szombathely|szolnok|sopron|somogy|szekszárd|salgótarján|szabolcs\-szatmár\-bereg|tatabánya|tolna|vas|veszprém\
            \(county\)|veszprém|zala|zalaegerszeg|aceh|bali|bangka\
            belitung|bengkulu|banten|gorontalo|papua|jambi|jawa\ barat|jawa\
            timur|jakarta\ raya|jawa\ tengah|jawa|kalimantan|kalimantan\
            barat|kalimantan\ timur|kepulauan\ riau|kalimantan\
            selatan|kalimantan\ tengah|lampung|maluku|maluku|maluku\ utara|nusa\
            tenggara\ barat|nusa\ tenggara\ timur|nusa\ tenggara|papua|papua\
            barat|riau|sulawesi\ utara|sumatra\ barat|sulawesi\
            tenggara|sulawesi|sumatera|sulawesi\ selatan|sulawesi\
            barat|sumatra\ selatan|sulawesi\ tengah|sumatera\
            utara|yogyakarta|connacht|clare|cavan|cork|carlow|dublin|donegal|galway|kildare|kilkenny|kerry|leinster|longford|louth|limerick|leitrim|laois|munster|meath|monaghan|mayo|offaly|roscommon|sligo|tipperary|ulster|waterford|westmeath|wicklow|wexford|hadarom|hefa|yerushalayim\
            al\ quds|hamerkaz|tel\-aviv|hazafon|andaman\ and\ nicobar\
            islands|andhra\ pradesh|arunachal\
            pradesh|assam|bihar|chandigarh|chhattisgarh|daman\ and\
            diu|delhi|dadra\ and\ nagar\ haveli|goa|gujarat|himachal\
            pradesh|haryana|jharkhand|jammu\ and\
            kashmir|karnataka|kerala|lakshadweep|maharashtra|meghalaya|manipur|madhya\
            pradesh|mizoram|nagaland|odisha|punjab|puducherry|rajasthan|sikkim|telangana|tamil\
            nadu|tripura|uttar\ pradesh|uttarakhand|west\ bengal|al\
            anbar|arbil|al\ basrah|babil|baghdad|dahuk|diyala|dhi\
            qar|karbala'|maysan|al\ muthanna|an\ najef|ninawa|al\
            qadisiyah|salah\ ad\ din|as\ sulaymaniyah|at\
            ta'mim|wasit|āzarbāyjān\-e\ sharqī|āzarbāyjān\-e\
            gharbī|ardabīl|eşfahān|īlām|būshehr|tehrān|chahār\ mahāll\ va\
            bakhtīārī|khūzestān|zanjān|semnān|sīstān\ va\
            balūchestān|fārs|kermān|kordestān|kermānshāh|kohgīlūyeh\ va\ būyer\
            ahmad|gīlān|lorestān|māzandarān|markazī|hormozgān|hamadān|yazd|qom|golestān|qazvīn|khorāsān\-e\
            janūbī|khorāsān\-e\ razavī|khorāsān\-e\
            shemālī|reykjavík|höfuðborgarsvæðið|suðurnes|vesturland|vestfirðir|norðurland\
            vestra|norðurland\ eystra|austurland|suðurland|piemonte|valle\
            d'aosta|lombardia|trentino\-alto\ adige|veneto|friuli\-venezia\
            giulia|liguria|emilia\-romagna|toscana|umbria|marche|lazio|abruzzo|molise|campania|puglia|basilicata|calabria|sicilia|sardegna|agrigento|alessandria|ancona|aosta|ascoli\
            piceno|l'aquila|arezzo|asti|avellino|bari|bergamo|biella|belluno|benevento|bologna|brindisi|brescia|barletta\-andria\-trani|bolzano|cagliari|campobasso|caserta|chieti|carbonia\-iglesias|caltanissetta|cuneo|como|cremona|cosenza|catania|catanzaro|enna|forlì\-cesena|ferrara|foggia|firenze|fermo|frosinone|genova|gorizia|grosseto|imperia|isernia|crotone|lecco|lecce|livorno|lodi|latina|lucca|monza\
            e\
            brianza|macerata|messina|milano|mantova|modena|massa\-carrara|matera|napoli|novara|nuoro|ogliastra|oristano|olbia\-tempio|palermo|piacenza|padova|pescara|perugia|pisa|pordenone|prato|parma|pistoia|pesaro\
            e\ urbino|pavia|potenza|ravenna|reggio\ calabria|reggio\
            emilia|ragusa|rieti|roma|rimini|rovigo|salerno|siena|sondrio|la\
            spezia|siracusa|sassari|savona|taranto|teramo|trento|torino|trapani|terni|trieste|treviso|udine|varese|verbano\-cusio\-ossola|vercelli|venezia|vicenza|verona|medio\
            campidano|viterbo|vibo\ valentia|kingston|saint\ andrew|saint\
            thomas|portland|saint\ mary|saint\ ann|trelawny|saint\
            james|hanover|westmoreland|saint\
            elizabeth|manchester|clarendon|saint\ catherine|‘ajlūn|‘ammān\ \(al\
            ‘aşimah\)|al\ ‘aqabah|aţ\ ţafīlah|az\ zarqā'|al\
            balqā'|irbid|jarash|al\ karak|al\
            mafraq|mādabā|ma‘ān|hokkaido|aomori|iwate|miyagi|akita|yamagata|fukushima|ibaraki|tochigi|gunma|saitama|chiba|tokyo|kanagawa|niigata|toyama|ishikawa|fukui|yamanashi|nagano|gifu|shizuoka|aichi|mie|shiga|kyoto|osaka|hyogo|nara|wakayama|tottori|shimane|okayama|hiroshima|yamaguchi|tokushima|kagawa|ehime|kochi|fukuoka|saga|nagasaki|kumamoto|oita|miyazaki|kagoshima|okinawa|baringo|bomet|bungoma|busia|elgeyo/marakwet|embu|garissa|homa\
            bay|isiolo|kajiado|kakamega|kericho|kiambu|kilifi|kirinyaga|kisii|kisumu|kitui|kwale|laikipia|lamu|machakos|makueni|mandera|marsabit|meru|migori|mombasa|murang'a|nairobi\
            city|nakuru|nandi|narok|nyamira|nyandarua|nyeri|samburu|siaya|taita/taveta|tana\
            river|tharaka\-nithi|trans\ nzoia|turkana|uasin\
            gishu|vihiga|wajir|west\
            pokot|batken|chü|bishkek|jalal\-abad|naryn|osh|talas|ysyk\-köl|banteay\
            mean\ chey|krachoh|mondol\ kiri|phnom\ penh|preah\ vihear|prey\
            veaeng|pousaat|rotanak\ kiri|siem\ reab|krong\ preah\
            sihanouk|stueng\ traeng|battambang|svaay\ rieng|taakaev|otdar\ mean\
            chey|krong\ kaeb|krong\ pailin|kampong\ cham|kampong\
            chhnang|kampong\ speu|kampong\ thom|kampot|kandal|kach\
            kong|gilbert\ islands|line\ islands|phoenix\ islands|andjouân\
            \(anjwān\)|andjazîdja\ \(anjazījah\)|moûhîlî\ \(mūhīlī\)|christ\
            church\ nichola\ town|saint\ anne\ sandy\ point|saint\ george\
            basseterre|saint\ george\ gingerland|saint\ james\ windward|saint\
            john\ capisterre|saint\ john\ figtree|saint\ mary\ cayon|saint\
            paul\ capisterre|saint\ paul\ charlestown|saint\ peter\
            basseterre|saint\ thomas\ lowland|saint\ thomas\ middle\
            island|trinity\ palmetto\ point|saint\
            kitts|nevis|p’yŏngyang|p’yŏngan\-namdo|p’yŏngan\-bukto|chagang\-do|hwanghae\-namdo|hwanghae\-bukto|kangwŏn\-do|hamgyŏng\-namdo|hamgyŏng\-bukto|yanggang\-do|nasŏn\
            \(najin\-sŏnbong\)|seoul\ teugbyeolsi|busan\ gwang'yeogsi|daegu\
            gwang'yeogsi|incheon\ gwang'yeogsi|gwangju\ gwang'yeogsi|daejeon\
            gwang'yeogsi|ulsan\
            gwang'yeogsi|gyeonggido|gang'weondo|chungcheongbukdo|chungcheongnamdo|jeonrabukdo|jeonranamdo|gyeongsangbukdo|gyeongsangnamdo|jejudo|al\
            ahmadi|al\ farwānīyah|hawallī|al\ jahrrā’|al\ kuwayt\ \(al\
            ‘āşimah\)|mubārak\ al\ kabīr|aqmola\ oblysy|aqtöbe\
            oblysy|almaty|almaty\ oblysy|astana|atyraū\ oblysy|qaraghandy\
            oblysy|qostanay\ oblysy|qyzylorda\ oblysy|mangghystaū\
            oblysy|pavlodar\ oblysy|soltüstik\ quzaqstan\ oblysy|shyghys\
            qazaqstan\ oblysy|ongtüstik\ qazaqstan\ oblysy|batys\ quzaqstan\
            oblysy|zhambyl\
            oblysy|attapu|bokèo|bolikhamxai|champasak|houaphan|khammouan|louang\
            namtha|louangphabang|oudômxai|phôngsali|salavan|savannakhét|vientiane|vientiane|xaignabouli|xékong|xiangkhouang|xaisômboun|aakkâr|liban\-nord|beyrouth|baalbek\-hermel|béqaa|liban\-sud|mont\-liban|nabatîyé|balzers|eschen|gamprin|mauren|planken|ruggell|schaan|schellenberg|triesen|triesenberg|vaduz|basnāhira\
            paḷāta|kŏḷamba|gampaha|kaḷutara|madhyama\
            paḷāta|mahanuvara|mātale|nuvara\ ĕliya|dakuṇu\
            paḷāta|gālla|mātara|hambantŏṭa|uturu\
            paḷāta|yāpanaya|kilinŏchchi|mannārama|vavuniyāva|mulativ|næ̆gĕnahira\
            paḷāta|maḍakalapuva|ampāara|trikuṇāmalaya|vayamba\
            paḷāta|kuruṇægala|puttalama|uturumæ̆da\
            paḷāta|anurādhapura|pŏḷŏnnaruva|ūva\
            paḷāta|badulla|mŏṇarāgala|sabaragamuva\
            paḷāta|ratnapura|kægalla|bong|bomi|grand\ cape\ mount|grand\
            bassa|grand\ gedeh|grand\
            kru|lofa|margibi|montserrado|maryland|nimba|rivercess|sinoe|maseru|butha\-buthe|leribe|berea|mafeteng|mohale's\
            hoek|quthing|qacha's\ nek|mokhotlong|thaba\-tseka|alytaus\
            apskritis|klaipėdos\ apskritis|kauno\ apskritis|marijampolės\
            apskritis|panevėžio\ apskritis|šiaulių\ apskritis|tauragés\
            apskritis|telšių\ apskritis|utenos\ apskritis|vilniaus\
            apskritis|diekirch|grevenmacher|luxembourg|aglonas\
            novads|aizkraukles\ novads|aizputes\ novads|aknīstes\ novads|alojas\
            novads|alsungas\ novads|alūksnes\ novads|amatas\ novads|apes\
            novads|auces\ novads|ādažu\ novads|babītes\ novads|baldones\
            novads|baltinavas\ novads|balvu\ novads|bauskas\ novads|beverīnas\
            novads|brocēnu\ novads|burtnieku\ novads|carnikavas\
            novads|cesvaines\ novads|cēsu\ novads|ciblas\ novads|dagdas\
            novads|daugavpils\ novads|dobeles\ novads|dundagas\ novads|durbes\
            novads|engures\ novads|ērgļu\ novads|garkalnes\ novads|grobiņas\
            novads|gulbenes\ novads|iecavas\ novads|ikšķiles\ novads|ilūkstes\
            novads|inčukalna\ novads|jaunjelgavas\ novads|jaunpiebalgas\
            novads|jaunpils\ novads|jelgavas\ novads|jēkabpils\ novads|kandavas\
            novads|kārsavas\ novads|kocēnu\ novads|kokneses\ novads|krāslavas\
            novads|krimuldas\ novads|krustpils\ novads|kuldīgas\ novads|ķeguma\
            novads|ķekavas\ novads|lielvārdes\ novads|limbažu\ novads|līgatnes\
            novads|līvānu\ novads|lubānas\ novads|ludzas\ novads|madonas\
            novads|mazsalacas\ novads|mālpils\ novads|mārupes\ novads|mērsraga\
            novads|naukšēnu\ novads|neretas\ novads|nīcas\ novads|ogres\
            novads|olaines\ novads|ozolnieku\ novads|pārgaujas\
            novads|pāvilostas\ novads|pļaviņu\ novads|preiļu\ novads|priekules\
            novads|priekuļu\ novads|raunas\ novads|rēzeknes\ novads|riebiņu\
            novads|rojas\ novads|ropažu\ novads|rucavas\ novads|rugāju\
            novads|rundāles\ novads|rūjienas\ novads|salas\ novads|salacgrīvas\
            novads|salaspils\ novads|saldus\ novads|saulkrastu\ novads|sējas\
            novads|siguldas\ novads|skrīveru\ novads|skrundas\ novads|smiltenes\
            novads|stopiņu\ novads|strenču\ novads|talsu\ novads|tērvetes\
            novads|tukuma\ novads|vaiņodes\ novads|valkas\ novads|varakļānu\
            novads|vārkavas\ novads|vecpiebalgas\ novads|vecumnieku\
            novads|ventspils\ novads|viesītes\ novads|viļakas\ novads|viļānu\
            novads|zilupes\
            novads|daugavpils|jelgava|jēkabpils|jūrmala|liepāja|rēzekne|rīga|ventspils|valmiera|banghāzī|al\
            buţnān|darnah|ghāt|al\ jabal\ al\ akhḑar|jaghbūb|al\ jabal\ al\
            gharbī|al\ jifārah|al\ jufrah|al\ kufrah|al\ marqab|mişrātah|al\
            marj|murzuq|nālūt|an\ nuqaţ\ al\ khams|sabhā|surt|ţarābulus|al\
            wāḩāt|wādī\ al\ ḩayāt|wādī\ ash\ shāţiʾ|az\
            zāwiyah|tanger\-tétouan\-al\
            hoceïma|l'oriental|fès\-meknès|rabat\-salé\-kénitra|béni\
            mellal\-khénifra|casablanca\-settat|marrakech\-safi|drâa\-tafilalet|souss\-massa|guelmim\-oued\
            noun\ \(eh\-partial\)|laâyoune\-sakia\ el\ hamra\
            \(eh\-partial\)|dakhla\-oued\ ed\-dahab\
            \(eh\)|agadir\-ida\-ou\-tanane|aousserd\ \(eh\)|assa\-zag\
            \(eh\-partial\)|azilal|béni\ mellal|berkane|benslimane|boujdour\
            \(eh\)|boulemane|berrechid|casablanca|chefchaouen|chichaoua|chtouka\-ait\
            baha|driouch|errachidia|essaouira|es\-semara\
            \(eh\-partial\)|fahs\-anjra|fès|figuig|fquih\ ben\
            salah|guelmim|guercif|el\ hajeb|al\ haouz|al\
            hoceïma|ifrane|inezgane\-ait\ melloul|el\ jadida|jerada|kénitra|el\
            kelâa\ des\ sraghna|khemisset|khenifra|khouribga|laâyoune\
            \(eh\)|larache|marrakech|m’diq\-fnideq|médiouna|meknès|midelt|mohammadia|moulay\
            yacoub|nador|nouaceur|ouarzazate|oued\ ed\-dahab\
            \(eh\)|oujda\-angad|ouezzane|rabat|rehamna|safi|salé|sefrou|settat|sidi\
            bennour|sidi\ ifni|sidi\ kacem|sidi\
            slimane|skhirate\-témara|tarfaya\
            \(eh\-partial\)|taourirt|taounate|taroudant|tata|taza|tétouan|tinghir|tiznit|tanger\-assilah|tan\-tan\
            \(eh\-partial\)|youssoufia|zagora|la\ colle|la\
            condamine|fontvieille|la\ gare|jardin\
            exotique|larvotto|malbousquet|monte\-carlo|moneghetti|monaco\-ville|moulins|port\-hercule|sainte\-dévote|la\
            source|spélugues|saint\-roman|vallon\ de\ la\ rousse|anenii\
            noi|bălți|tighina|briceni|basarabeasca|cahul|călărași|cimișlia|criuleni|căușeni|cantemir|chișinău|dondușeni|drochia|dubăsari|edineț|fălești|florești|găgăuzia,\
            unitatea\ teritorială\
            autonomă|glodeni|hîncești|ialoveni|leova|nisporeni|ocnița|orhei|rezina|rîșcani|șoldănești|sîngerei|stînga\
            nistrului,\ unitatea\ teritorială\ din|soroca|strășeni|ștefan\
            vodă|taraclia|telenești|ungheni|andrijevica|bar|berane|bijelo\
            polje|budva|cetinje|danilovgrad|herceg\-novi|kolašin|kotor|mojkovac|nikšić|plav|pljevlja|plužine|podgorica|rožaje|šavnik|tivat|ulcinj|žabljak|toamasina|antsiranana|fianarantsoa|mahajanga|antananarivo|toliara|ailuk|ailinglaplap|arno|aur|ebon|enewetak|jabat|jaluit|kili|kwajalein|ralik\
            chain|lae|lib|likiep|majuro|maloelap|mejit|mili|namdrik|namu|rongelap|ratak\
            chain|ujae|utirik|wotje|wotho|aerodrom|aračinovo|berovo|bitola|bogdanci|bogovinje|bosilovo|brvenica|butel|valandovo|vasilevo|vevčani|veles|vinica|vraneštica|vrapčište|gazi\
            baba|gevgelija|gostivar|gradsko|debar|debarca|delčevo|demir\
            kapija|demir\ hisar|dojran|dolneni|drugovo|gjorče\
            petrov|želino|zajas|zelenikovo|zrnovci|ilinden|jegunovce|kavadarci|karbinci|karpoš|kisela\
            voda|kičevo|konče|kočani|kratovo|kriva\
            palanka|krivogaštani|kruševo|kumanovo|lipkovo|lozovo|mavrovo\-i\-rostuša|makedonska\
            kamenica|makedonski\ brod|mogila|negotino|novaci|novo\
            selo|oslomej|ohrid|petrovec|pehčevo|plasnica|prilep|probištip|radoviš|rankovce|resen|rosoman|saraj|sveti\
            nikole|sopište|staro\
            nagoričane|struga|strumica|studeničani|tearce|tetovo|centar|centar\
            župa|čair|čaška|češinovo\-obleševo|čučer\ sandevo|štip|šuto\
            orizari|kayes|koulikoro|sikasso|ségou|mopti|tombouctou|gao|kidal|bamako|sagaing|bago|magway|mandalay|tanintharyi|yangon|ayeyarwady|kachin|kayah|kayin|chin|mon|rakhine|shan|orhon|darhan\
            uul|hentiy|hövsgöl|hovd|uvs|töv|selenge|sühbaatar|ömnögovi|övörhangay|dzavhan|dundgovi|dornod|dornogovi|govi\-sumber|govi\-altay|bulgan|bayanhongor|bayan\-ölgiy|arhangay|ulanbaatar|hodh\
            ech\ chargui|hodh\ el\
            charbi|assaba|gorgol|brakna|trarza|adrar|dakhlet\
            nouadhibou|tagant|guidimaka|tiris\
            zemmour|inchiri|nouakchott|attard|balzan|birgu|birkirkara|birżebbuġa|bormla|dingli|fgura|floriana|fontana|gudja|gżira|għajnsielem|għarb|għargħur|għasri|għaxaq|ħamrun|iklin|isla|kalkara|kerċem|kirkop|lija|luqa|marsa|marsaskala|marsaxlokk|mdina|mellieħa|mġarr|mosta|mqabba|msida|mtarfa|munxar|nadur|naxxar|paola|pembroke|pietà|qala|qormi|qrendi|rabat\
            għawdex|rabat\ malta|safi|san\ ġiljan|san\ ġwann|san\ lawrenz|san\
            pawl\ il\-baħar|sannat|santa\ luċija|santa\
            venera|siġġiewi|sliema|swieqi|ta’\
            xbiex|tarxien|valletta|xagħra|xewkija|xgħajra|żabbar|żebbuġ\
            għawdex|żebbuġ\ malta|żejtun|żurrieq|agalega\ islands|black\
            river|beau\ bassin\-rose\ hill|cargados\ carajos\
            shoals|curepipe|flacq|grand\ port|moka|pamplemousses|port\
            louis|port\ louis|plaines\ wilhems|quatre\ bornes|rodrigues\
            island|rivière\ du\ rempart|savanne|vacoas\-phoenix|alifu\
            dhaalu|seenu|alifu\ alifu|lhaviyani|vaavu|laamu|haa\
            alifu|thaa|meemu|raa|faafu|dhaalu|baa|haa\
            dhaalu|shaviyani|noonu|kaafu|gaafu\ alifu|gaafu\
            dhaalu|gnaviyani|central|male|north\ central|north|south\
            central|south|upper\ north|upper\ south|balaka|blantyre|central\
            region|chikwawa|chiradzulu|chitipa|dedza|dowa|karonga|kasungu|lilongwe|likoma|mchinji|mangochi|machinga|mulanje|mwanza|mzimba|northern\
            region|nkhata\
            bay|neno|ntchisi|nkhotakota|nsanje|ntcheu|phalombe|rumphi|southern\
            region|salima|thyolo|zomba|aguascalientes|baja\ california|baja\
            california\ sur|campeche|chihuahua|chiapas|ciudad\ de\
            méxico|coahuila\ de\
            zaragoza|colima|durango|guerrero|guanajuato|hidalgo|jalisco|méxico|michoacán\
            de\ ocampo|morelos|nayarit|nuevo\
            león|oaxaca|puebla|querétaro|quintana\ roo|sinaloa|san\ luis\
            potosí|sonora|tabasco|tamaulipas|tlaxcala|veracruz\ de\ ignacio\ de\
            la\ llave|yucatán|zacatecas|johor|kedah|kelantan|melaka|negeri\
            sembilan|pahang|pulau\
            pinang|perak|perlis|selangor|terengganu|sabah|sarawak|wilayah\
            persekutuan\ kuala\ lumpur|wilayah\ persekutuan\ labuan|wilayah\
            persekutuan\ putrajaya|niassa|manica|gaza|inhambane|maputo|maputo\
            \(city\)|numpula|cabo\
            delgado|zambezia|sofala|tete|caprivi|erongo|hardap|karas|khomas|kunene|otjozondjupa|omaheke|okavango|oshana|omusati|oshikoto|ohangwena|agadez|diffa|dosso|maradi|tahoua|tillabéri|zinder|niamey|abia|adamawa|akwa\
            ibom|anambra|bauchi|benue|borno|bayelsa|cross\
            river|delta|ebonyi|edo|ekiti|enugu|abuja\ capital\
            territory|gombe|imo|jigawa|kaduna|kebbi|kano|kogi|katsina|kwara|lagos|nassarawa|niger|ogun|ondo|osun|oyo|plateau|rivers|sokoto|taraba|yobe|zamfara|atlántico\
            norte|atlántico\
            sur|boaco|carazo|chinandega|chontales|estelí|granada|jinotega|león|madriz|managua|masaya|matagalpa|nueva\
            segovia|rivas|río\ san\ juan|aruba|bonaire|saba|sint\
            eustatius|curaçao|drenthe|flevoland|friesland|gelderland|groningen|limburg|noord\-brabant|noord\-holland|overijssel|sint\
            maarten|utrecht|zeeland|zuid\-holland|østfold|akershus|oslo|hedmark|oppland|buskerud|vestfold|telemark|aust\-agder|vest\-agder|rogaland|hordaland|sogn\
            og\ fjordane|møre\ og\ romsdal|nordland|troms|finnmark|svalbard\
            \(arctic\ region\)|jan\ mayen\ \(arctic\
            region\)|trøndelag|madhyamanchal|madhya\
            pashchimanchal|pashchimanchal|purwanchal|sudur\
            pashchimanchal|bagmati|bheri|dhawalagiri|gandaki|janakpur|karnali|kosi|lumbini|mahakali|mechi|narayani|rapti|sagarmatha|seti|aiwo|anabar|anetan|anibare|baiti|boe|buada|denigomodu|ewa|ijuw|meneng|nibok|uaboe|yaren|auckland|bay\
            of\ plenty|canterbury|chatham\ islands\ territory|gisborne\
            district|hawke's\ bay|marlborough\
            district|manawatu\-wanganui|north\ island|nelson\
            city|northland|otago|south\ island|southland|tasman\
            district|taranaki|wellington|waikato|west\ coast|al\ bāţinah|al\
            buraymī|ad\ dākhilīya|masqaţ|musandam|ash\ sharqīyah|al\ wusţá|az̧\
            z̧āhirah|z̧ufār|bocas\ del\
            toro|coclé|colón|chiriquí|darién|herrera|los\
            santos|panamá|veraguas|emberá|kuna\
            yala|ngöbe\-buglé|amazonas|ancash|apurímac|arequipa|ayacucho|cajamarca|el\
            callao|cusco\ \[cuzco\]|huánuco|huancavelica|ica|junín|la\
            libertad|lambayeque|lima|municipalidad\ metropolitana\ de\
            lima|loreto|madre\ de\ dios|moquegua|pasco|piura|puno|san\
            martín|tacna|tumbes|ucayali|chimbu|central|east\ new\
            britain|eastern\ highlands|enga|east\ sepik|gulf|milne\
            bay|morobe|madang|manus|national\ capital\ district\ \(port\
            moresby\)|new\ ireland|northern|bougainville|sandaun|southern\
            highlands|west\ new\ britain|western\ highlands|western|national\
            capital\ region|ilocos\ \(region\ i\)|cagayan\ valley\ \(region\
            ii\)|central\ luzon\ \(region\ iii\)|bicol\ \(region\ v\)|western\
            visayas\ \(region\ vi\)|central\ visayas\ \(region\ vii\)|eastern\
            visayas\ \(region\ viii\)|zamboanga\ peninsula\ \(region\
            ix\)|northern\ mindanao\ \(region\ x\)|davao\ \(region\
            xi\)|soccsksargen\ \(region\ xii\)|caraga\ \(region\
            xiii\)|autonomous\ region\ in\ muslim\ mindanao\
            \(armm\)|cordillera\ administrative\ region\ \(car\)|calabarzon\
            \(region\ iv\-a\)|mimaropa\ \(region\ iv\-b\)|abra|agusan\ del\
            norte|agusan\ del\
            sur|aklan|albay|antique|apayao|aurora|batasn|basilan|benguet|biliran|bohol|batangas|batanes|bukidnon|bulacan|cagayan|camiguin|camarines\
            norte|capiz|camarines\ sur|catanduanes|cavite|cebu|compostela\
            valley|davao\ oriental|davao\ del\ sur|davao\ del\ norte|dinagat\
            islands|eastern\ samar|guimaras|ifugao|iloilo|ilocos\ norte|ilocos\
            sur|isabela|kalinga\-apayso|laguna|lanao\ del\ norte|lanao\ del\
            sur|leyte|la\ union|marinduque|maguindanao|masbate|mindoro\
            occidental|mindoro\ oriental|mountain\ province|misamis\
            occidental|misamis\ oriental|north\ cotabato|negros\
            occidental|negros\ oriental|northern\ samar|nueva\ ecija|nueva\
            vizcaya|pampanga|pangasinan|palawan|quezon|quirino|rizal|romblon|sarangani|south\
            cotabato|siquijor|southern\ leyte|sulu|sorsogon|sultan\
            kudarat|surigao\ del\ norte|surigao\ del\
            sur|tarlac|tawi\-tawi|western\ samar|zamboanga\ del\
            norte|zamboanga\ del\ sur|zambales|zamboanga\
            sibugay|balochistan|gilgit\-baltistan|islamabad|azad\
            kashmir|khyber\ pakhtunkhwa|punjab|sindh|federally\ administered\
            tribal\
            areas|dolnośląskie|kujawsko\-pomorskie|lubuskie|łódzkie|lubelskie|małopolskie|mazowieckie|opolskie|podlaskie|podkarpackie|pomorskie|świętokrzyskie|śląskie|warmińsko\-mazurskie|wielkopolskie|zachodniopomorskie|bethlehem|deir\
            el\ balah|gaza|hebron|jerusalem|jenin|jericho\ \-\ al\ aghwar|khan\
            yunis|nablus|north\
            gaza|qalqilya|ramallah|rafah|salfit|tubas|tulkarm|aveiro|beja|braga|bragança|castelo\
            branco|coimbra|évora|faro|guarda|leiria|lisboa|portalegre|porto|santarém|setúbal|viana\
            do\ castelo|vila\ real|viseu|região\ autónoma\ dos\ açores|região\
            autónoma\ da\
            madeira|aimeliik|airai|angaur|hatobohei|kayangel|koror|melekeok|ngaraard|ngarchelong|ngardmau|ngatpang|ngchesar|ngeremlengui|ngiwal|peleliu|sonsorol|concepción|alto\
            paraná|central|ñeembucú|amambay|canindeyú|presidente\ hayes|alto\
            paraguay|boquerón|san\
            pedro|cordillera|guairá|caaguazú|caazapá|itapúa|misiones|paraguarí|asunción|ad\
            dawhah|al\ khawr\ wa\ adh\ dhakhīrah|ash\ shamal|ar\ rayyan|umm\
            salal|al\ wakrah|az̧\
            z̧a‘āyin|alba|argeș|arad|bucurești|bacău|bihor|bistrița\-năsăud|brăila|botoșani|brașov|buzău|cluj|călărași|caraș\-severin|constanța|covasna|dâmbovița|dolj|gorj|galați|giurgiu|hunedoara|harghita|ilfov|ialomița|iași|mehedinți|maramureș|mureș|neamț|olt|prahova|sibiu|sălaj|satu\
            mare|suceava|tulcea|timiș|teleorman|vâlcea|vrancea|vaslui|beograd|severnobački\
            okrug|srednjebanatski\ okrug|severnobanatski\ okrug|južnobanatski\
            okrug|zapadnobački\ okrug|južnobački\ okrug|sremski\
            okrug|mačvanski\ okrug|kolubarski\ okrug|podunavski\
            okrug|braničevski\ okrug|šumadijski\ okrug|pomoravski\ okrug|borski\
            okrug|zaječarski\ okrug|zlatiborski\ okrug|moravički\ okrug|raški\
            okrug|rasinski\ okrug|nišavski\ okrug|toplički\ okrug|pirotski\
            okrug|jablanički\ okrug|pčinjski\ okrug|kosovski\ okrug|pećki\
            okrug|prizrenski\ okrug|kosovsko\-mitrovački\
            okrug|kosovsko\-pomoravski\
            okrug|kosovo\-metohija|vojvodina|adygeya,\ respublika|altay,\
            respublika|altayskiy\ kray|amurskaya\ oblast'|arkhangel'skaya\
            oblast'|astrakhanskaya\ oblast'|bashkortostan,\
            respublika|belgorodskaya\ oblast'|bryanskaya\ oblast'|buryatiya,\
            respublika|chechenskaya\ respublika|chelyabinskaya\
            oblast'|chukotskiy\ avtonomnyy\ okrug|chuvashskaya\
            respublika|dagestan,\ respublika|respublika\
            ingushetiya|irkutiskaya\ oblast'|ivanovskaya\ oblast'|kamchatskiy\
            kray|kabardino\-balkarskaya\ respublika|karachayevo\-cherkesskaya\
            respublika|krasnodarskiy\ kray|kemerovskaya\
            oblast'|kaliningradskaya\ oblast'|kurganskaya\ oblast'|khabarovskiy\
            kray|khanty\-mansiysky\ avtonomnyy\ okrug\-yugra|kirovskaya\
            oblast'|khakasiya,\ respublika|kalmykiya,\ respublika|kaluzhskaya\
            oblast'|komi,\ respublika|kostromskaya\ oblast'|kareliya,\
            respublika|kurskaya\ oblast'|krasnoyarskiy\ kray|leningradskaya\
            oblast'|lipetskaya\ oblast'|magadanskaya\ oblast'|mariy\ el,\
            respublika|mordoviya,\ respublika|moskovskaya\
            oblast'|moskva|murmanskaya\ oblast'|nenetskiy\ avtonomnyy\
            okrug|novgorodskaya\ oblast'|nizhegorodskaya\
            oblast'|novosibirskaya\ oblast'|omskaya\ oblast'|orenburgskaya\
            oblast'|orlovskaya\ oblast'|permskiy\ kray|penzenskaya\
            oblast'|primorskiy\ kray|pskovskaya\ oblast'|rostovskaya\
            oblast'|ryazanskaya\ oblast'|sakha,\ respublika\
            \[yakutiya\]|sakhalinskaya\ oblast'|samaraskaya\
            oblast'|saratovskaya\ oblast'|severnaya\ osetiya\-alaniya,\
            respublika|smolenskaya\ oblast'|sankt\-peterburg|stavropol'skiy\
            kray|sverdlovskaya\ oblast'|tatarstan,\ respublika|tambovskaya\
            oblast'|tomskaya\ oblast'|tul'skaya\ oblast'|tverskaya\
            oblast'|tyva,\ respublika\ \[tuva\]|tyumenskaya\
            oblast'|udmurtskaya\ respublika|ul'yanovskaya\
            oblast'|volgogradskaya\ oblast'|vladimirskaya\ oblast'|vologodskaya\
            oblast'|voronezhskaya\ oblast'|yamalo\-nenetskiy\ avtonomnyy\
            okrug|yaroslavskaya\ oblast'|yevreyskaya\ avtonomnaya\
            oblast'|zabajkal'skij\ kraj|ville\ de\ kigali|est|nord|ouest|sud|ar\
            riyāḍ|makkah|al\ madīnah|ash\ sharqīyah|al\ qaşīm|ḥā'il|tabūk|al\
            ḥudūd\ ash\ shamāliyah|jīzan|najrān|al\ bāhah|al\
            jawf|`asīr|central|choiseul|capital\ territory\
            \(honiara\)|guadalcanal|isabel|makira|malaita|rennell\ and\
            bellona|temotu|western|anse\ aux\ pins|anse\ boileau|anse\
            etoile|anse\ louis|anse\ royale|baie\ lazare|baie\ sainte\
            anne|beau\ vallon|bel\ air|bel\ ombre|cascade|glacis|grand\ anse\
            mahe|grand\ anse\ praslin|la\ digue|english\ river|mont\
            buxton|mont\ fleuri|plaisance|pointe\ larue|port\ glaud|saint\
            louis|takamaka|les\ mamelles|roche\ caiman|zalingei|sharq\
            dārfūr|shamāl\ dārfūr|janūb\ dārfūr|gharb\ dārfūr|al\ qaḑārif|al\
            jazīrah|kassalā|al\ kharţūm|shamāl\ kurdufān|janūb\ kurdufān|an\
            nīl\ al\ azraq|ash\ shamālīyah|an\ nīl|an\ nīl\ al\ abyaḑ|al\ baḩr\
            al\ aḩmar|sinnār|stockholms\ län|västerbottens\ län|norrbottens\
            län|uppsala\ län|södermanlands\ län|östergötlands\ län|jönköpings\
            län|kronobergs\ län|kalmar\ län|gotlands\ län|blekinge\ län|skåne\
            län|hallands\ län|västra\ götalands\ län|värmlands\ län|örebro\
            län|västmanlands\ län|dalarnas\ län|gävleborgs\ län|västernorrlands\
            län|jämtlands\ län|central\ singapore|north\ east|north\ west|south\
            east|south\ west|ascension|saint\ helena|tristan\ da\
            cunha|ajdovščina|beltinci|bled|bohinj|borovnica|bovec|brda|brezovica|brežice|tišina|celje|cerklje\
            na\ gorenjskem|cerknica|cerkno|črenšovci|črna\ na\
            koroškem|črnomelj|destrnik|divača|dobrepolje|dobrova\-polhov\
            gradec|dol\ pri\ ljubljani|domžale|dornava|dravograd|duplek|gorenja\
            vas\-poljane|gorišnica|gornja\ radgona|gornji\ grad|gornji\
            petrovci|grosuplje|šalovci|hrastnik|hrpelje\-kozina|idrija|ig|ilirska\
            bistrica|ivančna\
            gorica|izola/isola|jesenice|juršinci|kamnik|kanal|kidričevo|kobarid|kobilje|kočevje|komen|koper/capodistria|kozje|kranj|kranjska\
            gora|krško|kungota|kuzma|laško|lenart|lendava/lendva|litija|ljubljana|ljubno|ljutomer|logatec|loška\
            dolina|loški\
            potok|luče|lukovica|majšperk|maribor|medvode|mengeš|metlika|mežica|miren\-kostanjevica|mislinja|moravče|moravske\
            toplice|mozirje|murska\ sobota|muta|naklo|nazarje|nova\ gorica|novo\
            mesto|odranci|ormož|osilnica|pesnica|piran/pirano|pivka|podčetrtek|podvelka|postojna|preddvor|ptuj|puconci|rače\-fram|radeče|radenci|radlje\
            ob\ dravi|radovljica|ravne\ na\ koroškem|ribnica|rogašovci|rogaška\
            slatina|rogatec|ruše|semič|sevnica|sežana|slovenj\ gradec|slovenska\
            bistrica|slovenske\ konjice|starče|sveti\
            jurij|šenčur|šentilj|šentjernej|šentjur|škocjan|škofja\
            loka|škofljica|šmarje\ pri\ jelšah|šmartno\ ob\
            paki|šoštanj|štore|tolmin|trbovlje|trebnje|tržič|turnišče|velenje|velike\
            lašče|videm|vipava|vitanje|vodice|vojnik|vrhnika|vuzenica|zagorje\
            ob\ savi|zavrč|zreče|železniki|žiri|benedikt|bistrica\ ob\
            sotli|bloke|braslovče|cankova|cerkvenjak|dobje|dobrna|dobrovnik/dobronak|dolenjske\
            toplice|grad|hajdina|hoče\-slivnica|hodoš/hodos|horjul|jezersko|komenda|kostel|križevci|lovrenc\
            na\ pohorju|markovci|miklavž\ na\ dravskem\ polju|mirna\
            peč|oplotnica|podlehnik|polzela|prebold|prevalje|razkrižje|ribnica\
            na\ pohorju|selnica\ ob\ dravi|sodražica|solčava|sveta\ ana|sveta\
            andraž\ v\ slovenskih\ goricah|šempeter\-vrtojba|tabor|trnovska\
            vas|trzin|velika\
            polana|veržej|vransko|žalec|žetale|žirovnica|žužemberk|šmartno\ pri\
            litiji|apače|cirkulane|kosanjevica\ na\
            krki|makole|mokronog\-trebelno|poljčane|renče\-vogrsko|središče\ ob\
            dravi|straža|sveta\ trojica\ v\ slovenskih\ goricah|sveti\
            tomaž|šmarjeske\ topliče|gorje|log\-dragomer|rečica\ ob\
            savinji|sveti\ jurij\ v\ slovenskih\
            goricah|šentrupert|banskobystrický\ kraj|bratislavský\ kraj|košický\
            kraj|nitriansky\ kraj|prešovský\ kraj|trnavský\ kraj|trenčiansky\
            kraj|žilinský\ kraj|eastern|northern|southern\ \(sierra\
            leone\)|western\ area\
            \(freetown\)|acquaviva|chiesanuova|domagnano|faetano|fiorentino|borgo\
            maggiore|san\
            marino|montegiardino|serravalle|diourbel|dakar|fatick|kaffrine|kolda|kédougou|kaolack|louga|matam|sédhiou|saint\-louis|tambacounda|thiès|ziguinchor|awdal|bakool|banaadir|bari|bay|galguduud|gedo|hiirsan|jubbada\
            dhexe|jubbada\ hoose|mudug|nugaal|saneag|shabeellaha\
            dhexe|shabeellaha\ hoose|sool|togdheer|woqooyi\
            galbeed|brokopondo|commewijne|coronie|marowijne|nickerie|paramaribo|para|saramacca|sipaliwini|wanica|northern\
            bahr\ el\ ghazal|western\ bahr\ el\ ghazal|central\
            equatoria|eastern\ equatoria|western\ equatoria|jonglei|lakes|upper\
            nile|unity|warrap|príncipe|são\
            tomé|ahuachapán|cabañas|chalatenango|cuscatlán|la\
            libertad|morazán|la\ paz|santa\ ana|san\ miguel|sonsonate|san\
            salvador|san\ vicente|la\ unión|usulután|dimashq|dar'a|dayr\ az\
            zawr|al\ hasakah|homs|halab|hamah|idlib|al\ ladhiqiyah|al\
            qunaytirah|ar\ raqqah|rif\ dimashq|as\
            suwayda'|tartus|hhohho|lubombo|manzini|shiselweni|al\ baṭḩah|baḩr\
            al\ ghazāl|būrkū|shārī\ bāqirmī|innīdī|qīrā|ḥajjar\ lamīs|kānim|al\
            buḩayrah|lūqūn\ al\ gharbī|lūqūn\ ash\ sharqī|māndūl|shārī\ al\
            awsaṭ|māyū\ kībbī\ ash\ sharqī|māyū\ kībbī\ al\ gharbī|madīnat\
            injamīnā|waddāy|salāmāt|sīlā|tānjilī|tibastī|wādī\ fīrā|région\ du\
            centre|région\ de\ la\ kara|région\ maritime|région\ des\
            plateaux|région\ des\ savannes|krung\ thep\ maha\ nakhon\
            bangkok|samut\ prakan|nonthaburi|pathum\ thani|phra\ nakhon\ si\
            ayutthaya|ang\ thong|lop\ buri|sing\ buri|chai\ nat|saraburi|chon\
            buri|rayong|chanthaburi|trat|chachoengsao|prachin\ buri|nakhon\
            nayok|sa\ kaeo|nakhon\ ratchasima|buri\ ram|surin|si\ sa\ ket|ubon\
            ratchathani|yasothon|chaiyaphum|amnat\ charoen|nong\ bua\ lam\
            phu|khon\ kaen|udon\ thani|loei|nong\ khai|maha\ sarakham|roi\
            et|kalasin|sakon\ nakhon|nakhon\ phanom|mukdahan|chiang\
            mai|lamphun|lampang|uttaradit|phrae|nan|phayao|chiang\ rai|mae\
            hong\ son|nakhon\ sawan|uthai\ thani|kamphaeng\
            phet|tak|sukhothai|phitsanulok|phichit|phetchabun|ratchaburi|kanchanaburi|suphan\
            buri|nakhon\ pathom|samut\ sakhon|samut\
            songkhram|phetchaburi|prachuap\ khiri\ khan|nakhon\ si\
            thammarat|krabi|phangnga|phuket|surat\
            thani|ranong|chumphon|songkhla|satun|trang|phatthalung|pattani|yala|narathiwat|phatthaya|gorno\-badakhshan|khatlon|sughd|aileu|ainaro|baucau|bobonaro|cova\
            lima|díli|ermera|lautem|liquiça|manufahi|manatuto|oecussi|viqueque|ahal|balkan|daşoguz|lebap|mary|aşgabat|tunis|ariana|ben\
            arous|la\ manouba|nabeul|zaghouan|bizerte|béja|jendouba|le\
            kef|siliana|kairouan|kasserine|sidi\
            bouzid|sousse|monastir|mahdia|sfax|gafsa|tozeur|kebili|gabès|medenine|tataouine|'eua|ha'apai|niuas|tongatapu|vava'u|adana|adıyaman|afyonkarahisar|ağrı|amasya|ankara|antalya|artvin|aydın|balıkesir|bilecik|bingöl|bitlis|bolu|burdur|bursa|çanakkale|çankırı|çorum|denizli|diyarbakır|edirne|elazığ|erzincan|erzurum|eskişehir|gaziantep|giresun|gümüşhane|hakkâri|hatay|isparta|mersin|i̇stanbul|i̇zmir|kars|kastamonu|kayseri|kırklareli|kırşehir|kocaeli|konya|kütahya|malatya|manisa|kahramanmaraş|mardin|muğla|muş|nevşehir|niğde|ordu|rize|sakarya|samsun|siirt|sinop|sivas|tekirdağ|tokat|trabzon|tunceli|şanlıurfa|uşak|van|yozgat|zonguldak|aksaray|bayburt|karaman|kırıkkale|batman|şırnak|bartın|ardahan|iğdır|yalova|karabük|kilis|osmaniye|düzce|arima|chaguanas|couva\-tabaquite\-talparo|diego\
            martin|eastern\ tobago|penal\-debe|port\ of\ spain|princes\
            town|point\ fortin|rio\ claro\-mayaro|san\ fernando|sangre\
            grande|siparia|san\ juan\-laventille|tunapuna\-piarco|western\
            tobago|funafuti|niutao|nukufetau|nukulaelae|nanumea|nanumanga|nui|vaitupu|changhua|chiay\
            city|chiayi|hsinchu|hsinchui\ city|hualien|ilan|keelung\
            city|kaohsiung\
            city|kaohsiung|miaoli|nantou|penghu|pingtung|taoyuan|tainan\
            city|tainan|taipei\ city|taipei|taitung|taichung\
            city|taichung|yunlin|arusha|dar\-es\-salaam|dodoma|iringa|kagera|kaskazini\
            pemba|kaskazini\ unguja|kigoma|kilimanjaro|kusini\ pemba|kusini\
            unguja|lindi|mara|mbeya|mjini\
            magharibi|morogoro|mtwara|mwanza|pwani|rukwa|ruvuma|shinyanga|singida|tabora|tanga|manyara|vinnyts'ka\
            oblast'|volyns'ka\ oblast'|luhans'ka\ oblast'|dnipropetrovs'ka\
            oblast'|donets'ka\ oblast'|zhytomyrs'ka\ oblast'|zakarpats'ka\
            oblast'|zaporiz'ka\ oblast'|ivano\-frankivs'ka\ oblast'|kyïvs'ka\
            mis'ka\ rada|kyïvs'ka\ oblast'|kirovohrads'ka\
            oblast'|sevastopol|respublika\ krym|l'vivs'ka\ oblast'|mykolaïvs'ka\
            oblast'|odes'ka\ oblast'|poltavs'ka\ oblast'|rivnens'ka\
            oblast'|sums\ 'ka\ oblast'|ternopil's'ka\ oblast'|kharkivs'ka\
            oblast'|khersons'ka\ oblast'|khmel'nyts'ka\ oblast'|cherkas'ka\
            oblast'|chernihivs'ka\ oblast'|chernivets'ka\
            oblast'|kalangala|kampala|kiboga|luwero|masaka|mpigi|mubende|mukono|nakasongola|rakai|sembabule|kayunga|wakiso|mityana|nakaseke|lyantonde|bugiri|busia|iganga|jinja|kamuli|kapchorwa|katakwi|kumi|mbale|pallisa|soroti|tororo|kaberamaido|mayuge|sironko|amuria|budaka|bukwa|butaleja|kaliro|manafwa|namutumba|bududa|bukedea|adjumani|apac|arua|gulu|kitgum|kotido|lira|moroto|moyo|nebbi|nakapiripirit|pader|yumbe|amolatar|kaabong|koboko|abim|dokolo|amuru|maracha|oyam|bundibugyo|bushenyi|hoima|kabale|kabarole|kasese|kibaale|kisoro|masindi|mbarara|ntungamo|rukungiri|kamwenge|kanungu|kyenjojo|ibanda|isingiro|kiruhura|buliisa|central|eastern|northern|western|johnston\
            atoll|midway\ islands|navassa\ island|wake\ island|baker\
            island|howland\ island|jarvis\ island|kingman\ reef|palmyra\
            atoll|alaska|alabama|arkansas|american\
            samoa|arizona|california|colorado|connecticut|district\ of\
            columbia|delaware|florida|georgia|guam|hawaii|iowa|idaho|illinois|indiana|kansas|kentucky|louisiana|massachusetts|maryland|maine|michigan|minnesota|missouri|northern\
            mariana\ islands|mississippi|montana|north\ carolina|north\
            dakota|nebraska|new\ hampshire|new\ jersey|new\ mexico|nevada|new\
            york|ohio|oklahoma|oregon|pennsylvania|puerto\ rico|rhode\
            island|south\ carolina|south\ dakota|tennessee|texas|united\ states\
            minor\ outlying\ islands|utah|virginia|virgin\
            islands|vermont|washington|wisconsin|west\
            virginia|wyoming|artigas|canelones|cerro\
            largo|colonia|durazno|florida|flores|lavalleja|maldonado|montevideo|paysandú|río\
            negro|rocha|rivera|salto|san\ josé|soriano|tacuarembó|treinta\ y\
            tres|andijon|buxoro|farg'ona|jizzax|namangan|navoiy|qashqadaryo|qoraqalpog'iston\
            respublikasi|samarqand|sirdaryo|surxondaryo|toshkent|toshkent|xorazm|charlotte|saint\
            andrew|saint\ david|saint\ george|saint\
            patrick|grenadines|distrito\
            federal|anzoátegui|apure|aragua|barinas|bolívar|carabobo|cojedes|falcón|guárico|lara|mérida|miranda|monagas|nueva\
            esparta|portuguesa|sucre|táchira|trujillo|yaracuy|zulia|dependencias\
            federales|vargas|delta\ amacuro|amazonas|lai\ châu|lào\ cai|hà\
            giang|cao\ bằng|sơn\ la|yên\ bái|tuyên\ quang|lạng\ sơn|quảng\
            ninh|hoà\ bình|hà\ tây|ninh\ bình|thái\ bình|thanh\ hóa|nghệ\ an|hà\
            tỉnh|quảng\ bình|quảng\ trị|thừa\ thiên\-huế|quảng\ nam|kon\
            tum|quảng\ ngãi|gia\ lai|bình\ định|phú\ yên|đắc\ lắk|khánh\
            hòa|lâm\ đồng|ninh\ thuận|tây\ ninh|đồng\ nai|bình\ thuận|long\
            an|bà\ rịa\-vũng\ tàu|an\ giang|đồng\ tháp|tiền\ giang|kiên\
            giang|vĩnh\ long|bến\ tre|trà\ vinh|sóc\ trăng|bắc\ kạn|bắc\
            giang|bạc\ liêu|bắc\ ninh|bình\ dương|bình\ phước|cà\ mau|hải\
            duong|hà\ nam|hưng\ yên|nam\ định|phú\ thọ|thái\ nguyên|vĩnh\
            phúc|điện\ biên|đắk\ nông|hậu\ giang|cần\ thơ|đà\ nẵng|hà\ nội|hải\
            phòng|hồ\ chí\ minh\ \[sài\
            gòn\]|malampa|pénama|sanma|shéfa|taféa|torba|a'ana|aiga\-i\-le\-tai|atua|fa'asaleleaga|gaga'emauga|gagaifomauga|palauli|satupa'itea|tuamasaga|va'a\-o\-fonoti|vaisigano|abyān|'adan|'amrān|al\
            bayḑā'|aḑ\ ḑāli‘|dhamār|ḩaḑramawt|ḩajjah|ibb|al\
            jawf|laḩij|ma'rib|al\ mahrah|al\ ḩudaydah|al\
            maḩwīt|raymah|şa'dah|shabwah|şan'ā'|tā'izz|eastern\ cape|free\
            state|gauteng|limpopo|mpumalanga|northern\
            cape|kwazulu\-natal|north\-west\ \(south\ africa\)|western\
            cape|western|central|eastern|luapula|northern|north\-western|southern\
            \(zambia\)|copperbelt|lusaka|bulawayo|harare|manicaland|mashonaland\
            central|mashonaland\ east|midlands|matabeleland\ north|matabeleland\
            south|masvingo|mashonaland\ west)$
          title: Region Name
        city:
          type: string
          maxLength: 256
          title: City
        linkedin:
          type: string
          maxLength: 2048
          pattern: >-
            ^(https?:)?//(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+[a-z\u00a1-\uffff]{2,}\.?(?:[/?#]\S*)?$
          format: uri
          title: Linkedin
        experience:
          items:
            type: object
          type: array
          title: Experience
        skills:
          items:
            type: string
          type: array
          title: Skills
        interests:
          items:
            type: string
          type: array
          title: Interests
        age_group:
          type: string
          title: Age Group
        education:
          items:
            type: object
          type: array
          title: Education
        gender:
          type: string
          enum:
            - male
            - female
          title: Gender
        company_name:
          type: string
          maxLength: 256
          title: Company Name
        company_website:
          type: string
          maxLength: 2048
          pattern: >-
            ^(https?:)?//(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+[a-z\u00a1-\uffff]{2,}\.?(?:[/?#]\S*)?$
          format: uri
          title: Company Website
        company_linkedin:
          type: string
          maxLength: 2048
          pattern: >-
            ^(https?:)?//(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+[a-z\u00a1-\uffff]{2,}\.?(?:[/?#]\S*)?$
          format: uri
          title: Company Linkedin
        job_department:
          $ref: '#/components/schemas/JobDepartmentEnrichment'
        job_department_array:
          items:
            $ref: '#/components/schemas/JobDepartment'
          type: array
        job_department_main:
          $ref: '#/components/schemas/JobDepartment'
        job_seniority_level:
          $ref: '#/components/schemas/JobLevel'
        job_level_array:
          items:
            $ref: '#/components/schemas/JobSeniorityLevel'
          type: array
        job_level_main:
          $ref: '#/components/schemas/JobSeniorityLevel'
        job_title:
          type: string
          title: Job Title
        linkedin_url_array:
          items:
            type: string
            maxLength: 2048
            pattern: >-
              ^(https?:)?//(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+[a-z\u00a1-\uffff]{2,}\.?(?:[/?#]\S*)?$
            format: uri
          type: array
          title: Linkedin Url Array
      type: object
      title: ProfilesOutputSchema
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
    JobDepartmentEnrichment:
      type: string
      enum:
        - Real estate
        - Customer service
        - Trades
        - Unknown
        - Public relations
        - Legal
        - Operations
        - Media
        - Sales
        - Marketing
        - Finance
        - Engineering
        - Education
        - General
        - Health
        - Design
        - Human resources
      title: JobDepartmentEnrichment
      description: >-
        The `JobDepartmentEnrichment` enum for enrichment responses with
        enhanced taxonomy.

        This is used for v1 fields from enrichment.
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
    JobLevel:
      type: string
      enum:
        - owner
        - cxo
        - vp
        - director
        - senior
        - manager
        - partner
        - non-managerial
        - entry
        - training
        - unpaid
        - unknown
      title: JobLevel
      description: |-
        The `JobLevel` enum for enrichment responses with enhanced taxonomy.
        This is used for v1 fields from enrichment.
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
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````