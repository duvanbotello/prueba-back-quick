from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from apps.users.models import Users
from apps.users.api.serializers import UserSerializer


@api_view(['GET'])
def api_anything(request, resource):
    if request.method == 'GET':
        return Response({"error": "Not found"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_users(request):
    if request.content_type == 'application/json':
        # list users
        if request.method == 'GET':
            users = Users.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return Response(users_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Request should have 'Content-Type' header with value 'application/json'"},
                        status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def api_users_create(request):
    if request.content_type == 'application/json':
        # create user
        if request.method == 'POST':
            request.data['password'] = make_password(request.data['password'])
            user_serializer = UserSerializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                response = user_serializer.data
                response.pop('password', None)
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Request should have 'Content-Type' header with value 'application/json'"},
                        status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getuser(request, pk=None):
    if request.content_type == 'application/json':
        # queryset
        user = Users.objects.filter(id=pk).first()

        # validation
        if user:
            # bring user
            if request.method == 'GET':
                user_serializer = UserSerializer(user)
                response = user_serializer.data
                response.pop('password', None)
                return Response(response, status=status.HTTP_200_OK)

        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Request should have 'Content-Type' header with value 'application/json'"},
                        status=status.HTTP_403_FORBIDDEN)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_user(request, pk=None):
    if request.content_type == 'application/json':
        user = Users.objects.filter(id=pk).first()
        if user:
            if request.method == 'PUT':
                if len(request.data) != 0:
                    try:
                        if request.data['password']:
                            request.data['password'] = make_password(request.data['password'])
                    except:
                        pass
                    user_serializer = UserSerializer(user, data=request.data)
                    if user_serializer.is_valid():
                        user_serializer.save()
                        response = user_serializer.data
                        response.pop('password', None)
                        return Response(response, status=status.HTTP_200_OK)
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': 'empty body'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Request should have 'Content-Type' header with value 'application/json'"},
                        status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def edit_p_user(request, pk=None):
    if request.content_type == 'application/json':
        user = Users.objects.filter(id=pk).first()
        if user:
            if request.method == 'PATCH':
                if len(request.data) != 0:
                    list_field_edit = user.edit_user_patch(request)
                    Users.objects.filter(id=pk).update(**list_field_edit)
                    user_update = Users.objects.filter(id=pk).first()
                    user_serializer = UserSerializer(user_update)
                    response = user_serializer.data
                    response.pop('password', None)
                    return Response(response, status=status.HTTP_200_OK)

                else:
                    return Response({'message': 'empty body'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Request should have 'Content-Type' header with value 'application/json'"},
                        status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_user(request, pk=None):
    if request.content_type == 'application/json':
        user = Users.objects.filter(id=pk).first()
        if user:
            # delete user
            if request.method == 'DELETE':
                user = Users.objects.filter(id=pk).first()
                user_serializer = UserSerializer(user)
                user.delete()
                return Response(user_serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Request should have 'Content-Type' header with value 'application/json'"},
                        status=status.HTTP_403_FORBIDDEN)
