from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

# Complete Database of 35 Categories and 180 Problems & Solutions for Tamil Nadu
DATABASE = {
    "1. Public Administration and Home": {
        "1. Problem: Delay in receiving government certificates and services.": (
            "Solution: Submit an application through the relevant government"
            " service centre or online portal and keep the acknowledgement"
            " number. If the application is delayed beyond the prescribed"
            " period, submit a grievance to the responsible officer and use the"
            " applicable appeal procedure."
        ),
        "2. Problem: Corruption while obtaining government services.": (
            "Solution: Keep evidence such as receipts and messages, and report"
            " suspected bribery to the appropriate vigilance or"
            " anti-corruption authority. Do not pay unofficial fees. Request an"
            " acknowledgement or complaint reference number."
        ),
        (
            "3. Problem: Police refusing to register a complaint about a"
            " cognizable offence."
        ): (
            "Solution: Submit the complaint in writing to the Superintendent of"
            " Police or other appropriate senior police authority. Depending on"
            " the circumstances, seek assistance from a lawyer or the"
            " jurisdictional Magistrate under the applicable criminal"
            " procedure law."
        ),
        (
            "4. Problem: Citizens are unaware of their rights and government"
            " services."
        ): (
            "Solution: Ask the relevant government department for its official"
            " service list, eligibility conditions and application process."
            " Use government information portals and, where appropriate, file"
            " a Right to Information (RTI) application to obtain public"
            " information."
        ),
        (
            "5. Problem: Misuse of public funds or irregularities in government"
            " offices."
        ): (
            "Solution: Submit a documented complaint to the department's"
            " grievance authority, vigilance authority or other competent"
            " oversight body. An RTI application may help obtain records that"
            " can support a complaint, subject to legal exemptions."
        ),
    },
    "2. Rural Development and Water Resources": {
        "6. Problem: Shortage of drinking water in a village.": (
            "Solution: File a written complaint with the responsible local body"
            " or water-supply authority. Request an inspection and details of"
            " the repair or supply schedule. Escalate the complaint to the"
            " relevant higher-level department if the issue remains unresolved."
        ),
        "7. Problem: Poor maintenance of village roads and public buildings.": (
            "Solution: Report the damaged road or building to the responsible"
            " local body or public works authority, providing photographs and"
            " the exact location of the asset. Request an inspection and"
            " complaint number, then follow up through the department's"
            " grievance process."
        ),
        "8. Problem: Poor drainage and stagnant wastewater in residential areas.":
        (
            "Solution: Submit a complaint to the local sanitation or public"
            " health authority and request drainage clearance and inspection."
            " If the problem creates a public-health risk and is not"
            " addressed, escalate it to the relevant district-level health or"
            " local-government authority."
        ),
        (
            "9. Problem: Eligible rural families are unable to obtain housing"
            " assistance."
        ): (
            "Solution: Contact the rural development office or the official"
            " implementing authority to check the current housing scheme,"
            " eligibility rules and beneficiary list. Submit the required"
            " documents and appeal through the prescribed process if an"
            " eligible application is wrongly rejected."
        ),
        "10. Problem: Water bodies are polluted or illegally encroached upon.": (
            "Solution: Report the issue to the responsible water resources,"
            " revenue or pollution-control authority, attaching available"
            " evidence. Request an official inspection and action under the"
            " applicable water-protection, environmental or land laws."
        ),
    },
    "3. Public Works and Sports Development": {
        "11. Problem: Unsafe public buildings due to structural damage.": (
            "Solution: Report cracks, damaged roofs or other hazards to the"
            " building-owning department or local authority. Request a"
            " structural inspection and written confirmation of the safety"
            " measures required."
        ),
        "12. Problem: Unsafe bridges and damaged public infrastructure.": (
            "Solution: Notify the responsible roads or public works authority"
            " and request an urgent inspection. If there is immediate danger,"
            " inform the police or emergency services so the area can be"
            " secured."
        ),
        "13. Problem: Lack of safe public playgrounds and sports facilities.": (
            "Solution: Submit a request to the local body or sports department"
            " asking for access to existing facilities or repairs to unsafe"
            " equipment. Ask for the relevant maintenance plan and eligibility"
            " rules for public sports programmes."
        ),
        (
            "14. Problem: Eligible students cannot access government sports"
            " training or competition opportunities."
        ): (
            "Solution: Contact the school sports coordinator or the relevant"
            " sports department to obtain details of trials, training"
            " programmes, scholarships and selection criteria. Apply within the"
            " stated deadline and use the official appeal process if selection"
            " procedures are not followed."
        ),
    },
    "4. Health and Family Welfare": {
        "15. Problem: A low-income family cannot afford hospital treatment.": (
            "Solution: Approach the government hospital's help desk and ask"
            " about free treatment and applicable government health schemes."
            " Submit the required documents and check eligibility for cashless"
            " treatment. If an eligible benefit is denied, complain to the"
            " scheme's grievance authority."
        ),
        "16. Problem: A patient cannot afford prescribed medicines.": (
            "Solution: Ask the government hospital whether the prescribed"
            " medicines are available through its pharmacy or an applicable"
            " public medicine scheme. If they are unavailable, ask the treating"
            " doctor about suitable alternatives and the official process for"
            " obtaining them."
        ),
        (
            "17. Problem: Pregnant women cannot access eligible maternal"
            " healthcare benefits."
        ): (
            "Solution: Contact the nearest government health facility or"
            " authorised health worker to register for antenatal care and check"
            " eligibility for maternity benefits. Submit the required"
            " documents and seek help from the health department if an"
            " eligible benefit is delayed."
        ),
        (
            "18. Problem: People cannot access mental-health support because"
            " of cost or lack of information."
        ): (
            "Solution: Contact a government hospital or public health service"
            " and request a mental-health consultation. Ask about free or"
            " subsidised treatment and referral services. If access is denied,"
            " submit a grievance to the responsible health authority."
        ),
        (
            "19. Problem: Eligible families are unaware of vaccination and"
            " preventive-health services."
        ): (
            "Solution: Contact a government health facility to obtain the"
            " official vaccination schedule and available services. Ask the"
            " health worker to explain eligibility, timings and any required"
            " records."
        ),
    },
    "5. Revenue and Disaster Management": {
        "20. Problem: Delay in obtaining an income certificate.": (
            "Solution: Apply through the authorised government service portal"
            " or service centre and retain the application receipt. If the"
            " prescribed processing period passes, submit a grievance to the"
            " revenue authority and use the applicable appeal process."
        ),
        "21. Problem: Delay or errors in community or other revenue certificates.":
        (
            "Solution: Submit the application and supporting documents required"
            " by the official rules. If the certificate is delayed or contains"
            " an error, request correction or appeal to the competent revenue"
            " officer."
        ),
        (
            "22. Problem: Eligible families cannot obtain government"
            " disaster-relief assistance."
        ): (
            "Solution: Report the damage to the relevant revenue or"
            " disaster-management authority, submit the required evidence and"
            " apply under the applicable relief rules. If the claim is"
            " rejected, request the reason in writing and ask about the"
            " prescribed review or appeal procedure."
        ),
        "23. Problem: People do not receive timely warnings about natural disasters.":
        (
            "Solution: Follow official alerts issued by disaster-management and"
            " weather authorities. Report failures in warning systems to the"
            " responsible authority and request information about local"
            " emergency procedures and evacuation arrangements."
        ),
        (
            "24. Problem: A person faces an unlawful land-record entry or"
            " property-record error."
        ): (
            "Solution: Obtain the relevant land records and submit a"
            " correction request to the competent revenue authority. If the"
            " dispute concerns ownership or legal title, consult a lawyer or"
            " seek eligible free legal aid to determine the appropriate court"
            " or legal procedure."
        ),
    },
    "6. Food and Civil Supplies": {
        "25. Problem: An eligible family is unable to obtain a ration card.": (
            "Solution: Apply through the authorised public distribution or"
            " civil supplies service and submit the required documents. If the"
            " application is rejected or delayed, ask for the reason in writing"
            " and appeal through the designated authority."
        ),
        (
            "26. Problem: A ration shop refuses to provide an eligible household's"
            " entitled supplies."
        ): (
            "Solution: Keep the ration card details and any transaction record,"
            " then complain to the civil supplies department through its"
            " official grievance channel. Request an investigation and retain"
            " the complaint reference number."
        ),
        "27. Problem: A ration card contains incorrect family details.": (
            "Solution: Apply for correction through the authorised civil"
            " supplies portal or service centre, supplying the required"
            " supporting records. Follow up with the responsible officer if the"
            " correction is not completed within the prescribed period."
        ),
        (
            "28. Problem: A ration shop charges an unauthorised amount or"
            " demands unofficial payment."
        ): (
            "Solution: Preserve receipts or other available evidence and report"
            " the matter to the civil supplies department or appropriate"
            " vigilance authority. Request a complaint number and follow up"
            " through the official process."
        ),
        "29. Problem: Eligible families are unaware of food-security benefits.": (
            "Solution: Contact the civil supplies department or an authorised"
            " service centre to check eligibility for available food-security"
            " benefits and the documents needed to apply. Use the official"
            " grievance or appeal process if an eligible application is wrongly"
            " denied."
        ),
    },
    "7. Electricity and Law": {
        "30. Problem: Frequent power cuts or prolonged power-supply interruptions.":
        (
            "Solution: Register a service complaint with the electricity"
            " distribution authority and record the complaint number. If the"
            " issue is not resolved, escalate it to the appropriate supervisory"
            " officer or consumer grievance redressal forum."
        ),
        "31. Problem: Incorrect electricity bills or unexplained charges.": (
            "Solution: Submit a written billing dispute to the electricity"
            " distribution office, attaching the bill and relevant meter"
            " readings or payment records. If unresolved, approach the"
            " applicable consumer grievance forum and follow its appeal"
            " procedure."
        ),
        "32. Problem: A household cannot afford its electricity charges.": (
            "Solution: Ask the electricity distribution authority whether the"
            " household qualifies for any applicable tariff concession or"
            " government benefit. Request the official eligibility rules and"
            " apply with the required documents rather than relying on an"
            " unofficial promise of exemption."
        ),
        "33. Problem: A person cannot afford a lawyer for a legal dispute.": (
            "Solution: Contact the District Legal Services Authority or"
            " another appropriate Legal Services Authority and ask whether they"
            " qualify for free legal aid under the Legal Services Authorities"
            " Act, 1987. Eligible applicants may receive legal advice or"
            " representation."
        ),
        (
            "34. Problem: A citizen's legal rights are violated but they do not"
            " know where to complain."
        ): (
            "Solution: Identify the authority responsible for the particular"
            " violation and submit a written complaint with supporting"
            " evidence. Depending on the issue, the remedy may involve the"
            " police, a regulator, a statutory commission or a court. Seek"
            " legal aid if eligible."
        ),
    },
    "8. School Education, Tamil Development and Information": {
        (
            "35. Problem: An eligible child cannot access school education"
            " because of financial hardship."
        ): (
            "Solution: Approach the school head or the education department to"
            " ask about applicable free-education provisions, fee exemptions,"
            " textbooks, uniforms and other student benefits. Where relevant,"
            " refer to Article 21A of the Constitution and the Right of"
            " Children to Free and Compulsory Education Act, 2009."
        ),
        "36. Problem: A student is denied an eligible scholarship.": (
            "Solution: Check the scholarship's official eligibility rules,"
            " application status and required documents. Submit a grievance to"
            " the scholarship authority or education department and use the"
            " specified appeal process if the application was wrongly rejected."
        ),
        (
            "37. Problem: A school lacks safe drinking water, toilets or basic"
            " facilities."
        ): (
            "Solution: Submit a written complaint to the school head and the"
            " responsible education authority, requesting an inspection and"
            " corrective action. If a serious safety or sanitation issue"
            " remains unresolved, escalate it to the competent public-health"
            " or education authority."
        ),
        "38. Problem: A student faces discrimination or harassment at school.": (
            "Solution: Report the incident to the school head and the"
            " appropriate education authority. If the conduct involves a"
            " criminal offence, serious abuse or unlawful discrimination,"
            " seek assistance from the police or the competent statutory"
            " authority. A parent or student can also seek legal aid where"
            " eligible."
        ),
        (
            "39. Problem: A student cannot access learning support or"
            " educational materials."
        ): (
            "Solution: Ask the school and education department about available"
            " textbooks, learning resources, remedial classes and eligible"
            " student-support programmes. Submit a written request if an"
            " entitled resource is not provided."
        ),
        (
            "40. Problem: Citizens cannot obtain public information about"
            " government decisions or services."
        ): (
            "Solution: Submit a request to the relevant department or file an"
            " RTI application with the appropriate public information officer."
            " If information is denied or no response is received within the"
            " statutory period, use the applicable first or second appeal"
            " process under the RTI Act, 2005."
        ),
    },
    "9. Natural Resources and Mines": {
        "41. Problem: Suspected illegal mining damages public land or property.": (
            "Solution: Report the suspected activity to the competent mining,"
            " revenue or police authority, providing available evidence."
            " Request an inspection and action under the applicable mining and"
            " environmental laws."
        ),
        "42. Problem: Dust and noise from quarrying affect nearby residents.": (
            "Solution: Submit a complaint to the relevant pollution-control"
            " authority and mining department, requesting inspection of permits"
            " and compliance with environmental conditions. Escalate the matter"
            " through the prescribed grievance or legal process if violations"
            " are found."
        ),
        "43. Problem: A person is harmed by unsafe mining operations.": (
            "Solution: Report immediate danger to the police and the responsible"
            " safety or mining authority. Seek medical treatment, preserve"
            " relevant records and ask the competent authority about"
            " compensation or other remedies available under the applicable"
            " law."
        ),
        (
            "44. Problem: Natural resources are extracted without the required"
            " authorisation."
        ): (
            "Solution: Report the suspected unauthorised extraction to the"
            " relevant regulatory authority, with dates and supporting evidence"
            " where available. Request verification of permits and enforcement"
            " action under the applicable rules."
        ),
        (
            "45. Problem: Citizens cannot obtain information about approved"
            " mining activities."
        ): (
            "Solution: Ask the responsible mining or environmental authority"
            " for publicly available permits, clearances and compliance"
            " records. If the information is not supplied through ordinary"
            " channels, submit an RTI request, subject to applicable disclosure"
            " exemptions."
        ),
    },
    "10. Industries and Investment Promotion": {
        (
            "46. Problem: A person wants to start a business but does not know"
            " the required approvals."
        ): (
            "Solution: Contact the official state industry facilitation service"
            " or the relevant licensing department to obtain the current list of"
            " registrations, permits and eligibility requirements. Apply"
            " through authorised channels and retain the acknowledgements."
        ),
        (
            "47. Problem: An eligible entrepreneur cannot access a government"
            " business-support scheme."
        ): (
            "Solution: Ask the implementing department or authorised bank about"
            " current schemes, eligibility criteria, required documents and"
            " application deadlines. If an eligible application is wrongly"
            " rejected, request written reasons and use the designated"
            " grievance process."
        ),
        (
            "48. Problem: A business faces an unexplained delay in a government"
            " licence or approval."
        ): (
            "Solution: Track the application using its acknowledgement number"
            " and submit a grievance to the department responsible for the"
            " approval. If a statutory deadline or appeal mechanism applies,"
            " follow that procedure."
        ),
        (
            "49. Problem: A small business faces an unlawful demand for payment"
            " by an official."
        ): (
            "Solution: Preserve available evidence and report the suspected"
            " demand to the appropriate vigilance or anti-corruption authority."
            " Avoid making unofficial payments and seek legal advice if the"
            " business faces retaliation or threats."
        ),
        (
            "50. Problem: A person loses money because of a misleading business"
            " or investment promise."
        ): (
            "Solution: Preserve agreements, receipts and messages. Report"
            " suspected fraud to the police or appropriate financial"
            " regulator, depending on the circumstances. If the issue is a"
            " consumer dispute, use the applicable consumer grievance or"
            " redressal mechanism."
        ),
    },
    "11. Higher Education": {
        "51. Problem: An eligible student cannot afford college fees.": (
            "Solution: Contact the college's scholarship or student welfare"
            " office and the relevant government education department to check"
            " fee concessions, scholarships and financial assistance. Submit"
            " the required documents and appeal through the official process if"
            " an eligible benefit is denied."
        ),
        (
            "52. Problem: A student is unaware of government scholarships for"
            " higher education."
        ): (
            "Solution: Check the official scholarship portals and the relevant"
            " department's notifications for schemes matching the student's"
            " eligibility. Apply before the deadline and retain the"
            " acknowledgement for tracking."
        ),
        (
            "53. Problem: A college refuses to issue a certificate or academic"
            " record without a clear reason."
        ): (
            "Solution: Submit a written request to the college administration"
            " and ask for the applicable rule and reason for refusal. If"
            " unresolved, approach the affiliating university or competent"
            " higher-education authority and use the available grievance or"
            " appeal process."
        ),
        "54. Problem: A student faces discrimination or harassment in a college.":
        (
            "Solution: Report the incident through the institution's designated"
            " grievance mechanism and the competent higher-education authority."
            " If the conduct involves a crime or unlawful discrimination,"
            " approach the appropriate police or statutory authority and seek"
            " legal aid if eligible."
        ),
        (
            "55. Problem: A student cannot afford accommodation or other"
            " essential study expenses."
        ): (
            "Solution: Ask the college and relevant government department about"
            " eligible hostel assistance, scholarships and student welfare"
            " schemes. Submit the required proof of eligibility and appeal if"
            " an eligible application is wrongly rejected."
        ),
    },
    "12. Tourism": {
        (
            "56. Problem: Visitors are charged unauthorised fees at a public"
            " tourist attraction."
        ): (
            "Solution: Keep the ticket or other evidence and complain to the"
            " tourism department or authority managing the attraction. Ask for"
            " the official fee schedule and request an investigation into the"
            " extra charge."
        ),
        "57. Problem: A tourist attraction has unsafe facilities.": (
            "Solution: Report the hazard to the attraction's management and"
            " responsible public authority. If there is immediate danger, alert"
            " the police or emergency services and request that the unsafe"
            " area be secured."
        ),
        (
            "58. Problem: Visitors cannot find reliable information about"
            " official tourist facilities."
        ): (
            "Solution: Use official tourism department information channels"
            " and request verified details from the managing authority. Report"
            " inaccurate public information to the responsible department so"
            " it can be corrected."
        ),
        "59. Problem: A tourist is cheated by a service provider.": (
            "Solution: Preserve receipts, messages and booking details. Submit"
            " a complaint to the relevant tourism or consumer authority; if"
            " fraud or a criminal offence is suspected, report it to the"
            " police."
        ),
        (
            "60. Problem: A tourism facility is inaccessible to a person with a"
            " disability."
        ): (
            "Solution: Submit a written request to the facility's managing"
            " authority for accessible entry and reasonable access"
            " arrangements. Where disability-access requirements are violated,"
            " approach the competent disability-rights authority under the"
            " Rights of Persons with Disabilities Act, 2016."
        ),
    },
    "13. Minorities Welfare": {
        (
            "61. Problem: An eligible minority student cannot obtain a"
            " government scholarship."
        ): (
            "Solution: Check the current official scholarship conditions and"
            " apply through the authorised portal or department. If an"
            " eligible application is rejected or delayed, submit a grievance"
            " with the application reference number and supporting documents."
        ),
        (
            "62. Problem: An eligible family does not know about minority welfare"
            " schemes."
        ): (
            "Solution: Contact the relevant minority welfare department or"
            " authorised service centre for the current list of schemes,"
            " eligibility conditions and required documents. Apply through the"
            " official process and retain the acknowledgement."
        ),
        (
            "63. Problem: A person faces religious discrimination in access to a"
            " public service."
        ): (
            "Solution: Document the incident and complain to the responsible"
            " public authority. Depending on the facts, seek assistance from"
            " the police, the appropriate statutory commission or a court."
            " Article 15 of the Constitution prohibits specified forms of"
            " discrimination by the State, including discrimination on grounds"
            " of religion."
        ),
        "64. Problem: A minority welfare application remains unresolved.": (
            "Solution: Track the application and submit a written grievance to"
            " the scheme's implementing authority. Request the reason for delay"
            " or rejection and use the prescribed appeal mechanism if"
            " available."
        ),
        (
            "65. Problem: A person is threatened or attacked because of their"
            " religion."
        ): (
            "Solution: If there is immediate danger, contact the police or"
            " emergency services. Submit a formal complaint and preserve"
            " available evidence. Seek medical assistance if needed and legal"
            " aid if eligible; the police should assess the incident under the"
            " applicable criminal law."
        ),
    },
    "14. Adi Dravidar Welfare and Social Justice": {
        (
            "66. Problem: An eligible student cannot access an Adi Dravidar"
            " welfare scholarship or educational benefit."
        ): (
            "Solution: Apply through the authorised welfare department or"
            " scholarship portal with the required documents. If an eligible"
            " benefit is denied, request written reasons and use the official"
            " grievance or appeal process."
        ),
        (
            "67. Problem: A person faces caste-based discrimination or is denied"
            " access to a public service."
        ): (
            "Solution: Document the incident and report it to the responsible"
            " authority. If the facts indicate an offence, approach the police"
            " and ask that the complaint be handled under the applicable law,"
            " including the Scheduled Castes and the Scheduled Tribes"
            " (Prevention of Atrocities) Act, 1989, where its conditions are"
            " met."
        ),
        (
            "68. Problem: An eligible family cannot obtain a welfare benefit"
            " because of a documentation issue."
        ): (
            "Solution: Ask the implementing department which documents are"
            " legally required and how missing or incorrect records can be"
            " corrected. Submit the correction request and use the designated"
            " appeal process if the benefit is wrongly refused."
        ),
        (
            "69. Problem: A person is subjected to untouchability or related"
            " unlawful exclusion."
        ): (
            "Solution: Report the incident to the police or the competent"
            " authority. Article 17 of the Constitution abolishes"
            " untouchability, and the Protection of Civil Rights Act, 1955,"
            " provides legal measures against specified related practices."
        ),
        (
            "70. Problem: A person eligible for social-justice-related legal"
            " assistance cannot afford representation."
        ): (
            "Solution: Contact the District Legal Services Authority and ask"
            " about eligibility for free legal aid. Explain the issue and"
            " provide the documents requested so the authority can assess the"
            " assistance available."
        ),
    },
    "15. Transport": {
        (
            "71. Problem: A passenger is charged more than the authorised public"
            " transport fare."
        ): (
            "Solution: Keep the ticket and details of the journey, then"
            " complain to the transport operator or competent transport"
            " authority. Request verification against the official fare schedule"
            " and retain the complaint reference number."
        ),
        (
            "72. Problem: A bus or other public transport service is unsafe or"
            " poorly maintained."
        ): (
            "Solution: Report the defect to the transport operator and the"
            " responsible transport authority. If there is immediate danger,"
            " alert the police or emergency services and avoid using the"
            " unsafe vehicle."
        ),
        (
            "73. Problem: A person with a disability cannot access public"
            " transport."
        ): (
            "Solution: Submit a complaint to the transport authority identifying"
            " the access barrier and requesting the applicable accessibility"
            " measures. If disability rights are not respected, approach the"
            " competent disability-rights authority under the relevant law."
        ),
        (
            "74. Problem: A passenger is injured in a transport accident and"
            " does not know how to seek compensation."
        ): (
            "Solution: Obtain medical records, preserve tickets and other"
            " relevant evidence, and report the accident to the appropriate"
            " authority. Seek advice from a lawyer or the Legal Services"
            " Authority about the applicable compensation process and deadlines."
        ),
        (
            "75. Problem: A citizen cannot obtain a driving licence or"
            " vehicle-related service despite meeting the requirements."
        ): (
            "Solution: Track the application through the official transport"
            " service and submit a written grievance to the licensing"
            " authority. If the application is rejected, ask for the reasons"
            " and use the prescribed review or appeal process."
        ),
    },
    "16. Housing and Urban Development": {
        (
            "76. Problem: An eligible family cannot obtain government housing"
            " assistance."
        ): (
            "Solution: Contact the department implementing the applicable"
            " housing scheme and check the current eligibility rules and"
            " beneficiary list. Submit the required documents and appeal"
            " through the designated process if the application is wrongly"
            " rejected."
        ),
        "77. Problem: A tenant faces unlawful eviction or an unfair housing dispute.":
        (
            "Solution: Keep the rental agreement, payment records and relevant"
            " communications. Seek advice from a lawyer or legal aid service"
            " about the applicable tenancy law and the appropriate court or"
            " authority. If threats or violence occur, contact the police."
        ),
        (
            "78. Problem: A building has an unsafe structure or violates"
            " applicable building rules."
        ): (
            "Solution: Report the suspected violation to the competent building"
            " or planning authority and request an inspection. If the building"
            " presents an immediate danger, alert emergency services and the"
            " authority responsible for public safety."
        ),
        (
            "79. Problem: A resident faces an unresolved sewage or"
            " waste-management problem."
        ): (
            "Solution: Submit a complaint to the responsible local body or"
            " sanitation authority, requesting inspection and corrective action."
            " If the problem poses a serious public-health risk, escalate it to"
            " the competent public-health authority."
        ),
        (
            "80. Problem: A person cannot obtain approval or records relating"
            " to a building or property."
        ): (
            "Solution: Apply to the competent planning, local-government or"
            " registration authority for the relevant record or approval. If"
            " there is an unexplained refusal or delay, request written reasons"
            " and use the prescribed grievance or appeal procedure."
        ),
    },
    "17. Backward Classes Welfare": {
        (
            "81. Problem: An eligible student cannot access a Backward Classes"
            " welfare scholarship."
        ): (
            "Solution: Apply through the official welfare department or"
            " scholarship portal and provide the required documents. If an"
            " eligible application is rejected or delayed, submit a grievance"
            " with the application reference."
        ),
        (
            "82. Problem: A person eligible for a community certificate faces"
            " an unexplained delay."
        ): (
            "Solution: Apply through the authorised revenue service and track"
            " the application. If the certificate is delayed or refused,"
            " request the reason in writing and use the prescribed appeal"
            " procedure."
        ),
        (
            "83. Problem: An eligible family does not know about a welfare or"
            " educational assistance scheme."
        ): (
            "Solution: Contact the relevant welfare department or authorised"
            " government service centre for current scheme details. Confirm"
            " eligibility, submit the required application and retain the"
            " acknowledgement."
        ),
        (
            "84. Problem: A student is denied an eligible hostel or educational"
            " support benefit."
        ): (
            "Solution: Ask the implementing institution or welfare department"
            " for the written reason for refusal. If the student meets the"
            " scheme's conditions, file a grievance and appeal through the"
            " official process."
        ),
        (
            "85. Problem: A welfare benefit is delayed after an application has"
            " been approved."
        ): (
            "Solution: Obtain the application or sanction reference and submit"
            " a written status request to the implementing department. If"
            " payment remains pending, escalate the matter through the"
            " department's grievance mechanism."
        ),
    },
    "18. Handlooms, Textiles and Khadi": {
        (
            "86. Problem: An eligible handloom worker cannot access a"
            " government welfare benefit."
        ): (
            "Solution: Contact the relevant handloom or textile department or"
            " authorised cooperative and ask about current worker-welfare"
            " schemes. Submit the required worker records and apply through the"
            " official procedure."
        ),
        "87. Problem: A handloom worker is not paid for completed work.": (
            "Solution: Preserve work orders, delivery records and payment"
            " communications. Submit a written demand to the employer or"
            " contracting organisation and seek assistance from the"
            " appropriate labour authority or court, depending on the"
            " employment arrangement."
        ),
        (
            "88. Problem: An eligible artisan cannot obtain support under a"
            " government training or development scheme."
        ): (
            "Solution: Contact the scheme's implementing department for the"
            " current eligibility rules, application dates and required"
            " documents. If eligible, apply through the authorised channel and"
            " appeal if the application is wrongly rejected."
        ),
        "89. Problem: A textile worker faces unsafe working conditions.": (
            "Solution: Report the safety issue to the employer and the"
            " competent labour or factory-inspection authority. If there is"
            " immediate danger, move away from the hazard and contact the"
            " appropriate emergency service."
        ),
        "90. Problem: A handloom producer is cheated in a business transaction.":
        (
            "Solution: Preserve invoices, purchase orders and messages. Seek"
            " payment through the applicable contractual or civil remedy, and"
            " report suspected fraud to the police where the facts support a"
            " criminal complaint. Ask the relevant department about any eligible"
            " artisan-support service."
        ),
    },
    "19. Prohibition and Excise": {
        "91. Problem: Illegal sale of alcohol creates a safety risk.": (
            "Solution: Report suspected illegal sales to the police or the"
            " competent excise authority, providing factual details and any"
            " safely obtained evidence. Do not confront suspected offenders"
            " yourself."
        ),
        (
            "92. Problem: A person is harmed by the sale of unsafe or illicit"
            " liquor."
        ): (
            "Solution: Seek urgent medical treatment and inform the police or"
            " excise authority. Preserve relevant evidence if safe to do so and"
            " cooperate with the official investigation."
