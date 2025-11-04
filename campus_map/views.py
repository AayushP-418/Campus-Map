from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Landmark, LandmarkPhoto
from .forms import PhotoUploadForm

def campus_map_view(request):
    landmarks = Landmark.objects.all()

    if not landmarks.exists():
        landmarks_data = [
            {
                'id': 1,
                'name': 'Tech Tower',
                'latitude': 33.7756,
                'longitude': -84.3963,
                'description': 'The iconic Tech Tower, the main administrative building of Georgia Tech.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=Tech+Tower+1', 'caption': 'Tech Tower - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Tech+Tower+2', 'caption': 'Tech Tower - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Tech+Tower+3', 'caption': 'Tech Tower - Photo 3'},
                ]
            },
            {
                'id': 2,
                'name': 'Bobby Dodd Stadium',
                'latitude': 33.7725,
                'longitude': -84.3933,
                'description': 'Home of the Georgia Tech Yellow Jackets football team.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=Bobby+Dodd+Stadium+1', 'caption': 'Bobby Dodd Stadium - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Bobby+Dodd+Stadium+2', 'caption': 'Bobby Dodd Stadium - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Bobby+Dodd+Stadium+3', 'caption': 'Bobby Dodd Stadium - Photo 3'},
                ]
            },
            {
                'id': 3,
                'name': 'Klaus Advanced Computing Building',
                'latitude': 33.7775,
                'longitude': -84.3958,
                'description': 'State-of-the-art computing facility housing the College of Computing.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=Klaus+Building+1', 'caption': 'Klaus Building - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Klaus+Building+2', 'caption': 'Klaus Building - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Klaus+Building+3', 'caption': 'Klaus Building - Photo 3'},
                ]
            },
            {
                'id': 4,
                'name': 'Student Center',
                'latitude': 33.7750,
                'longitude': -84.3980,
                'description': 'The heart of student life with dining, events, and student services.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=Student+Center+1', 'caption': 'Student Center - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Student+Center+2', 'caption': 'Student Center - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Student+Center+3', 'caption': 'Student Center - Photo 3'},
                ]
            },
            {
                'id': 5,
                'name': 'Library',
                'latitude': 33.7765,
                'longitude': -84.3975,
                'description': 'Price Gilbert Library - the main library on campus.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=Library+1', 'caption': 'Library - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Library+2', 'caption': 'Library - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Library+3', 'caption': 'Library - Photo 3'},
                ]
            },
            {
                'id': 6,
                'name': 'Campus Recreation Center',
                'latitude': 33.7730,
                'longitude': -84.3950,
                'description': 'CRC - Campus recreation and fitness facility.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=CRC+1', 'caption': 'CRC - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=CRC+2', 'caption': 'CRC - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=CRC+3', 'caption': 'CRC - Photo 3'},
                ]
            },
            {
                'id': 7,
                'name': 'Clough Undergraduate Learning Commons',
                'latitude': 33.7745,
                'longitude': -84.3965,
                'description': 'CULC - Modern study and collaboration space for students.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=CULC+1', 'caption': 'CULC - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=CULC+2', 'caption': 'CULC - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=CULC+3', 'caption': 'CULC - Photo 3'},
                ]
            },
            {
                'id': 8,
                'name': 'Tech Green',
                'latitude': 33.7755,
                'longitude': -84.3965,
                'description': 'The central green space on campus, a popular gathering area.',
                'photos': [
                    {'image_url': 'https://via.placeholder.com/600x400?text=Tech+Green+1', 'caption': 'Tech Green - Photo 1'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Tech+Green+2', 'caption': 'Tech Green - Photo 2'},
                    {'image_url': 'https://via.placeholder.com/600x400?text=Tech+Green+3', 'caption': 'Tech Green - Photo 3'},
                ]
            },
        ]
    else:
        landmarks_data = []
        for landmark in landmarks:
            photos = landmark.photos.filter(is_approved=True)
            if not photos.exists():
                photos_data = [
                    {'image_url': f'https://via.placeholder.com/600x400?text={landmark.name.replace(" ", "+")}+1', 'caption': f'{landmark.name} - Photo 1'},
                    {'image_url': f'https://via.placeholder.com/600x400?text={landmark.name.replace(" ", "+")}+2', 'caption': f'{landmark.name} - Photo 2'},
                    {'image_url': f'https://via.placeholder.com/600x400?text={landmark.name.replace(" ", "+")}+3', 'caption': f'{landmark.name} - Photo 3'},
                ]
            else:
                photos_data = [{'image_url': photo.image_url_display, 'caption': photo.caption} for photo in photos]

            landmarks_data.append({
                'id': landmark.id,
                'name': landmark.name,
                'latitude': float(landmark.latitude),
                'longitude': float(landmark.longitude),
                'description': landmark.description,
                'photos': photos_data
            })

    context = {'landmarks': landmarks_data}
    return render(request, 'campus_map/map.html', context)

