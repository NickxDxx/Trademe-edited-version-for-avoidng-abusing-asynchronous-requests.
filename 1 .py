import time
import asyncio
import aiohttp
from datetime import datetime
import csv
import re





async def get_responses(number):
    stringnumber = str(number)
    print("Start at " + stringnumber)
    params = {
        }
    async with aiohttp.ClientSession() as session:
        async with session.get(url = url,headers = headers, params = params) as resp:
            very_raw = await resp.json()
            
            
            '''Data comparison'''
            for current_dic_number in range(len(very_raw["List"])):
                local_dic = very_raw["List"][current_dic_number]
                print(local_dic)
                local_key_list = []
                final_list = []
                for keys in local_dic:
                    if keys not in low_list:
                        local_key_list.append(keys)
                for key in long:
                    if key not in local_key_list:
                        final_list.append("/")
                    '''Data processing'''    
                    elif key == "StartDate" or key == "EndDate":
                        new_key = str(datetime.fromtimestamp(int(re.findall('\d+', local_dic[key])[0]) / 1000))
                        final_list.append(new_key)
                    elif key == "OpenHomes":
                        if len(local_dic[key]) == 1:
                            local_dic[key][0]["Start"] = str(datetime.fromtimestamp(
                                int(re.findall('\d+', local_dic["OpenHomes"][0]["Start"])[0]) / 1000))
                            local_dic[key][0]["End"] = str(datetime.fromtimestamp(
                                int(re.findall('\d+', local_dic["OpenHomes"][0]["End"])[0]) / 1000))
                            final_list.append(local_dic[key])
                        elif len(local_dic[key]) == 2:
                            local_dic[key][0]["Start"] = str(datetime.fromtimestamp(
                                int(re.findall('\d+', local_dic["OpenHomes"][0]["Start"])[0]) / 1000))
                            local_dic[key][0]["End"] = str(datetime.fromtimestamp(
                                int(re.findall('\d+', local_dic["OpenHomes"][0]["End"])[0]) / 1000))
                            local_dic[key][1]["Start"] = str(datetime.fromtimestamp(
                                int(re.findall('\d+', local_dic["OpenHomes"][1]["Start"])[0]) / 1000))
                            local_dic[key][1]["End"] = str(datetime.fromtimestamp(
                                int(re.findall('\d+', local_dic["OpenHomes"][1]["End"])[0]) / 1000))
                            final_list.append(local_dic[key])
                        else:
                            final_list.append(" ")
                    else:
                        final_list.append(local_dic[key])

                # with open("120920223.csv", "a", newline="") as file:
                #     writer = csv.writer(file)
                #     writer.writerow(final_list)
            print("Finished " + stringnumber)



async def main():
    tasks = []
    for number in range(1, 64):
        tasks.append(get_responses(number))
    await asyncio.gather(*tasks)


if __name__ == '__main__':

    long = ['ListingId', 'StartDate', 'Title', 'EndDate', 'Region', 'Suburb', 'OpenHomes', 'GeographicLocation',
            'PriceDisplay', 'HasEmbeddedVideo', 'Has3DTour', 'Address', 'District', 'Area', 'LandArea', 'Bathrooms',
            'Bedrooms', 'Parking', 'PropertyType', 'RateableValue', 'AdjacentSuburbNames', 'Agency', 'TotalParking']
    low_list = ['StartPrice', 'Category', 'AsAt', 'CategoryPath', 'PictureHref', 'RegionId', 'ListingLength',
                'IsFeatured', 'HasGallery', 'IsBold', 'IsHighlighted', 'IsClassified', 'NoteDate', 'SuburbId',
                'ReserveState', 'PhotoUrls', 'AdditionalData', 'ListingGroup', 'ListingExtras', 'MemberId',
                'AgencyReference', 'DistrictId', 'AdjacentSuburbIds', ]
    headers = {
        'authority': 'api.trademe.co.nz',
        'method': 'GET',
        'accept': 'pplication/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,en-US;q=0.9',
        'cache-control': 'max-age=0',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQzODYzOCIsImFwIjoiMzgwMDc2Nzg0IiwiaWQiOiIxOGZjMWRkNzM1YTE4MmViIiwidHIiOiI4NGRiNzIyODE2Yjk1NzhjZDEzMTIxYjc3MGQ3MzQwMCIsInRpIjoxNjcwMjg3Mjg0NzU2fX0=',
        'origin': 'https://www.trademe.co.nz',
        'referer': 'https://www.trademe.co.nz/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'some-site',
        'upgrade-insecure-requests': '1',
        # 'x-trademe-uniqueclientid': '51f6a3d6-24e6-c673-45fe-8646ad15be04'

    }
    url = "https://api.trademe.co.nz/v1/search"

    with open("120920222.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(long)
    start = time.time()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    stop = time.time()
    print(stop - start)


# if __name__ == '__main__':
#
#     with Pool(5) as p:
#         print(p.map(get_data, terms))

    # text = raw.split(",")
    # print(text[0:4])
    # print(text)
    # stop = time.time()
    # running_time = stop - start

