import requests
from coordinate_finder import settings


# query function
#
# query - string of query
# type_query - search type (default: suggest)
def run_query_by(query: str, type_query: str = 'suggest'):
    response = requests.get(f'{settings.url}suggestions/api/4_1/rs/{type_query}/address',
                            {"query": query, "language": settings.language},
                            headers={"Content-Type": settings.content_type,
                                     "Accept": settings.content_type,
                                     "Authorization": "Token " + settings.token}
                            )
    return response


# function to get possible addresses on query
def get_addresses_on_query(query: str):
    response = run_query_by(query)
    if response.status_code == 200:
        result_list = []
        for elem in response.json()['suggestions']:
            result_list.append(
                {'value': elem['value'], 'fias_id': elem['data']['fias_id']}
            )
        return result_list
    else:
        return response.status_code


# function to get coordinate on fias id
def get_coords_on_query(fias_id: str):
    response = run_query_by(fias_id, 'findById')
    if response.status_code == 200:
        temp_list = response.json()['suggestions']
        result_list = {'lat': temp_list[0]['data']['geo_lat'], 'lon': temp_list[0]['data']['geo_lon']}
        return result_list
    else:
        return response.status_code