def landmark_detail(request, landmark_id):
    try:
        landmark = Landmark.objects.get(id=landmark_id)
        photos = landmark.photos.filter(is_approved=True)

        if not photos.exists():
            photos_data = [
                {'image_url': 'https://via.placeholder.com/800x600?text=' + landmark.name.replace(' ', '+'), 'caption': f'{landmark.name} - Photo 1'},
                {'image_url': 'https://via.placeholder.com/800x600?text=' + landmark.name.replace(' ', '+') + '+2', 'caption': f'{landmark.name} - Photo 2'},
                {'image_url': 'https://via.placeholder.com/800x600?text=' + landmark.name.replace(' ', '+') + '+3', 'caption': f'{landmark.name} - Photo 3'},
            ]
        else:
            photos_data = [{'image_url': photo.image_url_display, 'caption': photo.caption} for photo in photos]

        context = {
            'landmark': landmark,
            'photos': photos_data,
            'latitude': float(landmark.latitude),
            'longitude': float(landmark.longitude),
        }
    except Landmark.DoesNotExist:
        default_landmarks = {
            1: {'name': 'Tech Tower', 'description': 'The iconic Tech Tower, the main administrative building of Georgia Tech.', 'latitude': 33.7756, 'longitude': -84.3963},
            2: {'name': 'Bobby Dodd Stadium', 'description': 'Home of the Georgia Tech Yellow Jackets football team.', 'latitude': 33.7725, 'longitude': -84.3933},
            3: {'name': 'Klaus Advanced Computing Building', 'description': 'State-of-the-art computing facility housing the College of Computing.', 'latitude': 33.7775, 'longitude': -84.3958},
            4: {'name': 'Student Center', 'description': 'The heart of student life with dining, events, and student services.', 'latitude': 33.7750, 'longitude': -84.3980},
            5: {'name': 'Library', 'description': 'Price Gilbert Library - the main library on campus.', 'latitude': 33.7765, 'longitude': -84.3975},
            6: {'name': 'Campus Recreation Center', 'description': 'CRC - Campus recreation and fitness facility.', 'latitude': 33.7730, 'longitude': -84.3950},
            7: {'name': 'Clough Undergraduate Learning Commons', 'description': 'CULC - Modern study and collaboration space for students.', 'latitude': 33.7745, 'longitude': -84.3965},
            8: {'name': 'Tech Green', 'description': 'The central green space on campus, a popular gathering area.', 'latitude': 33.7755, 'longitude': -84.3965},
        }

        if landmark_id in default_landmarks:
            landmark_data = default_landmarks[landmark_id]
            photos_data = [
                {'image_url': 'https://via.placeholder.com/800x600?text=' + landmark_data['name'].replace(' ', '+'), 'caption': f"{landmark_data['name']} - Photo 1"},
                {'image_url': 'https://via.placeholder.com/800x600?text=' + landmark_data['name'].replace(' ', '+') + '+2', 'caption': f"{landmark_data['name']} - Photo 2"},
                {'image_url': 'https://via.placeholder.com/800x600?text=' + landmark_data['name'].replace(' ', '+') + '+3', 'caption': f"{landmark_data['name']} - Photo 3"},
            ]
            context = {
                'landmark': type('Landmark', (), {'name': landmark_data['name'], 'description': landmark_data['description']})(),
                'photos': photos_data,
                'latitude': landmark_data['latitude'],
                'longitude': landmark_data['longitude'],
            }
        else:
            from django.http import Http404
            raise Http404("Landmark not found")

    return render(request, 'campus_map/landmark_detail.html', context)

@login_required
def upload_photo(request, landmark_id):
    landmark = get_object_or_404(Landmark, id=landmark_id)

    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES, landmark=landmark, user=request.user)

        if form.is_valid():
            try:
                photo = form.save()
                messages.success(request, 'Photo uploaded successfully!')

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': True,
                        'message': 'Photo uploaded successfully!',
                        'photo': {
                            'id': photo.id,
                            'url': photo.image_url_display,
                            'caption': photo.caption,
                            'uploaded_by': photo.uploaded_by.username if photo.uploaded_by else 'Anonymous'
                        }
                    })

                return redirect('landmark_detail', landmark_id=landmark.id)

            except Exception as e:
                messages.error(request, f'Error uploading photo: {str(e)}')

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': False,
                        'message': f'Error uploading photo: {str(e)}'
                    })
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': 'Please correct the errors below.',
                    'errors': form.errors
                })

    else:
        form = PhotoUploadForm(landmark=landmark, user=request.user)

    context = {'form': form, 'landmark': landmark}
    return render(request, 'campus_map/photo_upload.html', context)

def landmark_photos_api(request, landmark_id):
    landmark = get_object_or_404(Landmark, id=landmark_id)

    photos = LandmarkPhoto.objects.filter(landmark=landmark, is_approved=True).order_by('order', '-uploaded_at')

    photos_data = []
    for photo in photos:
        photos_data.append({
            'id': photo.id,
            'url': photo.image_url_display,
            'caption': photo.caption,
            'uploaded_by': photo.uploaded_by.username if photo.uploaded_by else 'Anonymous',
            'uploaded_at': photo.uploaded_at.strftime('%Y-%m-%d %H:%M') if photo.uploaded_at else '',
            'likes': photo.likes,
            'order': photo.order
        })

    return JsonResponse({
        'success': True,
        'photos': photos_data,
        'total_photos': len(photos_data)
    })