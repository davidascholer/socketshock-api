from django.http import HttpResponse, JsonResponse
import requests
from rest_framework import status
import json

from api.services.cloudfront_signer import sign_url
 
def vinyl_list(request):

    # example url: .../api/vinyl/?id=MichaelJackson_Thriller

    try:
        # Open the JSON file
        with open('api/data/list_data.json') as f:
            # Load the JSON data into a Python dictionary
            vinyl_data = json.load(f)

    except:
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    data = vinyl_data

    artist = request.GET.get('artist')
    if artist:
        data = filter(lambda x: artist in x['artist'], vinyl_data)
    # for val in vinyl_data:
    #     if val['id'] == id:
    #         data = val
    #         break
    
    # Set page-size
    page_size_param = request.GET.get('page-size')
    page_size = page_size_param if page_size_param else 3

    # Set page
    page_param = request.GET.get('page')
    page = page_param if page_param else 1

    # Paginate
    start_index = (int(page) - 1) * int(page_size)
    end_index = start_index + int(page_size)
    data = data[start_index:end_index]

    # Add image urls to each item
    for val in data:
        url = sign_url(f'/vinyl/{val["id"]}_image.jpg')
        val["image_url"] = url
    
    # Serialize the data
    serializable_response = {"data": data}
    json_string_response = json.dumps(serializable_response)

    return HttpResponse(json_string_response, status=status.HTTP_200_OK)

def vinyl_detail(request, id):

    if not id:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    print("id",id)
    try:
        # example url: .../api/vinyl/detail/MichaelJackson_Thriller/
        url = sign_url(f'/vinyl/data/detail/{id}.json')

        # To retch that data and return it as the response
        # response = requests.get(url)
        # return_obj = {"data":response.content.decode()}
        # return_obj = {"data":response.content.decode()}
        # return HttpResponse(JsonResponse(return_obj), status.HTTP_200_OK)

        # To just return the link as the response
        return_obj = {"data": {"url" : url}}
        return HttpResponse(JsonResponse(return_obj), status.HTTP_200_OK)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
    
