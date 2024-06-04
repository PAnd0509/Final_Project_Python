from rest_framework.permissions import BasePermission

class IsManage(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return hasattr(request.user, 'waiter') and request.user.waiter.charge == 'MG'
    
class IsAdminTables(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return hasattr(request.user, 'waiter') and request.user.waiter.charge == 'AT'