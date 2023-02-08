from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	message = 'only the owner can perform this action'
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
				return True
		print(obj.owner)
		print(request.user)
		return obj.owner is request.user