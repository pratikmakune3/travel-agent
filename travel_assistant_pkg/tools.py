from typing import List, Dict, Any


class AirlineSearchTool:
    __name__ = "AirlineSearchTool"

    def __call__(
        self,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        cabin: str | None = None,
    ) -> List[Dict[str, Any]]:
        providers = [
            {
                "provider": "Air India",
                "flights": [
                    {
                        "airline": "Air India",
                        "flight": "AI322",
                        "depart": f"{depart_date} 09:15",
                        "arrive": f"{depart_date} 13:05",
                        "from": origin,
                        "to": destination,
                        "duration": "12h 30m",
                        "stops": 0,
                        "cabin": cabin or "Economy",
                        "price_usd": 420,
                    }
                ],
            },
            {
                "provider": "Emirates",
                "flights": [
                    {
                        "airline": "Emirates",
                        "flight": "EM118",
                        "depart": f"{depart_date} 20:35",
                        "arrive": f"{depart_date} 23:40",
                        "from": origin,
                        "to": destination,
                        "duration": "11h 05m",
                        "stops": 0,
                        "cabin": cabin or "Economy",
                        "price_usd": 465,
                    }
                ],
            },
            {
                "provider": "SpiceJet",
                "flights": [
                    {
                        "airline": "SpiceJet",
                        "flight": "SJ907",
                        "depart": f"{depart_date} 06:25",
                        "arrive": f"{depart_date} 10:20",
                        "from": origin,
                        "to": destination,
                        "duration": "13h 00m",
                        "stops": 0,
                        "cabin": cabin or "Economy",
                        "price_usd": 389,
                    }
                ],
            },
        ]
        return providers


class HotelSearchTool:
    __name__ = "HotelSearchTool"

    def __call__(
        self,
        city: str,
        check_in: str,
        check_out: str,
        beds: int | None = None,
        amenities: List[str] | None = None,
    ) -> List[Dict[str, Any]]:
        hotel_results = [
            {
                "brand": "Marriott",
                "name": "Marriott City Center",
                "city": city,
                "check_in": check_in,
                "check_out": check_out,
                "beds": beds or 1,
                "amenities": ["wifi", "gym", "breakfast"],
                "price_usd_per_night": 210,
                "rating": 4.5,
            },
            {
                "brand": "Sheraton",
                "name": "Sheraton Express Downtown",
                "city": city,
                "check_in": check_in,
                "check_out": check_out,
                "beds": beds or 1,
                "amenities": ["wifi", "breakfast"],
                "price_usd_per_night": 150,
                "rating": 4.1,
            },
            {
                "brand": "Accor",
                "name": "Novotel Riverside",
                "city": city,
                "check_in": check_in,
                "check_out": check_out,
                "beds": beds or 1,
                "amenities": ["wifi", "pool", "spa"],
                "price_usd_per_night": 185,
                "rating": 4.3,
            },
        ]
        if amenities:
            amenities_lower = {a.lower() for a in amenities}
            hotel_results = [
                h for h in hotel_results if amenities_lower.issubset(set(map(str.lower, h["amenities"])))
            ]
        return hotel_results


