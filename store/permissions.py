from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina ko'rish uchun ruhsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # o'zgartirish yani yozish uchun ruhsat post muallifiga beriladi
        return obj.author == request.user
    