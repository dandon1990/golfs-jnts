from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import TipsPost, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TipsPostList(generic.ListView):
    model = TipsPost
    queryset = TipsPost.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 4


class TipsPostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TipsPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        author = TipsPost.author
        featured_image = post.featured_image
        comments = post.comments.filter(approved=True).order_by('created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "tips_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class CreateCommentView(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        model = Comment
        queryset = TipsPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "tips_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(TipsPost, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class EditComment(LoginRequiredMixin, View):

    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(instance=comment)
        return render(
            request,
            "edit_comment.html",
            {
                "comment_form": form,
                "comment": comment
            },
        )

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = comment.post
            new_form.save()
        return HttpResponseRedirect(
            reverse('post_detail', args=[comment.post.slug]))


class DeleteComment(LoginRequiredMixin, View):
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return HttpResponseRedirect(
            reverse('post_detail', args=[comment.post.slug]))
