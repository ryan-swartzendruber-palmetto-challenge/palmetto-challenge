def get_usage_profile_example_response():
    data = {
        "status": "success",
        "count": 1,
        "type": "UsageProfile",
        "results": [
            {
                "profileId": "b7559f37-8020-4969-8bd1-48d8c3d58976",
                "providerProfileId": "ELECTRICITY_RESIDENTIAL_CA_2012",
                "profileName": "2012 CA Electricity Residential Profile",
                "accountId": "4b1dd606-a72a-46b2-8c12-34db20be69fa",
                "description": "Residential Electricity Profile",
                "serviceTypes": "ELECTRICITY",
                "source": {
                    "sourceId": "ReadingEntry",
                    "name": "Readings"
                },
                "isDefault": True,
                "dataStatus": 2,
                "properties": None,
                "readingDataSummaries": [
                    {
                    "quantityUnit": "kWh",
                    "fromDateTime": "2012-01-01T00:00:00+00:00",
                    "toDateTime": "2013-01-01T00:00:00+00:00",
                    "numberOfReadings": 12
                    }
                ],
                "readings": {
                    "totalCount": 12,
                    "pageCount": 0,
                    "pageStart": 0
                },
                "intervals": {
                    "totalCount": 12,
                    "pageCount": 25,
                    "pageStart": 0,
                    "list": [
                        {
                            "fromDateTime": "2012-01-01T00:00:00+00:00",
                            "toDateTime": "2012-02-01T00:00:00+00:00",
                            "duration": 2678400000,
                            "kWh": {
                                "quantityAmount": 699.9998,
                                "rateAmount": 0
                            },
                            "kW": {
                                "quantityAmount": 0.94086,
                                "rateAmount": 0
                            }
                        },
                        {
                            "fromDateTime": "2012-12-01T00:00:00+00:00",
                            "toDateTime": "2013-01-01T00:00:00+00:00",
                            "duration": 2678400000,
                            "kWh": {
                                "quantityAmount": 699.9998,
                                "rateAmount": 0
                            },
                            "kW": {
                                "quantityAmount": 0.94086,
                                "rateAmount": 0
                            }
                        }
                    ]
                }
            }
        ]
    }

    return data