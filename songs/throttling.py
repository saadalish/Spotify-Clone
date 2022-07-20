from rest_framework.throttling import UserRateThrottle


class AlbumListCreateRateThrottle(UserRateThrottle):
    scope = 'album'
    rate = '2/day'
