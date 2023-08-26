import datetime
from .serializers import AttendanceSerializer
from .models import Attendance
from rest_framework import permissions, generics, response


class ListCreateAttendanceView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        date = self.request.GET.get('date')
        id = self.request.GET.get('id')
        if date and id:
            return Attendance.objects.filter(finger_id = id, timestamp__date=date)
        elif date:
            return Attendance.objects.filter(timestamp__date=date)
        elif id:
            return Attendance.objects.filter(finger_id = id)
        return Attendance.objects.all()


    def post(self, request, *args, **kwargs):
        finger_id = kwargs.get("finger_id")
        record = Attendance.objects.filter(finger_id = finger_id, timestamp__date=datetime.datetime.now())
        if record:
            return response.Response(status=200, data="Attendance already taken")
        request.data.update({"finger_id":finger_id})
        return super().post(request, *args, **kwargs)
    



