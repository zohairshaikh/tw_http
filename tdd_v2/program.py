

"""
Write an API server


path 1
POST short_me/
body {
   "long_url": xxxx,
}

GET give_my_long_url/<short_url>
* Update analytics
* redirects to long url


POST share_metrics/
body {
   "short_url": "xxxx",
   "long_url": "xxxx"
}




* Auth layer not required
* Custom ORM layer for query
* Using Flask - lite weight
*

Sample DS
{
    "id": xx,
    "short_url": "url",
    "long_url": "url",
    "access_count": 0,
    "is_active": False
}

"""
