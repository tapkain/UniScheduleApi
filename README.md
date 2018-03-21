# UniScheduleApi
This api is designed to transform data from various providers into common models, that will be consumed by iOS and Android clients respectively.

## Endpoints
* **GET api/v1/universities** - get list of all supported universities, example `["IFNTUNG", "LNY", "KPI"]`
* **GET api/v1/groups/university={UNIVERSITY_ID}** - get list of all groups for the desired university
*  **GET api/v1/schedule/university={UNIVERSITY_ID}&group_id={GROUP_ID}** - get list of all unique lessons for the desired group
