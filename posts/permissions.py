from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthorOrReadonly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read only permissions for all requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions are only allowed to the author of a post
        return obj.author == request.user


class IsPostMethod(BasePermission):
    def has_permission(self, request, view):
        return request.method.upper() == 'POST'

class IsSafeMethod(BasePermission):
    def has_permission(self, request, view):
        return request.method.upper() in ('OPTIONS', 'HEAD', 'GET')
