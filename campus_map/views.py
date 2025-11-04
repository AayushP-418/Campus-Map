from django.shortcuts import render


def campus_map_view(request):
    """
    View for displaying the interactive Georgia Tech campus map.
    """
    # Georgia Tech campus landmarks with coordinates
    landmarks = [
        {
            'name': 'Tech Tower',
            'latitude': 33.7756,
            'longitude': -84.3963,
            'description': 'The iconic Tech Tower, the main administrative building of Georgia Tech.'
        },
        {
            'name': 'Bobby Dodd Stadium',
            'latitude': 33.7725,
            'longitude': -84.3933,
            'description': 'Home of the Georgia Tech Yellow Jackets football team.'
        },
        {
            'name': 'Klaus Advanced Computing Building',
            'latitude': 33.7775,
            'longitude': -84.3958,
            'description': 'State-of-the-art computing facility housing the College of Computing.'
        },
        {
            'name': 'Student Center',
            'latitude': 33.7750,
            'longitude': -84.3980,
            'description': 'The heart of student life with dining, events, and student services.'
        },
        {
            'name': 'Library',
            'latitude': 33.7765,
            'longitude': -84.3975,
            'description': 'Price Gilbert Library - the main library on campus.'
        },
        {
            'name': 'Campus Recreation Center',
            'latitude': 33.7730,
            'longitude': -84.3950,
            'description': 'CRC - Campus recreation and fitness facility.'
        },
        {
            'name': 'Clough Undergraduate Learning Commons',
            'latitude': 33.7745,
            'longitude': -84.3965,
            'description': 'CULC - Modern study and collaboration space for students.'
        },
        {
            'name': 'Tech Green',
            'latitude': 33.7755,
            'longitude': -84.3965,
            'description': 'The central green space on campus, a popular gathering area.'
        },
    ]
    
    context = {
        'landmarks': landmarks,
    }
    
    return render(request, 'campus_map/map.html', context)

