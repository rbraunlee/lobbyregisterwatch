# Lobby Register Watch
The [Lobbyregister](https://www.lobbyregister.bundestag.de/startseite) is a valuable source of information about the lobby efforts of different groups and the legislation they are targeting. 
But to extract deeper connections, insights or historical changes isn't easy or even possible. It requires manual research and effort.
This project aims to pull the most recent data, build a history of it and extend the evaluation beyond simple grouping and wiki like linking.

State: Initializing Project
# To-Dos
## API Connector
The first step in this project is to write a connector that queries all available data via the public API. This could be a simple curl script (with which I'll start), but I want to build something solid with proper testing, error handling, and documentation. 
## EDA
After the first data pull, parallel to the API connector implementation, I'll start with a first assessment of the data and recreate the Information displayed by the Lobbyregister to verify the pulled data is correct.

The Goal of this step is to think of and define interesting data points and the relations between them.

## Transformations
At this point data is flowing in and data points are defined. Now I'll implement transformations to generate the value add to the raw data. Weapon of choice in the first step probably gonna be dbt core.

## Dashboarding
After loading the transformed data it's time to create the visualizations that make it accessible. 
For the beginning I plan on using [evidence](https://github.com/evidence-dev/evidence) (always wanted to play around with it)

## After first Implementation
Depending on the data I imagine a graph visualization to better show connections between actors, proposed regulations, expert opinions, and federal laws. This could be extended and enriched by additional data sources.




 © 2026 Rudolf Braun-Lee. All rights reserved
