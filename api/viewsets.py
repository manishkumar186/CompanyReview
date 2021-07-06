from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers
from reviewapp.models import Company, Review

@api_view(["GET","POST","PUT","DELETE"])
def company_api(request):
    if request.method == "GET":
        if "id" in request.GET:
            id = request.GET.get("id")
            detail = Company.objects.filter(id=id)
        else:
            detail = Company.objects.all()

        obj = serializers.CompanySerializer(detail,many=True)

        dt={
            "message":"{} record found".format(len(obj.data)),
            "data":obj.data,   
        }
        return Response(dt)
    
    elif request.method == "POST":
        all_data = request.data
        res = serializers.CompanySerializer(data=all_data)

        if res.is_valid():
            res.post()
            return Response(data={"message":"Your data POST successfully","data":all_data})
        else:
            return Response(res.errors)

    elif request.method == "PUT":
        all_data = request.data
        res = serializers.CompanySerializer(data=all_data)
        if res.is_valid():
            try:
                con_obj = Company.objects.get(id=all_data.get("id"))
                con_obj.company_name = all_data.get("company_name")
                con_obj.founder = all_data.get("founder")
                con_obj.description = all_data.get("description")
                con_obj.date = all_data.get("date")
                con_obj.averageRating = all_data.get("averageRating")
                con_obj.save()
                return Response({"message":"Data Updated Successfully"})
            except:
                return Response({"status":"ID Does not exists","message":"Data not update"})
        else:
            return Response(res.errors)

    elif request.method == "DELETE":
        try:
            id = request.data.get("id")
            Company.objects.get(id=id).delete()
            return Response({"status":"success","message":"Data deleted successfully"})
        except:
            return Response({"status":"Id does not exits","message":"Data not deleted"})

@api_view(["GET"])
def review_api(request):
    if request.method == "GET":
        qryset = Review.objects.all().order_by("-id")
        all_data = serializers.ReviewSerializer(qryset,many=True)
        return Response(all_data.data)