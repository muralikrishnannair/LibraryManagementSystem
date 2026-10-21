from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from LibraryApp.models import BookDb
from LibraryApp.serializers import BookSerializer


class BookListCreateView(APIView):

    def get(self, request):
        qs=BookDb.objects.all()
        serializer_instance=BookSerializer(qs, many=True)

        return Response(data=serializer_instance.data)


    def post(self, request):
        form_data=request.data
        serializer_instance=BookSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            qs=BookDb.objects.create(**actual_data)

            return Response(data=BookSerializer(qs).data)

        else:
            return Response(data=serializer_instance.errors)


class BookRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs=get_object_or_404(BookDb, id=pk)
        serializer_instance=BookSerializer(qs)

        return Response(data=serializer_instance.data)


    def put(self, request, pk):
        qs=get_object_or_404(BookDb, id=pk)
        serializer_instance=BookSerializer(qs, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


    def delete(self, request, pk):
        qs=get_object_or_404(BookDb, id=pk)
        qs.delete()

        return Response(data={
            "Message":"Book deleted successfully...!"
        })


class IssueBookView(APIView):

    def put(self, request, pk):
        qs=get_object_or_404(BookDb, id=pk)

        if qs.quantity > 0 and qs.is_available:
            qs.quantity=qs.quantity-1

            if qs.quantity == 0:
                qs.is_available=False

            qs.save()

            return Response(data={
                "Message":"Book issued successfully...!",
                "Remaining Quantity":qs.quantity
            })

        else:
            return Response(data={
                "Message":"Book is not available...!"
            })


class ReturnBookView(APIView):

    def put(self, request, pk):
        qs=get_object_or_404(BookDb, id=pk)

        qs.quantity=qs.quantity+1
        qs.is_available=True
        qs.save()

        return Response(data={
            "Message":"Book returned successfully...!",
            "Remaining Quantity":qs.quantity
        })