Factorial Technical test
Scenario: Lead Routing & Enrichment Flow
Our SDRs struggle with slow lead assignment and poor data quality. We want to automate the enrichment of new leads and route them based on geography, company size, and intent.
Task:
Build a simplified version of the following flow using any stack/language/tool you're comfortable with:
Trigger: A new contact is created in HubSpot (or simulate with a mock input JSON).
Enrichment: Simulate an enrichment by calling an external API (e.g., Clearbit mock or dummy function).
Routing Logic: Based on country and company size, assign an owner_id (can be a hardcoded routing map).
Output: Print or log a final JSON with enriched and routed lead.
Bonus (Optional):
Store the final result in a mock S3 bucket or local JSON store.
Wrap it as a function or reusable module.
Use Node/Python/N8N/AWS Lambda to show your preferred style.
Take into account Owner variables for a better routing (CR / pipeline)