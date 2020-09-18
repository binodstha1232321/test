# from rest_framework import permissions
#
# class BlogUpdate(permissions.BasePermission):
#     '''returns true or false'''
#
#     def has_object_permission(self, request, view, obj):
#         '''Check user is trying to '''
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.id == request.user.id