from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Post, Profile, Like, Following
from django.contrib.auth.models import User
import json
from django.views.generic import ListView
from django.core.paginator import Paginator


def user_home(request):
    user = Following.objects.get(user=request.user)
    followed_users = [i for i in user.followed.all()]
    followed_users.append(request.user)
    posts = Post.objects.filter(user__in=followed_users).order_by('-pk')
    liked_ = [i for i in posts if Like.objects.filter(post=i, user=request.user)]
    context = {
        'posts': posts,
        'liked_post': liked_,
    }

    return render(request, 'userpage/postfeed.html', context)


def post(request):
    if request.method == "POST":
        image_ = request.FILES['image']
        captions_ = request.POST.get('captions', '')
        user_ = request.user
        post_obj = Post(user=user_, caption=captions_, image=image_)
        post_obj.save()
        messages.success(request, "We showed them")
        return redirect('/userpage')
    else:
        messages.error(request, "Something went wrong")
        return redirect('/userpage')


def delete_post(request, post_id):
    post_ = Post.objects.filter(pk=post_id)
    image_path = post_[0].image.url
    post_.delete()
    messages.info(request, 'Post successfully deleted')
    return redirect('/userpage')


def user_profile(request, username):
    user = User.objects.filter(username=username)
    if user:
        user = user[0]
        profile = Profile.objects.get(user=user)
        post = get_post(user)
        bio = profile.bio
        conn = profile.connection
        user_img = profile.user_image
        follower, following = profile.follower, profile.following
        is_following = Following.objects.filter(user=request.user, followed=user)
        following_obj = Following.objects.get(user=user)
        follower, following = following_obj.follower.count(), following_obj.followed.count()

        data = {
            'user_obj': user,
            'bio': bio,
            'conn': conn,
            'follower': follower,
            'following': following,
            'user_image': user_img,
            'posts': post,
            'connection': is_following,
        }
    else:
        return HttpResponse('No such user')

    return render(request, 'userpage/user_profile.html', data)


def get_post(user):
    post_obj = Post.objects.filter(user=user)
    img_list = [
        post_obj[i:i+3] for i in range(0, len(post_obj), 3)
    ]
    return img_list


def like_post(request):
    post_id = request.GET.get("likeId", "")
    post = Post.objects.get(pk=post_id)
    user = request.user
    like = Like.objects.filter(post=post, user=user)
    liked = False
    if like:
        Like.dislike(post, user)
    else:
        liked = True
        Like.like(post, user)

    resp = {
        'liked': liked
    }

    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")


def comment(request):
    comment_ = request.GET.get('comment', '')
    print(comment_)
    return render(request, "comment/comment.html")


def follow(request, username):
    main_user = request.user
    to_follow = User.objects.get(username=username)
    following = Following.objects.filter(user=main_user, followed=to_follow)
    is_following = True if following else False

    if is_following:
        Following.unfollow(main_user, to_follow)
        is_following = False
    else:
        Following.follow(main_user, to_follow)
        is_following = True

    resp = {
        'following': is_following,
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")


class Search(ListView):
    model = User
    template_name = "userpage/searchUser.html"
    paginate_by = 2

    def get_query_set(self):
        username = self.request.GET.get("username", "")
        queryset = User.objects.filter(username__icontains=username)
        return queryset
