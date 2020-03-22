import sys
from django.shortcuts import render, get_object_or_404
from bleet.models import Bleet, Comment
from users.models import Follow, Profile
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from .forms import NewCommentForm


def is_author(post, request):
    """
    Returns a boolean indication if the post is authored by the logged in
    user who made the request.
    """
    return post.author == request.user 


#: Number of bleets to show per page.
PAGINATION_COUNT = 10


class BleetListView(LoginRequiredMixin, ListView):
    """
    Displays a list of bleets
    """
    model = Bleet 
    template_name = 'bleet/home.html'
    context_object_name = 'bleets'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_queryset(self):
        user = self.request.user
        qs = Follow.objects.filter(user=user)
        follows = [user]
        for obj in qs:
            follows.append(obj.follow_user)
        return Bleet.objects.filter(author__in=follows).order_by('-date_posted')


class UserBleetListView(LoginRequiredMixin, ListView):
    model = Bleet 
    template_name = 'bleet/user_posts.html'
    context_object_name = 'bleets'
    paginate_by = PAGINATION_COUNT

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        visible_user = self.visible_user()
        logged_user = self.request.user

        if logged_user.username == '' or logged_user is None:
            can_follow = False
        else:
            can_follow = (Follow.objects.filter(user=logged_user,
                                                follow_user=visible_user).count() == 0)
        data = super().get_context_data(**kwargs)

        data['user_profile'] = visible_user
        data['can_follow'] = can_follow
        return data

    def get_queryset(self):
        user = self.visible_user()
        return Bleet.objects.filter(author=user).order_by('-date_posted')

    def post(self, request, *args, **kwargs):
        if request.user.id is not None:
            follows = Follow.objects.filter(user=request.user,
                                            follow_user=self.visible_user())
            if 'follow' in request.POST:
                    new_relation = Follow(user=request.user, follow_user=self.visible_user())
                    if follows.count() == 0:
                        new_relation.save()
            elif 'unfollow' in request.POST:
                    if follows.count() > 0:
                        follows.delete()

        return self.get(self, request, *args, **kwargs)


class BleetDetailView(DetailView):
    model = Bleet 
    template_name = 'bleet/bleet_detail.html'
    context_object_name = 'bleet'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(bleet_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              bleet_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


class BleetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bleet 
    template_name = 'bleet/bleet_delete.html'
    context_object_name = 'bleet'
    success_url = '/'

    def test_func(self):
        return is_author(self.get_object(), self.request)


class BleetCreateView(LoginRequiredMixin, CreateView):
    model = Bleet 
    fields = ['content']
    template_name = 'bleet/bleet_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Add a new bleet'
        return data


class BleetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bleet 
    fields = ['content']
    template_name = 'bleet/bleet_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_author(self.get_object(), self.request)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a bleet'
        return data


class FollowsListView(ListView):
    model = Follow
    template_name = 'bleet/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'follows'
        return data


class FollowersListView(ListView):
    model = Follow
    template_name = 'bleet/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(follow_user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'followers'
        return data
