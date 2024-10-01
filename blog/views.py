from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# View to display a list of published posts
class PostList(generic.ListView):
    # Query to filter posts with a status of 1 (published)
    queryset = Post.objects.filter(status=1)
    # Template to render the list of posts
    template_name = "blog/index.html"
    # Pagination: limit the posts displayed per page to 12
    paginate_by = 12


# View to display details of a single post and handle comments
def post_detail(request, slug):
    """
    Displays a detailed view of a single blog post, its comments, and a comment form.

    **Context**:
    - post: The blog post being displayed.
    - comments: All comments associated with the post.
    - comment_count: The number of approved comments on the post.
    - comment_form: A form for users to submit new comments.

    **Template**:
    - Uses 'blog/post_detail.html'.
    """

    # Query to fetch published posts
    queryset = Post.objects.filter(status=1)
    # Fetch the specific post based on its slug, or return 404 if not found
    post = get_object_or_404(queryset, slug=slug)
    # Get all comments related to the post, ordered by creation date (newest first)
    comments = post.comments.all().order_by("-created_on")
    # Count only approved comments to display
    comment_count = post.comments.filter(approved=True).count()
    # Initialize a blank comment form
    comment_form = CommentForm()

    # If the form was submitted via POST
    if request.method == "POST":
        # Populate the form with submitted data
        comment_form = CommentForm(data=request.POST)
        # Check if the form data is valid
        if comment_form.is_valid():
            # Create a new comment but don't save it to the database yet
            comment = comment_form.save(commit=False)
            # Associate the comment with the current user and the current post
            comment.author = request.user
            comment.post = post
            # Save the comment to the database
            comment.save()
            # Display a success message indicating the comment is awaiting approval
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    # Render the post detail template with the post, comments, comment count, and comment form
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


# View to handle editing of a comment
def comment_edit(request, slug, comment_id):
    """
    Allows a user to edit their comment on a post. After editing, the comment is set to unapproved.
    """

    # If the form was submitted via POST
    if request.method == "POST":
        # Fetch the post and comment to be edited
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        # Re-populate the form with the current comment data
        comment_form = CommentForm(data=request.POST, instance=comment)

        # Check if the form is valid and if the comment's author matches the current user
        if comment_form.is_valid() and comment.author == request.user:
            # Update the comment but don't save it immediately
            comment = comment_form.save(commit=False)
            comment.post = post
            # Set the comment to unapproved again after editing
            comment.approved = False
            comment.save()
            # Display a success message indicating the comment was updated
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            # Display an error message if the update failed
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    # Redirect the user back to the post's detail view
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# View to handle the deletion of a comment
def comment_delete(request, slug, comment_id):
    """
    Allows a user to delete their comment from a post.
    """

    # Fetch the post and the specific comment to be deleted
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the current user is the author of the comment
    if comment.author == request.user:
        # Delete the comment if the user is the author
        comment.delete()
        # Display a success message indicating the comment was deleted
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        # Display an error message if the user is not the author of the comment
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    # Redirect the user back to the post's detail view
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
