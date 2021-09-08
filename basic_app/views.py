from datetime import date, datetime
from django.contrib import auth
from django.db.models.fields import EmailField
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import UserForm,UserProfileInfoForm
import uuid
from .models import UserProfileInfo
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
    
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registration.html',    
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # profile_form = UserProfileInfoForm()
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(username=username, password=password, email=email)

        # context = {}
        # context['profile_form'] = profile_form
        if user:
            # print('123')
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('index'))
                return redirect('index')
                # return redirect(request, 'index.html', context)
                
            else:
                # return HttpResponse("Your account is not active.")
                return redirect('login')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'basic_app/login.html', {})

def index(request):
    u = UserProfileInfo.objects.get(user=request.user)
    # m = str(u.dob)
    # d_t = datetime.fromtimestamp(m)
    # d = d_t.strftime("%d-%m-%Y")
    # print(d)

    # m = UserProfileInfo.objects.filter(user = request.dob)
    # old_dob=u.dob
    # split_date = str(old_dob).split('-')
    # year_d = split_date[0]
    # month_d = split_date[1]
    # date_d = split_date[2]   
    # new_dob = (date_d + '-' + month_d + '-' + year_d)
    # print(old_dob)


    context = {}
    t = str(u.dob).split('-')
    context['fname'] = u.fname
    context['lname'] = u.lname
    context['mobile'] = u.mobile
    context['dob'] = t[2]+ '-' +t[1]+ '-' +t[0]
    # print(u.dob.year)
    # print(u.dob.month)
    # print(u.dob.day)

    context['profile_pic'] = u.profile_pic
    context['gender'] = u.gender
    context['number'] = u.number
    context['address'] = u.address
    context['city'] = u.city
    context['zip'] = u.zip  
    return render(request,'basic_app/index.html', context)

# @login_required
# def special(request):
    # return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):

    logout(request)
    return redirect('user_login')


# class ProfileUpdateView(LoginRequiredMixin, TemplateView):
#     user_form = UserForm
#     profile_form = UserProfileInfoForm
#     template_name = 'common/edit_profile.html'

# class UserProfileUpdateView(UpdateView):
#     template_name = "basic_app/edit_profile.html"
#     form_class = UserForm
#     form_class_2 = UserProfileInfoForm
    # def get_context_data(self, **kwargs):
        # context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        # if "form" not in context:
        #     context["form"] = self.form_class(instance=self.request.user)
        # if "form2" not in context:
        #     context["form2"] = self.form_class_2(
        #         instance=self.request.user.profile)
        # return context

    # def get(self, request, *args, **kwargs):
    #     super(UserProfileUpdateView, self).get(request, *args, **kwargs)
    #     self.object = self.get_object()
    #     form = self.form_class(instance=self.request.user)
    #     form2 = self.form_class_2(instance=self.request.user.profile)
    #     return self.render_to_response(self.get_context_data(form=form, form2=form2))

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.form_class(instance=self.request.user)
    #     form2 = self.form_class(instance=self.request.user.profile)
    #     if form.is_valid() and form2.is_valid():
    #         form.save()
    #         data = form2.save(commit=False)
    #         if request.FILES.get("profile_pic", None):
    #             data.profile_pic = request.FILES.get("profile_pic")
    #             data.profile_pic.name = "{}_profile.jpg".format(str(uuid.uuid4()))
    #         data.save()
    #         return redirect("basic_app:user_profile")
    #     else:
    #         return self.render_to_response(
    #             self.get_context_data(form=form, form2=form2)
    #         )

    # def get_object(self, qs=None):
    #     return self.request.user
