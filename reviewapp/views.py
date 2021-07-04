from django.shortcuts import render,redirect
from .models import *
from django.db.models import Avg


# Create your views here.


def home(request):
    all_company = Company.objects.all()
    context = {
        "company": all_company
    }

    return render(request, "home.html", context)


def detail(request, id):

    company = Company.objects.get(id=int(id))
    review = Review.objects.filter(company=id).order_by("-comment")
    average = review.aggregate(Avg("rating"))['rating__avg']
    if average == None:
        average=0
    avg = round(average,2)
    context = {
        "companys": company,
        "review":review,
        "average":avg
    }

    return render(request, "detail.html", context)


def addcompany(request):
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.method == "POST":
                cname = request.POST["cname"]
                fname = request.POST["fname"]
                dname = request.POST["dname"]
                launchdate = request.POST["launchdate"]
                crating = request.POST["crating"]
                image = request.POST["image"]

                data = Company(company_name=cname, founder=fname, description=dname,
                            date=launchdate, averageRating=crating, image=image)
                data.save()
                return redirect("reviewapp:home")

            return render(request, "addcompany.html")
        else:
            return redirect("reviewapp:home")
    else:
        return redirect("account:login")


def editcompany(request, id):
    if request.user.is_authenticated:
        if request.user.is_active:

            data = Company.objects.get(id=int(id))
            context = {
                "data": data,
            }

            if request.method == "POST":
                cname = request.POST["cname"]
                fname = request.POST["fname"]
                dname = request.POST["dname"]
            #    launchdate = request.POST["launchdate"]
                crating = request.POST["crating"]
                image = request.POST["image"]

                data.company_name = cname
                data.founder = fname
                data.description = dname
            #    data.date=launchdate
                data.averageRating = crating
                data.image = image
                data.save()

                all_company = Company.objects.all()
                context = {
                "company": all_company
                }
                return render(request, "home.html", context)

            return render(request, "editcompany.html", context)
        else:
            return redirect("reviewapp:home")
    else:
        return redirect("account:login")



def deletecompany(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            delete_company = Company.objects.get(id=int(id))
            delete_company.delete()
            return redirect("reviewapp:home")
        else:
            return redirect("reviewapp:home")
    else:
        return redirect("account:login")

def addreview(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.method == "POST":
                company = Company.objects.get(id=int(id))
                comment = request.POST["comment"]
                rating = request.POST["rating"]
                data=Review(comment=comment,rating=rating,user=request.user,company=company)
                data.save()
                return redirect("reviewapp:detail",id)
                
            return render(request,"detail.html")
        else:
            return redirect("reviewapp:detail")
    else:
        return redirect("account:login")

def editreview(request,company_id,review_id):
    if request.user.is_authenticated:
        company = Company.objects.get(id=company_id)
        review = Review.objects.get(company=company,id=review_id)

        context={
                "review":review
            }

        if request.method == "POST":
            comment = request.POST["comment"]
            rating = request.POST["rating"]
            review.comment=comment
            review.rating=rating
            final_rating = review.rating
            if(float(final_rating)>10 or float(final_rating)<0):
                context["status"]="Out of range. Please enter rating 1 to 10.."
                return render(request,"editreview.html",context)
            else:
                review.save()        
                return redirect("reviewapp:detail",company_id)
        return render(request,"editreview.html",context)
    else:
        return redirect("account:login")

def deletereview(request,company_id,review_id):
    if request.user.is_authenticated:
        company = Company.objects.get(id=company_id)
        review = Review.objects.get(company=company,id=review_id)
        review.delete()    
        return redirect("reviewapp:detail",company_id)
    else:
        return redirect("account:login")

            
        


