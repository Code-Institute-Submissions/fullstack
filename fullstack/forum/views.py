# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from models import Subject, Thread, Post
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import ThreadForm, PostForm
from django.forms import formset_factory
from polls.forms import PollSubjectForm, PollForm
from polls.models import PollSubject


def forum(request):
    """
    Render the forum subject
    """
    return render(request, 'forum/subjects.html', {'subjects': Subject.objects.all()})


def threads(request, subject_id):
    """
    View all threads per subject selected
    """
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/threads.html', {'subject': subject})


@login_required
def new_thread(request, subject_id):
    """
    Add a new thread
    """
    subject = get_object_or_404(Subject, pk=subject_id)
    poll_subject_formset_class = formset_factory(PollSubjectForm, extra=3)

    # If request is POST, create a new thread
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        poll_form = PollForm(request.POST)
        poll_subject_formset = poll_subject_formset_class(request.POST)

        # Save Thread and Post
        if thread_form.is_valid() and post_form.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            # If user creates a Poll then save it too
            if poll_form.is_valid() and poll_subject_formset.is_valid():
                poll = poll_form.save(False)
                poll.thread = thread
                poll.save()

                for subject_form in poll_subject_formset:
                    subject = subject_form.save(False)
                    subject.poll = poll
                    subject.save()

            messages.success(request, "You have created a new thread!")

            return redirect(reverse('thread', args=[thread.pk]))

    # If request is GET, render blank form
    else:
        thread_form = ThreadForm()
        post_form = PostForm()
        poll_form = PollForm()
        poll_subject_formset = poll_subject_formset_class()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset,
    }

    args.update(csrf(request))

    return render(request, 'forum/thread_form.html', args)


def thread(request, thread_id):
    """
    View single thread
    """
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_}
    args.update(csrf(request))
    return render(request, 'forum/thread.html', args)


@login_required
def new_post(request, thread_id):
    """
    Create a new post/ Add a reply to a thread
    """
    thread = get_object_or_404(Thread, pk=thread_id)

    # If method is POST, save Post/Reply
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post has been added to the thread!")

            return redirect(reverse('thread', args={thread.pk}))

    # If method is GET, render blank form
    else:
        form = PostForm()

    args = {
        'form': form,
        'subtitle': 'Reply to ',
        'thread': thread,
        'form_action': reverse('new_post', args={thread_id}),
        'button_text': 'Add Post'
    }

    args.update(csrf(request))

    return render(request, 'forum/post_form.html', args)


@login_required
def edit_post(request, thread_id, post_id):
    """
    Edit a thread post
    """
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)

    # If method is POST, update and save the Post.
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "You have updated your thread!")

            return redirect(reverse('thread', args={thread.pk}))

    # If method is GET, render the existing Post to edit
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'subtitle': 'Edit your post on ',
        'thread': thread,
        'form_action': reverse('edit_post',  kwargs={"thread_id": thread.id, "post_id": post.id}),
        'button_text': 'Update Post',
    }
    args.update(csrf(request))

    return render(request, 'forum/post_form.html', args)

# NEED TO FIX: SEE README.md > Report > Known Bugs
# @login_required
# def delete_post(request, thread_id, post_id):
#     """
#     Delete post
#     """
#     post = get_object_or_404(Post, pk=post_id)
#     thread_id = post.thread.id
#     post.delete()
#
#     messages.success(request, "Your post was deleted!")
#
#     return redirect(reverse('thread', args={thread_id}))


@login_required
def thread_vote(request, thread_id, subject_id):
    """
    Allow users to cast vote
    """
    thread = Thread.objects.get(id=thread_id)

    subject = thread.poll.votes.filter(user=request.user)

    if subject:
        messages.error(request, "You already voted on this!")
        return redirect(reverse('thread', args={thread_id}))

    subject = PollSubject.objects.get(id=subject_id)

    subject.votes.create(poll=subject.poll, user=request.user)

    messages.success(request, "We've registered your vote!")

    return redirect(reverse('thread', args={thread_id}))
